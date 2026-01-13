# Pixels and Image filter

La plupart des infos sont véhiculées ds les niveaux de gris, ds la luminance, **pas** ds la chrominance.

La convol de deux filtres gaussiens est un filtre gaussien.

Si le filtre est séparable, ie. que son kernel se factorise en vec col $\times$ vec ligne, alors on peut convoluer sur seulement les lignes puis seulement les colonnes.
