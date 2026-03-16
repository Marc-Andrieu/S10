# Identification & connexion

## 1. Introduction

Y a des objets connectés en permanence, d'autres par intermittance, etc.

## 2. Indentification des objets

Niveaux d'identification possibles : non-identifié, identifiant non-unique (e.g. code-barre de produit), identifiant unique (e.g. N° de série).

Exemples :

- noms : URI, URN
- n° : GTIN, adresse MAC, adresse IP
- coordonnées géographiques pr des objets ficxes
- tatouages
- codes à barres

### Codes à barres

- à 1 dim
    - [0-9]+
        - EAN-13 : 13 chiffres, etc
    - chiffres, lettres, symboles
        - Code_39, etc
- à 2 dims
    - data matrix
    - QR Code (Quick Response)

Un organisme, le GSA, normalise tous les GTIN (Global Trade Item Number).

### RFID

Par radio-fréq

- Tag passif : alimentation & lecture/écriture du tag par champ magnétique
- Tag actif : batterie interne

Différents types :

- basique : un UID (unique ID) non-modifiable
- mémoire en read only, ou pas
- cartes à puce sans contact (CB, etc)

On peut faire plusieurs reads qui semblent simultanés (en ft le tag répond avec un délai random donc en vrai c plusieurs lectures successives).

Principales fréquences, portée & usages

- 125 kHZ (10 cm) : logistique, animaux
- ...

### EPC (Electronic Product Code)

## 3. Réseaux filaires

### Ethernet & PoE (Power over Ethernet)

## 4. Réseaux sans-fils

Comparaison des réseaux sans fils : selon débit et distance, ça va du RFID (petit débit, petite distance) à la 5G

### Réseaux PAN (Personal Area Network)

Y a mm le LiFi (lumière) qui arrive (enfin ça des des années qu'on dit que ça arrive)

### Transmission raido longue distance

LoRa : on est "sous le niveau de bruit thermique", on envoie 4096 bits pr en envoyer 8, et on espère qu'avec toute cette redondance on arrivera à reconstruire les 8 voulus

### Réseaux

## 5. IEEE 802.15.4

## 6. ZigBee

## 7. 6LoWPAN

Si on met les en-têtes TCP + IP + réseau, ça met monter à 60 octets, sur 70 octets ds un paquet, donc 10 octets de données seulement : c pas ouf.

Pas un routage IP classique, ça chiffre et compresse la totale des en-têtes

C bien pr des apps locales

## 8. Autres réseaux
