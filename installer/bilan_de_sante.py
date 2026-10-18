"""Bilan de santé de mtg-commander-coach : vérifie, par de vrais appels, que tout fonctionne.

Lancé à la fin de l'installation, ou seul :

    uv run --no-project --python 3.13 installer/bilan_de_sante.py

Chaque contrôle a une réponse connue d'avance. Un outil qui « répond » mais renvoie des zéros
est compté comme une panne : c'est la façon la plus courante dont ces outils échouent.
"""

from __future__ import annotations

import argparse
import json
import os
import queue
import shutil
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

ICI = Path(__file__).resolve().parent
DECK_REFERENCE = ICI / "deck-de-reference.txt"  # « Animated Army » (Bloomburrow Commander, 2024)
COMMANDANT_REFERENCE = "Bello, Bard of the Brambles"
# Réponse connue, relevée le 17/10/2026 sur deck-wizard du 14/10 : 15 cartes d'interaction.
# Sans PYTHONUTF8 sous Windows, il en compte 8, sans la moindre erreur.
INTERACTION_MINIMUM = 12
OUTILS_MINIMUM = 60

resultats: list[tuple[str, str, str]] = []


def noter(etat: str, quoi: str, detail: str = "") -> None:
    resultats.append((etat, quoi, detail))
    print(f"   {etat:<9} {quoi}" + (f" — {detail}" if detail else ""), flush=True)


class ServeurMCP:
    """Dialogue JSON-RPC minimal avec un serveur MCP en stdio."""

    def __init__(self, commande: list[str]) -> None:
        self.processus = subprocess.Popen(commande, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                          stderr=subprocess.DEVNULL, text=True, encoding="utf-8",
                                          bufsize=1)
        self.file: queue.Queue[str] = queue.Queue()
        threading.Thread(target=self._lire, daemon=True).start()
        self.prochain = 0

    def _lire(self) -> None:
        for ligne in self.processus.stdout:
            self.file.put(ligne)

    def envoyer(self, methode: str, params: dict | None = None, *, notification: bool = False) -> None:
        message = {"jsonrpc": "2.0", "method": methode}
        if params is not None:
            message["params"] = params
        if not notification:
            message["id"] = self.prochain
        self.processus.stdin.write(json.dumps(message) + "\n")
        self.processus.stdin.flush()

    def demander(self, methode: str, params: dict | None = None, delai: float = 120) -> dict:
        numero = self.prochain
        self.envoyer(methode, params)
        self.prochain += 1
        while True:
            reponse = json.loads(self.file.get(timeout=delai))
            if reponse.get("id") == numero:
                if "error" in reponse:
                    raise RuntimeError(reponse["error"].get("message", "erreur"))
                return reponse["result"]

    def appeler(self, outil: str, arguments: dict, delai: float = 90) -> str:
        resultat = self.demander("tools/call", {"name": outil, "arguments": arguments}, delai)
        texte = " ".join(c.get("text", "") for c in resultat.get("content", []) if c.get("type") == "text")
        if resultat.get("isError"):
            raise RuntimeError(texte[:200])
        return texte

    def fermer(self) -> None:
        try:
            self.processus.stdin.close()
            self.processus.terminate()
        except OSError:
            pass


