# Mesurer un changement (phase 6)

Quand lire ce fichier : avant de lancer un goldfish, un tirage de mains, une simulation écrite en
séance ou une comparaison entre deux versions d'une liste ; avant d'annoncer un chiffre qui fonde
une coupe, un achat ou un verdict ; quand un résultat paraît trop net ou contredit la table.

**D'où viennent les chiffres.** De séances réelles sur des decks Commander papier, avec des scripts
écrits en séance. *(sim. complète)* : parties à quatre simulées sous Forge, non fourni avec ce
skill ; n'en garde que la leçon et l'ordre de grandeur. Récits complets : `cas-d-ecole.md`.

## 1. Choisir l'instrument : ce que chacun tranche

| Instrument | Ce qu'il tranche | Ce qu'il ne voit pas | Rôle |
| :--- | :--- | :--- | :--- |
| Calcul hypergéométrique | Probabilité d'avoir une carte ou une catégorie en main au tour T | Lançabilité (couleurs, mana), terrains engagés, tout ce qui se passe en jeu | Premier filtre ; second chemin d'un script |
| `playtest-goldfish` (deck-wizard) | Gardes au mulligan, terrains et sorts lancés par tour, vissage de couleur | Tour de victoire, cartes vues, combos, dégâts, terrains engagés, adversaires | Ressources seulement (§5) |
| Goldfish à la main ou script de goldfish | Tour de victoire, cartes vues, séquençage réel | Interaction, politique de table | Comparer deux variantes de la même liste |
| Simulation écrite en séance | Disponibilité de chaque pièce, assemblage de la condition de succès | Adversaires (chiffres optimistes), tout ce qui n'est pas codé | Trouver le goulot (§6) |
| `playtest-match` (deck-wizard) | Une partie entre IA, en duel ; absent sans `playtest-install-phase` (compilation Rust de 5 à 10 min, git et cargo requis) | La table de quatre (§4) | Test de fumée seulement |
| Parties réelles du joueur | Ce qui sort, ce qui meurt, ce qui ne sert jamais | Les taux : trop peu de parties (§8) | Validateur final ; compter des événements |

- **Test de la chaîne causale** (relecture critique externe) : écris « X augmente la probabilité
  de Y, donc améliore l'issue ». Si la seconde flèche n'est pas mécanique, l'instrument ne tranche
  que Y : il écarte les candidats dominés, il ne désigne pas de vainqueur. Passe aux parties
  réelles dès que l'avantage dépend de survie, d'interaction, de tempo ou de politique à quatre.
