# Outils : serveur `mtg`, deck-wizard, sites de deckbuilding

- Lis ce fichier avant le premier appel d'outil d'une séance, et chaque fois qu'un outil renvoie
  une erreur, un zéro, un « ok », un PASS, une liste vide ou un résultat trop net.
- Relis la section de l'outil concerné avant de citer un de ses chiffres à l'utilisateur.

Les états d'outils datent du **17/10/2026** (serveur `mtg-mcp-server` 3.0.0) et du **18/10/2026**
(copie de deck-wizard du 14/10/2026). Un outil peut changer de comportement à la mise à jour
suivante. Aucun simulateur
de parties n'est installé (Forge n'est pas fourni) : la méthode de mesure est dans `mesure.md`.

## 1. Quel outil pour quelle question

| Question | Premier choix | Second chemin, contrôle | À savoir |
| :--- | :--- | :--- | :--- |
| Texte d'une carte (oracle) | `mcp__mtg__scryfall_card_details` | `scryfall-lookup "<Nom>"` (deck-wizard), `web-fetch` sur l'API Scryfall | Jamais de mémoire. Recto-verso : face arrière absente, voir §2 |
| Prix | `mcp__mtg__scryfall_card_price` (USD, USD foil, EUR du jour) | `price-check` (deck-wizard), comme estimation | Prix local en USD seulement, daté du téléchargement des données : §3, ligne `price-check` |
| Combos d'une liste | `mcp__mtg__spellbook_find_decklist_combos` | `combo-search` (deck-wizard), lecture des oracles à la main | Zéro combo n'est pas une preuve : `bracket-et-combos.md` |
| Combos d'une carte | `mcp__mtg__spellbook_find_combos` avec `color_identity`, puis `spellbook_combo_details` | `combo-discover --card` (deck-wizard) | Sans le filtre de couleur, des combos hors identité sortent |
| Bracket | Aucun outil fiable : audit à la main | `spellbook_estimate_bracket` comme indice seulement | Procédure : `bracket-et-combos.md` |
| Staples EDHREC | `mcp__mtg__edhrec_commander_staples` | `commander_overview` | Nommer la métrique citée : §5 |
| Synergie carte-commandant | `mcp__mtg__edhrec_card_synergy` | `evaluate_upgrade` | Ne contrôle pas l'identité de couleur |
| Règle complète | `mcp__mtg__rules_lookup` (texte intégral de la règle) | Grep dans `comprehensive-rules-*.txt`, `rules-lookup --term` | `rules_interaction`, `rules_scenario`, `keyword_explain` : à recouper sur le texte de la règle |
| Rulings officiels | `mcp__mtg__scryfall_card_rulings` | `rulings-lookup --card` (deck-wizard) | Second chemin de tout cas litigieux |
| Recherche par effet | `mcp__mtg__scryfall_search_cards` | `card-search` (deck-wizard, données locales) | Pas d'oracle dans les résultats : §2 |
| Analyse d'une liste | deck-wizard : `deck-tune`, `mana-audit`, `deck-stats` | Recompte à la main des points qui fondent une décision | Pas `deck_analysis` : il expire |
| Légalité, identité, total | `legality-audit` + compte des 100 cartes soi-même | `scryfall_card_details` → `legalities.commander` pour une carte récente | `deck_validate` est cassé |
| Liste publiée en ligne | Export texte natif fourni par l'utilisateur | `mcp__mtg__moxfield_decklist` | Jamais de scraping HTML : §5 |

## 2. Serveur `mtg`

Déclaré dans `.mcp.json` du dossier des decks : ses outils (`mcp__mtg__<nom>`, 69 outils)
n'existent que dans une session ouverte dans ce dossier. S'ils manquent, dis-le et propose de
rouvrir la session dans le dossier des decks ; ne remplace pas l'oracle par ta mémoire.

### État au 17/10/2026

