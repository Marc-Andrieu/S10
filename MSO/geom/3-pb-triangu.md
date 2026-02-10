# _Problem of triangulating a surface passing through points_

T'as un nuage de pts 2D, cmt tu triangules (il faut recouvrir l'envelope convexe) ?

_Connect the ponts together avoiding crossings to produce non-overlapping triangles_

## Cmt on sait si on pt est à l'extérieur de l'enveloppe convexe ?

Soit $P$ le nouveau pt, $A$ et $B$ deux pts sur le bord ds le sens trigo.

On regarde si $(\overrightarrow{PB} \times \overrightarrow{PA}) \cdot \vec n > 0$.

## Cmt on sait si un pt est ds un triangle ?

$P$ est ds ABC nommés ds le sens trigo si PAB, PBC et PCA sont aussi nommés ds le sens trigo.

## Qualité

### Qualité d'un triangle

- \+ un triangle est équilatéral, + c un "bon" triangle
- aspect ratio d'un triangle
    - rayon du cercle inscrit / rayon du cercle circonscrit
    - sinus du + petit angle

### Qualité d'une triangulation

On cherche le + petit angle d'une triangulation.

### Triangulation de Delaunay

Il faut que les cercles circonscrits à chacun des triangles soient "vides", ie. d'un ait aucun pt ds le disque ouvert.

Elle existe tjs, c un théorème, et c non trivial.

Ca se montre assez simplement pr 4 pts en connaissant le théorème de l'angle inscrit et en ajoutant que si on rentre l'angle ds le cercle il s'agrandit, si on l'en sort il rétrécit.

Etre localement de Delaunay, pr une arête, c si les triangles inscrits aux deux triangles ayant cette arête ne contiennet pas le 3e pt de l'autre triangle.

Fun fact : une triangulation est de Delaunay ssi toutes les arêtes sont de Delaunay : ça permet de vérifier une triangulation en $O(n)$ en checkant chaque arête en $O(1)$.

La triangulation de Delaunay est "pas" unique, ms presque (en gros).

## Algo de Lawson

On "flip" localement des arêtes de Delaunay.

## En 1D

$z = f(x; y) = x^2 + y^2$ : on "monte" les pts 2D ds la 3D.

Qd on "monte" un cercle, le résultat appartient à un plan.