- **Le raisonnement seul élimine les erreurs certaines** (« cette clause vise la main »), pas les
  jugements stratégiques (« cette carte est incohérente » dépend de sa fréquence d'usage).
- **Ordre d'une campagne** : exploration bon marché (calcul, goldfish, script) → peu de candidats
  choisis → parties réelles → confirmation sur des parties qui n'ont pas servi à choisir.
- **Vérifie que l'instrument voit le mécanisme du deck** ; sinon écris « aucune mesure » et chiffre
  à la main. Un compteur de sorts lancés, qui met Arcane Signet à égalité avec Purphoros, a pénalisé
  (8,61 → 8,27 sorts sur 8 tours, sur un deck de duel) une passe qui comblait justement le trou de fin de partie.

## 2. Quand ne pas mesurer

- **Pose d'abord la question du gain minimal** : « quel gain justifierait cette concession ? ».
  « Aucun » : ne teste pas. « Au moins cinq points » : dimensionne pour cinq points (§8).
- **Une contrainte dure décide déjà** : budget, carte refusée, bracket, règle maison, identité
  voulue du deck. Élimine-les avant de choisir les expériences.
- **La question est de règles ou d'oracle** : lis, ne simule pas. Teferi, Mage of Zhalfir ne donne
  le flash qu'aux cartes hors du champ de bataille : zéro déclenchement pour Sonic.
- **L'échantillon possible ne peut pas détecter l'effet cherché** : dis-le avant, au lieu de
  lancer la mesure puis de lire du bruit.
- **La liste est gelée** (imprimée, achetée) tant que le joueur ne relance pas ; **les parties
  réelles ont déjà tranché** : leur retour prime sur les probabilités.

## 3. Cadrer la mesure avant de la lancer

- **Traduis la plainte en métrique.** « Inconsistant » était un vissage de couleur à 53,2 %
  (Sonic), pas l'éparpillement qu'un outil classait premier. Ne compare jamais deux « sévérités »
  d'outil sans savoir comment chacune est calculée.
- **Mesure la condition de succès, pas une ressource.** Runo se transformait au T5 dans 70,9 % des
  parties, mais le payoff réel (Krothuss qui copie une *autre* attaquante) n'arrivait que dans
  6,4 % : quatre versions avaient été optimisées sur la ressource.
- **Cale la condition sur le bracket visé.** « 40 points à chaque adversaire », forme cEDH, a fait
  passer pour un échec un deck de bracket 3 qui draine 14 points à toute la table, fiablement.
- **Fixe avant de voir les résultats** : métrique, tours examinés, définition d'une main gardable,
  seuil de décision, nombre maximal de comparaisons. Ne compose jamais une métrique après coup : le
  calcul ne coûte rien, mais chaque réglage choisi après coup sur-optimise l'instrument.
- **Mesure la liste réellement appliquée.** Un « effet de la passe » a déjà été publié sur une liste
  qui contenait une carte jamais ajoutée, et pas celle que le joueur avait mise.
- **Une heuristique contredit ton résultat** : cherche sur quelle question elle est calibrée ; si
  c'est la même, teste au lieu de débattre (`base-de-mana.md`).
- **Plusieurs critères** (performance, prix, esthétique, complexité) : présente les options côte à
  côte, pas un score arbitraire. On ne paie pas un compromis dont un seul côté est chiffré.

## 4. Mesurer au format joué : la table de quatre

- **Rien de ce qui est mesuré en solitaire ou en duel ne conclut pour une table de quatre.** Le
  duel ne sert qu'au test de fumée : la liste se charge, le commandant arrive, rien ne plante.
- *(sim. complète)* Tour de fin moyen 9,6 en duel miroir contre 25 à quatre : une carte à 6 manas
  ou plus n'est jamais lancée dans une partie qui finit au T9. Un precon à 66,7 % de victoires en
  duel a fait 0 sur 16 à quatre : trois sources de dégâts, 120 points à infliger au lieu de 40.
- **Nuance** (relecture critique externe) : le duel servirait de filtre si ses écarts entre versions
  suivaient ceux mesurés à quatre. Non démontré : n'en conclus rien.
- **Code les règles du multijoueur dans tout script** (vérifiées le 17/10/2026) : personne ne saute
  la pioche de son premier tour (CR 103.8c) ; le premier mulligan est gratuit (CR 103.5c). Un script
  « premier joueur sans pioche » ou qui compte chaque mulligan mesure un duel, plus pessimiste.
  `playtest-goldfish` ne modélise pas le mulligan gratuit (revérifié le 18/10/2026 sur la version
  du 14/10 ; `outils.md`).
- **Demande la durée réelle des parties du joueur** avant de juger une carte chère, et **comment sa
  table défend** avant de chiffrer de l'évasion ou une protection (§7).

## 5. Goldfish et tirages de mains

**Protocole de goldfish.** Goldfisher sans compter ne mesure rien.
1. Vingt mains de départ, garde ou mulligan avec la raison : cela calibre la politique de mulligan.
2. Goldfish des cinq premiers tours, répété, en séquençant réellement les terrains.
3. Sur chaque main jouée jusqu'au bout, relève **le tour de victoire** (condition de succès
   remplie sur une table sans interaction) et **les cartes vues** (piochées ou cherchées).
4. Simule l'interaction adverse (sort clé contré, commandant retiré) puis l'aléa (moteur de pioche
   contré au T1, Wheel adverse, wrath).
5. Trois vraies parties au minimum avant tout changement majeur.

- **Deux nombres, toujours** : le tour de victoire parle du plan complet, les cartes vues de la
  consistance (22 cartes vues contre 34 pour un même T9 : pas le même deck). Plus l'écart-type sur
  plusieurs graines (§8). Compare des variantes de la même liste, jamais un chiffre dans l'absolu.
