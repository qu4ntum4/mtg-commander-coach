# Le message à coller dans Claude

Ouvre l'app Claude sur ton ordinateur, va dans l'onglet **Code**, ouvre une session dans
n'importe quel dossier (par exemple tes Documents), puis colle tout le bloc ci-dessous.
Claude te demandera la permission avant chaque action ; l'installation prend 5 à 10 minutes et
télécharge environ 1 Go.

---

```text
Installe pour moi « mtg-commander-coach », un coach de deck Magic Commander :
https://github.com/qu4ntum4/mtg-commander-coach

Fais les étapes dans l'ordre, explique-moi chacune en une phrase simple avant de la lancer,
et ne modifie rien d'autre sur ma machine que ce que ces étapes demandent.

1. Vérifie si uv est installé (`uv --version`, puis `~/.local/bin/uv --version`).
   S'il ne l'est pas, installe-le avec la méthode officielle d'Astral :
   - Windows : powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   - Mac : curl -LsSf https://astral.sh/uv/install.sh | sh
   Après une installation, utilise le chemin complet de uv (`~/.local/bin/uv`, ou
   `%USERPROFILE%\.local\bin\uv.exe` sous Windows) : ta session ne voit pas encore le nouveau PATH.

2. Récupère le dépôt dans le dossier `mtg-commander-coach` de mon dossier personnel :
   `git clone` s'il est disponible ; sinon télécharge l'archive
   https://github.com/qu4ntum4/mtg-commander-coach/archive/refs/heads/main.zip et décompresse-la
   à cet endroit. S'il existe déjà, mets-le à jour (`git pull`, ou nouvelle archive).

3. Depuis la racine du dépôt, lance :
   uv run --no-project --python 3.13 installer/installer.py
   (avec le chemin complet de uv si nécessaire). Laisse-lui le temps : il télécharge les
   données de cartes.

4. Lis le bilan de santé affiché à la fin. Dis-moi en français simple ce qui marche et ce qui
   ne marche pas. En cas d'échec, cherche la cause dans le message, propose-moi une correction
   et attends mon accord avant de l'appliquer.

5. Pour finir, dis-moi comment commencer : ouvrir une nouvelle session de l'onglet Code dans le
   dossier « Mes decks MTG » créé par l'installation (l'app peut demander d'autoriser l'accès à
   ce dossier : il faut accepter), remplir la section « Ce que Claude doit savoir sur moi et mon
   groupe » de son fichier CLAUDE.md, puis parler de mon deck.
```
