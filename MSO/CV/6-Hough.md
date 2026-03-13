# Hough transform

Bon :

- le cours s'appelle pareil que l'électif "Capteurs et traitement d'images"
- c le mm prof
- c les mm slides

Donc : https://github.com/Marc-Andrieu/S8/tree/main/Img_Processing#hough-transform

$$\rho = x \cos \theta + y \sin \theta$$

```
Pr chaque (x, y):
    Pr chaque theta:
        Case[ x*cos(theta) + y*sin(theta) ] += 1
```

Amélio possible : on pose :

$$\theta = gradient(x; y) = \arctan \left( \dfrac{\dfrac{\partial I}{\partial y}}{\dfrac{\partial I}{\partial y}} \right)$$

On obtient les gradients suivant $x$ à un pt en convoluant avec :

$$
\begin{bmatrix}
-1 & 0 & 1 \\
-1 & 0 & 1 \\
-1 & 0 & 1 \\
\end{bmatrix}
$$

Et suivant $y$ à un pt en convoluant avec :

$$
\begin{bmatrix}
1 & 1 & 1 \\
0 & 0 & 0 \\
-1 & -1 & -1 \\
\end{bmatrix}
$$

Equation du cercle pr un rayon connu :

$$(x_i - a)^2 + (y_i - b)^2 = r^2$$

Fast connective Hough transform : euh c vraiment pas clair...

Generalized Hough Transform :

- pr une forme dont y a pas d'équation simple
- un pose un centre à cette forme arbitrairement, pr chaque pt du contour, on note sa distance $r$ au centre et son angle $\varphi$ du contour (ouais on suppose une forme de dérivabilité du contour ms le prof l'a pas dit explicitement).
