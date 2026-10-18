# Cas d'école — vingt-cinq histoires vraies d'optimisation de decks

Quand lire ce fichier : avant la première séance sur un deck, pour savoir d'où viennent les règles d'or.
Quand une situation ressemble à un titre ci-dessous (zéro d'outil, combo rapporté, gain à attribuer).
Quand l'utilisateur conteste une analyse : chercher ici les cas où il avait raison.

Ces cas viennent de plusieurs mois de séances sur une dizaine de decks Commander. Les chiffres sont
ceux mesurés en séance. « Simulation maison » désigne un petit script Python écrit en séance par
Claude (méthode dans mesure.md). « L'utilisateur » est le joueur qui possédait le deck. Les règles
détaillées vivent dans bracket-et-combos.md, base-de-mana.md, construction-et-choix.md, mesure.md et
outils.md ; la liste de contrôle tirée de ces cas est dans erreurs-frequentes.md.

## 1. Lire l'oracle et les rulings

### Lire la clause qualifiante, pas le nom de la carte

**Deck.** Sonic the Hedgehog — Jeskai, aggro à compteurs, bracket 3. Quand Sonic attaque, chaque
créature « with flash or haste » reçoit un +1/+1 ; chaque dégât qu'elles subissent crée un Trésor.
**Ce qui s'est passé.** Teferi, Mage of Zhalfir semblait un allumeur évident ; sa clause (« creature
cards you own that aren't on the battlefield have flash ») vise la main, pas les permanents : zéro
déclenchement pour `{2}{U}{U}{U}`, coupé. À l'inverse, Caltrops et Pyrohemia, lues au nom comme des
cartes anti-créatures, sont des moteurs : leurs dégâts symétriques frappent les propres créatures
qualifiantes et créent des Trésors. Et 21 des 32 créatures qualifiaient déjà : l'hypothèse de départ,
« commandant quasi inerte », était fausse.
**Repéré par.** Relecture de l'oracle, carte par carte.
**Leçon.** Avant de couper ou d'ajouter, relire la clause qualifiante du commandant et vérifier
exactement la zone et la condition qu'elle vise.

### Un déclencheur qui compte des événements, pas des cartes

**Deck.** Quintorius, History Chaser — Boros, jetons. « Whenever one or more cards leave your
graveyard » : un Esprit 3/2.
**Ce qui s'est passé.** Un effet qui sort sept cartes du cimetière d'un coup ne déclenche qu'une fois :
les bons moteurs sont les petits événements répétés, pas les grosses sorties. Laelia, Ao et Atsushi
exilent depuis la bibliothèque, jamais depuis le cimetière : elles ne déclenchent jamais le commandant.
Les 63 sorts ont été classés à la main, oracle par oracle, puis confirmés par un second chemin.
**Repéré par.** Un journal de partie, confirmé par le ruling officiel du commandant.
**Leçon.** Lire si le déclencheur du commandant compte des événements ou des cartes, et choisir les
moteurs en conséquence (construction-et-choix.md).

### Deck à thème : le commandant que nourrissent les traits communs du thème

**Deck.** Donal, Herald of Wings — mono-bleu, construit de zéro sur la demande « un deck hibou ».
**Ce qui s'est passé.** « Owl » n'est pas un type de créature (les hiboux sont des Bird) et la
recherche `art:owl is:commander` donnait 25 candidats. La bonne question : quel commandant récompense
ce qu'ont en commun les cartes hiboux — non légendaires, volantes, à effet d'arrivée, de force 1,
bleues. Donal copie un sort de créature volante non légendaire (la copie est un 1/1) : chaque hibou
coche tout. Puis la lecture mot à mot : « once each turn » veut dire chaque tour, adverses compris —
un volant à flash lancé au tour d'un adversaire est copié aussi, jusqu'à quatre copies par tour de
table. Le levier devient le flash (Teferi, Leyline of Anticipation, Vedalken Orrery).
**Repéré par.** Oracle et rulings (Wan Shi Tong, All-Knowing écarté : il ne se déclenche ni sur scry
ni sur surveil) ; tableau des neuf commandants écartés, chacun avec son motif.
**Leçon.** Choisir le commandant dont le déclencheur est nourri par les traits communs du thème, puis
lire « each turn », « your turn », « cast », « nonlegendary » mot à mot.

### Ce qu'un multiplicateur multiplie vraiment, coûts compris

**Deck.** Obeka, Splitter of Seconds — Grixis, value/grind, bracket 3 strict. Obeka (2/5, menace)
donne autant d'étapes d'entretien supplémentaires que de dégâts de combat infligés à un joueur.
**Ce qui s'est passé.** L'exemple de la documentation de deck-wizard lui donne 3 de force ; elle en a 2.
Les rulings fixent le reste : chaque « at the beginning of your upkeep » se déclenche à chaque étape
ajoutée, mais dégagement et pioche sont sautés ; seuls des dégâts de combat comptent, donc « deals
damage equal to its power » ne fait rien. Faux payoffs : Replicating Ring (8 marqueurs avant tout
effet), Midnight Clock, The Soul Stone (`{6}{B}` par activation, 83,30 €). Coûts qui se multiplient
contre soi : Mystic Remora, The One Ring, Demonic Pact (ses quatre modes s'épuisent dans le même tour,
dont « vous perdez la partie »), toute perte de vie obligatoire.
**Repéré par.** Oracle, rulings, recherche dans le pool légal. L'utilisateur a corrigé un classement :
As Foretold n'est pas un faux payoff — le nombre de sorts gratuits ne monte pas, ses marqueurs si.
**Leçon.** Juger chaque carte sur ce que rapporte l'occurrence de plus et sur ce qu'elle coûte à
chaque occurrence ; n'est faux payoff que la carte à qui elle n'apporte rien du tout.

### Une carte validée meurt quand le plan change

**Deck.** Runo Stromkirk // Krothuss, Lord of the Deep — Dimir, cycling et réanimation, bracket 3.
**Ce qui s'est passé.** Le deck a basculé vers la réanimation et la copie par Krothuss. Slinn Voda,
gardé de l'ancienne version, est devenu un 8/8 vanille : un permanent mis en jeu sans être lancé ne
peut pas être kické, un jeton-copie non plus. Elder Deep-Fiend a un déclencheur « when you cast » que
les copies ne déclenchent pas. Krothuss a une valeur de mana de 3 (celle de la face avant) : tout
balayage à 3 ou moins le tue, et il revient en jeu face avant.
**Repéré par.** L'agent contradicteur pour Slinn Voda, puis relecture des oracles et des rulings.
**Leçon.** Quand l'architecture change, relire l'oracle de chaque carte gardée, en priorité les
déclencheurs de lancement et les kickers : aucun outil ne signale une carte devenue morte.

## 2. Juger une carte sur sa fonction dans le deck, pas sur son effet

### L'imblocabilité coupée parce qu'elle « n'ajoutait rien »

**Deck.** Arabella, Abandoned Doll — Boros, aggro go-wide. Quand Arabella (1/3) attaque, elle inflige X
dégâts à chaque adversaire, X = créatures de force 2 ou moins : elle doit attaquer, pas toucher.
**Ce qui s'est passé.** Le déclencheur n'étant pas un dégât de combat, Claude coupe Goblin Tunneler et
Subira (imblocabilité). Or l'imblocabilité a deux fonctions : augmenter le déclenchement (non) et
préserver l'attaquant (oui — le deck n'existe que si Arabella attaque chaque tour). À 1/3, seul un
bloqueur de force 3 ou plus la tue, et la seconde clause de Delney, Streetwise Lookout interdit
exactement ces bloqueurs. Sept contrôles mécaniques au vert ; l'autocritique de Claude partageait la
prémisse (« ces cartes augmentent-elles X ? »). Suite : en singleton, six pièces de protection ne
donnent que 54,9 % d'en tenir une au T6 ; le deck a surtout gagné de quoi refuser l'attaque.
**Repéré par.** L'utilisateur, en une phrase : si Arabella meurt à chaque attaque, le deck ne marche pas.
**Leçon.** Classer une carte sur la fonction qu'elle remplit dans le plan ; ce qui garde en vie la
source d'un déclencheur récurrent ne s'évalue pas sur ce qu'il ajoute au déclenchement.

