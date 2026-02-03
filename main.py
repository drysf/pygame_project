"""
Philladelphia Liberty
Incarnez un soldat de la révolution américaine et combattez les anglais pour déclarer l'indépendance des Etats-Unis !
"""
import pygame
import sys
from game import Game
from menu import MainMenu, LevelSelectMenu, PauseMenu
from shop import Shop
from player_data import PlayerData


# États du jeu
STATE_MENU = "menu"
STATE_LEVEL_SELECT = "Selectionner niveau"
STATE_SHOP = "shop"
STATE_PLAYING = "En jeu"
STATE_PAUSED = "En pause"


def main():
    """Configuration principale du jeu"""
    pygame.init()
    
    # Configuration de la fenêtre
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("PHILADELPHIA LIBERTY")
    
    clock = pygame.time.Clock()
    
    # Données du joueur (persistantes)
    player_data = PlayerData()
    
    # Initialisation des menus
    main_menu = MainMenu(screen)
    main_menu.set_player_data(player_data)
    
    level_select = LevelSelectMenu(screen)
    level_select.set_player_data(player_data)
    
    shop = Shop(screen)
    shop.set_player_data(player_data)
    
    pause_menu = PauseMenu(screen)
    
    # État actuel
    current_state = STATE_MENU
    game = None
    current_level = None
    
    # Boucle principale
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # Delta de temps en secondes
        
        # Événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
            
            # Événements selon l'état
            if current_state == STATE_MENU:
                action = main_menu.handle_event(event)
                if action == "play":
                    current_state = STATE_LEVEL_SELECT
                elif action == "shop":
                    current_state = STATE_SHOP
                elif action == "Niveaux":
                    current_state = STATE_LEVEL_SELECT
                elif action == "quit":
                    running = False
            
            elif current_state == STATE_LEVEL_SELECT:
                action = level_select.handle_event(event)
                if action == "Retour":
                    current_state = STATE_MENU
                elif action == "play":
                    current_level = level_select.get_selected_level()
                    if current_level:
                        game = Game(screen, current_level, player_data)
                        current_state = STATE_PLAYING
                elif action == "Dévérouiller":
                    player_data.save()
            
            elif current_state == STATE_SHOP:
                action = shop.handle_event(event)
                if action == "Précédent":
                    player_data.save()
                    current_state = STATE_MENU
                elif action == "Acheté":
                    player_data.save()
            
            elif current_state == STATE_PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        current_state = STATE_PAUSED
                        continue
                
                result = game.handle_event(event)
                if result == "Menu":
                    player_data.save()
                    current_state = STATE_MENU
                    game = None
                elif result == "Niveau suivant":
                    level_index = level_select.selected_level
                    if level_index + 1 < len(level_select.levels):
                        level_select.selected_level = level_index + 1
                        current_level = level_select.get_selected_level()
                        if current_level and current_level["unlocked"]:
                            game = Game(screen, current_level, player_data)
                    else:
                        current_state = STATE_MENU
                        game = None
            
            elif current_state == STATE_PAUSED:
                action = pause_menu.handle_event(event)
                if action == "Reprendre":
                    current_state = STATE_PLAYING
                elif action == "Menu":
                    player_data.save()
                    current_state = STATE_MENU
                    game = None
                elif action == "quit":
                    running = False
        
        if current_state == STATE_MENU:
            main_menu.update(dt)
        elif current_state == STATE_LEVEL_SELECT:
            level_select.update(dt)
        elif current_state == STATE_SHOP:
            shop.update(dt)
        elif current_state == STATE_PLAYING:
            if game:
                game.update(dt)
        elif current_state == STATE_PAUSED:
            pause_menu.update(dt)
        
        # Rendu selon l'état
        if current_state == STATE_MENU:
            main_menu.draw()
        elif current_state == STATE_LEVEL_SELECT:
            level_select.draw()
        elif current_state == STATE_SHOP:
            shop.draw()
        elif current_state == STATE_PLAYING:
            if game:
                game.draw()
        elif current_state == STATE_PAUSED:
            if game:
                game.draw()
            pause_menu.draw()
        
        pygame.display.flip()
    
    # Sauvegarder avant de quit
    player_data.save()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
