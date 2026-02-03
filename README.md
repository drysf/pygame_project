# Philadelphia Liberty

Un jeu de tir vu du dessus où vous contrôlez un soldat américain tentant de vaincre les soldats anglais.

A vous de sauvez l'indépendance américaine !

## Fonctionnalités

- **Contrôle du joueur** : Déplacement avec WASD ou les flèches directionnelles
- **Visée à la souris** : Le personnage se tourne automatiquement vers le curseur
- **Système de tir** : Clic gauche pour tirer dans la direction de la souris
- **IA des ennemis** : Les ennemis détectent et attaquent le joueur
- **Système de collision** : Murs et obstacles dans les salles
- **Système de santé** : Interface affichant la santé et le nombre d'ennemis
- **Conditions de victoire/défaite** : Éliminez tous les ennemis pour gagner

## Installation

1. Assurez-vous d'avoir Python 3.7+ installé
2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Lancement du jeu

```bash
python main.py
```

## Contrôles

- **WASD** ou **Flèches directionnelles** : Déplacement
- **Souris** : Visée
- **Clic gauche** : Tir
- **R** : Recommencer (après game over ou victoire)
- **ESC** : Quitter

## Architecture du code

Le projet utilise une architecture orientée objet avec les bonnes pratiques :

- `main.py` : Point d'entrée et boucle de jeu principale
- `game.py` : Gestionnaire principal du jeu
- `player.py` : Classe du joueur avec contrôles et tir
- `enemy.py` : Classe des ennemis avec IA
- `bullet.py` : Classe des projectiles
- `room.py` : Classe de la salle avec génération de murs

## Bonnes pratiques implémentées

- **Séparation des responsabilités** : Chaque classe a une responsabilité unique
- **Delta time** : Mouvement indépendant du framerate
- **Groupes de sprites** : Gestion optimisée des collisions
- **Commentaires et docstrings** : Code bien documenté
- **Constantes configurables** : Facile à modifier les paramètres du jeu
