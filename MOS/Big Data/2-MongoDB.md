# MongoDB

En C++, manipule des _documents_
Un shard c bien une replica.
Y a une notion de server, avec un deamon `mongod`

Chaque doc à un `_id`, cette colonne est obligatoire.

Un doc c un arbre, avec des clefs et valeurs, bon en gros c du JSON/YAML quoi.

Y a pas de validation du schema.

Chaque requête commence avec ``db.NomDeLaCollection`.

Ppe de client-serveur (comme Postgres avec psql)

Pas + de 16 Mo par document, pas + de 100 niveaux [d'imbrication].

Ca reste relationnel.

Composants de MongoDB

-   `mongod` c le serv
