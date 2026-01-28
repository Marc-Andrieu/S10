# Un projet chez Thales : UX Design, Cybersec, test logiciel

Objectifs du CM:

- présenter 3 métiers à trav un proj pr un client
- montrer vision concrète de chez Thales
- ...

Ex d'une solution : TIGRIS software, comme sys d'orchestration d'un labo de microbio.

L'agilité Scrum chez Thalès :

- on fixe du Time et des Resources
- on estime un Scope

Ce qui me paraît le + flagrant c qu'ils montre une équipe de 10... avec que 3 dévs !
Après on se dmde pk l'économie va mal.
Y a un UX Designer, un architecte, un cyber, un scrum master, un PO, un tech lead, un test lead, et les 3 pauv' dévs sont les esclaves tout en bas.

## 1. L'UX/UI Design

Ds l'indus, un design incompris ça peut vrmt faire tout basculer.
L'idée c davantage que l'user _comprenne_ plutôt que ce soit joli (ouais j'invente la phrase ms elle dit la mm).

Notion d'_eXpérience_, cmt l'end-user vit l'usage de notre app, ça va au-delà des mesures habituelles de l'utilité, là on ajoute une valeur émotionnelle.

Les grds vars dl'X c l'humain, le contxt, et sys

### Comment : le Design Thinking

Les 2 grdes étapes :

- **Exploration** : empathie (entretiens & observations des users) & définition (personae (archétype du user, c les "grands profils"), "UX Map" c un livrable ut pr rpz les émotions, attentes & obstacles du user à chaque étape)
- **Conception** : idéation (brainstorming...), maquette Figma !

Bref, c giga important de comprendre ton client.

Simplifie tes vues, pr qu'y ait que les données utiles de déjà affichées.

## 2. La cybersécurité

ANSSI : Agence nationale de la sécurité des systèmes d’information

- Acronyme DICT (Disponiblité Intégrité Confidentialité Traçabilité)
- People, Process,Technology

Nuisances quotidiennes, menaces cybercriminelles, menaces étatiques (les russes qui piratent la gestion des trains baltes)

OWASP Top 10 (top 10 des menaces sur une WebApp) : en gros SQLi, XSS, etc.

### Intégration de la sécu ds les projets

Objectifs :

- amélio la sécu ds les apps
- réduire les risques id
- réduire les coûts de traitements & assurer délais de MEP
- démontrer/certifier la confiance que le client a

Analyse statiques (du code source (non-compilé)) et dynamique (comportement du binary)

### La démarche pr le client : moyens organisationnels & humains

- Pré-market : intégration dla cyber ds le proj
    - analyse de risque : threat model (vraisemblances & impacts)
    - formation des dévs : secure coding guidelines
    - PenTest
    - dossier de sécu
- Post-market : maintien en condition de sécu (MCS)
    - veille & traitement des vuln
    - suivi de conformité

Moyens techniques

- Stack durcie
    - Identity & Access Management (IAM)
    - Gestionnaire de mdp
    - certificate control panel
    - audit trail pr gérer les logs
- Outils de gestion de code source sécurisé
    - Sonarkube...
- Gestion d'inventaire (sécu dla "Supply Chain")
    - BlackDuck : suivre la sécu des dépendances
- Outils de gestion des vuln : là le produit a déjà été livré

Clasico on fait tjs de la validation de schema ds le back, on se dit jms que ça a été bien traité par le client.

## 3. Le test logiciel

C l'ens des actis qui cherchent à veiller à ce que ça réponde aux "exigences spécifiées" (le CdC), aux exigences de qualité / sécu / performances etc, id les défauts/failles/erreurs.

Le coût d'un bug augmente avec le tps qu'on met à le découvrir : en élaborant l'archi, en codant, en lançant les tests, ou en prod

## Les 7 ppes du test logiciel

- Les tests montrent la présence de défaut : c pas une assurance d'absence de défauts
- Les tests exhaustifs n'existent pas
- Tester tôt
- Regroupement des défauts : 80% des pb viennent de 20% des cuases
- Le paradoxe du pesticide : + on passe un mm test, - il est susceptible de trouver des erreurs
- Tester selon le contxt : selon la logique métier, on teste pas la mm chose
- L'illusion d'absence d'erreur

Cqui est cool avec les tests, c qu'y a N trucs à tester : i18n, endurance, portabilité, accessibilité, maintenance, sécu, perf, conformité, fiabilité.
Ms tt ça c les tests _non-fn-els_ ; les tests fn-els c pr checker que ttes les fn du logiciel fonctionnent correctement, suivant un scenario ou des tests exploratoires.

Niveaux de tests (pyramide, y a N unit tests ms peu de tests d'acceptation) :

- tests d'acceptation : par un humain, on est ds la peau d'un user
- tests système :
- tests d'intégration : automatisables, testent plusieurs blocs
- tests unitaires / de composants : automatisés, testent 1 truc

Automatiser les tests ?

- automatisés
    - cool : rapide, répétable, efficace pr détec les régressions
    - pas cool : moins flexible, ...
- manuels
    - cool : + flexibles, aspect UX/UI (cmt l'humain a compris le front)
    - ...
