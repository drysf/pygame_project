"""
Classe représentant les projectiles
"""
import pygame
import math


class Bullet(pygame.sprite.Sprite):
    """Projectile tiré par le joueur ou les ennemis"""
    
    def __init__(self, x, y, dx, dy, color, is_player=True, damage=None, speed=None, image=None):
        super().__init__()
        
        # Position
        self.pos = pygame.math.Vector2(x, y)
        
        # Direction
        self.dx = dx
        self.dy = dy
        
        # Propriétés
        self.speed = speed if speed else (600 if is_player else 400)
        self.damage = damage if damage else (25 if is_player else 10)
        self.is_player = is_player
        
        # Apparence
        if image:
            # Pivoter l'image dans la direction du tir
            angle = math.degrees(math.atan2(-dy, dx))
            self.image = pygame.transform.rotate(image, angle)
        else:
            # Créer une balle par défaut
            radius = 5 if is_player else 4
            self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(self.image, color, (radius, radius), radius)
        
        self.rect = self.image.get_rect(center=(x, y))
        
        # Durée de vie
        self.lifetime = 3.0
        self.age = 0
    
    def update(self, dt):
        """Met à jour la position de la balle"""
        # Déplacement
        self.pos.x += self.dx * self.speed * dt
        self.pos.y += self.dy * self.speed * dt
        
        self.rect.centerx = int(self.pos.x)
        self.rect.centery = int(self.pos.y)
        
        # Vieillissement
        self.age += dt
        if self.age >= self.lifetime:
            self.kill()
