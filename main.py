"""
Philladelphia Liberty
Incarnez un soldat de la révolution américaine et combattez les anglais pour déclarer l'indépendance des Etats-Unis !
"""
import pygame
import sys
from game import Game
from pause import Pause
from state_manager import StateManager


def main():
    """Configuration principale du jeu"""
    pygame.init()
    
    # Configuration de la fenêtre
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Philadelphia Liberty")
    
    # Initialisation du jeu et de pause
    game = Game(screen)
    pause_menu = Pause(screen)
    
    # Initialisation du manager d'état
    state_manager = StateManager()
    state_manager.add_state("game", game)
    state_manager.add_state("pause", pause_menu)
    state_manager.set_state("game")  # Démarrer en mode jeu
    
    clock = pygame.time.Clock()
    
    # Boucle principale
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # Delta de temps en secondes
        
        # Événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Toggle entre jeu et pause
                    if state_manager.current_state == "game":
                        state_manager.set_state("pause")
                    elif state_manager.current_state == "pause":
                        state_manager.set_state("game")
            
            # Déléguer les évènements au manager
            state_manager.handle_event(event)
        
        # Mise à jour si en jeu
        if state_manager.current_state == "game":
            state_manager.update(dt)
        
        # Rendu
        game.draw()  # Toujours afficher le jeu en arrière-plan
        
        # Affichage écran pause au premier plan si nécessaire
        if state_manager.current_state == "pause":
            pause_menu.draw()
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
