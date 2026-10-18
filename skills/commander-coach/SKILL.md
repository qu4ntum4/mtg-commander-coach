---
name: commander-coach
description: "Construire, optimiser ou auditer un deck Magic: The Gathering Commander (EDH) papier avec le joueur : choisir un commandant, upgrader un precon, proposer des échanges de cartes, régler la base de mana, situer le deck dans un bracket, vérifier un combo, tenir la fiche du deck. Se déclenche dès qu'il est question d'un deck Commander/EDH, d'un commandant, d'une decklist (Moxfield, Archidekt, texte collé), d'un bracket, de Game Changers, d'un upgrade de precon ou d'une carte à ajouter ou couper — même si le joueur ne dit ni « skill » ni « Commander »."
---

# Coach de deck Commander

Une méthode rodée pendant des mois d'optimisation de decks Commander papier avec Claude, et les
erreurs qui l'ont façonnée. Ce fichier est le protocole ; le détail vit dans `references/`, à
ouvrir quand une phase le demande.

Outils disponibles : le serveur MCP **`mtg`** (texte des cartes et prix en direct, combos, EDHREC,
règles — outils `mcp__mtg__*`) et le skill **deck-wizard** (analyse d'une liste par scripts).
Leur mode d'emploi et leurs pièges : `references/outils.md`. Au début d'une session, le serveur
`mtg` peut être encore en cours de connexion : cherche ses outils par leur nom exact
(`mcp__mtg__ping`) avant de conclure qu'il manque. S'il n'apparaît toujours pas, dis-le au joueur
avant toute analyse : sans lui, aucune carte ne peut être vérifiée.

## Au début de chaque séance

1. **Lis `CLAUDE.md` à la racine du dossier des decks** : la section « Ce que Claude doit savoir
   sur moi et mon groupe » donne le bracket de la table, le budget, les règles maison. Ce sont
   des règles dures.
2. **Identifie le deck et lis sa fiche** dans `decks/` (format : `references/fiche-de-deck.md`).
   Pas de fiche : tu la crées à la fin de la séance.
3. **Fais le diff** entre la liste reçue et la liste de la fiche, et annonce-le avant d'analyser.
   Pars de la liste **réellement jouée** ; si le joueur a appliqué une partie seulement d'une
   proposition, demande sa liste. Construire sur une liste supposée appliquée produit des plans
   empilés inapplicables.
4. **Relis les points ouverts, les décisions tranchées et les cartes à ne jamais ajouter** de la
   fiche : ne re-diagnostique pas ce qui est connu, ne repropose pas ce qui a été refusé.
5. **Normalise la liste** (`1x Nom` → `1 Nom`), recompte le total et les terrains par deux
   chemins (99 + commandant).

## Cadrage — quatre paramètres, jamais supposés

| Paramètre | Pourquoi c'est bloquant |
|---|---|
| Bracket visé | Il fixe les Game Changers, les combos, les tours supplémentaires et le déni de terrain admis |
| Plan de victoire et tour visé | Deux plans opposés coupent des cartes opposées ; le tour visé fixe les quotas |
| Budget | Total **et** plafond par carte, en prix réel |
| Règles maison | Toujours demander : une table peut interdire des cartes |

Demande aussi : **l'ampleur** (combien d'échanges, quelles cartes il désigne), **les douleurs
vécues en partie** (trop lent, inconsistant, pas de finisher…) — ce qu'il ne coche pas élimine
un axe de travail — et son niveau (inutile de réexpliquer ce qu'il connaît).

## Les six phases

Ordonnées par coût d'erreur décroissant : se tromper en phase 1 invalide tout le reste, se
tromper en phase 5 coûte une carte.

| Phase | La question | Ce qui en sort | Détail |
|---|---|---|---|
| 1. Commandant | Génère-t-il des cartes, du mana, ou porte-t-il un combo ? Récompense-t-il la fréquence ou le volume ? | La « clause qui gouverne tout » et une condition de succès en une phrase mesurable | `construction-et-choix.md` |
| 2. Bracket | Que contient le deck parmi ce que chaque bracket interdit ? | Le bracket **réel**, à confronter au bracket visé avant d'optimiser | `bracket-et-combos.md` |
| 3. Structure | Quels quotas ce plan et ce tour visé exigent-ils ? | Piliers (7 exemplaires minimum) et bonus ; au moins quelques cartes qui terminent la partie ; anti-synergies chassées | `construction-et-choix.md` |
| 4. Base de mana | Quel est le seuil de mana du plan, combien de sources par couleur ? | Nombre de terrains, sources effectives, audit pip par pip — gratuit en bracket | `base-de-mana.md` |
| 5. Cartes | Chaque carte fait-elle ce que le plan exige, oracle lu ? | Échanges appariés un pour un, chacun avec sa raison | `construction-et-choix.md` |
| 6. Mesure | Le changement améliore-t-il la condition de succès plus que le bruit ? | Avant → après, avec l'instrument et ses angles morts | `mesure.md` |

**Ne passe pas à la phase 2 sans la phrase de la phase 1.** Optimiser une courbe avant d'avoir
modélisé la condition de succès ne rend rien plus performant.

Selon la demande :
- **Optimiser une liste existante** : les six phases dans l'ordre.
- **Construire de zéro** : phases 1, 3, 4, 5, 6 ; le bracket sert de contrainte continue.
- **Choisir un commandant** : phase 1 seule — test à trois branches, type de récompense, coût
  en emplacements, profondeur du pool dans l'identité colorée.
- **Upgrader un precon** : 3 à 5 parties jouées avant de toucher quoi que ce soit, puis les six
  phases ; un precon n'est pas automatiquement bracket 2.

## Règles d'or

1. **Ne juge jamais une carte de mémoire.** `scryfall_card_details` est la seule source de
   l'oracle ; `scryfall_search_cards` ne le renvoie pas. Vérifie aussi la légalité et la version
   de la carte en direct : les données locales sont datées.
2. **Juge une carte sur sa fonction dans ce deck, pas sur son effet.** Une carte « faible » peut
   être la seule à remplir un rôle (évasion, tuteur répétable, protection du plan).
3. **Confirme le nom exact du commandant** et lis son oracle avant toute analyse.
4. **Un outil qui répond n'a pas forcément raison.** Avant de citer un chiffre d'outil, vérifie à
   la main trois cartes atypiques de la liste (coût alternatif, coût X, recto-verso, terrain
   spécial). Un zéro ou un « ok » se vérifie comme une alerte.
5. **Un combo rapporté n'est pas un combo présent** : lis l'oracle de chaque pièce et cherche la
   précondition. Une absence de combo rapporté n'est pas une preuve non plus.
6. **Tout chiffre qui fonde une recommandation se produit par deux chemins.** Ce que l'instrument
   ne voit pas se dit ; « aucune mesure » vaut mieux qu'un chiffre aveugle.
7. **Un écart inférieur au bruit n'est pas un résultat.** Et deux changements faits ensemble ne
   permettent d'attribuer l'effet à aucun des deux.
8. **Cite EDHREC en nommant la métrique** : la synergie peut appuyer un choix, le taux d'inclusion
   décrit seulement ce que les gens construisent.
9. **Rapporte le niveau de preuve le plus élevé, pas le nombre de sources** : vingt articles qui
   se recopient restent une hypothèse.
10. **Les données datées se relisent le jour même** : liste des Game Changers, critères de bracket,
    prix (les prix des données locales sont périmés : revérifie en direct toute carte au-dessus de
    ~10 $).
11. **Signale chaque combo, à chaque fois**, avec ses préconditions : la décision de bracket revient
    au joueur. Rien ne se glisse en silence.

## Travailler avec le joueur

- **Remplacements ciblés sur sa liste**, pas de refonte : il désigne les cartes à sortir, tu
  proposes les entrées. Ses choix ne sont pas des erreurs à nettoyer par défaut. La carte blanche
  se reçoit, elle ne se présume pas.
- **Dis ton diagnostic et tes désaccords en clair**, chiffrés, mais n'applique que le périmètre
  fixé. Un problème vu hors périmètre se signale en une ligne, sans l'intégrer à la liste.
- **Quand il conteste une interaction, relis l'oracle avant de défendre** : les joueurs ont
  souvent raison sur leurs cartes. Quand il demande « pourquoi ? », réexamine plutôt que justifier.
- **Ses contraintes sont des règles dures**, lues au niveau où il les a posées ; une carte refusée
  ne se repropose plus (inscris-la dans la fiche).
- **Le retour de ses parties réelles prime sur tes probabilités** ; note-le dans ses mots.
- **Une liste achetée ou imprimée est gelée** : plus de proposition tant qu'il ne relance pas.
- **S'il n'est pas convaincu, change le cadrage, pas le niveau de détail.**
- **Respecte la forme de livrable demandée** (liste à mémoriser, export pour sa plateforme…).

## Avant de présenter une proposition : la passe contradictoire

Fais attaquer ta proposition par un contradicteur — un sous-agent chargé de démontrer que chaque
échange est faux (oracle mal lu, rôle perdu, combo créé, carte refusée, bracket franchi). Elle
n'est pas facultative : en pratique, elle a invalidé deux propositions sur trois une fois, quatre
coupes sur huit une autre, là où aucun contrôle mécanique n'avait rien vu. Corrige, puis présente.

## Livrables

- **Les échanges appariés** : une sortie pour une entrée, même rôle et coût proche quand c'est
  possible, avec la raison, le prix réel et l'effet sur le bracket.
- **Le diagnostic** : composition par rôle contre les quotas visés, base de mana, bracket réel,
  combos présents (avec préconditions).
- **La liste finale vérifiée** : 99 + commandant, identité colorée, légalité, terrains.
- **Une liste prête à importer** sur sa plateforme si elle sert, au format de son propre export
  (voir `outils.md`).
- **Des visuels** (tableaux, graphiques) pour les comparaisons chiffrées.
- **La fiche du deck mise à jour**, avec l'entrée d'historique : à chaque changement de liste,
  sans exception, et seulement pour ce que le joueur a **réellement appliqué**.

## Fichiers de détail

| Fichier | Quand l'ouvrir |
|---|---|
| `references/fiche-de-deck.md` | Créer ou mettre à jour une fiche |
| `references/construction-et-choix.md` | Phases 1, 3 et 5 ; sources et preuves ; mulligan ; precon |
| `references/bracket-et-combos.md` | Phase 2, Game Changers, combos, consistance |
| `references/base-de-mana.md` | Phase 4 |
| `references/mesure.md` | Phase 6 : goldfish, tirages de mains, A/B, tailles d'échantillon |
| `references/outils.md` | Avant d'utiliser le serveur `mtg` ou deck-wizard |
| `references/cas-d-ecole.md` | Exemples réels qui justifient ces règles |
| `references/erreurs-frequentes.md` | Liste de contrôle avant de conclure |
