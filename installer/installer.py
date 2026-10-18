"""Installe mtg-commander-coach sur Windows ou macOS.

Lancement, depuis la racine du dépôt :

    uv run --no-project --python 3.13 installer/installer.py

Ce que fait le script, dans l'ordre :
  1. copie les skills `commander-coach` et `deck-wizard` dans ~/.claude/skills/ ;
  2. prépare deck-wizard : environnement Python figé, données de cartes (~1 Go), règles ;
  3. crée le dossier « Mes decks MTG » (dans Documents) et y déclare le serveur MTG ;
  4. lance le bilan de santé.

On peut le relancer sans risque : il met à jour ce qu'il a installé et ne touche ni aux fiches
de deck ni aux préférences écrites dans le dossier des decks.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

VERSION = "1.0.0"
DEPOT = Path(__file__).resolve().parent.parent
SKILLS = ("commander-coach", "deck-wizard")
MARQUEUR = ".installe-par-mtg-commander-coach"
# Versions figées : mtg-mcp-server 3.0.0 importe selectolax.parser, supprimé en selectolax 1.0.
ARGS_SERVEUR = ["--with", "selectolax<1", "mtg-mcp-server==3.0.0"]
NOM_SERVEUR = "mtg"
# Ce qui survit à une mise à jour de deck-wizard : son environnement, ses fichiers générés,
# les règles téléchargées.
GARDER_DECK_WIZARD = {".venv", "tests"}


def dire(texte: str = "") -> None:
    print(texte, flush=True)


def etape(numero: int, total: int, texte: str) -> None:
    dire(f"\n[{numero}/{total}] {texte}")


def arreter(texte: str) -> None:
    dire(f"\nÉCHEC : {texte}")
    sys.exit(1)


def dossier_documents() -> Path:
    """Le vrai dossier Documents, y compris quand OneDrive l'a déplacé (Windows)."""
    if os.name == "nt":
        import ctypes
        import ctypes.wintypes

        tampon = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        # CSIDL_PERSONAL = 5 : le dossier Documents de l'utilisateur.
        if ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, tampon) == 0 and tampon.value:
            return Path(tampon.value)
    return Path.home() / "Documents"


def trouver_uv() -> tuple[Path, Path]:
    """Chemins absolus de uv et uvx, sans résoudre les liens (Homebrew les change à chaque mise à jour)."""
    suffixe = ".exe" if os.name == "nt" else ""
    candidats = [
        os.environ.get("UV"),  # uv le définit pour les commandes qu'il lance
        shutil.which("uv"),
        str(Path.home() / ".local" / "bin" / f"uv{suffixe}"),
        str(Path.home() / ".cargo" / "bin" / f"uv{suffixe}"),
        "/opt/homebrew/bin/uv",
        "/usr/local/bin/uv",
    ]
    for candidat in candidats:
        if candidat and Path(candidat).is_file():
            uv = Path(os.path.abspath(candidat))
            uvx = uv.with_name(f"uvx{suffixe}")
            if uvx.is_file():
                return uv, uvx
    arreter("uv est introuvable. Installe-le (voir le README), puis relance ce script.")
    raise AssertionError  # pour les vérificateurs de types


def lancer(commande: list, *, env: dict | None = None, quoi: str) -> None:
    dire(f"   … {quoi}")
    resultat = subprocess.run([str(c) for c in commande], env=env, capture_output=True, text=True,
                              encoding="utf-8", errors="replace")
    if resultat.returncode != 0:
        fin = (resultat.stdout + resultat.stderr).strip().splitlines()[-15:]
        arreter(f"{quoi} n'a pas abouti (code {resultat.returncode}).\n      " + "\n      ".join(fin))