### Un anthem dans un deck qui compte les petites forces

**Deck.** Arabella, Abandoned Doll — même deck.
**Ce qui s'est passé.** Warleader's Call (+1/+1 global) semblait naturel en go-wide. Sur les 42
créatures : 27 en force 0–1, 12 en force exactement 2, 3 au-dessus. L'anthem sortait ces douze du
compte d'Arabella, des déclencheurs de Raid Bombardment (« power 2 or less ») et de la clause de
Delney. Plateau de référence : 19 dégâts avec l'anthem, 21 sans. Coupé, avec une règle dans la fiche :
jamais d'anthem global. En chemin, l'outil de recherche renvoyait la force des 42 créatures à `None`,
sans erreur, et Claude a d'abord soupçonné son propre script.
**Repéré par.** Le recensement de force, fait à la main.
**Leçon.** Quand le moteur compte une caractéristique (force, valeur de mana…), la recenser sur toute
la liste avant d'ajouter un effet qui la modifie.

### Le deck pouvait se tuer lui-même, et quatre coupes sur huit étaient fausses

**Deck.** Muldrotha, the Gravetide — Sultai, value/grind par le cimetière, bracket 3.
**Ce qui s'est passé.** Le deck se meulait ~14 cartes par tour ; la proposition coupait Thassa's Oracle
et Laboratory Maniac sans toucher au moteur de meule : la bibliothèque vide passait de victoire à
défaite vers le tour 11, avec sept contrôles mécaniques au vert. Une passe plus tard, quatre coupes sur
huit tombaient : Satyr Wayfinder (son « put the rest into your graveyard » déclenche Hedge Shredder,
ajouté dans la même passe), Jarad's Orders (seul tuteur qui assemble Jarad et Lord of Extinction),
Cauldron of Essence (classé « burn », sa seconde capacité réanime), Gray Merchant (6-9 annoncé de
mémoire, 3,5 recompté trop vite, 5,9 de dévotion vérifiée, soit ~18 points sur la table).
**Repéré par.** L'agent contradicteur ; Thassa's Oracle gardée sur décision de l'utilisateur.
**Leçon.** Un contradicteur qui cherche les relations entre cartes trouve ce que des contrôles de
propriétés de cartes ne voient jamais, surtout quand l'analyse paraît solide.

