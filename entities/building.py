"""Entité des bâtiments d'arrière-plan."""
import pygame
import random
from config import GameConfig


class Building(pygame.sprite.Sprite):
    """Représente un bâtiment de Philadelphie en arrière-plan."""
    
    def __init__(self, x, y, width, height):
        """
        Initialise un bâtiment.
        
        Args:
            x: Position x
            y: Position y
            width: Largeur du bâtiment
            height: Hauteur du bâtiment
        """
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self._draw_building(width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def _draw_building(self, width, height):
        """Dessine un bâtiment colonial."""
        colors = [GameConfig.BRICK_RED, GameConfig.CREAM, (200, 180, 160)]
        color = random.choice(colors)
        pygame.draw.rect(self.image, color, (0, 20, width, height - 20))
        
        # Toit
        pygame.draw.polygon(self.image, GameConfig.DARK_GRAY, 
                          [(0, 20), (width // 2, 0), (width, 20)])
        
        # Fenêtres
        window_width = width // 5
        window_height = height // 6
        for row in range(2):
            for col in range(2):
                wx = 10 + col * (width // 2)
                wy = 40 + row * (height // 3)
                if wx + window_width < width and wy + window_height < height:
                    pygame.draw.rect(self.image, GameConfig.LIGHT_BLUE, 
                                   (wx, wy, window_width, window_height))
                    pygame.draw.rect(self.image, GameConfig.BROWN, 
                                   (wx, wy, window_width, window_height), 2)
                    pygame.draw.line(self.image, GameConfig.BROWN, 
                                   (wx + window_width//2, wy), 
                                   (wx + window_width//2, wy + window_height), 2)
                    pygame.draw.line(self.image, GameConfig.BROWN, 
                                   (wx, wy + window_height//2), 
                                   (wx + window_width, wy + window_height//2), 2)
        
        # Porte
        door_width = width // 4
        door_height = height // 3
        pygame.draw.rect(self.image, GameConfig.BROWN, 
                        (width//2 - door_width//2, height - door_height, 
                         door_width, door_height))
