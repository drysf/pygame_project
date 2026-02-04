"""
Classe représentant les projectiles
"""
import pygame
import math
import os



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
            # Essayer de charger le sprite de bullet
            try:
                import os
                bullet_path = os.path.join("assets", "player", "bullet", "bullet.png")
                bullet_sprite = pygame.image.load(bullet_path).convert_alpha()
                
                # Redimensionner selon si c'est le joueur ou l'ennemi
                size = 12 if is_player else 8
                bullet_sprite = pygame.transform.scale(bullet_sprite, (size, size))
                
                # Pivoter dans la direction du tir
                angle = math.degrees(math.atan2(-dy, dx))
                self.image = pygame.transform.rotate(bullet_sprite, angle)
            except Exception as e:
                # Fallback : balle géométrique par défaut si le sprite n'est pas trouvé
                print(f"Impossible de charger le sprite de bullet: {e}")
                radius = 5 if is_player else 4
                self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(self.image, color, (radius, radius), radius)
        
        # LIGNE IMPORTANTE : Créer le rect APRÈS avoir créé l'image
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