def verifier_serveur(dossier_decks: Path) -> None:
    print("\nServeur MTG (cartes, prix, combos, EDHREC, règles)")
    config = json.loads((dossier_decks / ".mcp.json").read_text(encoding="utf-8-sig"))
    entree = config["mcpServers"]["mtg"]
    serveur = ServeurMCP([entree["command"], *entree["args"]])
    try:
        # Le premier lancement télécharge le serveur : on lui laisse le temps.
        info = serveur.demander("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                               "clientInfo": {"name": "bilan", "version": "1"}}, delai=300)
        serveur.envoyer("notifications/initialized", notification=True)
        noter("OK", "le serveur démarre", f"{info['serverInfo']['name']} {info['serverInfo']['version']}")
        outils = serveur.demander("tools/list")["tools"]
        etat = "OK" if len(outils) >= OUTILS_MINIMUM else "ÉCHEC"
        noter(etat, "liste des outils", f"{len(outils)} outils")
        reponse = serveur.appeler("ping", {})
        noter("OK" if "pong" in reponse else "ÉCHEC", "ping", reponse[:40])
        fiche = serveur.appeler("scryfall_card_details", {"name": "Arcane Signet"})
        noter("OK" if "Arcane Signet" in fiche and "{T}" in fiche else "ÉCHEC",
              "fiche de carte en direct (Scryfall)")
        try:
            # Témoin de selectolax, la dépendance qui a cassé le serveur le 03/10/2026.
            meta = serveur.appeler("goldfish_metagame", {"format": "Modern", "response_format": "concise"})
            noter("OK" if "Metagame" in meta and "%" in meta else "ATTENTION",
                  "lecture de pages web (MTGGoldfish)")
        except (RuntimeError, queue.Empty) as erreur:
            noter("ATTENTION", "lecture de pages web (MTGGoldfish)",
                  f"le site n'a pas répondu ({erreur}) ; le reste du serveur fonctionne")
    except (RuntimeError, queue.Empty, KeyError, json.JSONDecodeError) as erreur:
        noter("ÉCHEC", "dialogue avec le serveur", str(erreur) or "pas de réponse dans le délai")
    finally:
        serveur.fermer()


def verifier_deck_wizard(dossier_decks: Path, deck_wizard: Path, uv: Path) -> None:
    print("\ndeck-wizard (analyse d'un deck de référence)")
    reglages = json.loads((dossier_decks / ".claude" / "settings.json").read_text(encoding="utf-8-sig"))
    # On utilise exactement l'environnement que Claude Code donnera aux commandes de ce dossier.
    env = {k: v for k, v in os.environ.items() if k != "PYTHONUTF8"}
    env.update(reglages.get("env", {}))
    donnees = Path.home() / ".cache" / "mtg-skills" / "mtgjson" / "AllPrintings.json"
    if not donnees.exists():
        noter("ÉCHEC", "données de cartes", f"{donnees} est absent : relance l'installation")
        return
    with tempfile.TemporaryDirectory(prefix="bilan-mtg-") as temporaire:
        dossier = Path(temporaire)
        deck, sortie = dossier / "deck.json", dossier / "tune.json"

        def executer(*args: object) -> subprocess.CompletedProcess:
            return subprocess.run([str(uv), "run", "--directory", str(deck_wizard), "--frozen",
                                   *map(str, args)], env=env, capture_output=True, text=True,
                                  encoding="utf-8", errors="replace")

        etapes = [
            ("lecture de la liste", ("parse-deck", DECK_REFERENCE, "--format", "commander", "--output", deck)),
            ("choix du commandant", ("set-commander", deck, COMMANDANT_REFERENCE)),
            ("texte des cartes", ("deck-hydrate", deck, "--bulk-data", donnees)),
        ]
        for quoi, args in etapes:
            resultat = executer(*args)
            if resultat.returncode != 0:
                noter("ÉCHEC", quoi, (resultat.stdout + resultat.stderr).strip().splitlines()[-1:][0]
                      if (resultat.stdout + resultat.stderr).strip() else f"code {resultat.returncode}")
                return
        resultat = executer("deck-tune", deck, "--bulk-data", donnees, "--bracket", "2",
                            "--max-swaps", "1", "--output", sortie)
        if resultat.returncode != 0 or not sortie.exists():
            noter("ÉCHEC", "analyse du deck", f"code {resultat.returncode}")
            return
        budgets = json.loads(sortie.read_text(encoding="utf-8"))["scorecard"]["template"]["budgets"]
        interaction = budgets["interaction"]["current"]
        terrains = budgets["lands"]["current"]
        if interaction >= INTERACTION_MINIMUM:
            noter("OK", "analyse du deck", f"{terrains} terrains, {interaction} cartes d'interaction")
        else:
            noter("ÉCHEC", "analyse du deck",
                  f"{interaction} cartes d'interaction au lieu d'une quinzaine : deck-wizard lit mal ses "
                  "données (réglage PYTHONUTF8 absent de .claude/settings.json ?)")
    regles = sorted(deck_wizard.glob("comprehensive-rules*.txt"))
    noter("OK" if regles else "ATTENTION", "règles complètes du jeu",
          regles[-1].name if regles else "absentes : les citations de règles manqueront")


def verifier_fichiers(dossier_decks: Path, deck_wizard: Path) -> None:
    print("\nFichiers")
    coach = deck_wizard.parent / "commander-coach" / "SKILL.md"
    noter("OK" if coach.exists() else "ÉCHEC", "skill commander-coach", str(coach.parent))
    noter("OK" if (deck_wizard / "SKILL.md").exists() else "ÉCHEC", "skill deck-wizard", str(deck_wizard))
    noter("OK" if (dossier_decks / "CLAUDE.md").exists() else "ÉCHEC", "dossier des decks", str(dossier_decks))


def bilan(dossier_decks: Path, deck_wizard: Path, uv: Path) -> int:
    print("\n=== Bilan de santé ===")
    verifier_fichiers(dossier_decks, deck_wizard)
    verifier_serveur(dossier_decks)
    verifier_deck_wizard(dossier_decks, deck_wizard, uv)
    echecs = [r for r in resultats if r[0] == "ÉCHEC"]
    print()
    if echecs:
        print(f"RÉSULTAT : {len(echecs)} contrôle(s) en échec. Le détail est ci-dessus.")
        return 1
    print("RÉSULTAT : tout fonctionne.")
    print(f"Pour commencer : dans l'app Claude, onglet Code, ouvre le dossier « {dossier_decks.name} »")
    print(f"({dossier_decks}) et parle-lui de ton deck.")
    return 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parseur = argparse.ArgumentParser(description="Bilan de santé de mtg-commander-coach.")
    parseur.add_argument("--dossier-decks", type=Path, required=True)
    parseur.add_argument("--deck-wizard", type=Path, default=Path.home() / ".claude" / "skills" / "deck-wizard")
    args = parseur.parse_args()
    uv = shutil.which("uv") or os.environ.get("UV")
    if not uv:
        print("ÉCHEC : uv est introuvable.")
        return 1
    return bilan(args.dossier_decks.resolve(), args.deck_wizard.resolve(), Path(uv))


if __name__ == "__main__":
    sys.exit(main())
