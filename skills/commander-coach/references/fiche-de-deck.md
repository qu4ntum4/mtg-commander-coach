# La fiche de deck

Quand lire ce fichier : pour créer la fiche d'un deck, ou la mettre à jour après un changement
de liste, une mesure, un retour de partie ou une décision du joueur.
La fiche est la mémoire du deck d'une séance à l'autre : sans elle, tu reproposes ce qui a été
refusé et tu re-diagnostiques ce qui est connu.

## Les règles

- **Un fichier vivant par deck**, dans `decks/` du dossier des decks, nommé
  `Commandant — identité.md` (ex. `Sonic the Hedgehog — Jeskai.md`).
- **Lis-la en entier avant toute analyse** ; fais le diff entre la liste reçue et la liste
  enregistrée et annonce-le ; relis les points ouverts.
- **Traçabilité non négociable** : à chaque changement de liste, une entrée **en tête**
  d'historique. Ne remplace jamais la liste sans écrire l'entrée correspondante. Six mois plus
  tard, il faut savoir pourquoi une carte est sortie, pour ne pas la reproposer.
- **N'enregistre que ce que le joueur a réellement appliqué.** Une proposition refusée ou en
  attente va dans « Réserves » ou dans les points ouverts, pas dans la liste.
- **Une seule liste actuelle** : la précédente disparaît, l'historique dit ce qui a changé.
  N'empile pas les versions dans la fiche.
- **Ce qui devient faux ne s'efface pas** : barre-le, date-le, dis pourquoi (« ~~Avertissement
  du 2026-08-04~~ caduc depuis la v4 : … »). Un point ouvert levé reste visible, barré, avec son
  verdict.
- **Les paramètres de jeu vont dans la fiche**, pas dans ta mémoire : façon de jouer le
  commandant, usage réel de certaines cartes, retours de partie, préférences propres à ce deck.
- **Mesures volumineuses à part** : si une séance produit beaucoup de chiffres bruts, mets-les
  dans `decks/séances/AAAA-MM-JJ Commandant — résumé.md` et ne garde dans la fiche que le
  verdict et le nom de ce fichier.
- Mets à jour `dernière_maj` à chaque écriture. Écris le fichier en UTF-8.
- **Annonce ce que tu vas écrire dans la fiche avant de l'écrire**, en une ou deux lignes.

## Le modèle

Les sections marquées *(si utile)* n'existent que si le deck en a besoin.

````markdown
---
commandant: <Nom exact ; face avant // face arrière si recto-verso>
identité: <ex. WUR, Sultai, Mono-bleu>
bracket_visé: <1-5>
plan: <aggro | value/grind | combo | mix — une ligne>
budget: <enveloppe par passe, ou plafond par carte>
règles_maison: [<cartes interdites par la table>]
table: <papier, 4 joueurs, 40 PV ; plateforme et lien éventuels>
dernière_maj: AAAA-MM-JJ
statut: <actif | en projet | démonté>
---

# <Commandant> — <identité>

**Résumé.** <Une phrase : par quoi le deck gagne.>

## Cadrage

| Paramètre | Valeur |
| :--- | :--- |
| Commandant | <nom> `<coût>` — <type>, <F/E> |
| Déclencheur | « <oracle exact de la capacité qui compte> » |
| Type de récompense | <fréquence ou volume ; plafond éventuel> |
| Plan de victoire | <…> |
| Bracket | visé <N> ; réel <N> — <n> Game Changers, <n> combos, vérifié le AAAA-MM-JJ |
| Budget | <enveloppe ; dépensé à ce jour au prix réel> |
| Règles maison | <cartes interdites> |
| Terrains | <N> |
| Total | 99 + commandant, vérifié le AAAA-MM-JJ |

**La clause qui gouverne tout :** <le fait de l'oracle qui décide de ce qui compte et de ce qui
ne compte pas ; ex. « permanents seulement », « once each turn », « with flash or haste ».>

## Paramètres de jeu

- Niveau du joueur ; douleurs vécues, par priorité : <…>
- Table : <nombre de joueurs, défense habituelle, ce qui a été observé en partie>
- Façon de jouer : <usage réel du commandant et des cartes clés>
- Préférences propres à ce deck : <exclusions, cartes intouchables>

## Condition de succès *(si utile)*

<Ce qu'on mesure, en une phrase : ex. « avoir 4 déclenchements par tour au tour 6 ».>

## Composition par rôle — AAAA-MM-JJ *(si utile)*

| Rôle | Nb | Quota visé | Cartes |
| :--- | :--- | :--- | :--- |

## Points ouverts

- **<faiblesse connue, non corrigée>** — <chiffre, source, test qui fermerait la question>

### Points ouverts levés *(si utile)*

- ~~<ancien point>~~ **Infirmé / corrigé le AAAA-MM-JJ.** <pourquoi>

## Décisions tranchées, à ne pas rouvrir *(si utile)*

- **<carte> reste** — <raison, qui a tranché, date>

## Lectures d'oracle à ne pas re-dériver *(si utile)*

- **<carte>** : <ce que dit vraiment la clause, ruling vérifié le AAAA-MM-JJ>

## Alertes d'outil vérifiées fausses *(si utile)*

- <alerte, outil, et pourquoi elle est fausse pour ce deck>

## Cartes à ne jamais ajouter *(si utile)*

- **<carte>** — <combo qu'elle fermerait, refus du joueur, ou règle maison>

## Pièges de pilotage *(si utile)*

- <séquençage, timing d'un déclencheur, ordre de la pile…>

## Liste actuelle — AAAA-MM-JJ (vN)

```
1 <Commandant>

1 <Carte>
…
```

Total vérifié : 99 + 1 commandant, <N> terrains. Identité et légalité contrôlées le AAAA-MM-JJ.

## Historique

### AAAA-MM-JJ — vN, <titre court>

- **Entrées** : <cartes> — <coût au prix réel>
- **Sorties** : <cartes>
- **Motif** : <le défaut traité, dans les mots du joueur, et le principe qui le porte>
- **Effet mesuré** : <métrique avant → après, outil, nombre de parties, bruit> — ou « aucune mesure »
- **Réserves** : <propositions refusées et pourquoi ; limites de l'instrument ; erreurs rattrapées>

### Antérieur au AAAA-MM-JJ — état non tracé

<Ce qu'on sait de la liste reçue au départ : nombre de cartes, terrains, coût moyen.>
````

## L'entrée d'historique

- Elle existe **même sans changement de liste** quand une séance a établi quelque chose : une
  mesure de référence, un audit de rôles, un combo assumé à déclarer avant les parties.
- Ajoute au besoin : **Coût** (prix réel contre prix annoncé par l'outil), **Écartées en cours de
  route** (carte, prix, raison), **Annulation** (une version annulée se trace aussi, avec la cause).
- Le motif dit **pourquoi** ; l'effet mesuré dit **combien et avec quoi**. Un écart sous le bruit
  s'écrit « sans coût mesurable », pas « gain ».
