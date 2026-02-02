"""Entité des plateformes."""
import pygame
from config import GameConfig


class Platform(pygame.sprite.Sprite):
    """Représente une plateforme ou le sol."""
    
    def __init__(self, x, y, width, height, platform_type="ground"):
        """
        Initialise une plateforme.
        
        Args:
            x: Position x
            y: Position y
            width: Largeur de la plateforme
            height: Hauteur de la plateforme
            platform_type: Type de plateforme ('ground' ou 'brick')
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.platform_type = platform_type
        
        if platform_type == "ground":
            self._draw_cobblestone(width, height)
        elif platform_type == "brick":
            self._draw_brick(width, height)
        else:
            self.image.fill(GameConfig.BROWN)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def _draw_cobblestone(self, width, height):
        """Dessine une texture de pavés."""
        self.image.fill(GameConfig.GRAY)
        for i in range(0, width, 30):
            for j in range(0, height, 20):
                offset = 15 if (j // 20) % 2 else 0
                pygame.draw.rect(self.image, GameConfig.DARK_GRAY, 
                               (i + offset, j, 28, 18), 1)
    
    def _draw_brick(self, width, height):
        """Dessine une texture de briques."""
        self.image.fill(GameConfig.BRICK_RED)
        for i in range(0, width, 40):
            for j in range(0, height, 20):
                offset = 20 if (j // 20) % 2 else 0
                pygame.draw.rect(self.image, GameConfig.DARK_GRAY, 
                               (i + offset, j, 38, 18), 1)
