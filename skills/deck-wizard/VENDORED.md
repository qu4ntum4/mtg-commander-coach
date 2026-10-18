# Copie figée de deck-wizard

- Origine : <https://github.com/dan-blanchard/mtg-skills>, dossier `deck-wizard/`, et le paquet
  partagé `mtg-utils/src/` copié dans `src/` (le dépôt d'origine le relie par un lien
  symbolique, que Windows gère mal).
- Version : commit `4bcd621cc2f193606c3b7515457163c3cbe98f44` (14/10/2026).
- Licence : 0BSD (voir `LICENSE`), conservée.
- Dépendances Python figées par `uv.lock` ; l'installateur lance `uv sync --frozen`.

## Correctif appliqué

**Dossier `tests/fixtures`** — `src/mtg_utils/_card_ir/mirror/build.py`, `fixtures_dir()` :
`parents[5]` devient `parents[4]`. Le code d'origine suppose la disposition du dépôt source et
écrit hors du dossier du skill une fois installé seul (`WinError 3` sous Windows) ; le dossier
est désormais `deck-wizard/tests/fixtures`.

## Réglage requis

Sous Windows, les scripts doivent tourner avec `PYTHONUTF8=1`. L'installateur le pose dans
`.claude/settings.json` du dossier des decks. Sans lui, deck-wizard lit ses données dans le
mauvais encodage et sous-compte les rôles sans afficher d'erreur ; le bilan de santé le vérifie
sur un deck de référence.