## 3. Outils aveugles sans le dire

### Les fetchlands comptés comme ne produisant rien

**Deck.** Muldrotha, the Gravetide — Sultai, 37 terrains dont cinq fetchlands.
**Ce qui s'est passé.** `playtest-goldfish` lit le champ Scryfall `produced_mana`, vide pour tout
fetchland : 13,5 % de la base ne produisait rien. Claude a présenté 59,1 % de vissage de couleur comme
le point prioritaire et proposé quatre achats. Recompté à la main : B 29 · G 28 · U 23 au lieu de
24 / 23 / 18 ; seul déficit réel, le `{U}` de Muldrotha, à une source du seuil. Et l'audit de symboles
présenté comme seconde mesure indépendante lisait le même champ.
**Repéré par.** Lecture du code de l'outil : une variante sortait meilleure pour une raison qui ne
tenait pas.
**Leçon.** Avant de citer un chiffre d'outil, vérifier à la main trois cartes atypiques (fetch, coût X,
cycling, face arrière), et s'assurer que son propre contrôle ne lit pas la même donnée.

### Un tableau de bord plein de zéros

**Deck.** Quintorius, History Chaser — Boros, jetons.
**Ce qui s'est passé.** `deck-tune`, `slot-budgets` et `deck-signals` annonçaient `interaction: 0`,
`card_draw: 0`, `board_wipe: 0` et 49 cartes sur 63 « dead weight » (78 %) ; l'analyse en avait tiré un
déficit d'interaction. deck-wizard tournait en mode dégradé (`PYTHONUTF8` absent, dossier de fixtures
manquant, `HOME` non défini). Réparé, sur la même liste : pioche 0 → 13, interaction 0 → 10, cartes
mortes 78 % → 0 % — le déficit n'existait pas. Même séance : `cut-check` avait extrait 7 déclencheurs et
n'en avait analysé qu'un, un résultat nul et non un feu vert.
**Repéré par.** L'absurdité des chiffres ; l'agent contradicteur pour `cut-check`.
**Leçon.** Un résultat trop net signale un outil cassé, pas un deck cassé : réparer et remesurer avant
de conclure (réglages dans outils.md).

