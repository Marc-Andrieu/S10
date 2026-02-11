# MFA

## Concl

- c bien
- faut imposer l'authentification forte aux profils qui ont accès à des données perso en masse
- optionnel pr le reste
- techniquement facile...
- ... ms faire très attention à l'UX

ECL 2007, dév web, bcp de PHP, Python, SQL, HTML+CSS+JS.

- Identification (tqt jsuis untel) -> Authentification (jsuis untel, voici la preuve)
    - 3 facteurs d'authentification
        - facteur de connaissance : je connais telle info
        - facteur inhérent : qqch que je suis (empreinte, biométrie)
        - facteur de possession : clefs

RGPD : 1 article = 1 phrase, donc elle peut être giga longue

Risque = proba que ça se passe $\times$ à quel point c grave si ça se passe.

Les usurpations viennent de défauts d'authentification : faut vrmt faire super attention pr tous les profils "admins" (qui ont accès aux données des gens) : compta, presta de livraison, stagiaires, etc : donc faut de l'authentification forte pr eux

Crypto sym/asym

TOTP : time-based OTP (One-Time passwd), RFC 6238.
C symétrique, ms sa force c d'être éphémère.

RFC : Request For Comments.

En crypto, on fait pas les choses à la mano : on utilise des libs open-source, battle-tested, on utilise la fn de hashage incluse ds le framework.

> Une bonne interface, c qqch qui va vite, qui est cohérent.

Ecrire des tests bêtes.
Oui.
Pr éviter les bugs bêtes.

Accessibilité : c la base.
MDN.
