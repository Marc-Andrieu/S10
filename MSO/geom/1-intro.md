# Mesh and Computational Geometry

-   Pb géom & applications
    -   computer graphics
        -   collision detection
        -   illumination detection
        -   hidden parts not taken into account
    -   robotics & 3D vision
        -   trajectory planning
    -   telecom
        -   determination of the nearest relay
    -   chemistry
        -   molecular modelling
        -   pocket detection
        -   calculation of contact surfaces
    -   CAD/CAM (Computer-Aided Design/Manufacturing)
        -   Integrated circuit design
        -   reverse engineering
    -   scientific computation : physics, geology
    -   digital twins (jumeaux numériques)
    -   museums & virtual shops
    -   geoographic information systems
    -   virtual creation
    -   digital creation

Géométrie discrète : bah oui en info tout est discret, donc faut se démerder pr traiter les objets géométriques avec des structures discrètes.

On construit des classes Pt, Segm, Triangle, Polygon, Sphere etc, qui sont des combinatoires : un Segm a deux Pts comme attr, etc.
Et faut des méthodes cohérentes vis-à-vis de la géom : l'intersection de deux Segm c un Pt | null, etc.

Faut définit un type Rationnel ds le syst de typage.

Concept de combinaison affine :

$$
\begin{align*}
p &= \sum_i \lambda_i \vec x_i & \sum_i \lambda_i &= 1 & \lambda_i &\in \mathbb{R}
\end{align*}
$$

Ds le cas, $p \in Vec(x_1; \dots; x_n)$, et les $\lambda_i$ s'appellent les coordonnées barycentriques, qui sont uniques ssi les $\vec x_i$ sont indépendants.
Si on ajoute que $\lambda_i \in \mathbb{R}_+$, alors ça s'appelle une combinaison convexe.

Un $n$-simplexe c l'enveloppe convexe de $n + 1$ pts indépendants : en partant de 0, c le pt, le segm, le triangle, le tétraèdre, etc.

Pr un segm, les coor barycentriques c des rapports de longueurs, pr un triangle, les coor barycentriques c des rapports d'aires, etc.

Le volume d'un $n$-simplexe c comme je l'avais prophétisé en MPSI : $$\dfrac{1}{n!} |det(x_1 - x_0; x_2 - x_0; \dots; x_n - x_0)|$$

Les 0-faces, 1-faces, 2-faces, etc, ce sont des sous-simplexes formés à partir d'un sous-ens de pts.

Triangulation :
Soit $E \subset \mathbb{R}^k$, on appelle _triangulation_ de $E$ un ens de $k$-simplexes tq leurs sommets soient les pts de $E$ & vérifient :

-   Les intersections de deux $k$-simplexes est soit vide soit une face commune aux deux $k$-simplexes;
-   les $k$-simplexes... (c convexe en gros, ça pave toute l'enveloppe convexe de $E$)

Oh yes la formule d'Euler : $c - e + v = 1 - h$ où c les nbrs de cells (faces), edges (arêtes), vertices (sommets), et holes (trous).
(Un bail de caractéristique, c un profond théorème de Gauss et Euler, qui relie une propriété topologique (et même homologique) à une propriété purement géométrique : $c - e + s = 2 (1 - g)$ où $g$ c le genre (_genus_) de la surface, qui vaut $0$ si y a pas de trous (en gros), ms toute façon c trop avancé pour les centraliens communs)

Si on a $k$ arêtes sur le bord d'une triangulation, on a $2e = 3c + k$ : en orientant ds le mm sens chaque petit triangle.

Corollaires :

-   $c = 2(v - 1) - k$
-   $e = 3(v - 1) - k$

Structure de données : depuis chaque structure on peut descendre (c l'idée).
Ex: on a une instance de triangle, le n°505, on get un de ses sommets, le n°100 (le n°2 localement au triangle 505).

Eh oui, chaque sommet a un indice global et un indice relatif à chaque face à laquelle il appartient.

Struct de données :

-   info géom
-   info topologique (ds un Triangle on met les n° des pts, ie. les pointeurs, on n'y copie pas les valeurs, c teubé c dla redondance et le "maillage bouge", les coor des pts bougent ms pas quel pt est tricoté à quels triangles)

Les arêtes sont orientées ici, et on les appelle des $\tfrac{1}{2}$-arêtes (_half-edges_).

---

Le C++ ut bcp la pile (heap), qui est une liste LIFO, là où le Java se sert quasi-exclusivement de la stack.

Avec :

```cpp
LaClasse *p = new LaClasse();
```

Le pointeur `p` est ajouté à la heap, et il pointe à `p` sur la stack.

Pr libérer :

```
delete p;
```

Ds la heap, la durée de vie est liée au bloc.
Ds la stack, elle est liée l'existence d'un pointeur de la heap qui lui pointe dessus.

Le constructeur ne construit pas, il initialise (instancie).