### Une « sévérité 40 » qui ne mesurait pas la plainte

**Deck.** Sonic the Hedgehog — Jeskai. Plainte de l'utilisateur : « inconsistant ».
**Ce qui s'est passé.** L'analyseur de deck-wizard annonçait `spread thin` en sévérité 40, contre 4 pour
« rampe courte » ; Claude en a conclu à l'oral que l'éparpillement écrasait tout. Dans le code, la
sévérité vaut 4 + le nombre d'axes portés par une ou deux cartes : ici trente-six étiquettes de type
isolées (« Golem tribal », c'est un jeton ajouté par la passe elle-même). Le vrai défaut, mesuré au
goldfish sur trois graines : 53,2 % de vissage de couleur (51,9 / 52,9 / 54,9), ramené à 36,7 %.
**Repéré par.** Lecture du code de l'analyseur ; mesure du vissage sur trois graines.
**Leçon.** Traduire la plainte de l'utilisateur en une métrique mesurable, et ne jamais comparer deux
sévérités d'outil sans savoir comment chacune est calculée.

### Trois bases de mana identiques à la décimale

**Deck.** Sonic the Hedgehog — Jeskai ; puis Arabella, Abandoned Doll.
**Ce qui s'est passé.** Trois familles de terrains testées à couleurs constantes (rapides, checklands,
filtres) : 35,5 % / 35,4 % / 35,7 % de vissage, sur trois graines. Trois conditions d'entrée
radicalement différentes ne peuvent pas donner le même chiffre : `playtest-goldfish` traite l'entrée
engagée conditionnelle comme dégagée et mesure les couleurs, pas le tempo. Sur Arabella, il comptait
des sorts lancés (Arcane Signet vaut Purphoros), ne voyait aucun chemin de dégâts et pénalisait une
passe qui refermait pourtant le trou de fin de partie ; les dégâts ont été chiffrés à la main.
**Repéré par.** L'égalité parfaite elle-même.
**Leçon.** Un résultat identique entre variantes censées différer prouve que l'instrument ne voit pas
la variable testée : écrire alors « aucune mesure » et chiffrer à la main.

## 4. Combos : faux positifs, faux négatifs

### Deux combos gagnants fantômes, et des conditions de victoire « au vert »

**Deck.** Muldrotha, the Gravetide — Sultai, 17 terrains de base.
**Ce qui s'est passé.** `combo-search` annonçait Hermit Druid + Thassa's Oracle et Hermit Druid +
Laboratory Maniac. Hermit Druid s'arrête au premier terrain de base révélé : avec 17 basiques, ~4,5
cartes meulées par activation, pas 98 ; l'outil n'a aucun champ de précondition. `deck-tune` affichait
alors 4 conditions de victoire « ok », dont ces deux combos ; vrai compte : 2, sous la cible de 3 à 6.
Et `spellbook_estimate_bracket` rendait une liste de Game Changers vide sur une liste contenant
Cyclonic Rift et Thassa's Oracle.
**Repéré par.** Relecture de l'oracle de Hermit Druid.
**Leçon.** Un combo rapporté s'établit en lisant l'oracle de chaque pièce contre la liste réelle ; un
indicateur au vert hérite des défauts de la mesure qui l'alimente.

### Un infini qu'aucun outil ne voit, et une cible de bracket qui bouge

**Deck.** Quintorius, History Chaser — Boros, jetons ; bracket 2, relevé à 3 par l'utilisateur.
**Ce qui s'est passé.** Au bracket 2, la fiche interdisait Goblin Bombardment, Ashnod's Altar et Breath
of Fury : Cathars' Crusade était à une carte de six combos infinis. L'utilisateur relève la cible à 3
et ajoute Breath of Fury. Or Hofri Ghostforge + Breath of Fury + une créature de réserve bouclent : la
créature touche, est sacrifiée, Hofri l'exile et en fait une copie Esprit (l'exil déclenche le
commandant), combat supplémentaire ; +1 créature par tour de boucle, ~9 manas, T6-8, compatible
bracket 3. `combo-search` : 0 combo ; `spellbook_find_decklist_combos` : `included: []`.
**Repéré par.** Relecture d'oracle, deux fois indépendamment (une variante avec Anger, puis celle-ci).
**Leçon.** Un « zéro combo » n'est pas une preuve ; la liste des cartes interdites se relit quand la
cible de bracket change (bracket-et-combos.md).

