"""
Philladelphia Liberty
Incarnez un soldat de la révolution américaine et combattez les anglais
pour déclarer l'indépendance des États-Unis !
"""

import sys
import pygame

from game import Game
from menu import MainMenu, LevelSelectMenu, PauseMenu
from menu_game_over import GameOverScreen
from menu_win import WinScreen
from shop import Shop
from player_data import PlayerData


# États du jeu
STATE_MENU = "menu"
STATE_LEVEL_SELECT = "level_select"
STATE_SHOP = "shop"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_WIN = "win"
STATE_GAME_OVER = "game_over"


# Audio
pygame.mixer.init()
MUSIC_MENU = "assets/Sons/son_accueil.mp3"
MUSIC_GAME = "assets/Sons/audio_en_jeu.mp3"
MUSIC_GAMEOVER = "assets/Sons/gameover.mp3"
MUSIC_WIN = "assets/Sons/victoire.mp3"
MUSIC_SHOP = "assets/Sons/shop_music.mp3" 

def main():
    """Configuration principale du jeu."""
    pygame.init()

    # Configuration de la fenêtre
    screen_width = 1024
    screen_height = 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("PHILADELPHIA LIBERTY")

    # Musique du menu au lancement
    pygame.mixer.music.load(MUSIC_MENU)
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

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
    
    game_over_screen = GameOverScreen(screen)

    win_screen = WinScreen(screen)

    # État actuel
    current_state = STATE_MENU
    game = None
    current_level = None

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        # Gestion des événements
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
                    pygame.mixer.music.load(MUSIC_SHOP)
                    pygame.mixer.music.play(-1)
                elif action == "levels":
                    current_state = STATE_LEVEL_SELECT
                elif action == "quit":
                    running = False

            elif current_state == STATE_LEVEL_SELECT:
                action = level_select.handle_event(event)
                if action == "back":
                    current_state = STATE_MENU
                elif action == "play":
                    current_level = level_select.get_selected_level()
                    if current_level:
                        game = Game(screen, current_level, player_data)
                        current_state = STATE_PLAYING
                        pygame.mixer.music.load(MUSIC_GAME)
                        pygame.mixer.music.set_volume(0.8)
                        pygame.mixer.music.play(-1)
                elif action == "unlocked":
                    player_data.save()

            elif current_state == STATE_SHOP:
                action = shop.handle_event(event)
                if action == "back":
                    player_data.save()
                    current_state = STATE_MENU
                    pygame.mixer.music.load(MUSIC_MENU)
                    pygame.mixer.music.set_volume(0.6)
                    pygame.mixer.music.play(-1)
                elif action == "purchased":
                    player_data.save()

            elif current_state == STATE_PLAYING:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    current_state = STATE_PAUSED
                    pygame.mixer.music.set_volume(0.3)
                    continue

                result = game.handle_event(event)
                if result == "menu":
                    player_data.save()
                    current_state = STATE_MENU
                    game = None
                    pygame.mixer.music.load(MUSIC_MENU)
                    pygame.mixer.music.set_volume(0.6)
                    pygame.mixer.music.play(-1)
                elif result == "next_level":
                    level_index = level_select.selected_level
                    if level_index + 1 < len(level_select.levels):
                        level_select.selected_level = level_index + 1
                        current_level = level_select.get_selected_level()
                        if current_level and current_level["unlocked"]:
                            game = Game(screen, current_level, player_data)
                    else:
                        current_state = STATE_MENU
                        game = None
                        pygame.mixer.music.load(MUSIC_MENU)
                        pygame.mixer.music.set_volume(0.6)
                        pygame.mixer.music.play(-1)

            elif current_state == STATE_PAUSED:
                action = pause_menu.handle_event(event)
                if action == "resume":
                    current_state = STATE_PLAYING
                    pygame.mixer.music.set_volume(0.8)
                elif action == "menu":
                    player_data.save()
                    current_state = STATE_MENU
                    game = None
                    pygame.mixer.music.load(MUSIC_MENU)
                    pygame.mixer.music.set_volume(0.6)
                    pygame.mixer.music.play(-1)
                elif action == "quit":
                    running = False

            elif current_state == STATE_GAME_OVER:
                action = game_over_screen.handle_input(event)
                if action == "REESSAYER":
                    if game:
                        game._restart_game()
                        current_state = STATE_PLAYING
                        pygame.mixer.music.load(MUSIC_GAME)
                        pygame.mixer.music.set_volume(0.8)
                        pygame.mixer.music.play(-1)
                elif action == "MENU PRINCIPAL":
                    player_data.save()
                    current_state = STATE_MENU
                    game = None
                    pygame.mixer.music.load(MUSIC_MENU)
                    pygame.mixer.music.set_volume(0.6)
                    pygame.mixer.music.play(-1)
                elif action == "QUITTER":
                    running = False

            elif current_state == STATE_WIN:
                action = win_screen.handle_input(event)
                if action == "NIVEAU SUIVANT":
                    level_index = level_select.selected_level
                    if level_index + 1 < len(level_select.levels):
                        level_select.selected_level = level_index + 1
                        current_level = level_select.get_selected_level()
                        if current_level and current_level["unlocked"]:
                            game = Game(screen, current_level, player_data)
                            current_state = STATE_PLAYING
                            pygame.mixer.music.load(MUSIC_GAME)
                            pygame.mixer.music.set_volume(0.8)
                            pygame.mixer.music.play(-1)
                    else:
                        current_state = STATE_MENU
                        game = None
                        pygame.mixer.music.load(MUSIC_MENU)
                        pygame.mixer.music.set_volume(0.6)
                        pygame.mixer.music.play(-1)
                elif action == "MENU PRINCIPAL":
                    player_data.save()
                    current_state = STATE_MENU
                    game = None
                    pygame.mixer.music.load(MUSIC_MENU)
                    pygame.mixer.music.set_volume(0.6)
                    pygame.mixer.music.play(-1)
                elif action == "QUITTER":
                    running = False

        # Updates selon l'état
        if current_state == STATE_MENU:
            main_menu.update(dt)
        elif current_state == STATE_LEVEL_SELECT:
            level_select.update(dt)
        elif current_state == STATE_SHOP:
            shop.update(dt)
        elif current_state == STATE_PLAYING and game:
            game.update(dt)

            # Vérifier le game over après l'update
            if game.game_over and current_state == STATE_PLAYING:
                print("GAME OVER DETECTE!")  # DEBUG
                  
                print("CHANGEMENT VERS STATE_GAME_OVER")  # DEBUG
                current_state = STATE_GAME_OVER
                pygame.mixer.music.load(MUSIC_GAMEOVER)
                pygame.mixer.music.set_volume(0.8)
                pygame.mixer.music.play(0)
            
            # Vérifier la victoire après l'update
            if game.victory and current_state == STATE_PLAYING:
                print("VICTOIRE DETECTEE!")  # DEBUG
                current_state = STATE_WIN
                pygame.mixer.music.load(MUSIC_WIN)
                pygame.mixer.music.set_volume(0.8)
                pygame.mixer.music.play(0)
                
        elif current_state == STATE_PAUSED:
            pause_menu.update(dt)
        elif current_state == STATE_WIN:
            win_screen.update()
        elif current_state == STATE_GAME_OVER:
            print(f"Dans STATE_GAME_OVER, running={running}")  # DEBUG
            game_over_screen.update()

        # Rendu selon l'état
        if current_state == STATE_MENU:
            main_menu.draw()
        elif current_state == STATE_LEVEL_SELECT:
            level_select.draw()
        elif current_state == STATE_SHOP:
            shop.draw()
        elif current_state == STATE_PLAYING and game:
            game.draw()
        elif current_state == STATE_PAUSED:
            if game:
                game.draw()
            pause_menu.draw()
        elif current_state == STATE_GAME_OVER:
            if game:
                game.draw()
            game_over_screen.draw()
        elif current_state == STATE_WIN:
            if game:
                game.draw()
            win_screen.draw()

        pygame.display.flip()

    # Sauvegarder avant de quitter
    player_data.save()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
