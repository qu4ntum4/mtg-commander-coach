# Construction et choix des cartes

Quand lire ce fichier : avant de juger un commandant ou d'écrire la condition de succès (phase 1),
de fixer des quotas (phase 3), de proposer un échange de cartes (phase 5) ; quand une source doit
appuyer une recommandation ; pour le mulligan, le goldfish, les décisions de jeu, l'upgrade d'un precon.

Une erreur en phase 1 invalide tout le reste, une erreur en phase 5 coûte une carte. Niveaux de
preuve T1 à T4 : section « Les sources ». Les chiffres de cas illustrent une règle et ne se
transposent pas à un autre deck ; cas complets dans `cas-d-ecole.md` et `erreurs-frequentes.md`.

## Phase 1 — Le commandant et la condition de succès

### Le test à trois branches : cartes, mana, combo

- Demande si le commandant **génère des cartes**, **génère du mana** ou **active un combo**. Une
  branche suffit à le rendre autonome.
- S'il échoue sur les trois : **compte les slots des 99 qui n'existent que pour l'alimenter** et
  annonce ce coût, pas « commandant faible ». Ces slots sont pris à la rampe, à la pioche, à
  l'interaction.
- Pourquoi : le test mesure l'autonomie, pas la puissance ; il vaut donc à tous les brackets.
  Tergrid, God of Fright est forte mais n'existe que si le deck fournit Syphon Mind, Memory Jar et
  leurs semblables ; même diagnostic pour Zhulodok, Void Gorger. Un échec n'est pas un rejet : c'est
  un coût de construction à chiffrer.
- Limite : le coût d'opportunité de l'identité colorée (se priver du bleu) est un critère cEDH
  (guide de Corey Williams, T2). En bracket 2-3, regarde plutôt la **profondeur du pool** de cartes
  utiles dans l'identité.

### Lire le déclencheur : fréquence ou volume

- Lis l'oracle mot à mot. « One or more » compte des **événements**, pas des cartes : ruling WotC du
  20/03/2026 sur Quintorius, History Chaser, plusieurs cartes qui quittent le cimetière en même temps
  le déclenchent **une seule fois**. Ici, dix petits événements valent mieux qu'un gros.
- Des résolutions séparées font des événements séparés : Sevinne's Reclamation lancée en flashback
  quitte le cimetière, puis sa copie et l'original renvoient chacun une carte, l'un après l'autre.
- Demande aussi à quelle fréquence la condition est vraie en jeu : Ark of Hunger meule une carte,
  mais le déclencheur « une carte quitte votre cimetière » n'a lieu que si tu **joues** cette carte.
  Les rulings sont datés et peuvent changer : relis-les avec `scryfall_card_rulings`.
- Sortie attendue : le **type de récompense** (fréquence ou volume), qui oriente tout le choix des
  cartes de la phase 5.

### L'axe commander-centric / commander-agnostic

- Situe le deck sur l'axe. *Centric* : ne fonctionne pas sans le commandant, synergie élevée,
  qualité de carte moyenne plus basse (Shuko, Umbral Mantle, Sea Kings' Blessing sont inertes sans
  Nadu, Winged Wisdom). *Agnostic* : l'inverse (Tymna the Weaver et Kraum, Ludevic's Opus piochent
  et ne synergisent avec rien). C'est un axe de construction, pas une erreur.
- **Compte les cartes inertes sans le commandant** et annonce ce nombre avant tout échange carte à
  carte : il mesure la fragilité. Le commandant sera répondu, plusieurs fois, et chaque retour
  coûte 2 manas de plus.
- Trois façons de payer ce coût, **par efficacité décroissante** :
  1. **Rendre l'effet du commandant redondant** dans les 99 : Panharmonicon dans un deck Elesh Norn,
     Mother of Machines centré sur les déclenchements d'arrivée. Retire la dépendance au lieu de la
     défendre ; c'est la redondance la plus rentable.
  2. **Protéger le commandant** : Lightning Greaves, Malakir Rebirth, Slip Out the Back, Tamiyo's
     Safekeeping, Fierce Guardianship. Coûte des slots, sert une fois par menace ; en singleton,
     c'est un bonus, jamais un plan (chiffres en phase 5).
  3. **Réduire le nombre de cartes inertes** : échanger quelques pièces de très haute synergie
     contre des cartes autonomes.
