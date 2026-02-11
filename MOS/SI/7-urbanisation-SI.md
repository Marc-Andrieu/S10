# L'urbanisation du SI

## De la métaphore de la ville au mgt des SI

C une transformation.
On se base évidemment sur la strat existante de l'ep, du SI existant : on ft pas table rase du passé.

> Urbaniser, c simplifier.

C de l'architecture, c du high-level.
Les personnes dirigeantes changent bcp, l'archi du sys change peu.

Le Si est constitué de **blocs fn-els** : ils échangent entre eux, et un bon découpage _minimise_ les échanges d'infos entre blocs, & chacun doit fournir une interface standard pr permettre l'échange d'info avec lui.

Vues :

- processus
- fn
- applications

## Enjeux de l'urbanisme

L'urbanisme construit la vision globale, c fondé sur anticiper les évolutions de l'ep.
Les directeurs de département savent généralement mm pas cque font leurs employés, mm si ça paraîtrait être la base.

Une transformation, ça fait évoluer "sans rupture", d'un existant ("_as is_") vers une cible ("_to be_").

## Le processus d'urbanisation

C l'ens des actis liées à l'urbanisme du SI :

- poser des cadres & règles sur cmt le SI peut évoluer
- etc

### Etape 1 : définir le périmètre.

3 nivs de préoccupation :

- vision métier : strat, processus métiers, actis dl'ep
- vision fn-elle : fn qui constituent les actis; l'urbaniste les coupe en zones, ...
- vision technologique : ...

Autre rpzation : modèle en couches :

- Vision métier
- Vision fn-elle
- Vision applicative
- Vision technique

Autre rpzation : ... (pas important)

### Composantes du processus d'urbanisation

Cartographies

- métier
- fn-elle
- applicative

## Strat dl'ep

Approche top-down :

- mission dl'ep (sa raison d'être)
- vision dl'ep (objectifs high-level)
- strat dl'ep
- processus métier
- strat du SI
- sys informatique

**Diagramme d'Ishikawa** (enfin)

- décrit les objectifs à atteindre
- c pas la règle des 5M, osef ici, cqui compte c la rpzation graphique sous forme graphique :
    - objectif ppal
    - objectifs 2ndaires pr atteindre l'objectif ppal
    - sous-objectifs pr réaliser chaque objectif 2ndaire

Ex :

- être le n°1 du service informatique
    - opérer comme 1 seule ep
        - amélio la colab w/ filiales
            - présence unique
    - soutenir l'img
        - effort pub ++
        - maintenir les standards qualité
    - proposer tt type de services
        - investir ds des produits
        - dév le pôle conseil
        - ...
    - réduire les coûts de prod
        - délocaliser
        - ...
    - opérer mondialement
        - investir en Chine
        - ...

La strat du SI est définie avc :

- coûts
- qualité de service
- strat dl'ep

## Modèle de réf de l'urbaniste

### Carte des processus

Après une série d'interviews de différents acteurs de l'entreprise ds divers départements & services

**Pr réaliser l'urbanisation du SI, faut que l'ep définisse elle-mm précisément ses processus**, c un travail considérable qui doit déjà être fait à l'avance.

...

### Carte fn-elle

**Décrit les fn du SI**

- zones : bonnes pratiques
- quartiers : groupements d'ilôts : regroupent des composants hmgn ds le type d'info traitée
- îlots : entité remplaçable du SI, c une finalité fn-elle

Qlq règles :

- unicité des blocs (une îlot appartient à pile 1 quartier, qui appartient à pile 1 zone)
- async des îlots : peut traiter immédiatement un autre event

Zone d'échange : acquisition & restitution

### Carte applicative

### Carte physique

## L'indice d'urbanisation
