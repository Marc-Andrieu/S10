Pour la 3e fois depuis le début des vacances de Noël, la DSI a pété le CAS.
On est le 20 janvier, ça fait 1 mois.

Donc jsp si la 2e partie du titre c classification ou detection.

La distillation d'un gros modèle teacher, c entraîner un 2e modèle student bcp + petit, où l'apprentissage du student se fait en se confrontant au teacher.

$\mathcal{L}_{global} = (1 - \lambda) \mathcal{L}_{CE} (\psi(Z_s); y) + \lambda \tau^2 KL(\psi(Z_s / \tau); \psi(Z_t / \tau))$

Knowledge distillation

$y_i(\vec x|t) = \dfrac{e^\dfrac{z_i(\vec x)}{t}}{\sum_j e^\dfrac{z_j(\vec x)}{t}}$

Temperature

$y_i = \dfrac{exp(x_i/T)}{\sum_j exp(x_j/T)}$

## Segmentation

Fully Convolutional NN

**Downsampling puis upsampling**

Input $3 \times W \times H$ c haute résolution, on enchaîne les poolings et strided convolution, puis on upsample.

### Classification + Localization

Le R-CNN a une astuce qui divise par 10 le tps d'inférence.

Y a des Region Proposal Networks.

DETR : End-to-End Object Detection with Transformers

J'ai beau écouter, je comprends vrmt pas grd-chose...