| État | Outils | Conduite |
| :--- | :--- | :--- |
| Répondent | `ping`, `scryfall_card_details`, `scryfall_card_price`, `scryfall_search_cards`, `scryfall_card_rulings`, `rules_lookup`, `spellbook_find_decklist_combos`, `spellbook_find_combos`, `spellbook_combo_details`, `edhrec_commander_staples`, `edhrec_card_synergy`, `commander_overview`, `goldfish_metagame`, `moxfield_search_decks`, `moxfield_decklist` | Utiliser, en lisant les pièges ci-dessous |
| Répondent, jugement faux ou sortie incomplète | `spellbook_estimate_bracket`, `suggest_cuts`, `evaluate_upgrade`, `card_comparison` | Jamais comme preuve ni comme critère de coupe |
| Cassés : « Bulk metadata missing 'download_uri' » | tous les `bulk_*`, `price_comparison`, `deck_validate`, `theme_search`, `suggest_mana_base`, `color_identity_staples`, `precon_upgrade` | Ne pas réessayer : passer par `scryfall_card_details` ou deck-wizard |
| Expirent | `budget_upgrade` (toujours), `deck_analysis` (répond sur 5 cartes, expire sur 35) | Décomposer : combos + staples EDHREC + fiches de cartes |

Tout autre outil qui renvoie le message « Bulk metadata missing » souffre de la même panne
(Scryfall a renommé le champ lu par le serveur) : même conduite.

### Règles d'appel

- **Listes** : un tableau JSON de noms seuls, sans quantité ni préfixe `1x`. Le commandant est
  **exclu** de `decklist` et passé à part (`commanders` en tableau, ou `commander_name`).
- **Débit** : pas plus de 3 appels en parallèle (cinq `scryfall_card_details` simultanés ont
  échoué en « Connection closed » le 17/10, les mêmes un par un ont réussi). Après « Connection
  closed », appelle `ping`, puis relance les appels un par un. Après un délai dépassé, attends 30
  à 40 s avant de relancer, une seule fois. Serveur déconnecté pour de bon : `web-fetch` (§4).
- **Noms** : écris le nom exact, accents compris. Scryfall a retrouvé « Seance » pour « Séance »
  le 17/10, mais le nom renvoyé porte l'accent, et les comparaisons entre listes, fiches, diffs et
  outils se font caractère par caractère : reprends toujours le nom renvoyé. Nom approximatif :
  `fuzzy: true`, puis reprends le nom exact.
- **Recherche par effet** : `id<=<couleurs> o:"<texte exact>" cmc<=<n> f:commander` (exemple :
  `id<=rw o:"each opponent" cmc<=3 f:commander`). Les résultats donnent nom, coût, type, rareté,
  prix et rang EDHREC, **pas l'oracle** : appelle `scryfall_card_details` sur chaque candidat et
  cherche la clause qui restreint (zone visée, types, « once each turn ») avant de proposer. Une
  recherche plein texte trouve la phrase, pas l'effet : `construction-et-choix.md`.
- **Résultats tronqués par `limit`** (30 par défaut) : `has_more` reste `false` quand `showing` est
  inférieur à `total_cards` (vu le 17/10 : 3 cartes montrées sur 94, `has_more: false`). Compare
  `showing` à `total_cards`, puis augmente `limit` (0 = tout) ou pagine avec `page`.
- **Recto-verso** : `scryfall_card_details` renvoie l'enregistrement combiné, avec `power` et
  `toughness` à `null` et l'oracle de la **seule face avant** (Ojer Axonil, 17/10 : le texte de
  Temple of Power est absent). Lis les deux faces par l'API (`card_faces`) avec `web-fetch` (§4).
- **Prix** : `scryfall_card_details` et `scryfall_card_price` donnent le prix du jour d'une seule
  impression, pas forcément la moins chère. Pour un joueur européen, lis le champ `eur`
  (Cardmarket) : l'écart avec l'USD n'est pas constant (Ponder 3,07 € contre 1,69 $), le classement
  des cartes chères change avec la devise.
