# Composants tiers

## mtg-mcp-server — le serveur MTG

- Auteur : j4th — <https://github.com/j4th/mtg-mcp-server> — licence MIT.
- **Non inclus dans ce dépôt** : uv le télécharge depuis PyPI au lancement.
- Commande installée (dans `.mcp.json` du dossier des decks) :
  `uvx --with "selectolax<1" mtg-mcp-server==3.0.0`.
- Pourquoi ces versions figées : la version 3.0.0 importe `selectolax.parser`, que selectolax
  1.0 (sortie le 03/10/2026) a supprimé. Sans la contrainte `selectolax<1`, le serveur plante au
  démarrage. À retirer quand une version compatible du serveur sera publiée.

## deck-wizard — l'analyse de deck par scripts

- Auteur : Dan Blanchard — <https://github.com/dan-blanchard/mtg-skills> — licence 0BSD.
- **Copie figée incluse** dans `skills/deck-wizard/` (version du 14/10/2026), avec un correctif.
  Détail dans [skills/deck-wizard/VENDORED.md](skills/deck-wizard/VENDORED.md).

## Données

Les outils interrogent des services publics, chacun selon ses conditions : Scryfall (texte des
cartes, prix), MTGJSON (données de cartes de deck-wizard), EDHREC, Commander Spellbook,
MTGGoldfish, et les règles complètes publiées par Wizards of the Coast.

Contenu de fan non officiel, autorisé par la Fan Content Policy ; ni approuvé ni soutenu par
Wizards of the Coast.