### Une liste noire écrite à la main, trop étroite puis trop large

**Deck.** Obeka, Splitter of Seconds — Grixis, bracket 3 strict.
**Ce qui s'est passé.** Le chercheur de combos avait raté Aggravated Assault + Sword of Feast and
Famine (combats infinis). La liste noire écrite à la main bannissait alors l'Épée seule, alors que
l'infini exige aussi Aggravated Assault : seule celle-ci est restée interdite. Trouvé aussi à la main :
tout jeton-copie de créature avec Port Razer (dont Helm of the Host, ajout « naturel ») contourne son
auto-limite. Inversement, Mechanized Production donne une victoire bornée (sept déclenchements) : elle
passe la lettre du bracket 3, pas l'esprit. `combo-search` la classait combo à deux cartes,
`spellbook_estimate_bracket` non.
**Repéré par.** Lecture des préconditions à la main ; la nuance sur Mechanized Production quand
l'utilisateur a demandé pourquoi elle était coupée. La décision lui a été rendue.
**Leçon.** Une liste noire nomme le combo complet, pas une carte isolée, et la décision de bracket se
présente au joueur avec la différence entre la lettre et l'esprit.

## 5. Base de mana

### La base était à la cible, et le meilleur levier était gratuit

**Deck.** The Archimandrite — Jeskai, value/grind par le gain de vie, finishers à 6 manas.
**Ce qui s'est passé.** Claude recommandait d'acheter des terrains. Sources effectives (formule de
Schulze) : 37 terrains + 8,25 (onze rochers × 0,75) + 0,33 (un cantrip) ≈ 45,6 pour une cible de 46.
L'heuristique « au-delà du 4ᵉ terrain, rampe et pioche valent mieux » est calibrée sur 4 manas au T4 :
ici +3 terrains battaient +3 rampe/pioche (6 manas au T6 : 65,1 % contre 59,8 %). En simulation maison
(12 000 à 21 000 parties par variante), jeter les mains à 2 terrains faisait passer le commandant au
T5 de 68,8 % à 76,4 % pour zéro euro, contre +3 points pour le meilleur paquet d'échanges (~30 €).
Sur Muldrotha, la même règle coûtait 4,6 points.
**Repéré par.** Lecture intégrale de deux sources externes sur les bases de mana, testées sur le deck.
**Leçon.** Calculer les sources effectives avant de prescrire un achat, et tester les décisions de jeu
gratuites, deck par deck, avant les échanges (base-de-mana.md).

### « 38 terrains, c'est trop » : l'intuition retirée avant présentation

**Deck.** Arabella, Abandoned Doll — Boros aggro, coût moyen 1,81, 11 accélérateurs, 38 terrains.
**Ce qui s'est passé.** Claude avait annoncé « courbe basse, donc trop de terrains ». Hypergéométrique
sur 99 cartes : passer à 34 terrains gagnait 0,2 pioche morte sur cinq tours et perdait 6,4 points de
mains gardables (81,7 % → 75,8 %) ; le goldfish, second chemin, donnait 81,2 %. Le vrai défaut :
5,89 terrains en jeu au T8 pour une courbe qui plafonnait à 4 manas avec une seule carte à ce coût.
Correction : trois cartes à 4 manas. L'utilisateur n'avait coché ni « je noie » ni « trop lent au
démarrage » : le cadrage écartait déjà cet axe.
**Repéré par.** Le propre calcul de Claude, avant présentation, contrôlé par le goldfish.
**Leçon.** Sur un deck à courbe basse, calculer avant de conclure au flood, et chercher d'abord le
puits de mana manquant.

## 6. Mesure et attribution

### Optimiser une ressource au lieu de la condition de succès