- Cherche la **vraie dépendance** de chaque carte, qui n'est pas toujours le commandant.
  Containment Construct et Currency Converter, à très haute synergie avec un commandant qui
  récompense les cartes quittant le cimetière, produisent de la valeur seuls (rejouer la carte
  défaussée, Trésors, jetons Rogue) : ce dont ils dépendent, ce sont les **exutoires de défausse**.
  Ne les range pas parmi les inertes avant d'avoir lu ce qui les déclenche.

### La condition de succès en une phrase mesurable

- Écris l'enchaînement qui produit la victoire, puis résume-le en **une phrase mesurable** :
  « produire 6 manas au tour 5 », « avoir 4 déclenchements par tour au tour 6 ». C'est elle qui sera
  mesurée en phase 6 (voir `mesure.md`). **Ne passe pas à la phase 2 sans elle.**
- Calibre-la sur le **bracket visé** : « tuer la table seul » est une métrique cEDH qui condamne à
  tort un deck de bracket 3.
- Pourquoi : les métriques de ressources progressent toujours un peu. Cas : mana moyen passé de
  3,09 à 2,73, tout au vert, alors que la ligne de victoire n'était assemblée que dans 11 % des
  parties au tour 8. Le deck savait durer, pas conclure.
- Piège du **proxy plausible** : un commandant qui se transforme puis copie « another target
  attacking creature » gagne à la transformation **plus** une créature capable d'attaquer. Mesurés
  côte à côte : transformation au tour 5,99 en moyenne, vrai déclencheur utile au tour 8,71. Mesure
  le proxy **et** la vraie condition au moins une fois ensemble.
- Choisir un commandant (phases 0 et 1 seules) : rends le test à trois branches, le type de
  récompense, le coût en slots et la profondeur du pool dans l'identité.

## Phase 3 — Structure et quotas

### Dériver les quotas, jamais appliquer un template

- Les templates s'accordent sur un socle (**rampe, pioche, retrait**) et sur le fait qu'aucun n'est
  un livrable ; ils divergent sur tous les nombres. N'annonce jamais un quota comme une norme :
  donne **la fourchette, sa source, et la position choisie justifiée par le plan et le tour visé**.
  Format : « Retrait ciblé : 8 (fourchette 7 à 12 selon les templates ; bas de fourchette parce
  que le deck vise le tour 7 et paie cher chaque slot non proactif) ».
- Lecture des écarts (raisonnement, pas donnée) : un deck de valeur vit longtemps et veut plus de
  retrait ; un deck agressif qui vise un tour précoce en veut moins.
- Niveau de preuve : les templates sont des méthodes publiées (T2), mais leurs **nombres** relèvent
  du consensus de pratiquants (T3). Seul le calcul des 7 exemplaires est T1.

