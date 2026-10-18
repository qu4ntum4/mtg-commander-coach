# mtg-commander-coach

Un coach pour construire et améliorer tes decks **Magic: The Gathering Commander** (papier) avec
Claude. Il repose sur une méthode rodée pendant des mois d'optimisation de decks avec Claude :
six étapes du cadrage à la mesure, une soixantaine de leçons chiffrées, et le catalogue des
erreurs qui l'ont façonnée.

## Ce que ça fait

- Tu colles ta liste (export texte de Moxfield, Archidekt…), tu dis ton budget, le niveau de ta
  table (bracket) et ce que tu veux améliorer.
- Claude vérifie le texte exact de chaque carte au lieu de se fier à sa mémoire, cherche les
  combos, regarde les prix, la base de mana et le bracket. Il te propose ensuite des échanges carte
  pour carte, chacun avec sa raison. Il part de **ta** liste et ne touche qu'aux cartes que tu
  désignes.
- Il tient une fiche par deck dans un dossier « Mes decks MTG » : la liste, l'historique des
  changements et pourquoi, ce qui reste à régler. La fois suivante, il reprend où vous en étiez.

## Ce qu'il te faut

- L'app **Claude** sur Windows ou Mac, avec l'onglet **Code** (abonnement payant).
- Environ 1,5 Go d'espace disque et une connexion internet.

## Installer

Ouvre [PROMPT.md](PROMPT.md), copie le bloc et colle-le dans l'onglet Code de l'app Claude.
Claude installe tout et termine par un bilan de santé qui dit ce qui marche.

Installation à la main, si tu préfères : installe [uv](https://docs.astral.sh/uv/), récupère ce
dépôt, puis depuis sa racine :

```bash
uv run --no-project --python 3.13 installer/installer.py
```

## Utiliser

Dans l'onglet Code, ouvre une session dans le dossier **Mes decks MTG** (dans tes Documents). La
première fois, l'app peut te demander d'autoriser l'accès à ce dossier : accepte. Remplis ensuite
la section « Ce que Claude doit savoir sur moi et mon groupe » de son fichier `CLAUDE.md`. Puis
parle-lui, par exemple :

- « Voici ma liste Muldrotha, je veux la rendre plus régulière sans dépasser 10 € par carte. »
- « Je veux upgrader le precon Animated Army pour une table bracket 3. »
- « Quel commandant pour un deck hibou mono-bleu ? »
- « Est-ce que mon deck est vraiment bracket 2 ? »

## Ce qui est installé, et où

| Quoi | Où |
|---|---|
| Le skill `commander-coach` (la méthode) | `~/.claude/skills/commander-coach` |
| Le skill `deck-wizard` (analyse par scripts) et son environnement Python | `~/.claude/skills/deck-wizard` |
| Les données de cartes de deck-wizard (~950 Mo) | `~/.cache/mtg-skills` |
| Ton dossier de decks : `CLAUDE.md`, fiches dans `decks/`, déclaration du serveur MTG (`.mcp.json`), réglages (`.claude/settings.json`) | `Documents/Mes decks MTG` |

Le serveur MTG lui-même est téléchargé par uv à la demande (cache de uv).

## Mettre à jour

Relance le même message (ou `git pull` puis le script). L'installateur met à jour ce qu'il a
installé et ne touche ni à tes fiches de deck ni à ton `CLAUDE.md`.

## Désinstaller

Supprime `~/.claude/skills/commander-coach`, `~/.claude/skills/deck-wizard` et
`~/.cache/mtg-skills`. Garde ou supprime `Documents/Mes decks MTG` : ce sont tes fiches.

## Limites connues

- **Commander papier seulement.**
- **Mac** : l'installateur est prévu pour Mac mais n'a pas encore été essayé sur un Mac.
- Au 17/10/2026, une partie des outils du serveur MTG est en panne chez leur auteur (`bulk_*`,
  `price_comparison`, `deck_validate`, `suggest_mana_base`, `precon_upgrade`, `budget_upgrade`…),
  et d'autres répondent mais se trompent (`spellbook_estimate_bracket`, `suggest_cuts`). Le skill
  le sait : il les évite et passe par les outils qui fonctionnent.
- Les prix des données locales de deck-wizard sont périmés de plusieurs semaines : le skill
  revérifie en direct toute carte au-dessus de ~10 $.
- Les versions des outils sont figées volontairement (voir [TIERS.md](TIERS.md)) : une mise à jour
  non contrôlée d'une dépendance a déjà cassé le serveur MTG une fois.

## Crédits et licences

Le contenu de ce dépôt (skill `commander-coach`, installateur, prompt) est sous licence MIT
([LICENSE](LICENSE)). Il s'appuie sur le travail d'autres personnes, détaillé dans
[TIERS.md](TIERS.md) : le serveur [mtg-mcp-server](https://github.com/j4th/mtg-mcp-server) et le
skill [deck-wizard](https://github.com/dan-blanchard/mtg-skills).

mtg-commander-coach est un contenu de fan non officiel, autorisé par la Fan Content Policy. Il
n'est ni approuvé ni soutenu par Wizards of the Coast. Magic: The Gathering est une marque de
Wizards of the Coast LLC.
