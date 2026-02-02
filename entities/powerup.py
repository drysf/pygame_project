"""Entité des power-ups."""
import pygame
import math
from config import GameConfig


class PowerUp(pygame.sprite.Sprite):
    """Représente un power-up (amélioration temporaire)."""
    
    def __init__(self, x, y, powerup_type="fire_rate"):
        """
        Initialise un power-up.
        
        Args:
            x: Position x
            y: Position y
            powerup_type: Type de power-up ('fire_rate', 'health', 'speed')
        """
        super().__init__()
        self.powerup_type = powerup_type
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        
        if powerup_type == "fire_rate":
            self._draw_star(GameConfig.YELLOW)
        elif powerup_type == "health":
            self._draw_heart(GameConfig.RED)
        elif powerup_type == "speed":
            self._draw_lightning(GameConfig.LIGHT_BLUE)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.float_offset = 0
        self.base_y = y
    
    def _draw_star(self, color):
        """Dessine une étoile."""
        center = 15
        points = []
        for i in range(5):
            angle = math.radians(i * 72 - 90)
            points.append((center + 12 * math.cos(angle), 
                          center + 12 * math.sin(angle)))
            angle = math.radians(i * 72 - 90 + 36)
            points.append((center + 5 * math.cos(angle), 
                          center + 5 * math.sin(angle)))
        pygame.draw.polygon(self.image, color, points)
        pygame.draw.polygon(self.image, GameConfig.ORANGE, points, 2)
    
    def _draw_heart(self, color):
        """Dessine un cœur."""
        pygame.draw.circle(self.image, color, (10, 12), 7)
        pygame.draw.circle(self.image, color, (20, 12), 7)
        pygame.draw.polygon(self.image, color, [(3, 14), (15, 27), (27, 14)])
    
    def _draw_lightning(self, color):
        """Dessine un éclair."""
        points = [(15, 2), (8, 14), (13, 14), (10, 28), (22, 12), (16, 12), (20, 2)]
        pygame.draw.polygon(self.image, color, points)
        pygame.draw.polygon(self.image, GameConfig.BLUE, points, 2)
    
    def update(self):
        """Animation flottante du power-up."""
        self.float_offset += 0.1
        self.rect.y = self.base_y + math.sin(self.float_offset) * 5
