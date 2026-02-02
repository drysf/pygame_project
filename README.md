# Bataille de Philadelphie - Révolution Américaine 1776

Jeu de plateforme 2D développé en Python avec Pygame.

## Description

Incarnez un soldat américain pendant la Révolution Américaine et affrontez les soldats britanniques dans les rues de Philadelphie. Progressez à travers 5 niveaux avec une difficulté croissante et des ennemis variés.

## Fonctionnalités

- **5 niveaux** avec difficulté progressive
- **5 types d'ennemis** britanniques avec apparences et statistiques uniques :
  - Regular (2 PV)
  - Elite (3 PV)
  - Officer (4 PV)
  - Commander (6 PV)
  - Tank (8 PV)
- **3 skins** pour le joueur (soldat, général, minuteman)
- **Power-ups** : cadence de tir, santé, vitesse
- **Système de vie** à 4 cœurs
- **Sons synthétiques** générés dynamiquement
- **Génération procédurale** des niveaux
- **Défilement de caméra** fluide

## Structure du Projet

```
pygame-prj/
├── main_new.py          # Point d'entrée du jeu
├── config/              # Configuration
│   ├── __init__.py
│   └── settings.py      # Constantes et paramètres
├── managers/            # Gestionnaires
│   ├── __init__.py
│   ├── camera.py        # Gestion de la caméra
│   └── sound_manager.py # Gestion des sons
├── entities/            # Entités du jeu
│   ├── __init__.py
│   ├── player.py        # Joueur
│   ├── enemy.py         # Ennemis
│   ├── bullet.py        # Projectiles
│   ├── platform.py      # Plateformes
│   ├── building.py      # Bâtiments (décor)
│   └── powerup.py       # Power-ups
└── game/                # Logique principale
    ├── __init__.py
    └── game.py          # Classe Game principale
```

## Architecture

Le projet suit les principes de **programmation orientée objet** :

- **Séparation des responsabilités** : Chaque classe a un rôle unique
- **Une classe par fichier** : Meilleure lisibilité et maintenabilité
- **Modules logiques** : Organisation par fonctionnalité
- **Pattern Manager** : SoundManager, Camera pour centraliser les comportements
- **Sprites Pygame** : Utilisation du système de sprites pour les entités

## Installation

### Prérequis

- Python 3.7+
- Pygame

### Installation

```bash
# Cloner le projet
cd pygame-prj

# Créer un environnement virtuel (recommandé)
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Installer les dépendances
pip install pygame
```

## Utilisation

```bash
python main_new.py
```

## Contrôles

- **Flèches directionnelles / Q, D** : Se déplacer
- **Espace** : Sauter
- **C** : Changer de skin
- **ESC** : Pause / Menu
- **Tir automatique** : Le joueur tire continuellement

## Système de Points

- Regular : 100 points
- Elite : 250 points
- Officer : 400 points
- Commander : 600 points
- Tank : 800 points
- Power-up collecté : 50 points
- Niveau terminé : 500 × numéro du niveau

## Développement

### Ajouter un nouveau type d'ennemi

1. Dans [entities/enemy.py](entities/enemy.py), ajouter la configuration dans `ENEMY_TYPES`
2. Créer une méthode `_draw_<type>()` pour l'apparence
3. Ajouter le type dans la logique de génération de [game/game.py](game/game.py)

### Modifier les paramètres du jeu

Tous les paramètres sont centralisés dans [config/settings.py](config/settings.py)

## Auteurs

Projet PyGame - Groupe 9

## Licence

Projet éducatif