def lire_json(chemin: Path) -> dict:
    if not chemin.exists():
        return {}
    try:
        return json.loads(chemin.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as erreur:
        arreter(f"{chemin} n'est pas un JSON valide ({erreur}). Corrige-le ou renomme-le, puis relance.")
        raise


def ecrire_json(chemin: Path, donnees: dict) -> None:
    """UTF-8 sans BOM : certains lecteurs refusent un JSON qui commence par un BOM."""
    chemin.parent.mkdir(parents=True, exist_ok=True)
    temporaire = chemin.with_suffix(chemin.suffix + ".tmp")
    temporaire.write_text(json.dumps(donnees, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporaire.replace(chemin)


def installer_skill(nom: str, racine: Path, horodatage: str) -> Path:
    source, cible = DEPOT / "skills" / nom, racine / nom
    if cible.exists() and not (cible / MARQUEUR).exists():
        sauvegarde = cible.with_name(f"{nom}.avant-mtg-commander-coach-{horodatage}")
        cible.rename(sauvegarde)
        dire(f"   Un skill « {nom} » existait déjà : il est mis de côté dans {sauvegarde}")
    if cible.exists():
        garder = GARDER_DECK_WIZARD if nom == "deck-wizard" else set()
        for element in cible.iterdir():
            if element.name in garder or element.name.startswith("comprehensive-rules"):
                continue
            shutil.rmtree(element) if element.is_dir() else element.unlink()
    shutil.copytree(source, cible, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", ".venv", "*.pyc"))
    (cible / MARQUEUR).write_text(f"mtg-commander-coach {VERSION}\n", encoding="utf-8")
    dire(f"   OK  {nom} → {cible}")
    return cible


def preparer_deck_wizard(uv: Path, dossier: Path) -> None:
    env = dict(os.environ, PYTHONUTF8="1")
    executer = [uv, "run", "--directory", dossier, "--frozen"]
    lancer([uv, "sync", "--directory", dossier, "--frozen", "--python", "3.13"], env=env,
           quoi="environnement Python de deck-wizard (versions figées)")
    lancer([*executer, "download-mtgjson"], env=env,
           quoi="données de cartes MTGJSON (~800 Mo, une à quelques minutes)")
    lancer([*executer, "python", "-m", "mtg_utils._card_ir.mirror.build"], env=env,
           quoi="index des effets de cartes (1/2)")
    lancer([*executer, "python", "-m", "mtg_utils.card_ir_crosswalk_build"], env=env,
           quoi="index des effets de cartes (2/2)")
    lancer([*executer, "download-rules", "--output-dir", dossier], env=env,
           quoi="règles complètes du jeu")


def preparer_dossier_decks(dossier: Path, uvx: Path) -> None:
    modele = DEPOT / "installer" / "modele-mes-decks"
    (dossier / "decks").mkdir(parents=True, exist_ok=True)
    for fichier in modele.rglob("*"):
        if fichier.is_file():
            cible = dossier / fichier.relative_to(modele)
            if not cible.exists():  # ne jamais écraser ce que l'utilisateur a écrit
                cible.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(fichier, cible)

    mcp = lire_json(dossier / ".mcp.json")
    mcp.setdefault("mcpServers", {})[NOM_SERVEUR] = {"command": str(uvx), "args": ARGS_SERVEUR}
    ecrire_json(dossier / ".mcp.json", mcp)

    reglages = lire_json(dossier / ".claude" / "settings.json")
    actives = reglages.setdefault("enabledMcpjsonServers", [])
    if NOM_SERVEUR not in actives:
        actives.append(NOM_SERVEUR)
    # deck-wizard lit ses données en UTF-8 ; sans ce réglage, sous Windows, il compte
    # zéro carte d'interaction sans afficher la moindre erreur.
    reglages.setdefault("env", {})["PYTHONUTF8"] = "1"
    permis = reglages.setdefault("permissions", {}).setdefault("allow", [])
    if f"mcp__{NOM_SERVEUR}" not in permis:
        permis.append(f"mcp__{NOM_SERVEUR}")
    ecrire_json(dossier / ".claude" / "settings.json", reglages)
    dire(f"   OK  dossier des decks : {dossier}")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parseur = argparse.ArgumentParser(description="Installe mtg-commander-coach.")
    parseur.add_argument("--dossier-decks", type=Path,
                         help="Où créer le dossier des decks (par défaut : Documents/Mes decks MTG).")
    parseur.add_argument("--sans-bilan", action="store_true", help="Ne pas lancer le bilan de santé.")
    args = parseur.parse_args()

    if sys.platform not in ("win32", "darwin"):
        dire("ATTENTION : ce script est prévu pour Windows et macOS ; on continue quand même.")
    dossier_decks = (args.dossier_decks or dossier_documents() / "Mes decks MTG").resolve()
    racine_skills = Path.home() / ".claude" / "skills"
    horodatage = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    dire(f"mtg-commander-coach {VERSION}")

    etape(1, 4, "Recherche de uv")
    uv, uvx = trouver_uv()
    dire(f"   OK  {uv}")

    etape(2, 4, "Copie des skills")
    racine_skills.mkdir(parents=True, exist_ok=True)
    dossiers = {nom: installer_skill(nom, racine_skills, horodatage) for nom in SKILLS}

    etape(3, 4, "Préparation de deck-wizard")
    preparer_deck_wizard(uv, dossiers["deck-wizard"])

    etape(4, 4, "Dossier des decks et serveur MTG")
    preparer_dossier_decks(dossier_decks, uvx)

    if args.sans_bilan:
        return 0
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import bilan_de_sante

    return bilan_de_sante.bilan(dossier_decks, dossiers["deck-wizard"], uv)


if __name__ == "__main__":
    sys.exit(main())
