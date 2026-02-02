"""Entité des projectiles."""
import pygame
from config import GameConfig


class Bullet(pygame.sprite.Sprite):
    """Représente un projectile tiré par le joueur ou un ennemi."""
    
    def __init__(self, x, y, direction, is_player_bullet=True):
        """
        Initialise un projectile.
        
        Args:
            x: Position x initiale
            y: Position y initiale
            direction: Direction du tir (-1 gauche, 1 droite)
            is_player_bullet: True si tiré par le joueur, False sinon
        """
        super().__init__()
        self.image = pygame.Surface((12, 4))
        color = GameConfig.YELLOW if is_player_bullet else GameConfig.RED
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.direction = direction
        self.speed = 15 if is_player_bullet else 8
        self.is_player_bullet = is_player_bullet
    
    def update(self):
        """Met à jour la position du projectile."""
        self.rect.x += self.speed * self.direction
        
        # Détruire si hors écran
        if self.rect.right < -100 or self.rect.left > GameConfig.SCREEN_WIDTH + 1100:
            self.kill()
