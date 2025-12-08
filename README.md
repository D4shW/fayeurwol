# Nom du Projet : FAYEURWOL (Fire-Wall)

## Note : Ce projet est une simulation à des fins éducatives/de test. Il ne s'agit pas d'un véritable outil de sécurité réseau et ne doit pas être utilisé pour protéger des systèmes de production réels.

### Description :
Fayeurwol est un simulateur de pare-feu basé sur des règles, écrit entièrement en Python. Il permet de modéliser le trafic réseau entrant et sortant et de tester différentes configurations de filtrage de paquets sans avoir besoin d'une infrastructure réseau physique.

L'objectif principal de ce projet est de :

- 

- 

- 

...

### Fonctionnalités Clés :
Simulation de Trafic : Génération de paquets factices (IP, TCP, UDP).

Moteur de Règles : Supporte les règles de type ALLOW, DENY, et LOG.

Journalisation (Logging) : [Décrire comment les logs sont gérés, ex. fichier JSON ou console].

...

### Architecture (Optionnel) :
[Insérer ici un schéma simple ou une explication textuelle de l'architecture]

PacketGenerator : Crée des instances de paquets.

RuleEngine : Compare les paquets aux règles définies.

FirewallCore : Orchestre le flux de données.

### Structure du Projet :
```
firewall_project/
│
├── main.py                  # Point d'entrée (Simulation)
├── README.md
│
└── src/
    ├── __init__.py
    ├── domain.py            # Contient la classe Packet
    ├── interfaces.py        # Contient la classe abstraite Rule
    ├── core.py              # Contient Firewall (Singleton) et TerminalRule
    ├── decorators.py        # Contient RuleDecorator et ses implémentations (Logger, Ban...)
    └── configurator.py      # Contient FirewallConfigurator
```

### Installation :
Cloner le dépôt : 

'''Bash

git clone https://github.com/votre-username/nom-du-projet.git

cd fayeurwol'''

### Installer les dépendances (si nécessaire) :

'''Bash

pip install -r requirements.txt'''

### Utilisation :
Lancement basique
Pour lancer le simulateur avec la configuration par défaut :

'''Bash

python main.py --config rules.json'''

### Configuration des règles (rules.json) :
Le pare-feu utilise un fichier JSON pour définir les règles de filtrage. Voici la structure attendue :

JSON

[
  {
    "id": 1,
    "action": "ALLOW",
    "protocol": "TCP",
    "source_ip": "192.168.1.10",
    "destination_port": 80
  },
  {
    "id": 2,
    "action": "DENY",
    "protocol": "ANY",
    "source_ip": "10.0.0.5",
    "description": "Bloquer l'hôte suspect"
  }
]

### Tests :
Pour exécuter la suite de tests unitaires :

'''Bash

python -m unittest discover tests/'''

### Roadmap / À faire :
[x] Moteur de filtrage basique (IP/Port)

[ ] Support du protocole ICMP

[ ] Interface graphique (GUI) pour visualiser les paquets bloqués

[ ] [Autre fonctionnalité future]

### Licence :
Distribué sous la licence MIT. Voir LICENSE pour plus d'informations.

### Contact :
Votre Nom - email@exemple.com

Lien du projet : https://github.com/votre-username/nom-du-projet