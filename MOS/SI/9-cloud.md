# L'informatique dans les "nuages" (_cloud computing_)

## Modèles de services

Permet l'accès à des ressources **mutualisées & configurables** qui nécessitent un travail minimal de gestion (au sens sysadmin).

$\approx 10^{12} \$$ de marché en 2026.

Croissance de près de 20%/an depuis 2015, accélération ces dernières années due l'IA.

- Iaas (Infrastructure) : utilisé que par les ingés réseaux/devOps
    - PaaS (Platform) : ...
        - SaaS (Software) : utilisable par tout le monde

## SaaS (Software aaS) : 40% de parts de marché

Le provider Cloud se charge de littéralement tout : apps, runtime, db, logiciels sur le serv, virtualisation, matos, stockage, réseau...

### PaaS (Platform aaS) : 25% de parts de marché

L'entreprise cliente maintient juste les apps, et ut un framework qui a un support cloud, ms le provider fait qd mm quasi tout : provisionnement des servs, scalabilité automatique, sécu, déploiement, monitoring & logs, etc.

Etapes techniques : le dév push sur le repo, la plateforme crée un "env d'exéc" (_runtime_), installe les déps, [build une image] et déploie un container (Docker), un orchestrateur (K8s) distribue la charge, up ou down + d'instances, la plateforme connecte la db, les APIs etc.

#### IaaS (Infrastructure aaS) : 35% de parts de marché

L'entreprise cliente fournit bcp de choses, et le fournisseur ne fournit que le matos, la virtualisation, le stockage et le résaeu

Outils de virtualisation :

- VMWare
- Hyper-V (MS),
- Citrix
- KVM (Kernel-Based VM, intégré au kernel Linux)
- Xen
- Red Hat virtualisation (basé sur KVM)

Container $\neq$ hyperviseur (logique)

## Principaux acteurs

Que des américains et des chinois.

- AWS
- Azure
- Google Cloud
- Oracle Cloud
- IBM Cloud
- Alibaba Cloud
- Tencent Cloud

Ils font tous : hyperscaler, SaaS, PaaS, IaaS

Acteurs Fr :

- Dassault Systèmes : visu 3D
- Cegid : compta & RH
- Sendinblue : marketing
- ...

Les projets Fr souverains (Numergy, Cloudwatt) ont complètement disparus...

- SaaS : achat d'une licence, on peut ut le service sans avoir à l'installer.
  Ms giga dépendance, moins de personnalisation.

## Modèles de déploiement

Cloud public :

- accès par internet
- géré par un tiers (le fournisseur)
- infra mutualisées et partagées
- prix "réduit"

Cloud privé :

- hébergement : chez soi, ou chez un provider ms via VPN
- contrôle total sur ses données
- sécu : on le brasse soi-mm
- ...

## Remarques générales

Avantages :

- \+ d'agilité (intégration, updates, maintenance, déploiement)
- \- d'actis de déploiement et d'exploitation applicative
- disponbilité 99,9...%
- support de pics de charge
- pas d'install'
- scalabilité
- Payer que ce dont on a besoin

Inconvénient :

- qualité de service : réseau bcp + sollicité
- intégration : pouvoir la gérer avec l'existant
- sécu à tous les nivs
- santé des providers : le marché est jeune...
- intégrité : eh oui, faut faire confiance aux providers qu'ils vont pas faire n'importe quoi avec nos données (les perdre, supprimer, modifier, exfiltrer, etc)

## Les services web

Avantages : interop entre applis htrgènes
..