| Catégorie | Command Zone 2025 (ép. 658) | Command Zone 2021 (ép. 379) | 7x9 initial | 7x9 « flip » | 8x8 | Guides en ligne 2026 (T3) | Écart |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Rampe | 10 (jusqu'à 12) | 10-12 | 7 | 9 | 8 | 10-12 | 7 à 12 |
| Pioche, avantage de cartes | 12 (accès à plusieurs cartes) | 10 | 7 | 9 | 8 | 8-10 | 7 à 12 |
| Retrait, perturbation ciblée | 12 (contresorts et engagement compris) | 10-12 | 7 (tout retrait) | 9 (tout retrait) | 8 (tout retrait) | 8-10 | 7 à 12 : le plus large |
| Retrait, perturbation de masse | 6 (balayages, réponses aux artefacts, enchantements, cimetière) | 3-4 | inclus | inclus | inclus | — | seul le Command Zone le sépare |
| Plan, thèmes | 30 cartes de plan | — | 6 × 7 | 3 × 9 | 4 × 8, liées au commandant ou au thème | — | — |
| Divers (cartes perso) | — | — | — | 9, coupé en premier | 8 (« Personal ») | — | — |
| Terrains | 38 | 35-38 | 36 | 36 | 35 de base, ~38 visé | 36-38 | 35 à 38 |

- Sources revérifiées le 18/10/2026. **Command Zone** : épisode 658, « Commander Deckbuilding
  Template for the New Era » (18/02/2025), repris dans les épisodes 659 et 733 ; aucun template plus
  récent au 08/10/2026. Ses catégories se recoupent volontairement (108 cartes pour 99 places).
  L'épisode 379 (02/03/2021) est l'ancien template. **7x9** : WitchPHD, 12/08/2022. **8x8** :
  the8x8theory.tumblr.com (2016) — quatre catégories fixes (rampe, pioche, retrait, cartes perso)
  et quatre liées au commandant ou au thème ; 35 terrains de base, environ 38 visés au final.
  **Guides 2026** : Draftsim, KrakenTheMeta — des sites de contenu, pas des études.
- Le désaccord sur le retrait ciblé n'a aucune donnée pour le trancher : choisis selon le plan et
  dis-le.
- Entre 2021 et 2025, le Command Zone a surtout **élargi ses catégories** : « card advantage » ne
  compte que les cartes qui donnent accès à plusieurs cartes, la perturbation ciblée inclut
  contresorts et effets d'engagement, la perturbation de masse inclut 2-3 balayages de créatures,
  une réponse aux artefacts et enchantements, une au cimetière. Compare des définitions avant de
  comparer des nombres ; les raisons valent plus que les chiffres.
- Règle du 7x9 : une catégorie sous 9 en fin de construction, demande si l'effet est nécessaire,
  puis coupe-le, complète-le, ou garde les meilleures en « divers ». Le divers est la première
  réserve de coupes quand il faut plus de rampe, de pioche ou de retrait.

### Piliers à 7 exemplaires, bonus en dessous

- Pour chaque catégorie, décide d'abord si elle est **pilier** ou **bonus**. Pilier : **7
  exemplaires distincts minimum**. La question devient « combien de cartes distinctes remplissent ce
  rôle ? », pas « combien de retrait ? ».
- Pourquoi (T1, calcul vérifiable) : 7 copies dans 99 cartes donnent 41,1 % d'en avoir une en main
  de départ et 7,1 % par pioche, l'équivalent d'un 4-of en 60 cartes (39,9 % et 6,7 %). Les
  templates ne sont que des répartitions de ce plancher entre catégories.
- Corollaires : sous 7, l'effet est **occasionnel**, pas structurel (un plan qui dépend d'un effet
  à 4 exemplaires échoue régulièrement : monte à 7 ou assume-le comme bonus). Un effet qu'on ne peut
  pas monter à 7 dans l'identité colorée **n'est pas un axe de deck** : fais ce test de faisabilité
  avant de t'engager.
- Limite : le nombre dit la fréquence d'accès, pas la qualité de ce qu'on trouve.

### Effets symétriques et asymétriques

- Compte le **retrait de masse** comme une ressource **partagée** de la table, le **retrait
  ciblé** comme une ressource **privée** : pas la même logique de quota.
- Généralise : tout effet symétrique dont l'usage par un adversaire te profite (balayages, haine de
  cimetière, retrait d'artefacts et d'enchantements) peut être **sous-dosé** en multijoueur ; tout
  effet asymétrique en ta faveur ne te vient jamais de la table et **se compte seul**.

### Les cartes qui terminent la partie

- Avant de figer une liste, **désigne des cartes précises** et explique comment chacune finit la
  partie. Si tu n'en trouves pas, il manque des finisseurs.
- **Ne coupe pas une condition de victoire pour de la valeur** : les pièces de synergie alimentent
  les conditions de victoire, pas l'inverse. Erreurs récurrentes : générer de la valeur sans jamais
  convertir, dépendre d'une seule condition de victoire.
