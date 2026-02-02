"""
Bataille de Philadelphie - Révolution Américaine 1776
Jeu de plateforme 2D en Pygame

Point d'entrée principal du jeu.
"""
import pygame
from game import Game


def main():
    """Lance le jeu."""
    pygame.init()
    pygame.mixer.init()
    
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
