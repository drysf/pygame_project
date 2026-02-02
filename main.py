"""
Jeu de tir top-down en Pygame
Contrôlez un soldat américain dans des salles remplies d'ennemis
"""
import pygame
import sys
from game import Game


def main():
    """Point d'entrée principal du jeu"""
    pygame.init()
    
    # Configuration de la fenêtre
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Top-Down Shooter")
    
    # Initialisation du jeu
    game = Game(screen)
    clock = pygame.time.Clock()
    
    # Boucle principale
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # Delta time en secondes
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            
            game.handle_event(event)
        
        # Mise à jour du jeu
        game.update(dt)
        
        # Rendu
        game.draw()
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