- **Sorties longues** : passe `response_format: "concise"` et un `limit`. `spellbook_find_decklist_combos`
  renvoie tous les combos à une ou deux cartes près (`almost_included`, des dizaines d'entrées) :
  lis `included` d'abord. Si le client écrit le résultat sur disque, lis le fichier par tranches
  (Read avec `offset`/`limit`) ou cherche dedans avec Grep ; ne relance pas l'appel.

### Pièges propres à certains outils

- `spellbook_find_decklist_combos` : publie `easy_prerequisites` et `notable_prerequisites`, souvent
  vides ; lis quand même l'oracle de chaque pièce. Faux négatif connu : Hofri Ghostforge + Breath
  of Fury + une créature, boucle infinie absente de `included` (reconstaté le 17/10). Un
  `included: []` a déjà fondé un verdict de bracket faux.
- `spellbook_estimate_bracket` : le 17/10, sur une liste contenant Cyclonic Rift, Thassa's Oracle
  et Demonic Consultation, il a renvoyé `game_changer_cards: []` et `two_card_combos: []`, alors
  que `spellbook_find_decklist_combos` trouvait Thassa's Oracle + Demonic Consultation. Ses
  lettres (`E`, `R`, `S`, `P`, `C`) ne correspondent pas aux brackets officiels, et il contredit
  parfois `combo-search` sur la même paire. Ne le cite jamais comme verdict.
- `suggest_cuts` : le 17/10, sur une liste contenant Grizzly Bears, il a proposé de couper Sol
  Ring et Arcane Signet en premier. Il classe par taux d'inclusion et score de synergie EDHREC ; il
  a déjà proposé des pièces de moteur centrales. Une coupe se décide sur la fonction de la carte
  dans la liste : `construction-et-choix.md`.
- `evaluate_upgrade` : a évalué Grizzly Bears (vert) pour Talrand (mono-bleu) sans alerte. Vérifie
  toi-même l'identité de couleur de chaque ajout.
- `card_comparison` : répond sans les colonnes de synergie, d'inclusion et de combos annoncées.
- `commander_overview` : liste des combos qui sortent de l'identité du commandant (des combos
  Grixis pour un commandant mono-bleu le 17/10) ; filtre avant de les mentionner.
- `edhrec_commander_staples` : le `total_decks: 0` d'en-tête est un artefact ; les `num_decks` de
  chaque carte sont les vrais effectifs.
- `moxfield_*` : rapportés en panne (403 Cloudflare) par le passé ; `moxfield_search_decks` et
  `moxfield_decklist` répondent le 17/10 sur un deck public. S'ils retombent, demande l'export.

## 3. deck-wizard dans notre méthode

deck-wizard est un skill à part, installé dans `~/.claude/skills/deck-wizard`, avec son propre
`SKILL.md`, très long. Ne le suis pas étape par étape : prends-y les scripts, dans l'ordre de nos
phases. Commander papier seulement : ignore ses sections sur les autres formats, et pour les
règles de bracket, suis `bracket-et-combos.md`, pas son résumé. Son `SKILL.md` renvoie à un skill
`rules-lawyer` qui n'est pas installé : passe par les outils de règles du serveur `mtg` et par le
fichier des règles. Il demande aussi un `download-rules` par séance et des fichiers dans `/tmp` :
inutile ici, le fichier des règles est déjà dans le dossier du skill, et les fichiers de travail
vont dans le dossier du deck (ci-dessous).

### Préparer les appels

- **Lance les scripts depuis l'outil Bash** (Git Bash sous Windows, Terminal sur Mac) et passe
  toujours `--bulk-data` avec le chemin absolu des données, plutôt que de compter sur leur
  emplacement par défaut.
- **Chemins absolus partout** : `uv run --directory` place le dossier courant dans le skill, un
  chemin relatif pointe au mauvais endroit. Sous Windows, écris `C:/Users/<nom>/…`. L'état du
  shell ne survit pas d'un appel Bash à l'autre : réécris les chemins complets à chaque commande.
