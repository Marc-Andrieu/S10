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