- « Au moins trois cartes qui terminent la partie » est une **habitude répandue, non prouvée** :
  elle vient d'un article commercial généré par IA (T4) ; « 3 à 5 façons réalistes de gagner » vient
  d'un consensus non sourcé (T3). Présente-les comme des repères de vérification, jamais comme une
  règle ; les nombres de finisseurs par archétype qui circulent n'ont aucune assise.
- Taxonomie (citable même depuis un T4) : combat (large, haut, dégâts de commandant), combo,
  valeur (drain, avantage de cartes, verrou), victoire alternative (Thassa's Oracle, Felidar Sovereign).

### Chasser les anti-synergies récurrentes

- Haine de cimetière symétrique dans un deck de cimetière ; balayage symétrique dans un go-wide.
- **Payoffs sans masse critique d'enablers** : le cas type est un deck landfall plein de payoffs,
  sans moyen de poser des terrains supplémentaires.
- Rampe trop lente pour le plan ; interaction sous-dosée. (T3 : des pistes à vérifier, pas des
  verdicts.)

## Phase 5 — Le choix carte à carte

### Lire avant de juger

- **Lis l'oracle complet de chaque carte évaluée, sans exception**, avec `scryfall_card_details` :
  jamais la mémoire, le nom, le type ni la ligne qui a fait sortir la carte d'une recherche.
  `scryfall_search_cards` ne renvoie pas l'oracle (constaté au 17/10/2026 : nom, coût, type,
  rareté, prix, rang seulement). Cas litigieux : second chemin par `scryfall_card_rulings`. État des
  outils et pièges de débit : `outils.md`.
