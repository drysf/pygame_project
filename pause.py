"""
Classe gérant l'écran de pause
"""
import pygame


class Pause:
    """Gère l'écran de pause du jeu"""
    
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 100)
        self.font_medium = pygame.font.Font(None, 50)
        self.font_small = pygame.font.Font(None, 36)
    
    def handle_event(self, event):
        """Gère les événements spécifiques à la pause"""
        # Possibilité d'ajouter des boutons plus tard
        pass
    
    def update(self, dt):
        """Mise à jour de la pause (pas nécessaire pour l'instant)"""
        pass
    
    def draw(self):
        """Affiche l'écran de pause par-dessus le jeu"""
        # Overlay semi-transparent noir
        overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        overlay.set_alpha(180)  # Transparence
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Titre "PAUSE"
        pause_text = self.font_large.render("PAUSE", True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(self.screen.get_width()//2, 
                                                  self.screen.get_height()//2 - 80))
        self.screen.blit(pause_text, pause_rect)
        
        # Sous-titre thématique
        subtitle = self.font_medium.render("La révolution attend...", True, (200, 200, 200))
        subtitle_rect = subtitle.get_rect(center=(self.screen.get_width()//2, 
                                                   self.screen.get_height()//2))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Instructions
        instruction = self.font_small.render("Appuyez sur ECHAP pour continuer", 
                                             True, (150, 150, 150))
        instruction_rect = instruction.get_rect(center=(self.screen.get_width()//2, 
                                                        self.screen.get_height()//2 + 80))
        self.screen.blit(instruction, instruction_rect)