- **`playtest-goldfish`** (revérifié le 18/10/2026 sur la version du 14/10) : garde 2 à 5 terrains
  avec un sort à 3 manas ou moins ; mulligan sans gratuit, main de 6, 5 puis 4 cartes tirée
  directement (pas de vrai londonien : rien n'est vu puis remis dessous) ; toujours à la pioche ;
  commandant mélangé dans la bibliothèque ; un terrain par tour, tous dégagés sauf les fetchs
  engagés ; sorts du moins cher au plus cher. Il rapporte gardes, terrains et sorts par tour,
  vissage ; ni tour de victoire, ni cartes vues (son aide annonce un « combo timing » absent de la
  sortie). Ses chiffres mesurent cette politique (§9). Champs qu'il lit mal : `outils.md`.
- **Script de tirages de mains** : graine fixe, 20 000 tirages, règles du multijoueur, rôles
  comptés ; un goldfish de ressources, pas une simulation : dis-le. Donal (premier joueur sans
  pioche, donc un peu pessimiste) : en jeu au T4 dans 64-66 % seulement, condition recalée au T5
  (74,8 %) ; un 37ᵉ terrain ne rapportait que 1 à 2 points, « ne vaut pas un sort ».
- **Un goldfish fait un second chemin** pour un calcul : 81,7 % de mains gardables calculés contre
  81,2 % au goldfish. Un désaccord se résout avant de publier.

## 6. Simulation écrite en séance : deux couches

La couche ressources (mana par tour, mains gardées, sorts joués) rassure ; seule la couche
assemblage (toutes les pièces du succès réunies au même tour) répond à « est-ce que ça marche ».

0. **Audite la politique de jeu** (§9) avant toute autre mesure.
1. **Couche ressources** : code-la, ne recommande rien sur sa seule base.
2. **Couche assemblage** : écris la conjonction des conditions du succès, teste-la tour par tour,
   et **publie la disponibilité de chaque composant séparément**.
3. **Recommande d'abord sur le composant le plus bas.**
4. **Plusieurs graines, écart-type, seuil annoncé** (§8).

**Exigences du script** :
- Toute carte du deck absente des données lève une erreur fatale (`Troll of Khazad-dum` sans
  accent ne s'appariait pas à `Khazad-dûm` : la carte disparaissait sans bruit).
- Le commandant part de la zone de commandement, disponible près de 100 % : Muldrotha sortait à
  0,0 % (pioché dans les 99) sous des chiffres d'assemblage plausibles ; corrigé, 98,3 %.
- Terrains engagés modélisés (les oublier gonflait un résultat de 13 points : 48,1 → 35,1 %),
  couleurs payées symbole par symbole, règles du multijoueur.
- Un témoin bête par paquet : des terrains de base à sa place. Sur Runo, neuf cartes de sélection
  faisaient 24,3 %, neuf Îles 26,5 %, neuf créatures à cycling 48,1 % (mesuré avant la prise en
  compte des terrains engagés : seuls les écarts comptent).

**Ce que la décomposition a montré** :
- The Archimandrite : ressources correctes à tous les tours, conjonction à 11,0 % au T8 (aucun
  moyen de franchir les bloqueurs) ; 23,6 % après ajout d'évasion.
- Muldrotha : cimetière à 23,8 cartes au T14, assez ; goulot = redondance de la conversion
  (hypergéométrique, vu en 20 cartes : 1 copie 20,2 %, 3 copies 49,6 %, 5 copies 68,5 %, 7 copies
  80,5 %). Quatre convertisseurs ajoutés : disponibilité 46,9 → 78,0 %, létal 8,54 → 8,36 %, sous
  le bruit (deux relevés de la séance divergent : retiens l'ordre de grandeur). La bonne redondance sur le mauvais axe : ce plan ne pouvait pas atteindre la condition.

**Limites à dire** :
- Sans adversaire, toute probabilité est une borne haute et tout tour une borne basse.
- Si le script ne modélise pas le plan de l'autre version (bibliothèque vide, combat), le résultat
  dit « meilleur au plan modélisé », pas « meilleur ».
- **Un instrument est daté du plan pour lequel il a été écrit.** Quand le plan change, énumère par
  quoi la nouvelle version gagne et vérifie que le script voit chacun de ces chemins (Muldrotha a
  demandé une troisième couche, le combat, en passant aux jetons et à l'évasion).

## 7. Comparer deux versions

- **Une variable à la fois.** Avant d'attribuer un effet, liste tout ce qui a bougé avec le
  paramètre ; s'il y en a plus d'un, neutralise les autres ou ne conclus pas.
- **Paquet pour décider, témoin pour attribuer.** Un paquet cohérent, indétectable carte par carte,
  s'accepte ou se rejette en bloc ; ne le dissèque que si l'information change une décision. Pour
  attribuer, éteins un seul mécanisme, tout le reste égal, jamais d'après la forme de la courbe.
  Muldrotha : +25 points de taux de kill crédités à l'évasion ; sans les deux cartes d'évasion, elle
  ne valait que +2,0 points à 2 bloqueurs (80,2 contre 78,1 %), +15,1 à 12 (31,8 contre 16,7 %).
- **Apparie les deux bras** : mêmes graines. Dans un script, mélange des positions et remplace la
  carte à sa place : les deux versions voient les mêmes tirages, sauf la carte changée. Publie
  l'écart apparié et son bruit. Var(B − A) = Var(A) + Var(B) − 2·Cov(A, B) : l'appariement n'aide
  que si la corrélation est forte, vérifie-la.
- **Multiplicité** : enchaîner des comparaisons et garder chaque gagnant accumule les faux positifs
  et surestime le vainqueur. Fixe le nombre de comparaisons ; confirme le gagnant sur des graines
  neuves, jamais utilisées pour choisir.
- Une modification peut améliorer la ressource mesurée et dégrader la qualité des cartes piochées :
  regarde ce qui est vu, pas seulement combien.

## 8. Bruit, taille d'échantillon, écart minimal détectable

- **Aucun écart sans son incertitude.** Sous le bruit, écris « indistinguable » ou « sans coût
  mesurable », jamais « légèrement meilleur », et dis quel effet l'échantillon pouvait détecter.
- **Réplications = graines différentes** : un seul long passage ne donne aucun écart-type.
- **Seuil** : rien n'est annoncé sous environ deux écarts-types mesurés entre graines. Entre deux
  bras non appariés, l'écart-type de la différence vaut celui d'un bras × 1,4.
- **Bruit d'un taux sur n parties** : σ ≈ √(p(1−p)/n), × 100 pour l'avoir en points. À 1 000
  parties (défaut de `playtest-goldfish`, revérifié le 18/10/2026), σ ≈ 1,6 point près de 50 % ; à 20 000,
  σ ≈ 0,35. Les séances ont mesuré 0,2 à 0,9 point entre graines sur 12 000 à 21 000 parties :
  même ordre. Une dispersion entre graines bien plus large que la formule signale un défaut.
- **Écart minimal détectable** (80 % de chances, risque 5 %) ≈ 2,8 × σ de la différence ; effectif
  par bras ≈ 16 σ² / δ² pour une grandeur continue. Dimensionne avant de lancer.

**Tour de fin contre taux de victoire** *(sim. complète ; onze parties de calibrage à quatre :
tours 30, 19, 24, 26, 26, 27, 21, 28, 23, 23, 24 ; moyenne 24,6, σ 3,2 tours)*

| Écart à détecter | Parties par bras |
| :--- | :--- |
| 3 tours de fin | 18 |
| 2 tours | 40 |
| 1,5 tour | 71 |
| 1 tour | 158 |
| 5 points de victoire autour de 25 % | ~1 250 |

Effectifs recalculés par la formule, à 80 % de chances et 5 % de risque. La métrique continue
coûte dix à vingt fois moins de parties : « quatre-vingts parties par bras sur le tour de fin
valent mieux que deux mille sur le taux de victoire ». Ce choix est contesté (§10).

- **Parties réelles** : si leur écart-type ressemble à celui de la simulation (3 tours), dix parties
  par version ne détectent qu'un écart d'environ 4 tours, et aucun taux de victoire. Elles comptent
  des **événements** : combien de fois la carte a été lancée, a servi, est morte. Un combo qu'on
  avait en main dans 22 % des parties au T6 (calcul) n'a servi qu'une fois en une cinquantaine de
  parties (en duel) ; le joueur qui juge le burn « assez trivial » a confirmé une mesure.
- **Erreur symétrique** : conclure à l'absence d'effet sur un échantillon trop petit. Absence de
  différence significative n'est pas équivalence : fixe d'avance la marge indifférente. Quatre
  terrains donnant du rouge sont sortis indistinguables (σ 0,3 à 0,5 point) : si un écart sous un
  point est négligeable pour le joueur, la Montagne à 0,10 € plutôt que le fastland à 2,16 €.
- **Lecture** : Sonic, retrait d'une carte, vissage 36,7 → 35,8 % pour une dispersion de 1,3 : sans
  coût, pas gain ; un écart de 10,2 points, 3,4 fois la plus grande dispersion : solide.

## 9. Politique de jeu codée en dur

- **Toute décision que le simulateur prend à la place du joueur est une hypothèse** déguisée en
  constante : mulligan, terrain posé, ordre des sorts, cible. Énumère-les et teste chacune comme
  une variante, avant toute autre mesure.
- The Archimandrite : jeter les mains à 2 terrains fait passer le commandant au T5 de 68,8 à 76,4 %
  (+7,6 points, zéro euro) ; le meilleur paquet d'échanges valait +3 points pour une trentaine
  d'euros. Six analyses avaient été faites à travers la règle par défaut, avec des achats
  recommandés pour compenser un défaut du modèle. Contrepartie : mains gardées à 7, 80,0 → 51,4 %.
- Muldrotha : « terrains seuls » 12,6 % et « couverture de rôles » 12,3 % (σ 0,47),
  indistinguables ; mulliganer strictement coûtait 4,6 points. Teste ce levier deck par deck.
- Un mauvais séquençage mesure un joueur médiocre, pas un deck. L'IA d'un simulateur fait partie de
  l'expérience : un bon score peut vouloir dire que le deck est plus facile à piloter pour elle.

## 10. Tour de fin ou rang final : une contradiction non tranchée

- **Position du projet d'origine** : métrique principale = tour de fin de partie, continue, dix à
  vingt fois moins coûteuse ; taux de victoire en information secondaire.
- **Objection d'une relecture critique externe** : le tour de fin est une propriété de la table,
  pas de la qualité du deck. Une version plus forte peut finir plus tôt en gagnant ou en se faisant
  éliminer, ou plus tard par résilience ; un siège sur quatre dilue l'effet ; le σ vient d'un
  miroir. Elle propose victoire ou rang final en principal, tour d'élimination du deck testé en
  secondaire (parties sans élimination comptées comme censurées) ; dégâts, permanents et cartes
  vues en diagnostic seulement, chacun favorisant un archétype.
- **Ambiguïté à lever** : « tour 25 » global, tour de table ou tour d'un joueur peut multiplier un
  effet annoncé par quatre. Dis lequel.
- **Que faire** : choisis la métrique avant de mesurer, dis pourquoi et ce qu'elle ne voit pas.
  Dans un journal de parties, relève tout par partie (vainqueur, rang du deck, tour de sa victoire
  ou de son élimination, tour de table de fin) et décide d'avance quelle colonne tranche. En
  goldfish, la question ne se pose pas : le tour de victoire est celui du deck seul.

## 11. Valider l'instrument avant de croire le chiffre

- **Le mode d'échec dominant est le résultat plausible et faux, pas le plantage.** « Ça tourne sans
  erreur » ne valide rien. Un avertissement d'une ligne suivi d'un rapport complet rend tout le
  rapport suspect, même ses parties justes : `deck-tune` dégradé annonçait interaction 0 et 49
  cartes sur 63 « poids mort » (78 %) ; réparé, interaction 10 et 0 %.
- **Signes d'instrument cassé** : zéros partout ; trois variantes censées différer au même chiffre
  (35,5 / 35,4 / 35,7 % pour trois familles de terrains) ; un composant à zéro qui ne devrait pas
  l'être ; un résultat trop net. Vérifie aussi le résultat conforme à l'attente : 52,7 % ont été
  acceptés parce qu'ils confirmaient un diagnostic attendu.
- **Un cas dont tu connais la réponse** dans tout protocole de tri : s'il est mal rangé, jette
  l'instrument, pas le témoin. Avant de conclure qu'un réglage est sans effet, vérifie qu'il est lu,
  avec une valeur extrême dont l'effet est connu.
- **Trois cartes atypiques à la main** avant de citer un outil (coût alternatif, coût X, terrain
  qui ne produit pas de mana, face arrière) : deux minutes. Un outil compte comme nul, sans erreur,
  tout champ qu'il ne sait pas lire (cas dans `outils.md`).
- **Un chiffre qui fonde une recommandation se produit deux fois**, par un chemin qui ne partage
  ni le code, ni les données intermédiaires, ni l'hypothèse du premier. « Commandant au T4 :
  52,7 % » venait d'un test `"W" in ("RW",)` faux (seize terrains bicolores dans aucune couleur) ;
  un second script écrit autrement a donné 79 %. Réécrit de zéro par un second agent, un script a
  révélé deux bugs qui se compensaient (+3,1 et −2,1 points), puis convergé à 35,1 % au dixième.
  Deux calculs qui lisent le même champ ne font qu'un chemin : un audit maison a hérité du défaut
  de l'outil qu'il contrôlait (59,1 % de vissage annoncé, problème largement fabriqué).
- **La concordance valide le calcul, pas la grandeur** : vérifie à part que ce que tu comptes est
  ce dont tu parles. Un écart entre chemins peut informer : Jarad à 18,5 % en simulation contre
  20,2 % en hypergéométrique, l'écart est le coût de lançabilité.
- **Un contradicteur que tu diriges contrôle l'exécution, jamais le cadrage** : sept contrôles et
  une passe adverse partageaient la prémisse d'une coupe fausse, que le joueur a vue en une phrase.
- **Un feu vert hérite des défauts de sa mesure** : remonte sa provenance, cherche les
  contradictions du même rapport (« wincons : ok » à côté de « top_end : thin »). Avant d'accuser
  un défaut technique, compte combien d'autres cas le portent sans échouer.
- **Une mise à jour d'outil change la mesure** : remesure la référence, jamais deux bras sur deux
  versions *(sim. complète : tour de fin moyen 22,9 → 20,7 d'une version à l'autre)*.
- **Le joueur mesure le réel.** « Je ne la lance jamais », « le burn est trivial » contredisent ton
  chiffre : cherche l'hypothèse qui rend sa remarque vraie, ne défends pas le chiffre.

## 12. Si le joueur simule contre des adversaires

Valide le banc avant la première expérience, dans cet ordre :
1. **Platitude** : aucun adversaire au-dessus de 45 % ni sous 10 %, quatre parts proches de 25 %.
   Un adversaire qui ne gagne jamais transforme la table de quatre en table de trois, sans erreur.
2. **Zone sensible** : le deck testé entre 25 et 45 % (sinon, effet plafond ou plancher).
3. **Cohérence** : 100 cartes, commandant reconnu, aucune carte inconnue du moteur.
4. **Conformité** au bracket visé et aux règles maison : un adversaire qui joue une carte interdite
   à la table du joueur accélère plus que la vraie table.

- **12 à 16 parties = contrôle de plausibilité, pas certification.** À 25 % réels, 0 sur 16 a 1 %
  de chances ; mais 0 sur 16 reste compatible avec un taux réel proche de 20 % (borne haute à
  95 %). *(sim. complète : premier banc à 7, 6, 3 et 0 victoires sur 16 ; le deck à 0 fonctionnait,
  il était hors de rythme.)*
- **Fige le banc** pour toute l'optimisation du deck et consigne-le dans sa fiche ; garde un lot de
  confirmation qui ne sert jamais à choisir, sinon le deck s'adapte au banc. Fais tourner les deux
  versions sur les quatre sièges et permute les adversaires.
- **Parties anormales** (IA bloquée, partie coupée par une limite de durée) : ne les retire pas,
  rapporte leur taux par version, dis que la métrique est tronquée *(sim. complète : 20 sur 112)*.
  Conclus « meilleure sous cette politique et ce banc », pour deux versions du même archétype.
- **Seuil d'effet utile fixé avec le joueur avant de mesurer** *(sim. complète : 7,5 points de taux
  de victoire)* ; élimination séquentielle des candidats plutôt qu'un nombre de parties fixe.

## 13. Consigner une mesure

Dans l'entrée d'historique de la fiche (`fiche-de-deck.md`, champ « Effet mesuré ») : métrique,
avant → après, instrument, parties × graines, bruit, limites de l'instrument ; ou « aucune
mesure ». Écris « aucune partie réelle jouée sur cette liste » quand c'est le cas.
