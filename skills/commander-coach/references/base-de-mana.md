# Base de mana : terrains, sources, couleurs, courbe

Quand lire ce fichier : en phase 4 (base de mana), et dès qu'une question touche au nombre de
terrains, à la rampe, aux couleurs, aux terrains engagés ou à la courbe ; avant d'annoncer qu'un
deck a trop ou pas assez de terrains ; quand deux sources ou un outil donnent des chiffres différents.

Chiffres relevés au 17/10/2026. Ce qui se périme est listé à la fin, avec la façon de le revérifier.

## Les sources et ce qu'elles valent

| Source | Apport | Niveau de preuve |
| :--- | :--- | :--- |
| Frank Karsten (2022, mis à jour 2025) | Sources colorées en 60 et en 99 cartes, régression du nombre de terrains, seuils de mulligan | Modèle mathématique |
| Kelvin Chen (2023) | Régression de Karsten transposée aux singletons de 100 cartes, conventions de calcul, repères par cycle | Méthode publiée sur le modèle de Karsten ; écrite pour le Canadian Highlander (duel, 20 PV), concepts déclarés valables en Commander |
| Schulze (2019) | Sources effectives, cibles 40/46, couleurs en multijoueur, mulligan gratuit intégré | Raisonnement causal, sans validation indépendante |
| ScrollVault (2026) | Nombre de terrains par profil de deck, budget d'engagés, hiérarchie du fixing | Site à liens affiliés ; extrapolations Commander propres au site |
| EDHREC / MtGDS (2022) | Courbe moyenne des decks publics | Descriptif, aucune donnée de victoire |
| Mesures de séance | Calculs hypergéométriques, simulateurs écrits pour l'occasion | Mesuré, un deck à la fois ; « reproduit » si une seconde implémentation a confirmé |

Annonce le niveau de la meilleure source, pas le nombre de sources d'accord (construction-et-choix.md).

## 1. Le plan avant la formule

