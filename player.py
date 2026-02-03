"""
Classe représentant le joueur
"""
import pygame
import math
import random
from animation import PlayerAnimations
from weapon import WeaponManager


class Player(pygame.sprite.Sprite):
    """Joueur contrôlé par l'utilisateur"""
    
    def __init__(self, x, y):
        super().__init__()
        
        # Animations
        self.animations = PlayerAnimations()
        
        # Image initiale
        self.original_image = self.animations.get_current_frame()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        
        # Position précise
        self.pos = pygame.math.Vector2(x, y)
        
        # Statistiques
        self.max_health = 100
        self.health = self.max_health
        self.speed = 280
        
        # Armes
        self.weapon_manager = WeaponManager()
        self.shoot_timer = 0
        self.can_shoot = True
        
        # État
        self.is_moving = False
        self.angle = 0
    
    @property
    def current_weapon(self):
        return self.weapon_manager.current_weapon
    
    def update(self, dt, keys, mouse_pos, walls):
        """Met à jour le joueur"""
        self.shoot_timer += dt
        
        # Vecteur de déplacement
        direction = pygame.math.Vector2(0, 0)
        
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_z]:
            direction.y = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction.y = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_q]:
            direction.x = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            direction.x = 1
        
        # Normaliser et appliquer le mouvement
        self.is_moving = direction.length() > 0
        
        if self.is_moving:
            direction = direction.normalize()
            
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
        
        # Mettre à jour l'animation
        self.animations.update(dt, self.is_moving)
        
        # Rotation vers la souris
        self._rotate_to_mouse(mouse_pos)
    
    def _check_wall_collision(self, walls):
        """Vérifie la collision avec les murs"""
        # Créer un rect plus petit pour la collision
        collision_rect = pygame.Rect(0, 0, 30, 30)
        collision_rect.center = self.rect.center
        
        for wall in walls:
            if collision_rect.colliderect(wall.rect):
                return True
        return False
    
    def _rotate_to_mouse(self, mouse_pos):
        """Fait tourner le joueur vers la souris"""
        dx = mouse_pos[0] - self.pos.x
        dy = mouse_pos[1] - self.pos.y
        self.angle = math.degrees(math.atan2(-dy, dx))
        
        # Obtenir le frame actuel et le pivoter
        self.original_image = self.animations.get_current_frame()
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(int(self.pos.x), int(self.pos.y)))
    
    def shoot(self, target_pos, mouse_pressed):
        """Tire des balles vers la cible"""
        weapon = self.current_weapon
        
        # Vérifier le cooldown
        if self.shoot_timer < weapon.cooldown:
            return []
        
        # Armes semi-auto
        if not weapon.auto_fire:
            if not self.can_shoot:
                return []
            if mouse_pressed:
                self.can_shoot = False
        
        self.shoot_timer = 0
        self.animations.trigger_shoot()
        
        # Si c'est une arme de mêlée (pas de balles)
        if weapon.bullet_speed == 0:
            return self._melee_attack()
        
        bullets = []
        
        # Direction de base
        dx = target_pos[0] - self.pos.x
        dy = target_pos[1] - self.pos.y
        distance = math.sqrt(dx * dx + dy * dy)
        
        if distance > 0:
            base_angle = math.atan2(dy, dx)
            
            # Créer les balles avec dispersion
            for i in range(weapon.bullet_count):
                spread_angle = math.radians(random.uniform(-weapon.spread, weapon.spread))
                angle = base_angle + spread_angle
                
                bullet_dx = math.cos(angle)
                bullet_dy = math.sin(angle)
                
                from bullet import Bullet
                bullet = Bullet(
                    self.pos.x + bullet_dx * 30,
                    self.pos.y + bullet_dy * 30,
                    bullet_dx, bullet_dy,
                    (255, 255, 0),
                    is_player=True,
                    damage=weapon.damage,
                    speed=weapon.bullet_speed
                )
                bullets.append(bullet)
        
        return bullets
    
    def _melee_attack(self):
        """Attaque de mêlée (retourne les ennemis touchés via le système de jeu)"""
        # Retourne une liste vide, le jeu gère la détection de mêlée
        return []
    
    def handle_weapon_switch(self, event):
        """Gère le changement d'arme"""
        if event.type == pygame.KEYDOWN:
            weapon_changed = False
            
            if event.key == pygame.K_1:
                self.weapon_manager.select_weapon(0)
                weapon_changed = True
            elif event.key == pygame.K_2:
                self.weapon_manager.select_weapon(1)
                weapon_changed = True
            elif event.key == pygame.K_3:
                self.weapon_manager.select_weapon(2)
                weapon_changed = True
            elif event.key == pygame.K_4:
                self.weapon_manager.select_weapon(3)
                weapon_changed = True
            elif event.key == pygame.K_5:
                self.weapon_manager.select_weapon(4)
                weapon_changed = True
            
            if weapon_changed:
                # Mettre à jour l'animation pour la nouvelle arme
                self.animations.set_weapon(self.current_weapon.animation_key)
        
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                self.weapon_manager.previous_weapon()
            else:
                self.weapon_manager.next_weapon()
            self.animations.set_weapon(self.current_weapon.animation_key)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.can_shoot = True
    
    def take_damage(self, damage):
        """Inflige des dégâts au joueur"""
        self.health -= damage
        return self.health <= 0
    
    def get_melee_rect(self):
        """Retourne le rectangle d'attaque de mêlée"""
        # Zone devant le joueur
        angle_rad = math.radians(-self.angle)
        offset_x = math.cos(angle_rad) * 50
        offset_y = -math.sin(angle_rad) * 50
        
        melee_rect = pygame.Rect(0, 0, 60, 60)
        melee_rect.center = (self.pos.x + offset_x, self.pos.y + offset_y)
        return melee_rect