- **Encodage** : vérifie en début de séance que `echo $PYTHONUTF8` affiche `1` (réglage posé par
  l'installateur dans `.claude/settings.json` du dossier des decks). Vide, par exemple dans une
  session ouverte ailleurs, préfixe chaque appel par `PYTHONUTF8=1`. Sans lui, sous Windows, les
  scripts ne plantent pas : ils sous-comptent avec des chiffres plausibles (détail dans le tableau
  des pièges, ligne « Tous »).
- **Fichier des règles** : trouve son nom exact par Glob `comprehensive-rules-*.txt` dans le
  dossier du skill, et passe-le à chaque script qui l'accepte (`--rules-file`).
- **Données de cartes** : `~/.cache/mtg-skills/mtgjson/AllPrintings.json` (MTGJSON, environ
  800 Mo avec les prix `AllPricesToday.json`), figées à la date du dernier `download-mtgjson` :
  oracles, légalités, drapeau Game Changer et prix. Lis cette date (`ls -l`) quand une carte
  récente est en jeu. Pour les rafraîchir, demande d'abord à l'utilisateur (téléchargement
  d'environ 800 Mo), puis lance `download-mtgjson`.
- **Fichiers de travail** : un dossier par deck, `<dossier des decks>/.cache/<commandant>/`. Écris
  les JSON qui contiennent des noms de cartes (`cuts.json`, `adds.json`) avec l'outil Write, pas en
  heredoc : les apostrophes cassent le shell. Lis un fichier existant avant de le réécrire, et ne
  lance jamais dans le même message l'écriture d'un fichier et le script qui le lit : le script
  lirait l'ancienne version. Ne lis pas `deck.hydrated.json` en entier (énorme) : `card-summary`,
  ou Grep dedans.

### Séquence type

Revérifiée le 18/10/2026 sur la version du 14/10 : chaque ligne a été lancée telle quelle.

```bash
# <D> dossier du skill, <B> AllPrintings.json, <R> fichier des règles, <W> dossier de travail
# du deck : tous en chemins absolus.
# Chaque script deck-wizard se lance précédé de : uv run --directory "<D>" --frozen

# 1. Normaliser la liste (commande shell seule) : « N Nom », jamais « Nx Nom »
sed -E 's/^([0-9]+)x /\1 /' "<W>/liste-brute.txt" > "<W>/liste.txt"
# 2. Lire la liste ; vérifier que le total annoncé vaut 100
parse-deck "<W>/liste.txt" --format commander --output "<W>/deck.json"
# 3. Placer le commandant (nom exact) : muet s'il réussit, « not found in deck cards » sinon
set-commander "<W>/deck.json" "<Commandant>"
# 4. Hydrater : vérifier que missing est vide (card_count compte des noms distincts : 84 pour
#    100 cartes). Écrit <W>/deck.hydrated.json à côté du deck.
deck-hydrate "<W>/deck.json" --bulk-data "<B>"
# 5. Analyses : toutes prennent le seul deck.json
deck-tune "<W>/deck.json" --bulk-data "<B>" --bracket <1-5> --max-swaps <N> --output "<W>/tune.json"
mana-audit "<W>/deck.json" --bulk-data "<B>"
deck-stats "<W>/deck.json" --bulk-data "<B>"
combo-search "<W>/deck.json" --bulk-data "<B>"
cut-check "<W>/deck.json" --cuts "<W>/cuts.json" --multiplier-low <n> --multiplier-high <n> --opponents 3 --bulk-data "<B>" --rules-file "<R>"
price-check "<W>/deck.json" --bulk-data "<B>" --budget <usd>
legality-audit "<W>/deck.json" --bulk-data "<B>" --rules-file "<R>"
# Ponctuels
scryfall-lookup "<Nom>" --bulk-data "<B>"
rules-lookup --term "<mot-clé>" --rules-file "<R>"
rulings-lookup --card "<Nom>" --bulk-data "<B>"
web-fetch "https://api.scryfall.com/cards/named?exact=<Nom encodé pour une URL>"
```

Plus de chemin de cache à transmettre : chaque script se réhydrate seul depuis
`deck.hydrated.json`, indexé sur le contenu de `deck.json` et des données. Après une modification
de la liste, relance `deck-hydrate` pour relire `missing` avant les analyses. `scryfall-lookup
--batch` ne prend plus qu'une liste de noms (candidats, pièces de combo) : sur un deck parsé, il
s'arrête et renvoie à `deck-hydrate`. `cut-check` lit le commandant dans le deck (`--commander`
pour l'autre partenaire).

### Avant de citer un chiffre de deck-wizard

- Contrôle l'instrument sur trois cartes atypiques de la liste (fetchland, coût X ou réduction de
  coût, cycling, recto-verso à dos terrain), comme dit `mesure.md`, et assure-toi que ton propre
  recompte ne lit pas le même champ que l'outil.
- L'encodage cassé ne donne plus des zéros mais des chiffres plausibles : un `deck-tune` dont
  `focus` dit SPINE-LED avec `engine_pool: 0`, un `mana-audit` qui affiche « unmodelled (no IR) »
  et des terrains réduits à leurs basiques signalent un instrument cassé, pas un deck cassé :
  répare, remesure, puis conclus. Témoin connu : le deck de référence du bilan de santé (precon
  « Animated Army », commandant Bello, Bard of the Brambles) compte 15 cartes d'interaction quand
  tout fonctionne, 8 sans `PYTHONUTF8` (revérifié le 18/10/2026 sur la version du 14/10).

### Pièges connus et parades

Revérifié le 18/10/2026 sur la version du 14/10, sur le deck de référence et des listes de test
construites pour chaque piège, sauf mention contraire.

| Script | Piège constaté | Parade |
| :--- | :--- | :--- |
| `parse-deck` | Ne lit pas le préfixe `1x` : sort sans erreur et annonce le nombre de lignes comme nombre de cartes (« 84 cards » pour 100) ; « 8x Mountain » devient une carte nommée ainsi. Suite : `set-commander` « not found », puis `deck-hydrate` interroge l'API Scryfall pour chaque nom inconnu et s'arrête sur une erreur 429 | Normaliser en `N Nom` avant tout parsing ; vérifier le total |
| Tous | Sans `PYTHONUTF8=1`, passe dégradée silencieuse et plausible (deck de référence) : interaction 8 au lieu de 15, rampe 24 au lieu de 26, sources de couleur réduites aux basiques (`deck-stats` G=13 R=11 au lieu de G=27 R=25, couleurs de `mana-audit` en FAIL, vissage du goldfish 21,6 % au lieu de 17,0 %), `focus` de `deck-tune` en SPINE-LED. La pioche, elle, reste juste : un compte correct ne prouve pas l'encodage | Vérifier la variable ; signature : « unmodelled (no IR) » dans `mana-audit` ; ne jamais citer ces chiffres |
| `playtest-goldfish`, `mana-audit` | Les fetchlands sont désormais crédités (cinq fetchs typés à la place de cinq basiques : vissage 16,1 % contre 17,2 %), mais mal : un fetch typé reçoit les couleurs de ses types même absents du deck (Misty Rainforest fait lancer un sort vert dans un deck sans Forêt) ; un fetch générique (Evolving Wilds, Fabled Passage) vaut, au goldfish, les couleurs des basiques du deck (aucune s'il n'en a pas, avec un avertissement), et pour `mana-audit` toutes les couleurs (Evolving Wilds compté source de blanc sans Plaine). MDFC à face terrain joué comme terrain ; transformable à dos terrain (Ojer Axonil) compté, une fois lancé, comme une créature qui produit du mana | Avant de citer `color_screw_rate` ou une production de couleur : vérifier que chaque fetch trouve un terrain du deck, recompter les sources réelles (`base-de-mana.md`) |
| `playtest-goldfish` | Traite tout terrain qui produit du mana comme dégagé, entrée engagée conditionnelle ou systématique : avec Temple of Abandon, Gruul Turf ou Rootbound Crag seul en jeu, Sol Ring part au T1 comme avec une Forêt ; seuls les fetchs à entrée engagée sont retardés d'un tour | Il ne départage pas deux bases qui diffèrent par leurs terrains engagés : tempo chiffré à la main |
| `playtest-goldfish` | Mulligan selon son code (20 000 parties : 71,3 / 17,0 / 5,3 / 6,4 % gardées à 7/6/5/4 cartes, pour 71,2 / 17,3 / 5,2 / 6,3 % attendus) : aucun mulligan gratuit, main plus petite tirée directement, garde si 2 à 5 terrains et un non-terrain de coût 3 ou moins. Le commandant est mélangé dans la bibliothèque de 100 cartes, pas tiré de la zone de commandement. Compte des sorts lancés : Arcane Signet vaut Purphoros ; ni combo, ni dégât, ni tour de victoire, ni cartes vues, malgré « combo timing » dans son aide | Ressources seulement ; tour de victoire et cartes vues à la main : `mesure.md` |
| `combo-search` | Aucun champ de précondition (rend cartes, résultat, description, `mana_needed`, identité, popularité, `bracket_tag`). Hermit Druid + Thassa's Oracle marqué `GAME_WINNING` dans un deck à 17 basiques (≈4,5 cartes meulées par activation). Faux négatif : Hofri + Breath of Fury. Aggravated Assault + Sword of Feast and Famine, manqué autrefois, est trouvé | Lire l'oracle de chaque pièce et le champ `description` de chaque combo à une carte près (il nomme parfois d'autres pièces) ; boucles cherchées à la main |
| `deck-tune` | Le champ `wincons` et la section `combos` héritent des combos fantômes (« ok » à 14, dont 6 venus des combos, parmi lesquels les deux paires Hermit Druid d'un deck à 17 basiques) | Recompter les conditions de victoire sur l'oracle |
| `deck-tune` | Verdict `SPREAD-THIN` : seuil binaire (3 axes viables), sévérité = 4 + nombre d'axes portés par 1 ou 2 cartes. Deck de référence : 26, dont 22 axes isolés (« Bear tribal », « Dinosaur tribal »…) ; une carte d'un type de créature inédit la fait monter | Ne jamais le citer ; ne jamais comparer deux sévérités sans savoir comment chacune est calculée |
| `deck-tune` | Rôles comptés par motifs de texte : Fact or Fiction sans rôle, Crippling Fear compté interaction mais pas balayage, tout ce qui inflige des dégâts compté interaction, jusqu'au doubleur Gratuitous Violence (15 sur le deck de référence, dont trois enchantements à dégâts) | Lire quelles cartes il a rangées dans chaque rôle (`scorecard.shape.evidence`) avant de citer un compte |
| `deck-tune` | Échanges proposés : « barely played for this theme » mesure un taux de jeu, pas une synergie ; « over template band » coupe sur la seule bande d'un rôle ; a proposé de couper des pièces de moteur | Des candidats à examiner, jamais une liste à appliquer |
| `deck-stats` | Ignore les réductions de coût (Blasphemous Act compté à 9) ; compte un sort à X à sa valeur de mana (Stroke of Genius 3, Hydroid Krasis 2) ; ignore le cycling (Decree of Pain compté à 8 ; ailleurs, coût moyen 3,79 affiché, 3,05 recalculé). Sa liste de coûts alternatifs (suspend, evoke, flashback, aventure…) reste à côté du coût moyen | Recalculer la courbe au coût réellement payé : `base-de-mana.md` |
| `mana-audit`, `deck-stats` | Comptent comme terrain une MDFC à face terrain (Malakir Rebirth), plus un transformable à dos terrain (Ojer Axonil, compté créature) : 38 terrains réels + Malakir Rebirth + Ojer Axonil → « 39 lands » ; PASS/FAIL calculé sur ce compte | Compter les terrains réels à la main, signaler les recto-verso à part |
| `mana-audit` | Affiche une bande et deux repères nommés « Burgess » et « Karsten » qui ne sont pas la régression de `base-de-mana.md` | Ne cite pas son verdict sans recalcul |
| `deck.hydrated.json`, cache de `scryfall-lookup --batch` | `power` et `toughness` désormais remplis ; `None` au premier niveau d'un recto-verso transformable (Ojer Axonil), dont les valeurs sont dans `card_faces` | Pour un recto-verso, lire `card_faces` ou `scryfall_card_details` |
| `price-check` et prix du sidecar | Prix MTGJSON du jour du téléchargement, en USD seulement : le 18/10, à 1-4 % de Scryfall (Scroll Rack 31,64 contre 31,97 $, Rhystic Study 68,05 contre 69,03 $, Entomb 16,61 contre 17,28 $), puis vieillit avec les données. Une carte sans prix (pas encore sortie) est retirée du total sans avertissement | Revérifier en direct, dans la devise du joueur, toute carte au-dessus d'une dizaine de dollars avant de la recommander ; sous 5 $, inutile. Dater le total et nommer les cartes sans prix |
| `legality-audit` | PASS sur 101 cartes : il contrôle le minimum, pas le maximum. Légalité lue dans les données locales : une carte annoncée mais pas encore sortie au téléchargement y reste « not_legal » jusqu'au rafraîchissement (Cantankerous Captain, sortie le 13/11/2026 ; une carte récente déjà déclarée illégale deux fois à tort) | Compter les 100 cartes soi-même ; légalité d'une carte récente en direct (`legalities.commander`) |
| `cut-check` | Résultat nul n'est pas un feu vert : cinq coupes du deck de référence, dont Esika's Chariot et Unnatural Growth que Bello anime, toutes à zéro ; le déclencheur de Rampaging Baloths est extrait mais non compté (autrefois : 7 déclencheurs extraits, 1 analysé ; un lien de vie et une source d'imblocabilité manqués). Sans fichier de règles, « 0 keyword interactions » ne prouve rien | `--rules-file` toujours ; chaque coupe se juge sur sa fonction : `construction-et-choix.md` |
| Fichier des règles | Sans option, chaque script prend le plus récent `comprehensive-rules*.txt` du dossier courant (celui du skill sous `uv run --directory`), ou du dossier du deck pour `cut-check` et `legality-audit`. `rules-lookup --rule` rend le texte d'une sous-règle (702.19c) mais le seul titre d'une règle mère (702.19) ; `--grep` rend des extraits tronqués | `--rules-file <chemin absolu>` ; pour une règle mère, ses sous-règles une à une, `mcp__mtg__rules_lookup` ou Grep dans le `.txt` |
| `download-rules` | `PermissionError [WinError 5]` : c'est le dossier qui refuse (synchronisation ou antivirus sous Documents), pas le script (non revérifié le 18/10) | `--output-dir <dossier temporaire>`, puis copier dans le dossier du skill |
| `scryfall-lookup`, `deck-hydrate` | Les noms absents des données partent vers l'API en direct, un par un. Un 429 s'affiche désormais en clair (« 429 Client Error: Too Many Requests ») et arrête tout le script ; le 17/10, Scryfall l'a renvoyé dès la première requête. Un nom que l'API ignore donne « Card not found » | Corriger les noms d'abord ; sur un 429, attendre avant de relancer, sans conclure qu'une carte manque |
| Doc de deck-wizard | Son `SKILL.md` donne toujours 3 de force à Obeka dans un exemple ; elle en a 2 | L'oracle à la source, jamais un exemple de documentation |

## 4. Scryfall en direct, hors serveur

- `WebFetch` reçoit un 403 de Scryfall. Le script `web-fetch` de deck-wizard passe (revérifié le
  18/10 ; un 429 s'y affiche en clair : attendre, puis relancer une fois) :
  `web-fetch "https://api.scryfall.com/cards/named?exact=<Nom>"` renvoie la fiche
  complète, avec `card_faces` (oracle, force et endurance de chaque face) pour un recto-verso, et
  `/cards/search?q=<requête>` pour une recherche.
- Limite de Scryfall : 10 requêtes par seconde. En boucle, espace les appels et affiche le corps
  de chaque réponse en erreur.

## 5. Sources externes

### Listes en ligne : l'export texte natif, jamais le scraping

- **Scraping HTML** : une page Archidekt de ~75 entrées a rendu 72 lignes, sans aucune quantité
  de basique (« 8 Île » lue « 1 Île ») ; l'API JSON d'Archidekt a rendu une réponse vide par
  l'outil de lecture web. Ne fonde aucun diff de liste sur une page lue : demande l'export texte
  du site. Réserve la lecture de page aux métadonnées agrégées (un compteur `Size: 95` a révélé
  une liste incomplète).
- **Moxfield** : `moxfield_decklist` accepte l'identifiant ou l'URL d'un deck public et rend les
  zones (commandants, deck, réserve) avec les quantités. Deck privé ou outil en panne : export
  texte. `parse-deck` retire les codes d'édition de l'export Moxfield.
- **Liste à importer sur une plateforme** (Archidekt, Moxfield…) : ne devine pas sa syntaxe
  d'import. Demande au joueur un export de son deck fait depuis la plateforme et reprends-en le
  format ligne pour ligne ; rends une liste complète plutôt qu'un ajout, et demande-lui de vérifier
  le compteur de cartes du site juste après l'import.

### EDHREC

- Dis toujours quelle métrique tu cites. Le **taux d'inclusion** décrit une pratique (il capte
  disponibilité, prix, ancienneté, présence en precon) ; le **score de synergie** mesure un lien
  carte-commandant, jamais carte-carte. EDHREC n'a aucune donnée d'issue de partie.
- Un score bas est une question, pas une raison de couper : `construction-et-choix.md`.
- La liste des Game Changers se relit à chaque séance (page Game Changers d'EDHREC ou annonce
  officielle) : `bracket-et-combos.md`.

## 6. Règle transversale : zéro, « ok » et PASS ne prouvent rien

Le mode d'échec ordinaire de ces outils est le résultat plausible et faux, pas le plantage. Un
outil traite comme nul, sans erreur, tout champ qu'il ne sait pas lire. Cas vécus :

- `interaction: 0` (encodage absent) ; `color_screw_rate` sur des fetchlands lus sans couleur ;
- `included: []` à côté d'une boucle infinie réelle ; `game_changer_cards: []` sur trois Game
  Changers ; `wincons` « ok » nourri par deux combos fantômes ;
- `legality-audit` PASS sur 101 cartes ; `cut-check` muet ; trois bases de mana au même dixième ;
- un prix `null` compté zéro ; `power: None` sur 42 créatures pris pour un script bogué.

Conduite :

1. **Ouvre ce que l'outil a rangé** dans la catégorie : la liste des cartes derrière chaque compte
   (champ `evidence`, `included`, détail par carte), pas seulement le total ou le verdict.
2. **Fais-lui retrouver un cas dont la réponse est connue** avant de croire ce qu'il trouve (une
   carte atypique de la liste, le deck de référence du bilan de santé, une paire de combo connue
   comme Thassa's Oracle + Demonic Consultation).
3. **Recompte par un second chemin** qui ne lit pas le même champ ; un résultat identique entre
   des variantes censées différer prouve que l'outil ne voit pas la variable testée.
4. **Un « il n'existe pas »** est le résultat d'une recherche datée, pas un fait : dis-le ainsi.
5. Quand un outil manque ou ment, écris dans la fiche du deck le niveau de preuve atteint et
   l'alerte vérifiée fausse (`fiche-de-deck.md`), et pose à l'utilisateur la question qu'il peut
   trancher en dix secondes.