**Deck.** Runo Stromkirk // Krothuss — Dimir. Runo se transforme quand une créature de valeur de mana
6 ou plus est au sommet ; Krothuss copie « another target attacking creature ».
**Ce qui s'est passé.** Quatre versions optimisées sur le taux de transformation (simulation maison).
Or se transformer sur un plateau vide ne fait rien : au T5, 70,9 % de transformation pour 6,4 % de
payoff réel ; au T7, 89,9 % contre 44,1 %. Même schéma sur The Archimandrite : ressources bonnes
partout, victoire assemblée dans 11,0 % des parties au T8 faute d'évasion (23,6 % après ajout). Et sur
Muldrotha, le premier simulateur oubliait le commandant, absent des 99 : 0,0 % à tous les tours, mais
des chiffres de létal crédibles.
**Repéré par.** Un agent challenger (« le premier simulateur mesure une ressource ») ; pour Muldrotha,
la publication séparée de chaque pièce, dont une restait à zéro.
**Leçon.** Simuler la condition de succès réelle avant d'optimiser la ressource qui y mène, et publier
la disponibilité de chaque pièce — le commandant doit y être près de 100 %.

### Le correctif principal ne valait pas mieux que neuf Îles

**Deck.** Runo Stromkirk // Krothuss — 17 grosses créatures sur 99 ; plainte : « trop lent ».
**Ce qui s'est passé.** Claude présentait un paquet de sélection (Ponder, Preordain, Mystic
Speculation, Soothsaying, Crystal Ball) comme le correctif principal. Test de substitution sur 15 000
parties (transformation au T4) : liste construite 48,1 % ; neuf cyclers remplacés par ce paquet
24,3 % ; neuf cyclers remplacés par des Îles 26,5 %. Les grosses créatures à cycling sont à la fois la
cible et leur propre activateur : +22 à +24 points pour ~3 $ ; deux avaient été coupées à tort plus
tôt. Mesure faite avant la prise en compte des terrains engagés : seuls les écarts comptent.
**Repéré par.** Le test de substitution contre un témoin bête.
**Leçon.** Mesurer chaque paquet contre un témoin bête — des terrains de base — avant de le présenter
comme le correctif.

### Deux chemins attrapent ce que la relecture ne voit pas

