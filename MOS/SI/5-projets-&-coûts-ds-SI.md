# Projets et coûts ds le SI

## Les coûts du SI

Paradoxe : le SI coûte trop cher alors que le hardware et logiciel sont incroyablement bon marché, comparé à leur vraie valeur, encore + qd les orids sont achetés en série (en gros et pas en détail).

### Dimensionnement du SI

Valeur du SI

- incrémentale : modif par un projet
- globale : ens du SI
- financière : contrôle de gestion dl'ep
- immatérielle : contribue à la valeur de marché dl'ep
    - "goodwill" : capital humain, img dl'ep, satis des clients.

### Mesurer le parc applicatif

2 types de mesures : progiciel & apps.

On regarde en "homme-jour" (sympa comme unité), ou en coût si acheté.

### Mesurer le parc matériel

- Serv', réseaux, routeurs, etc
- Parc matériel
    - machines de prod
    - machines de test & pré-prod
    - machines de secours : DRP (Distater Recovery Plan) / PRA (Plan de Reprise d'Acti)
    - Composante de gestion des stocks & install'

2 types de métriques : TPM (transactions par minutes) et TPC (Transaction ...)

### Fiabilté

QoS (Qualité de Service)

- but : garantir les perfs. C un concept de gestion lié aux ressources d'un process/réseau
- Liée aux protocoles mis en oeuvre

Y a :

- Disponibilité : $\text{dispo} = \dfrac{\text{}}{\text{}}$
    - Les "trois neufs" : 99,9% de dispo, ie. 8h/an d'indispo
    - Les "quatre neufs" : 99,99% de dispo, ie. 52mn/an d'indispo
    - Les "cinq neufs" : 99,999% de dispo, ie. 5mn/an d'indispo
- Fiabilité : $\text{MTBSI} = \dfrac{\text{tps dispo}}{\text{\#coupures}}$ et $\text{MTBF} = \dfrac{\text{tps total dispo - }}{\text{}}$
- Maintenabilité :
    - anticiper/détec/diagn/réparer la panne
    - récup les données & le sys. Mettre ses disques en RAID
    - rétablir le sys
- Résilience

Durée de vie : ça se ressemble en logiciel & matériel.
Jeunesse -> période stable -> usure

Cycle de vie d'une app pdt sa MEP :

- exploitation : faire que l'app marche sur les serv'
- maintenance technique & corrective : fix les bugs & maintenir le match entre l'app et sont env logiciel (OS, libs)
- maintenance évolutive fn-elle : features dmdées par les "clients" ie. les directions métier

Durée de vie réelle != durée de vie perçue : le dév de l'app est perçu ms hors de l'exploitation, ms les migrations, les dévs suivants, le nettoyage, la version suivante, c ds la vie réelle ms pas perçu.

Coûts récurrents du lifecycle en prod : 25% du projet de dév applicatif

- exploitation : 15%
- maintenance (techn, corrective, évolutive) : 10%

### Evolutions ds le SI

### Socle des dépenses informatiques

- OPEX : _operiational expenses_
    - le "socle" : dépenses _sine qua none_ pr que le parc applicatif marche
- CAPEX : _capital expenses_

## Sélection d'un projet SI

### Construre un SI rentable

### Entonnoir de sélection des projets

Dmde -> étude d'avant-projet -> Projet d'étude (MOA) -> Projet réalisation (MOE) -> Mise en service

Sélection des projets infos :

- Si on est trop sélecte :
    - non-réalisation : "ce projet est useless", "y a + urgent"
    - non-concrétisation : "c pas techniquement faisable pr nous", "trop cher"
- Laisser un peu de marge

Les études :

- Etude d'avant-projet : 2 étapes
    - Etude d'opportunité
    - Etude de rentabilité/faisabilité
- Projet d'étude : 2 étapes
    - Etude détaillée
    - Etude technique

### Classif des projets

#### 1 - Projets obligatories

Dû à différentes contraintes

#### 2 - Projets stratégiques

- Doivent pas être externalisés car trop sensibles
- Peuvent être exemptés de l'étude de rentabilité

#### 3 - Applis opérationnelles

Gros débit d'infos, gros poids ds le budg' du SI

#### 4 - Applis métiers & infras

Projets les + courants, étude de rentabilité indispensable.

### Rentabilité d'un projet

La renta du projet s'évalue **EN COMPARANT DES SITUATIONS POSSIBLES FUTURES**

#### 1 - Définir les alternatives possibles

Proposer pleins de scenarii simples de l'évol dl'acti

#### 2 - Identifier les populatiions concernées

Clients, users, fournisseurs (providers), compta, etc

#### 3 - Définir & argumenter les hyp

Etude objective, hyp explicitées et hyp de calcul justifiées par une collecte d'infos & de chiffres

#### 4 - Raisonner ds le tps, éval

- Le lifetime initial dl'appli, ie. sans refonte
- Le lifetime du projet

#### 5 - Eval les risques

Retards, coûts, technologiques (liés à la stack technique), au projet (les users adoptent pas la solution)

#### 6 - Calc ts les coûts

Investissements, dépenses récurrentes & non-récurrentes

#### 7 - Estimer les gains (marges d'incertitude)

Sur les processus (charge de trav réduite), coûts (achat, prod) et valeur dl'ep

#### 8 - Calc la renta

Pay-back, ROI, VAN (valeur actuelle nette) > 0 si le projet est rentable

#### 9 - Opti la renta

**Prévoir de faire en 1er les parties du projet qui génèrent le + de gains**

#### 10 - Eval la sensibilité dla renta aux hyp

#### 11 - Get la décision

#### 12 - Mesurer la renta effective