- **Écris d'abord le seuil de mana du plan** : « de combien de mana ai-je besoin, à quel tour, pour
  que ce deck fasse ce qu'il fait ? ». Une formule fondée sur le coût moyen ne voit pas un point
  précis : un combo qui doit produire 6 manas, dans un deck où aucune carte ne coûte 6, reçoit trop
  peu de terrains (premier mode d'échec décrit par Chen). Seuil absent de la courbe : abandonne la
  formule, calcule directement (section 4).
- **La condition de succès, en une phrase mesurable, précède tout réglage de ressources** : une
  meilleure courbe ne prouve rien sans elle (construction-et-choix.md, mesure.md).
- **Choisis les non-terrains avant les terrains** (Chen) ; **teste d'abord les décisions gratuites**,
  car la politique de mulligan change le nombre de sources nécessaire (section 3) ; **valide l'outil**
  sur trois cartes atypiques (coût X, coût alternatif, fetchland, face arrière) : outils.md.

## 2. Combien de terrains

| Situation | Terrains | Source |
| :--- | :--- | :--- |
| Deck Commander moyen | 36 | Simulations de ScrollVault ; templates publiés : 35-38 (construction-et-choix.md) |
| Cartes décisives payées à 6 ou plus, commandant compris | 37-38 et au moins 10 rampes | ScrollVault ; même sens qu'une mesure de séance (ci-dessous) |
| cEDH combo : mana rapide, courbe très basse | 28-30 | ScrollVault |
| Ajustement | −1 sous 2,5 de coût moyen, +1 au-dessus de 3,5 | ScrollVault, non mesuré ici |

- **Annonce une fourchette, sa source, et justifie la position par le plan**, jamais un quota comme règle.
- **Choisis sur le coût des cartes qui font gagner, pas sur la moyenne.** Mesuré (finishers à 6,
  99 cartes constantes) : trois terrains de plus contre trois rampes et pioches bon marché donnent
  6 manas au tour 6 dans 65,1 % des parties contre 59,8 %. La rampe ne gagnait que pour avoir
  quelque chose à jouer avant le tour 4.
- **Compte le coût effectivement payé** : en réanimation, le coût du sort qui réanime ; avec le
  cycling, le coût de cycling (section 9). ⚠ Ouvert : un deck de réanimation à 36 terrains,
  19 créatures de valeur 6+ dont dix se cyclent pour 1-2 manas (coût moyen recalculé 3,05). Le test
  qui trancherait (même liste à 36, 37, 38 terrains, comparer le tour où le payoff arrive) n'a pas
  été fait : propose-le au lieu de trancher.
- **« Au-delà du quatrième terrain, rampe et pioche valent mieux que des terrains »** (Schulze)
  vaut pour 4 manas au tour 4, pas pour des finishers à 6 (mesure ci-dessus) : avant d'opposer deux
  sources, cherche la question sur laquelle chacune est calibrée (mesure.md).
- **Copier le nombre de terrains d'un autre deck** : point de départ seulement (Chen), après avoir
  comparé rampe et sélection. Exemple de Schulze : 36 terrains, mais 46,92 sources effectives grâce
  à 11 rochers, un Preordain et cinq cantrips.
- `mana-audit` affiche ses propres repères nommés « Burgess » et « Karsten », qui ne sont pas la
  régression ci-dessous : lis outils.md avant de citer son verdict.

**Régression de Karsten transposée par Chen (98-99 cartes) : un nombre de départ, pas une réponse.**

```
terrains = ((100 - commandants) / 60)
           * (19,59 + 1,90 * cmv_moy + 0,27 * commandants)
           - 0,28 * (rampe + pioche)
           - mana_rapide
           - 0,74 * mdfc_dégagées - 0,38 * mdfc_engagées
           - 1,35
```

- `- 1,35` couvre la pioche du premier tour et le mulligan gratuit. `commandants` : 1 ou 2.
  `cmv_moy` : valeur de mana des non-terrains divisée par leur nombre, mana rapide exclu des deux
  totaux, coûts corrigés selon la section 9.
- `rampe` : non-terrains de valeur ≤ 2 qui produisent du mana (Birds of Paradise, Lotus Petal,
  Mana Vault), augmentent un terrain (Utopia Sprawl), mettent un terrain (Nature's Lore) ou un sort
  (Aether Vial) en jeu. `pioche` : non-terrains de valeur ≤ 2 qui piochent ou mettent une carte de
  la bibliothèque en main (Elvish Visionary, Conjurer's Bauble, cycling bon marché).
- `mana_rapide` : non-terrains à coût 0 qui produisent du mana à chaque tour sans coût additionnel
  ni restriction, chacun pour un terrain plein. Les exemples de Chen (moxen d'origine, Mana Crypt)
  sont bannis en Commander ; reste surtout Chrome Mox. Mox Opal, Mox Amber : en rampe. Mox Diamond :
  exclu, il coûte un terrain.
- Écart admis par Chen : Sol Ring est un cas extrême, à compter 0,8 ou plus au lieu de 0,28.
- Contrôle de calcul : un commandant, coût moyen 3,0, 15 rampes et pioches, ni mana rapide ni
  MDFC → 1,65 × 25,56 − 4,2 − 1,35 ≈ 36,6. Vérifie ensuite les seuils qui comptent (section 4).

## 3. Sources effectives : deux modèles qui ne se comparent pas

| Carte | Schulze (causal) | Karsten via Chen (régression) |
| :--- | :--- | :--- |
| Terrain | 1 | 1 |
| Tuteur de terrain bon marché (Rampant Growth, Tithe) | 1 | 0,28 |
| Rocher, dork, Land Tax | 0,75 | 0,28 |
| Mana rapide à coût 0 (Chrome Mox) | 0,75 (c'est un rocher) | 1 |
| Sélection qui creuse plus d'une carte (Preordain) | 0,5 | 0,28 |
| Cantrip (Gitaxian Probe, Crash Through, Quicken) | 1/3 (suppose environ 33 % de terrains) | 0,28 |
| Cartes prises en compte | Lançables avant le tour 4, sans exigence de couleur raide | Valeur de mana ≤ 2 |

- **Cible de Schulze : 40 sources pour 90 %, 46 pour 95 %** d'avoir 4 manas au tour 4 (article
  de 2019, vérifié le 18/10/2026). Elle suppose sa politique de mulligan de l'époque : premier
  mulligan gratuit, mains de 7 à 0-2 ou 6-7 terrains rejetées ; sans rejeter les mains à deux
  terrains, il annonce 47 sources pour 90 %. En mars 2020, il a abandonné le comptage des rochers
  et cantrips en fractions : son modèle personnel est devenu 36 terrains ou plus et une dizaine de
  rampes à 2 manas ou moins.
- **Un rocher vaut 0,75 ou 0,5 selon la question** : 0,75 pour « lancer mon sort à 4 au tour 4 »,
  0,5 (ScrollVault) pour « toucher mes land drops », qu'un rocher n'aide pas. Dis laquelle tu poses.
- **Karsten contre Schulze : non tranché.** Explication avancée : la régression absorbe la rampe
  morte, détruite ou piochée trop tard, le raisonnement causal l'ignore ; à 10 rampes et 8 cantrips,
  l'écart atteint plusieurs terrains. Nomme le modèle à côté de chaque nombre, ne compare jamais un
  résultat de l'un à une cible de l'autre, départage par le calcul direct.
- **Sol Ring : quatre valeurs circulent** — 0,28 (formule), 0,8 ou plus (Chen), 0,75 (Schulze), deux
  sources (simulateur qui compte le mana produit). Aucune source ne les confronte : annonce la tienne.
- **Garde-fous.** Calcule avant de conclure : « tu rates un land drop dans 60 % des parties » sortait
  d'un compteur qui ignorait les rochers, pour un deck à 45,6, donc à la cible. Proche de 46, le
  problème est ailleurs. Le nombre de rochers ne dit pas le mana produit (huit rochers : 0,79 en jeu
  au tour 5, mesuré). La cible ne couvre ni les cartes décisives à 5 manas et plus (mesure-les à
  part), ni l'usage du mana : à 46,2 avec une seule carte à 4, le mana est inutilisable dès le
  tour 5 (section 5).

## 4. Calcul direct et seuils de fiabilité

- **Seuils** (convention de Chen, assumée comme personnelle) : 75 % pour une exigence non critique,
  85 % pour la plupart des métriques importantes, 90 % pour une critique. Annonce-le avec le résultat.
- **Paramètres** : population = bibliothèque (99, ou 98 avec deux commandants) ; échantillon =
  cartes vues, soit **7 + T au tour T à trois joueurs ou plus**, car personne ne saute sa première
  pioche (règles 103.8c et 800.7) ; en duel, le joueur qui commence voit 6 + T. Déduction : la
  correction « une source de plus quand on joue en premier » des nombres de Karsten ne s'applique pas
  en multijoueur. Le premier mulligan y est gratuit (règle 103.5c) : un calcul sans mulligan est
  pessimiste pour les mains vissées.
- **Contrôle de l'instrument** : 38 terrains sur 100 cartes → au moins 2 terrains en main de 7 dans
  82,33 % des cas, exactement 2 dans 28,42 %, aucun dans 3,07 % (exemple de Chen, recalculé à
  l'identique). Refais ce contrôle avant de te fier à un calcul écrit en séance.
- **Ne mélange pas modèle et calcul brut.** Les seuils de Karsten et de Schulze sortent de modèles
  (mulligan, hypothèses sur les land drops) ; le calcul brut donne moins : 29 sources sur 99 →
  environ 80 % d'en voir au moins deux parmi 9 cartes (tour 2 à quatre joueurs). Tout pourcentage
  annoncé dit de quel calcul il sort. Simulation, bruit, A/B, nombre de mains : mesure.md.

## 5. Courbe basse : chercher le puits avant de couper des terrains

Un deck agressif qui a trop de mana en fin de partie peut n'avoir rien à en faire. Mesuré
(hypergéométrique, 99 cartes, coût moyen 1,81, une seule carte au-dessus de 3, 11 accélérateurs) :

| Terrains | Main gardable (2-5) | Vissée (0-1) | Noyée (6-7) | Pioches mortes T6-T10 |
| :--- | :--- | :--- | :--- | :--- |
| 38 | 81,7 % | 17,1 % | 1,2 % | 1,92 |
| 35 | 77,5 % | 21,8 % | 0,7 % | 1,77 |
| 34 | 75,8 % | 23,5 % | 0,6 % | 1,72 |

- De 38 à 34 : 0,2 pioche morte évitée sur cinq tours, 6,4 points de mains gardables perdus. La queue
  haute est presque vide, la basse épaisse : on ne règle pas un problème de queue fine en déplaçant
  toute la distribution.
- Le vrai défaut : 5,89 terrains en jeu au tour 8 pour un sommet de courbe tenu par une seule carte à
  4. Correction : trois cartes à 4 (coût moyen 1,81 → 1,98) ; sorts lancés aux tours 6, 7 et 8 en
  hausse de 0,08, 0,06 et 0,05, pour un bruit mesuré à ±0,02.
- **Règle** : énumère ce que le deck ferait de son mana au tour 6 et au-delà ; si c'est « rien »,
  ajoute un puits (cartes plus chères, capacités activées, sorts à X) avant de couper, et ne coupe
  qu'après avoir chiffré séparément mains vissées et mains noyées.
- Limites : un seul deck ; le mulligan gratuit, non modélisé, allège le coût d'une main vissée et
  joue contre la conclusion. L'asymétrie des queues tient, pas le seuil exact où couper. ⚠ Chen
  estime au contraire que la formule donne trop de terrains (37 % de sources ou plus) à un deck qui
  ne veut jamais plus de 4 terrains en jeu. Question utile : trop de terrains, ou puits manquant ?

## 6. Couleurs : carte par carte, pip par pip

- **N'audite jamais sur le total de symboles par couleur.** Liste chaque carte à double ou triple
  symbole et confronte-la à son seuil, au tour où elle doit être lancée. Erreur d'origine : 43
  symboles blancs, 22 bleus, 15 rouges au total ; avec environ 21 sources blanches, une carte à
  {W}{W}{W} était inlançable sur la courbe, et six analyses ne l'avaient pas vu.

Sources colorées nécessaires selon Karsten (article de 2022, mis à jour le 13/02/2025, vérifié le
18/10/2026). Le coût se lit au tour où on veut lancer la carte : C au tour 1, 1C au tour 2, CC au
tour 2, 1CC au tour 3, etc.

| Coût | 60 cartes | 99 cartes |
| :--- | :--- | :--- |
| C | 14 | 19 |
| 1C | 13 | 19 |
| CC | 21 | 30 |
| 2C | 12 | 18 |
| 1CC | 18 | 28 |
| CCC | 23 | 36 |
| 3C | 10 | 16 |
| 2CC | 16 | 26 |
| 1CCC | 21 | 33 |
| 4C | 9 | 15 |
| 3CC | 15 | 23 |

- Seuil visé par Karsten : environ 90 % pour un sort à 1 mana, un point de plus par mana (91 % à 2,
  92 % à 3…), en probabilité d'avoir les bonnes couleurs sachant qu'on a assez de terrains,
  mulligans compris. Sa colonne 99 cartes intègre le premier mulligan gratuit et la pioche du
  premier tour en Commander.
- Il n'existe pas de multiplicateur unique de 60 à 99 cartes : le rapport va de 1,36 (C) à 1,67
  (4C). Lis la colonne 99 cartes.
- Schulze (2019, deck à 40 sources effectives) donne des ordres de grandeur voisins : 19 pour C,
  28 pour CC, 34 pour CCC. Quand une carte compte, calcule son cas (section 4).
- **Coûts multicolores** ⚠ : Schulze ajoute 1 à l'exigence par couleur au-delà de la première
  (4 couleurs : +3, soit 22 sources par couleur) ; Karsten ajoute 1 tout court. Annonce ta règle.
- Repères de Schulze : un deck multicolore moyen ne lance pas de double symbole au tour 2 ; à
  4 couleurs, les sources devraient produire 2 couleurs en moyenne. Command Tower, Arcane Signet et
  les Signets compensent en partie.
- **Ne comptent pas comme source d'une couleur** : sélection et cantrips, lancés seulement avec le
  mana déjà là (Schulze) ; terrains utilitaires, à ajouter en dernier (ScrollVault) ; Chrome Mox en
  multicolore, compté dans le total mais pour aucune couleur précise (Chen).
- **Source et source dégagée** : un terrain engagé est une source pour un sort au tour 4, pas au
  tour 1 ; compte les deux. Un fetchland est une source de chaque couleur qu'il peut chercher dans
  ce deck ; certains outils le comptent à zéro (outils.md).

## 7. Terrains engagés

- **Ce qui est sûr** : un terrain engagé ne produit rien le tour où il arrive ; ce mana est perdu,
  pas reporté. Premier terrain engagé → 0 mana au tour 1, puis 2 et 3 si les suivants arrivent
  dégagés. Pour un tour clé, seul compte le terrain posé ce tour-là.
- ⚠ **Formulation contestée** : ScrollVault écrit « en retard d'un mana à chaque tour suivant »,
  l'exemple ci-dessus ne montre de perte qu'au tour de pose. Ne reprends pas « à chaque tour » : dis
  qu'il coûte le mana du tour de pose, et que ce coût pèse quand ce tour est un tour clé ou quand le
  jeu perdu était une accélération (logique, non mesuré).
- **Mesuré** : un deck bleu-noir à 36 terrains dont sept arrivent engagés (Halimar Depths, Myriad
  Landscape, Temple of Deceit, Darkwater Catacombs, Sunken Hollow en début de partie, deux terrains
  sacrifiables qui cherchent un basique engagé). Modéliser l'engagement fait tomber la condition clé
  au tour 4 de 48,1 % à 35,1 % : treize points, plus que les couleurs (2,7) ; reproduit par une
  seconde implémentation. Mesure pessimiste (fastlands et checklands comptés toujours engagés) ;
  effet plus fort au tour 4 qu'au tour 8.
- **Budget** (ScrollVault, consensus non mesuré) : 4 à 6 engagés en Commander (0 à 2 en 60 cartes
  compétitif), chacun avec une contrepartie : un scry, trois couleurs, un type de base cherchable.
  Un bicolore engagé sans contrepartie n'a pas sa place.
- **Hiérarchie du fixing** (ScrollVault) : fetchlands > shocklands > fastlands > checklands (se
  dégradent quand les basiques sont rares) > painlands (un dégât par mana coloré) > engagés.
- **Applique la règle réelle de chaque terrain**, jamais une probabilité fixe : un modèle à
  probabilité fixe sous-estimait d'environ 10 points le commandant au tour 4 (mesuré).

| Type | Arrive dégagé si… |
| :--- | :--- |
| Fastland | on contrôle au plus deux autres terrains |
| Slowland | on contrôle au moins deux autres terrains |
| Checkland | on contrôle un terrain du type de base demandé |
| « unless you control two or more basic lands » | compter les basiques réellement en jeu |
| Terrain sacrifiable | lui-même dégagé ; le terrain cherché arrive engagé ou non selon la carte (Evolving Wilds : engagé) |

- En simulation, pose le terrain dégagé en priorité quand il faut du mana ce tour-ci, et vérifie
  que le simulateur active les capacités de mana qui coûtent du mana (Signets, filter lands) : mesure.md.
- **Après chaque modification, revérifie les seuils qui dépendent des basiques** : checklands
  (Chen : avec 20 terrains sur 100 qui ont ou cherchent le type voulu, un checkland présent dans la
  main de départ arrive dégagé au tour 1 dans environ 75 % des cas ; environ 80 % au tour 2,
  85 % au tour 3, 88 % au tour 4) ; terrains « unless you control N basics » ; effets qui comptent Plaines ou Montagnes
  (un terrain à deux types de base compte pour les deux).

## 8. Repères par cycle de terrains (Chen)

Calculés pour le Canadian Highlander (100 cartes, 20 PV, duel) : donne ce contexte avec eux.

| Cycle | Repère |
| :--- | :--- |
| Fetchlands | Tous ceux qui touchent une couleur du deck |
| Duals d'origine | Tous en 2-3 couleurs ; ceux des couleurs principales en 4-5 |
| Shocklands | Tous en 2-3 couleurs ; 3-4 en 4-5 couleurs, au-delà un handicap |
| Triomes | En 3 couleurs et plus, avec peu de sorts à 1 mana ; 4 sur 100 gardent sous 5-7 % le risque d'en voir deux ou plus en quatre tours, 6 sur 100 dépassent 10 % |
| Fastlands | Tous en 2-3 couleurs ; 3-4 en 4-5 |
| Painlands, horizon lands, City of Brass, Mana Confluence | Plafond global de 4 sur 100 sources douloureuses (moins contraignant à 40 PV) |
| Slowlands | À partir de 37 terrains sur 100 (environ 85 % de toucher ses deux premiers land drops, duel, en commençant) |
| Filter lands | 0-1, pour les doubles symboles dans deux couleurs |
| Pathways | Bons en bicolore ; en multicolore, préférer les terrains à plusieurs couleurs |

La qualité de la base de mana ne change pas le bracket ; seuls filtres : la liste des Game
Changers, où figurent quelques terrains, et le budget (bracket-et-combos.md).

## 9. Courbe : lire le coût réellement payé

- Les analyseurs comptent la valeur de mana imprimée. Avant de lire une courbe, isole coûts X,
  réductions, coûts alternatifs et cycling ; recalcule au coût d'usage, et dis-le en la présentant.
- Mesuré : un retrait à {X}{W}{W} rangé à 2 et une pioche à {X}{W}{U}{U} rangée à 3 → 16 cartes
  affichées à 2 pour 15 jouables au tour 2. Biais inverse : un sort à {3}{W} qui coûte {1}{W} dès
  le deuxième sort du tour est compté à 4 et joué à 2 ; une suspension se paie plus tard.
- Conventions de Chen pour le coût moyen :

| Cas | Valeur retenue |
| :--- | :--- |
| Coût alternatif presque toujours utilisé (Force of Will, transmutation) | Ce coût |
| Deux modes tous deux utilisés (Endurance, Brazen Borrower) | Le plus élevé |
| Delve | Coût coloré + 1 (Treasure Cruise → 2, Dig Through Time → 3) |
| Coût X | ⚠ La plus petite valeur de X réellement jouée (Chen) ; en séance, le coût d'usage habituel. Dis lequel tu prends |
| Carte scindée | La moitié réellement jouée (les sites additionnent les deux) |
| Suspension | Le coût de suspension |
| Carte jamais lancée (seulement réanimée ou mise en jeu par un combo) | Exclue des deux totaux |

- Cycling : 19 cartes de valeur 6+ sur 99, coût moyen affiché 3,79, recalculé au coût de cycling
  3,05 (mesuré). Le landcycling est un tuteur de terrain : cinq basiques ont été coupés pendant que
  le vissage de couleur baissait. Évaluer ces cartes : construction-et-choix.md ; ce que les outils
  lisent mal (réductions, cycling, MDFC comptées comme terrains) : outils.md.
- Courbe EDHREC (decks publics, hors terrains, article MtGDS du 14/04/2022) : pic à 2-3 manas (15,7
  et 15,4 cartes), 9,5 à 4 ; les commandants à 4 s'entourent d'un peu plus de cartes à 4 (9,7),
  contre le conseil inverse de The Command Zone. Sans donnée de victoire : décris, ne recommande pas.

## 10. Procédure base de mana, pas à pas

Les ⚠ marquent un désaccord à présenter, pas à trancher. Cette phase ne coûte aucun bracket.

0. **Prérequis** : condition de succès mesurable, non-terrains choisis, mulligan testé, outil validé (§ 1).
1. **Corrige la courbe** au coût d'usage : X, réductions, suspension, cycling, delve. ⚠ Valeur d'un X (§ 9).
2. **Écris le seuil du plan** ; absent de la courbe → calcul direct, seuil annoncé (§ 1, § 4).
3. **Fixe un nombre de départ** : 35-38 selon le coût payé des cartes qui gagnent, ou la régression.
   ⚠ Finishers qu'on ne paie pas (§ 2).
4. **Calcule les sources effectives en nommant le modèle.** ⚠ Karsten contre Schulze, Sol Ring (§ 3).
5. **Avant de retirer un terrain**, chiffre les deux queues et cherche le puits. ⚠ Decks agressifs (§ 5).
6. **Audite les couleurs carte par carte**, sources dégagées à part. ⚠ Symbole simple, multicolore (§ 6).
7. **Budgète les engagés**, règle réelle de chaque terrain. ⚠ Coût exact d'un engagé (§ 7).
8. **Revérifie les seuils qui dépendent des basiques** ; repères par cycle (§ 7, § 8).
9. **Mesure, puis clos** : un écart sous le bruit n'est pas un résultat (mesure.md) ; note dans la
   fiche du deck le modèle et les seuils retenus (fiche-de-deck.md).

## Chiffres à ne pas reprendre, données à revérifier

- **Ne cite pas** « 12 sources pour un double symbole ≈ 75 % » (taille de deck et tour inconnus),
  ni « la régression de Karsten a été faite sur des decks gagnants » (non sourcé).
- **Revérifie le jour de l'analyse** : sources colorées → article le plus récent de Karsten, qui donne
  le tour de chaque nombre ; formule et repères de Chen → son article de 2023 sur les bases de mana
  des singletons ; bannissements (Mana Crypt, moxen) → `scryfall_card_details` ; courbe EDHREC →
  pages commandant actuelles ; Game Changers → bracket-et-combos.md ; outils de deck-wizard → outils.md.