- Le souvenir de l'effet ment souvent entre cartes voisines. Exil répétable d'une carte de cimetière
  en s'engageant : Ghost Vacuum, Scrabbling Claws, Relic of Progenitus. Usage unique : Soul-Guide
  Lantern (un seul exil, à l'arrivée), Tormod's Crypt, Sentinel Totem.
- Détails qui changent un compte : un jeton a une valeur de mana de 0 ; des jetons bicolores
  profitent de deux anthems de couleur ; un terrain à deux types de base compte pour les deux.

### Classer par rôle en lisant la zone visée

- Aucun filtre textuel ne produit un **décompte** par rôle ; il produit des **candidats**. Le
  classement se fait **carte par carte**, oracle lu, zone et possesseur identifiés.
- Pourquoi : un filtre par expressions régulières a annoncé 31 moteurs pour 26 réels (zone non lue)
  et 2 réponses pour 12 réelles (créatures exclues : Skyclave Apparition, Selfless Spirit…).
- La correction manuelle peut se tromper en sens inverse : Relic of Progenitus et Scrabbling Claws
  écartés « parce qu'ils visent les adversaires », alors que « target player exiles a card from
  their graveyard » permet de se cibler soi-même (ruling du 08/06/2016 : le joueur ciblé choisit la
  carte). Hofri Ghostforge est un moteur sans aucun des mots-clés cherchés.
- Méthode :
  1. Définis chaque rôle par une phrase qui nomme **la zone et le possesseur** (« fait quitter
     **mon** cimetière à une ou plusieurs cartes »), et rappelle la règle de comptage du déclencheur.
  2. Lis l'oracle de chaque sort non-terrain, par petits lots ; aucune classification automatique.
  3. Catégories, à adapter au plan : moteurs récurrents (avec leur **cadence** : chaque entretien,
     y compris adverse, une fois par tour, à chaque attaque…), moteurs ponctuels, récompenses du
     déclencheur (redondance de l'effet du commandant, avec leurs restrictions), récompenses de
     largeur et anthems, réponses (créatures, permanents, balayages, protection, haine de cimetière),
     rampe et fixation, pioche et sélection, hors plan.
  4. **Autorise le double compte** : Mind Stone est rampe et pioche ; Relic of Progenitus réponse
     et moteur. Ranger une carte dans un seul rôle suffit à la faire couper à tort.
  5. Recense à part les terrains qui tiennent un rôle ; compare au décompte précédent ou automatique
     et nomme la cause de chaque écart (zone non lue, type exclu).
- Classe par **fonction dans le plan**, pas par effet brut, et à **plusieurs dimensions** : une
  carte qui « n'augmente pas X » peut être celle qui permet au commandant d'agir chaque tour.

### Chercher par effet, puis chercher la clause qui restreint

- Recherche par texte d'oracle dans l'identité (syntaxe Scryfall : `id<=rw o:"texte" mv<=3`),
  puis lis l'oracle complet de chaque résultat **en cherchant activement la clause restrictive**.
  Une recherche trouve la phrase, pas l'effet.
- Cas réels de quasi-recommandations : un dégagement de masse limité à quatre types de créatures
  absents de la liste ; un dégagement bon marché assorti d'une assignation des dégâts selon
  l'endurance, qui annulait le pump dont le deck dépendait ; une carte « taille de main » qui
  comptait les cartes piochées ce tour. Un mot-clé peut dire l'inverse de ce qu'on cherche : la
  convocation sort dans les recherches de dégagement alors qu'elle **engage** les créatures. Une
  clause **favorable** se rate tout autant (voir le cycling plus bas).
- « Il n'existe pas de carte qui… » est le résultat d'une recherche datée, pas un fait : dis quelle
  recherche, quel jour.

### L'ordre des leviers : horizontaux d'abord

- **Épuise les leviers horizontaux** (même puissance, meilleure synergie ou meilleure consistance)
  avant tout ce qui coûte un bracket. Optimiser et monter en puissance sont deux axes
  indépendants ; le premier est presque toujours celui qui reste à exploiter.
- Coût nul en bracket, tant que la carte n'est pas un Game Changer : base de mana, redondance d'un
  effet clé, rampe et pioche supplémentaires, cartes de puissance égale mieux synergiques,
  protection du commandant, tuteurs.
- Touche aux critères de bracket : un Game Changer, la seconde pièce d'un combo à deux cartes, des
  tours supplémentaires, un déni de terrain de masse. **Quand une carte change le bracket, dis-le
  explicitement.** Règles et liste des Game Changers à relire le jour même : `bracket-et-combos.md`.
- **La redondance avant le tuteur.** Face à un deck inconsistant, compte les exemplaires de l'effet
  qui manque et complète jusqu'à 7 : pars de la carte dont l'effet est nécessaire et cherche ses
  équivalents fonctionnels par texte d'oracle, puis lis chaque résultat. Pourquoi : la redondance
  diversifie les parties là où un tuteur les rend toutes pareilles, préoccupation que le panel du
  format Commander continue de citer. Un tuteur reste proposable : signale-le comme tel, avec son
  solde de cartes (dans la main ou sur la bibliothèque, ce n'est pas le même prix).
- Pioche, rummage et regard sont des **compléments partiels** : ils augmentent les cartes vues sans
  créer d'exemplaire.

### Évaluer une carte dans son contexte

- **Dans le scénario exact où elle servira** : une carte conditionnée à « une créature légendaire
  en jeu » est morte dans une version où le commandant n'est plus là. Teste toute carte qui touche
  le commandant contre ce qui le cible dans la liste (un linceul bloque aussi ses propres auras et
  équipements).
- **Une carte validée sous une architecture meurt quand l'architecture change.** Quand une refonte
  change le mode de déploiement (lancer devient réanimer, réanimer devient tricher en jeu, payer
  devient copier), relis toutes les cartes à clause conditionnelle, surtout celles déjà validées :
  kicker, évoquer, morph, coût alternatif, « if you cast it from your hand », « if it was kicked ».
  Cas : Slinn Voda, the Rising Deep, bonne tant que le deck lançait ; une fois le deck passé à la
  réanimation, 8/8 vanille (un permanent mis en jeu sans être lancé ne peut pas être kické). Aucun
  outil ne l'a signalé. Une validation est datée de l'architecture sous laquelle elle a été faite.
- **Un score de synergie ne voit pas les interactions internes à la liste** : il est calculé carte
  contre commandant, jamais carte contre carte. Ne coupe jamais sur un score bas, ni sur une
  proposition de `suggest_cuts`, sans avoir cherché ce que la carte fait avec les autres. Cas de
  coupes défendues après lecture : un gain de vie au dégagement couplé à une carte qui dégage à
  chaque étape adverse ; une force 1 que le pump massif de la liste rend imblocable ; un changelin.
- **Une grosse créature à cycling est la récompense et son propre activateur.** Quand un deck veut
  une carte chère dans une zone et un effet bon marché pour l'y mettre, cherche d'abord la carte qui
  fait les deux. Évalue-la à son coût de cycling ; le landcycling cherche en plus un terrain. Cas :
  pour un commandant qui veut une créature de valeur 6+ au sommet, cinq sorts de sélection (Ponder,
  Preordain…) ajoutaient 2 points de réussite au tour 4, dix créatures 6+ à cycling 22 à 24 points
  de plus. Prix annoncé : densité tribale de 75 % à 45 %. Effet sur la courbe : `base-de-mana.md`.
- **Un bonus de force sans évasion ne produit aucun dégât de plus** : +20/+0 bloqué par un jeton
  1/1 inflige zéro. Dans tout plan où la puissance brute est le levier, tiens **deux compteurs
  séparés** : les cartes qui produisent la puissance, celles qui la font arriver (piétinement, vol,
  imblocable, pump de masse). Le second est presque toujours le plus bas et plafonne le résultat.
  Cas : bonus de force de groupe massif, aucun piétinement ni imblocable dans les 99 ; un moyen de
  franchir les bloqueurs n'était disponible que dans 52 % des parties au tour 7. Timing : un gain
  de force venu du lien de vie arrive après l'assignation des dégâts.
- **Troisième compteur quand le levier est un déclencheur répété : la survie de la source.** Ne
  demande pas ce qu'une carte ajoute au déclenchement, mais **combien de fois il aura lieu avec
  elle, contre sans elle**. Cas : Arabella, Abandoned Doll (1/3) frappe à l'attaque, avant les
  bloqueurs ; « l'imblocabilité n'ajoute rien » a fait couper deux cartes. Or seul un bloqueur de
  force 3+ la tue, ce que Delney, Streetwise Lookout interdit justement. Pas de lecture à l'envers.
- **En singleton, la protection est un bonus, jamais un plan** : avec 4 exemplaires dans 99 cartes,
  tu en tiens un au tour 6 dans 40,9 % des parties (en commençant, 12 cartes vues) ; avec 6, 54,9 %.
  Réponse structurelle : un deck capable de **renoncer à l'action** sans s'effondrer.
- **Compte la densité de déclenchements**, pas le nombre de cartes « synergiques » : estime les
  déclenchements par tour de chaque permanent, avec sa cadence, somme, compare les versions.

### Présenter les échanges

- **Chaque échange est apparié un pour un**, avec la raison du remplacement. Jamais une liste
  d'entrées d'un côté et de sorties de l'autre.
- **Réévalue chaque coupe à la lumière des ajouts de la même passe** : une petite créature coupée
  « pour son corps » devient une source de dégâts quand on ajoute sept effets « une créature arrive
  → dégâts ».
- Avant de présenter, fais une **passe contradictoire** sur tes propres propositions : sur deux
  passes mesurées, elle en a invalidé 2 sur 3, puis 4 coupes sur 8, qu'aucun contrôle mécanique
  n'avait vues (ils mesurent des propriétés de cartes, jamais des relations). Elle teste
  l'exécution, pas le cadrage : expose le cadrage tôt au joueur.
- Une fois appliqués, les échanges entrent dans l'historique de la fiche avec leur motif :
  `fiche-de-deck.md`.

## Les sources

### La hiérarchie des niveaux de preuve

| Niveau | Nature | Exemples | Ce qu'on en tire |
| :-- | :-- | :-- | :-- |
| T1 | Documentation officielle, calcul vérifiable, régression publiée | règles et brackets WotC, hypergéométrique, formules de Karsten | constat |
| T2 | Méthode publiée et argumentée, avec ses limites | Kelvin Chen, Command Zone, Commander's Herald | constat si le raisonnement tient, sinon hypothèse |
| T3 | Consensus de pratiquants, non sourcé | quotas de rampe, nombres de conditions de victoire | hypothèse |
| T4 | Contenu commercial ou généré par IA | blogs d'outils à liens d'affiliation | taxonomie seulement, jamais un nombre |

- Le test sur le deck concerné (voir `mesure.md`) l'emporte sur une heuristique publiée quand la
  question est la même.
- Rapporte **le niveau le plus élevé qui affirme la chose**, jamais « N sources concordent ». Vingt
  sources T3 et aucune T1 font une hypothèse.
- **Le contenu de deckbuilding se recopie** : quatre guides d'upgrade de precon donnaient le même
  conseil dans le même ordre, sans donnée. Ne plus rien apprendre après cinq sources T3, c'est
  avoir épuisé les reformulations, pas avoir réglé la question.
- **Face à une source qui contredit**, retrouve la question précise sur laquelle elle est calibrée.
  Si elle diffère de la tienne, personne n'a tort ; si elle est identique, **teste, ne débats
  pas**. Cas : « la rampe vaut mieux qu'un terrain de plus » est vrai pour 4 manas au tour 4, faux
  pour un deck dont les cartes décisives coûtent 6 (détail : `base-de-mana.md`).

### EDHREC : synergie contre taux d'inclusion

- Dis toujours **quelle métrique** tu cites. Le **taux d'inclusion** décrit une pratique : EDHREC
  agrège des listes publiques sans aucun résultat de partie, et l'inclusion capte surtout
  disponibilité, prix, ancienneté, présence en precon. N'écris jamais « 92 % des decks la jouent,
  donc c'est une bonne carte ». Données EDHREC : T1 sur ce qu'elles comptent, T3 dès qu'on en tire
  une conclusion sur la force d'une carte.
- Le **score de synergie** (fréquence avec ce commandant comparée aux autres decks) est relatif et
  robuste à ce biais : il **peut appuyer** une recommandation, tant que le commandant est en jeu.
- Un score très élevé mesure aussi la **dépendance** au commandant : passe la carte au décompte des
  inertes (phase 1) après avoir lu ce qui la déclenche. Un score bas est une **question**, pas une
  raison de couper (phase 5).
- Exemple relevé au 17/10/2026 avec `edhrec_card_synergy` : Currency Converter sous Quintorius,
  History Chaser, synergie +89 %, inclusion 92,5 %. Aucun des deux chiffres ne dit que la carte
  gagne ; le premier appuie sa présence, le second décrit une habitude.

### Rapporter une preuve

- Source, niveau et date avec chaque affirmation : « Rampe 10, jusqu'à 12 (Command Zone,
  épisode 658, 2025 ; T2-T3) ». Les T3-T4 s'écrivent en hypothèse, jamais en constat. Une donnée qui se périme
  (Game Changers, prix, légalité, templates) porte sa date de lecture.
- Un chiffre mesuré sur le deck se rapporte avec son protocole et son bruit ; s'il fonde une
  recommandation, il se produit deux fois, par deux chemins : `mesure.md`.

## Le pilotage : mulligan, décisions de jeu, goldfish

### Une décision de jeu bien réglée bat souvent le meilleur échange de cartes

- Avant de proposer le moindre achat, **teste les décisions de jeu gratuites** — seuil de mulligan,
  ordre de priorité des sorts, choix de cible —, chiffre-les et présente-les **en premier**.
- Cas : quatre vagues d'échanges (baisser la courbe, ajouter des terrains, de l'évasion, une
  condition de victoire) ; la meilleure valait +3 points sur l'indicateur clé au tour 5, pour une
  trentaine d'euros. Jeter systématiquement les mains de sept à deux terrains : **+7,6 points, pour
  rien**, écart bien au-dessus du bruit. Ce réflexe manque parce qu'on demande d'optimiser une
  liste, et qu'on cherche alors dans la liste.

### Le mulligan : un filtre de terrains, puis une couverture de rôles

- **Le nombre de terrains filtre** (levier mesuré) : jeter les mains de sept à deux terrains a
  rapporté les +7,6 points ci-dessus, au prix d'une main de sept gardée dans 51 % des parties au
  lieu de 80 %. Repère publié pour la règle actuelle (Karsten, 2022 : mulligan de Londres, premier
  mulligan gratuit en multijoueur) : première main de 7 rejetée à 0, 1, 2, 6 ou 7 terrains ; main
  de 7 suivante rejetée à 0, 1, 6 ou 7 (gardée à 2 terrains) ; main de 6 après remise au fond
  rejetée à 0, 1, 5 ou 6 ; main de 5 rejetée à 0, 1 ou 5. Les seuils de Schulze (2019) datent de
  l'ancienne règle de mulligan. Mesuré sur un deck : re-mesure sur le tien avant d'en faire une
  règle. Effet sur le nombre de terrains nécessaire : `base-de-mana.md`.
- **La couverture de rôles décide** parmi les mains qui passent le filtre : terrains, accélération,
  accès aux cartes, interaction. Demande « quels rôles sont couverts, lesquels manquent ? », jamais
  « ai-je telle carte ? ». Liste type (Corey Williams, formulée pour le cEDH) : un ou deux terrains,
  un rocher, une source de pioche, une interaction. Une main de sept avec quatre cartes du même rôle
  vaut moins qu'une main de six qui en couvre quatre.
- Le premier mulligan est gratuit en multijoueur (règle 103.5c) : il autorise un seuil de garde
  plus exigeant qu'en 60 cartes.

### Le goldfish : tour de victoire et cartes vues

- Un goldfish sans compter ne mesure rien. Relève deux nombres sur chaque main jouée jusqu'au
  bout : le **tour de victoire** (seule mesure du plan complet : une courbe améliorée qui ne le
  déplace pas n'a rien amélioré) et les **cartes vues** (consistance indépendante de la vitesse :
  gagner au tour 9 en voyant 22 ou 34 cartes, ce n'est pas le même deck).
- Compare des variantes de la même liste, jamais dans l'absolu. « Ça a l'air plus fluide » n'est
  pas une mesure. **Trois vraies parties minimum** avant tout changement majeur.
- Protocole complet (vingt mains, cinq tours, interaction simulée, aléa, écart-type sur plusieurs
  tirages) : `mesure.md`.

## Upgrader un precon

- **Joue-le 3 à 5 fois tel quel** avant de toucher quoi que ce soit, et note : cartes mortes,
  situations où il manquait quelque chose, tenue de la base de mana, cartes qui ont surperformé.
- **Ne suppose pas le bracket 2** : un precon peut contenir un Game Changer. Audite-le comme tout
  deck (`bracket-et-combos.md`).
- Puis les phases dans l'ordre. Ordre de travail de la phase 5 : l'**intention** de l'upgrade, puis
  les **entrées**, puis **seulement** les sorties. Trie les 99 en trois groupes selon leur soutien
  au plan du commandant ; les premières coupes viennent du troisième groupe (consensus, T3).
- Profils à couper en premier (T3) : créatures vanille surcoûtées, tours de combat situationnels,
  retrait inefficace, cartes hors thème, pièces « win-more » redondantes.
- Ajouts (T3) : base de mana (terrains engagés remplacés par des bicolores dégagés), rampe,
  et **au moins deux** sources de pioche. Conseil budgétaire récurrent : painlands et checklands
  avant les fetchlands (détail : `base-de-mana.md`).
- **Question non tranchée : base de mana d'abord, ou rampe d'abord ?** Les guides se contredisent
  et aucun n'a de donnée. Ne tranche pas par principe : regarde ce que les parties jouées ont
  montré (couleurs ou terrains engagés au tour clé, ou bien quantité de mana insuffisante), dis
  sur quoi tu t'appuies, et laisse le joueur décider.