**Decks.** Runo Stromkirk // Krothuss (simulation maison) ; Quintorius (calcul de la base de mana).
**Ce qui s'est passé.** Sur Runo, `Troll of Khazad-dum` (sans accent) ne trouvait pas `Troll of
Khazad-dûm` dans les données : le cycler le moins cher disparaissait en silence ; un second bug
acceptait n'importe quelle créature. Ils se compensaient presque (net +1,3 point). Sur Quintorius,
« commandant au T4 dans 52,7 % des parties » : les bicolores étaient stockés `("RW",)`, et
`"W" in ("RW",)` est faux — seize terrains dans aucune couleur. Vrai chiffre : 79 % ; couper Turbulent
Steppe, comme le voulait un diagnostic hérité, aurait été une erreur.
**Repéré par.** Un agent qui a réécrit le simulateur sans voir le premier (35,1 % des deux côtés) ; un
second script écrit autrement. Le code tournait sans erreur : la relecture ne l'aurait pas montré.
**Leçon.** Un chiffre qui fonde une recommandation se produit par deux chemins, et toute carte du deck
absente des données doit faire échouer le script.

### La redondance ajoutée sur le mauvais axe

**Deck.** Muldrotha, the Gravetide — ~20 cartes remplissent le cimetière, ~5 le convertissent en perte
de vie.
**Ce qui s'est passé.** Le cimetière atteignait 23,8 cartes au T14 : pas de goulot. Jarad n'était
disponible que dans 18,5 % des parties (simulation maison), 20,2 % par hypergéométrique. Quatre
convertisseurs ajoutés, chacun sur un événement distinct : au moins un disponible, 46,9 % → 78,0 %.
Mais le létal n'a pas bougé (8,54 % → 8,36 %, sous le bruit) : le goutte-à-goutte plafonne vers 14
points au T14, seule la rafale de Jarad atteint 40. Et « 40 à chaque adversaire » supposait de tuer la
table seul, une exigence cEDH pour un bracket 3.
**Repéré par.** La mesure, confirmée par l'utilisateur (« le burn est assez trivial »). La passe
suivante, jetons et évasion, huit cartes choisies par lui : tuer un adversaire au T14, 28,3 % → 59,3 %
(ordres de grandeur : deux relevés de la séance divergent).
**Leçon.** Avant d'ajouter des copies d'un effet, vérifier qu'il peut atteindre la condition de succès,
et caler celle-ci sur le bracket visé.

### Le gain attribué à l'évasion venait des jetons

**Deck.** Muldrotha, the Gravetide — passe « jetons et évasion ».
**Ce qui s'est passé.** La passe ajoutait ensemble des générateurs de jetons et deux incarnations
d'évasion (Wonder, Brawn) ; il a fallu écrire une couche de simulation de combat, les deux premières
étant aveugles au nouveau plan. L'écart croissait avec le nombre de bloqueurs (+21,9, +25,5, +27,1
points) ; Claude a conclu « signature de l'évasion ». Témoin sans Wonder ni Brawn : mur de 2
bloqueurs, 80,2 % avec, 78,1 % sans ; mur de 6, 51,4 % / 40,7 % ; mur de 12, 31,8 % / 16,7 %. À table peu
défendue, les jetons font tout.
**Repéré par.** Le témoin.
**Leçon.** Attribuer un gain par un témoin qui éteint un seul mécanisme, jamais d'après la forme d'une
courbe ; et demander comment la table défend avant de recommander de l'évasion.

## 7. Collaboration : ce que l'utilisateur a vu et que Claude n'avait pas vu

### Avant d'analyser : la fiche, puis la liste réellement jouée

**Decks.** Quintorius ; The Archimandrite.
**Ce qui s'est passé.** Une séance Quintorius a démarré à froid sur une liste collée, sans lire la
fiche : une carte interdite par une règle maison, écrite dans l'en-tête, a été proposée ; Goblin
Bombardment, listé parmi les interdits du bracket, recommandé ; le point ouvert principal non traité.
Le plan hérité n'avait été appliqué qu'à moitié : cinq coupes convenues étaient encore dans la liste.
Sur The Archimandrite, deux itérations ont été bâties sur une liste supposée à jour qui ne l'était pas,
et une lecture automatique de la page publique du deck avait récupéré 72 entrées sur ~75.
**Repéré par.** L'utilisateur pour la carte interdite ; la comparaison de la liste réelle au plan.
**Leçon.** Lire la fiche avant toute analyse, puis repartir de la liste réellement jouée, prise dans
l'export texte de la plateforme et comparée à la dernière liste enregistrée.

### Les refus de l'utilisateur avaient raison

**Decks.** Quintorius ; Sonic the Hedgehog.
**Ce qui s'est passé.** Sur Quintorius, l'utilisateur applique neuf échanges sur onze, refuse trois
coupes et ajoute Breath of Fury. Garder Lorehold Charm était juste : avec Breath of Fury, il fait
passer les closers de 2 à 4. Une coupe refusée cachait un piège : Bag of Holding exile obligatoirement
(« exile that card », pas « may ») — défausser Anger avec Bag en jeu éteint la célérité pour de bon.
Sur Sonic, il garde Guardian Sunmare (seul tuteur répétable) et trois terrains-artefacts engagés :
25 artefacts avec, 22 sans, pour Hellkite Tyrant qui gagne à 20.
**Repéré par.** L'utilisateur ; l'agent contradicteur pour Bag of Holding.
**Leçon.** Les choix de l'utilisateur sur sa liste ne sont pas des erreurs à nettoyer : il connaît les
rôles cachés de ses cartes, et un « may » absent change la valeur d'une carte.

### Cinquante parties réelles contre une probabilité d'assemblage

**Deck.** Obeka, Splitter of Seconds — version de duel poussée vers le cEDH, sur carte blanche
explicite de l'utilisateur.
**Ce qui s'est passé.** Préconditions lues à la main : Sword of Feast and Famine + Aggravated Assault
exige cinq terrains dont deux rouges (l'Épée dégage les terrains, pas les rochers) ; Thassa's Oracle +
Tainted Pact s'arrête au deuxième Marais. Probabilité d'avoir un combo en main, tuteurs compris :
16,7 % au T4, 22,3 % au T6, 28,5 % au T8. Après ~50 parties : « presque moins bien que la version
d'avant » ; Aggravated Assault a servi une fois ; retirer Honden of Seeing Winds était une erreur.
**Repéré par.** Les parties réelles de l'utilisateur ; le goldfish ne voyait aucun des combos.
**Leçon.** Une probabilité d'assemblage basse est un signal ; le retour de parties réelles prime, et un
deck qui n'assemble pas régulièrement avant le T5 ne se présente pas comme du cEDH.
