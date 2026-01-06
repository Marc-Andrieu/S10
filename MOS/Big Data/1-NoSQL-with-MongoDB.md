# NoSQL with MongoDB

## Généralités

Y a d'autres façons de structurer les données, avec des contraintes entre données.

Le NoSQL ça apparaît en 2009, qd le SQL relationnel classique a montré ses limites avec le web qui grandit.

NoSQL = Not Only SQL : ça _reste_ relationnel !

Y a 5 types de db NoSQL :

-   column
-   graph
-   document
-   clef-valeur
-   vectoriel

Un "document" ça a 3 sens :

-   cque l'auteur veut expr
-   le sens "propre" du doc
-   le sens compris par le consommateur

Structure logique et physique d'un doc :

-   struc logique : remerciements, intro, sections, concl, etc
-   struc physique : page web, papier, rendu pr tél

## Les lims du SQL

En distribuant sur plusieurs serv, ça devient chaud de `join`.
On relâche la consistence (le C du théorème CAP : on reste dispo et on partitionne bah oui c distribuwei)

Les quatre (cinq) V :

-   Volume
-   Variété & hétérogénéité
-   Vélocité (Vitesse)
-   Véracité
-   (Valeur)

Nouvel acronyme :

-   BASE : BAsically available Soft State Eventually consistent

ReDis c une grosse table de hachage, c en RAM

Neo4j c graph, exemple de requête :

```neo4j
MATCH (bob:User{username:'Bob'})-[:SENT]->(email)-[:CC]->(alias),
 (alias)-[:ALIAS_OF]->(bob)
RETURN email
```

Type document : ces SGBD manipulent des données semi-structurées

Cassandra

> Conseil : utilise des db relationnelles dès que c possible.
