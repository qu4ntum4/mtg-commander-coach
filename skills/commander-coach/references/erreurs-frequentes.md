# Erreurs fréquentes — liste de contrôle par moment de la séance

Quand lire ce fichier : au début de chaque séance, puis avant de présenter une proposition ou un chiffre.
Quand un outil, une mesure ou une lecture de carte donne un résultat qui arrange trop bien l'analyse.
Quand on met à jour la fiche du deck, pour ne rien y laisser qui ferait refaire la même erreur.

Chaque ligne : l'erreur, de Claude ou d'un outil → la parade, puis le cas d'origine de cas-d-ecole.md
en italique. Détail des pièges d'outils : outils.md. Presque aucune de ces erreurs n'a produit de
message d'erreur : le mode d'échec dominant est le résultat plausible et faux, attrapé par une seconde
mesure indépendante, un agent contradicteur ou l'utilisateur — jamais par relecture.

## Avant d'analyser

- Analyser une liste collée sans ouvrir la fiche → lire d'abord règles maison, cartes interdites,
  points ouverts, décisions tranchées (*Avant d'analyser : la fiche, puis la liste réellement jouée*).
- Partir de la liste enregistrée, d'un plan supposé appliqué ou de la page web du deck → export texte
  de la liste réellement jouée, diff annoncé, diagnostic hérité remesuré (même cas).
- Passer une liste `1x Nom` à `parse-deck` → normaliser en `N Nom` (son « 96 cards » comptait des
  lignes), puis recompter total et terrains par deux chemins (deux outils : 33 et 37 terrains).
- Supposer bracket, budget, nombre d'échanges ou niveau → les demander ; une enveloppe par passe n'est
  pas un plafond par carte ; la carte blanche se reçoit, elle ne se présume pas.
- Traiter la plainte dans ses mots (« inconsistant ») → la traduire en métrique mesurable (*Une
  « sévérité 40 » qui ne mesurait pas la plainte*).
- Ouvrir un axe que l'utilisateur n'a pas signalé → cadrer par ses douleurs vécues ; ce qu'il ne coche
  pas élimine un axe (*« 38 terrains, c'est trop » : l'intuition retirée avant présentation*).
- Poser « tuer la table seul » comme condition de succès d'un bracket 3 → la caler sur le bracket visé
  (*La redondance ajoutée sur le mauvais axe*).
- Reprendre une liste venue d'un autre format ou d'un duel → la repasser sous les contraintes du deck
  cible : légalité, bracket, quatre joueurs, budget.
- Reporter les exclusions d'un deck sur un autre → les préférences sont par deck, dans sa fiche.
- Travailler sans un outil (serveur coupé, chercheur de combos absent) sans le dire → écrire le niveau
  de preuve atteint, et poser au joueur la question de règle qu'il peut trancher.
- Citer de mémoire les Game Changers ou les bans → les relire le jour même (bracket-et-combos.md).

## En lisant les cartes

- Prendre l'oracle dans sa mémoire ou un exemple de documentation → la source : l'exemple de deck-wizard
  donne 3 de force à Obeka, elle en a 2 (*Ce qu'un multiplicateur multiplie vraiment, coûts compris*).
- Juger une carte à son nom ou la ranger dans une catégorie → lire la clause qualifiante, la zone et la
  limite exactes (*Lire la clause qualifiante, pas le nom de la carte*).
- Supposer qu'un déclencheur compte des cartes → vérifier s'il compte des événements (« one or more »)
  (*Un déclencheur qui compte des événements, pas des cartes*).
- Survoler « each turn », « cast », « another », « nonlegendary », « dies » → mot à mot ; meuler n'est
  pas mourir (*Deck à thème : le commandant que nourrissent les traits communs du thème*).
- Ne pas voir qu'un « may » manque → l'effet obligatoire peut jouer contre le deck : Bag of Holding
  exile toute carte défaussée (*Les refus de l'utilisateur avaient raison*).
- Ajouter une carte qui touche le commandant sans la tester contre la liste → un linceul éteint ses
  propres équipements et auras ; une protection contre le noir bloque ses réanimations noires.
- Reprendre une recommandation « habituelle » sans filtre → la confronter aux cartes présentes : sous un
  plafond d'un attaquant (Silent Arbiter), toute carte dont le bonus exige d'attaquer est morte.
- Garder une carte validée sous l'ancien plan → relire son oracle quand l'architecture change (*Une
  carte validée meurt quand le plan change*).
- Compter en payoff ce que le multiplicateur ne fait que charger, oublier ce qu'il multiplie contre soi
  → ce que rapporte et coûte l'occurrence de plus (*Ce qu'un multiplicateur multiplie vraiment, coûts compris*).
- Évaluer une carte sur sa probabilité d'être en main → dans le scénario où elle sert : un tuteur qui
  exige une créature légendaire est mort juste après le retrait du commandant.
- Dire qu'« un tuteur coûte une carte » → solde selon la zone visée : Demonic Tutor 0, Vampiric Tutor −1.
- Compter un recto-verso pour la mauvaise face → la face réellement jouée ; une face arrière
  transformable a la valeur de mana de la face avant.
- Laisser au hasard l'ordre de deux déclencheurs simultanés → le décider et l'écrire dans la fiche.
- Classer les sorts par rôle avec un filtre textuel → carte par carte, zone vérifiée : un filtre a
  compté 31 « moteurs », dont des cartes visant les cimetières adverses.
- Donner un chiffre de carte de mémoire → le recompter : Gray Merchant, 6-9 annoncé, 5,9 vérifié (*Le
  deck pouvait se tuer lui-même, et quatre coupes sur huit étaient fausses*).

## En utilisant les outils

- Citer un chiffre d'outil sans l'éprouver, ou le « confirmer » par un contrôle qui lit la même donnée
  → trois cartes atypiques à la main (fetch, coût X, cycling, face arrière) et une seconde mesure par
  une autre donnée (*Les fetchlands comptés comme ne produisant rien*).
- Lire un champ vide comme un zéro (fetchland sans `produced_mana`, coût X, cycling ignoré : coût moyen
  3,79 affiché, 3,05 réel) → recompter à la main (base-de-mana.md).
- Croire un tableau de bord plein de zéros, ou des comptes plausibles mais bas (sans `PYTHONUTF8`,
  interaction 8 au lieu de 15 sur le deck de référence) → mode dégradé de deck-wizard : réparer,
  relancer, remesurer (*Un tableau de bord plein de zéros*).
- Croire un résultat identique entre variantes censées différer → l'instrument ne voit pas la variable
  (*Trois bases de mana identiques à la décimale*).
- Citer un verdict ou une sévérité d'outil (`spread thin`) sans lire son calcul → ne pas le citer
  (*Une « sévérité 40 » qui ne mesurait pas la plainte*).
- Citer `playtest-goldfish` sur un deck à dégâts, à combo ou à tempo, ou son `color_screw_rate` → il
  compte des sorts lancés, voit dégagé tout terrain engagé et crédite un fetch de couleurs absentes
  du deck : chiffrer à la main.
- Croire un combo de `combo-search` et les conditions de victoire « ok » qui en découlent → lire les
  préconditions (*Deux combos gagnants fantômes, et des conditions de victoire « au vert »*).
- Prendre un « 0 combo » pour une preuve → chercher les boucles à la main parmi les pièces présentes
  (*Un infini qu'aucun outil ne voit, et une cible de bracket qui bouge*).
- Trancher entre deux outils de combos en désaccord → aucun n'est une preuve (*Une liste noire écrite à
  la main, trop étroite puis trop large*).
- Croire une liste de Game Changers vide, ou un `cut-check` muet → recompter ; un résultat nul ne prouve
  aucune sûreté.
- Lire un PASS de `legality-audit` comme « 100 cartes » → il contrôle le minimum (PASS sur 101) ; ses
  données locales datées voient « not legal » une carte récente : vérifier en direct.
- Citer un prix d'outil → revérifier en direct au-dessus d'un seuil : Scroll Rack annoncé 14,14 $, rien
  sous 33,85 $ ; liste d'achat ~57 $ et non 46 $. Prix dans la devise et le marché du joueur.
- Compter les terrains avec `mana-audit` ou `deck-stats` → ils comptent les MDFC à face terrain :
  compter les terrains réels à la main.
- Accuser son script devant un résultat vide → regarder ce que l'outil a renvoyé : force à `None` pour
  42 créatures, sans erreur (*Un anthem dans un deck qui compte les petites forces*).
- S'obstiner sur un outil du serveur en panne (`bulk_*` en erreur, `deck_analysis` qui expire, serveur
  déconnecté) → `scryfall_card_details`, outils séparés ou API Scryfall (outils.md).
- Joindre des cartes par leur nom dans un script → une carte absente des données doit faire échouer le
  script (dûm contre dum) (*Deux chemins attrapent ce que la relecture ne voit pas*).
- Suivre une recommandation EDHREC en tête de liste → la vérifier contre les cartes à ne jamais
  ajouter : The Gitrog Monster ferme un infini avec Dakmor Salvage.

## En proposant des échanges

- Couper une carte sur son effet → la classer sur sa fonction, et faire attaquer le critère lui-même
  par le contradicteur (*L'imblocabilité coupée parce qu'elle « n'ajoutait rien »*).
- Ajouter un effet qui modifie la caractéristique que le moteur compte → la recenser d'abord sur toute
  la liste (*Un anthem dans un deck qui compte les petites forces*).
- Couper sans relire chaque coupe contre les ajouts de la même passe et contre la défaite → refaire ce
  croisement (*Le deck pouvait se tuer lui-même, et quatre coupes sur huit étaient fausses*).
- Ajouter une source de mana sans vérifier sa couleur → Boros Signet ne produit pas de bleu.
- Proposer une refonte à qui veut des remplacements ciblés → remplacer les cartes qu'il désigne ; un
  problème hors périmètre se signale en une ligne.
- Reproposer une carte refusée ou interdite → la fiche les liste ; elles ne reviennent plus.
- Empiler de la protection pour une pièce fragile → chiffrer l'accès (six pièces : 54,9 % au T6),
  préférer une redondance du plan (*L'imblocabilité coupée parce qu'elle « n'ajoutait rien »*).
- Ajouter une carte sans regarder les quasi-combos → relire les cartes à ne jamais ajouter, et à chaque
  changement de bracket (*Un infini qu'aucun outil ne voit, et une cible de bracket qui bouge*).
- Couper ou glisser un combo en silence, ou bannir une carte isolée → signaler chaque combo complet,
  lettre et esprit du bracket ; le joueur décide (*Une liste noire écrite à la main, trop étroite puis
  trop large*).
- Présenter un désaccord avec une analyse précédente (d'un autre assistant IA compris) sans l'avoir
  vérifié → vérifier d'abord : deux « désaccords » présentés ainsi étaient des erreurs.
- Payer un compromis dont un seul côté est chiffré → chiffrer les deux ou s'abstenir (City of Brass :
  1,2 point de vissage contre 8,65 $ et une blessure par engagement).
- Acheter ou couper des terrains sans calcul → sources effectives, règle de mulligan, puits de mana
  (*La base était à la cible, et le meilleur levier était gratuit*).
- Auditer les couleurs sur les totaux de symboles → chaque carte à double ou triple symbole contre les
  sources de sa couleur (base-de-mana.md).
- Empiler les pertes de vie obligatoires sous un multiplicateur → au plus trois sources, et respecter le
  refus du joueur (« je perds trop de vie trop vite »).
- Recommander de l'évasion sans savoir comment la table défend → le demander (*Le gain attribué à
  l'évasion venait des jetons*).
- Optimiser pour un combo assemblé dans un quart des parties → lire cette probabilité comme un signal
  (*Cinquante parties réelles contre une probabilité d'assemblage*).
- Livrer un budget sur des prix incertains → donner la marge et l'ordre des coupes de repli.
- Proposer des changements sur une liste imprimée ou achetée → elle est gelée jusqu'à ce que le joueur
  relance.

## En concluant d'une mesure

- Mesurer une ressource au lieu de la victoire, ou simuler sans vérifier ses pièces → publier chaque
  pièce, commandant près de 100 % (*Optimiser une ressource au lieu de la condition de succès*).
- Présenter un paquet sans témoin → le mesurer contre des terrains de base (*Le correctif principal ne
  valait pas mieux que neuf Îles*).
- Attribuer un gain quand deux paramètres ont bougé ensemble, ou mesurer un nouveau plan avec l'ancien
  instrument → témoin à un seul mécanisme (*Le gain attribué à l'évasion venait des jetons*).
- Ajouter des copies d'un effet sans vérifier qu'il atteint la condition de succès → le vérifier avant
  (*La redondance ajoutée sur le mauvais axe*).
- Présenter un écart sous le bruit comme un gain → le dire « sans coût » ; seuil de bruit explicite,
  trois graines (mesure.md).
- Fonder une recommandation sur un seul chemin → deux chemins indépendants (*Deux chemins attrapent ce
  que la relecture ne voit pas*).
- Valider un test ou un réglage sans cas connu → y inclure un cas dont on connaît la réponse (mesure.md).
- Attribuer un échec à un défaut technique supposé → compter combien d'autres cas l'ont sans échouer.
- Transposer une mesure faite en duel à une table de quatre → non : un deck à 66,7 % en duel a fait 0 %
  à quatre.
- Appliquer une heuristique hors de son domaine → vérifier la question sur laquelle elle a été calibrée
  (*La base était à la cible, et le meilleur levier était gratuit*).
- Annoncer « aucune carte ne fait… » → le présenter comme le résultat d'une recherche datée.
- Consigner comme effet d'une passe la mesure d'une liste proposée → mesurer la liste appliquée.
- Laisser les probabilités l'emporter sur le jeu, ou taire qu'aucune partie n'a été jouée → le retour
  de parties réelles prime (*Cinquante parties réelles contre une probabilité d'assemblage*).

## En mettant à jour la fiche (format : fiche-de-deck.md)

- Écraser la liste sans entrée d'historique → entrée datée en tête : entrées, sorties, motif dans les
  mots du joueur, effet mesuré, réserves ; une annulation a aussi son entrée.
- Enregistrer la liste proposée → la liste réellement appliquée, refus et ajouts du joueur compris.
- Laisser dans la conversation ce qui guide le deck → table, façon de jouer, préférences propres au
  deck, retours de partie, recherches reportées : dans la fiche.
- Effacer une affirmation devenue fausse → la barrer, avec la date et la raison.
- Ne pas noter une lecture d'oracle délicate, un ordre de pile, une alerte d'outil vérifiée fausse →
  « Lectures d'oracle à ne pas re-dériver », « Pièges de pilotage », « Alertes d'outil vérifiées fausses ».
- Ne pas noter les quasi-combos, ou un combo gardé exprès → « Cartes à ne jamais ajouter », avec le
  combo fermé ; un combo assumé se note « à déclarer avant partie ».
- Livrer sans revérifier → total, terrains réels, légalité et date sous une seule liste actuelle ; coût
  réel à côté du prix annoncé ; ce que l'instrument ne voyait pas.
