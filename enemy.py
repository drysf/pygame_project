"""
Classe représentant les ennemis
"""
import pygame
import math
import random


class Enemy(pygame.sprite.Sprite):
    """Ennemi contrôlé par l'IA"""
    
    def __init__(self, x, y):
        super().__init__()
        
        # Apparence
        self.original_image = pygame.Surface((35, 35), pygame.SRCALPHA)
        self.original_image.fill((200, 50, 50))
        pygame.draw.polygon(self.original_image, (150, 0, 0), 
                          [(17, 0), (35, 35), (0, 35)])
        
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        
        # Position précise
        self.pos = pygame.math.Vector2(x, y)
        
        # Statistiques
        self.max_health = 50
        self.health = self.max_health
        self.speed = 120
        
        # IA
        self.detection_range = 500
        self.attack_range = 400
        self.stop_distance = 150
        
        # Tir
        self.shoot_cooldown = 2.0
        self.shoot_timer = random.uniform(0, self.shoot_cooldown)
    
    def update(self, dt, player_pos, walls):
        """Met à jour l'ennemi"""
        self.shoot_timer += dt
        
        # Calculer la distance au joueur
        to_player = player_pos - self.pos
        distance = to_player.length()
        
        # Si le joueur est dans la portée de détection
        if distance < self.detection_range and distance > 0:
            # Rotation vers le joueur
            self._rotate_to_target(player_pos)
            
            # Mouvement vers le joueur si pas trop proche
            if distance > self.stop_distance:
                direction = to_player.normalize()
                
                # Mouvement horizontal
                self.pos.x += direction.x * self.speed * dt
                self.rect.centerx = int(self.pos.x)
                if self._check_wall_collision(walls):
                    self.pos.x -= direction.x * self.speed * dt
                    self.rect.centerx = int(self.pos.x)
                
                # Mouvement vertical
                self.pos.y += direction.y * self.speed * dt
                self.rect.centery = int(self.pos.y)
                if self._check_wall_collision(walls):
                    self.pos.y -= direction.y * self.speed * dt
                    self.rect.centery = int(self.pos.y)
    
    def _check_wall_collision(self, walls):
        """Vérifie la collision avec les murs"""
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                return True
        return False
    
    def _rotate_to_target(self, target_pos):
        """Fait tourner l'ennemi vers la cible"""
        dx = target_pos.x - self.pos.x
        dy = target_pos.y - self.pos.y
        angle = math.degrees(math.atan2(-dy, dx)) - 90
        
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=(int(self.pos.x), int(self.pos.y)))
    
    def shoot(self, target_pos):
        """Tire une balle vers la cible"""
        to_target = target_pos - self.pos
        distance = to_target.length()
        
        if distance < self.attack_range and distance > 0 and self.shoot_timer >= self.shoot_cooldown:
            self.shoot_timer = 0
            direction = to_target.normalize()
            
            from bullet import Bullet
            return Bullet(self.pos.x, self.pos.y, direction.x, direction.y, 
                         (255, 100, 0), is_player=False)
        
        return None
    
    def take_damage(self, damage):
        """Inflige des dégâts à l'ennemi"""
        self.health -= damage
        return self.health <= 0
