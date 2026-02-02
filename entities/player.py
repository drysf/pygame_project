"""Entité du joueur."""
import pygame
from config import GameConfig
from .bullet import Bullet


class Player(pygame.sprite.Sprite):
    """Représente le soldat américain contrôlé par le joueur."""
    
    def __init__(self, x, y):
        """
        Initialise le joueur.
        
        Args:
            x: Position x initiale
            y: Position y initiale
        """
        super().__init__()
        self.skins = ["default", "general", "minuteman"]
        self.skin_index = 0
        
        self.width = 40
        self.height = 60
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._draw_soldier()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Physique
        self.vel_x = 0
        self.vel_y = 0
        self.base_speed = 5
        self.speed = self.base_speed
        self.jump_power = -15
        self.gravity = 0.8
        self.on_ground = False
        self.direction = 1
        self.step_counter = 0
        
        # Combat
        self.max_health = 4
        self.health = self.max_health
        self.shoot_cooldown = 0
        self.base_fire_rate = 15
        self.fire_rate = self.base_fire_rate
        self.invincible = 0
        
        # Power-ups
        self.fire_rate_boost = 0
        self.speed_boost = 0
    
    def _draw_soldier(self):
        """Dessine le soldat américain selon le skin actuel."""
        self.image.fill((0, 0, 0, 0))
        
        skin = self.skins[self.skin_index]
        if skin == "general":
            uniform_color = GameConfig.DARK_BLUE
            accent_color = GameConfig.YELLOW
        elif skin == "minuteman":
            uniform_color = GameConfig.BROWN
            accent_color = GameConfig.CREAM
        else:
            uniform_color = (0, 0, 139)
            accent_color = (255, 215, 0)
        
        # Corps
        pygame.draw.rect(self.image, uniform_color, (10, 20, 20, 25))
        
        # Jambes
        pygame.draw.rect(self.image, GameConfig.CREAM, (12, 45, 7, 15))
        pygame.draw.rect(self.image, GameConfig.CREAM, (21, 45, 7, 15))
        
        # Bottes
        pygame.draw.rect(self.image, GameConfig.BLACK, (11, 55, 8, 5))
        pygame.draw.rect(self.image, GameConfig.BLACK, (20, 55, 8, 5))
        
        # Tête
        pygame.draw.circle(self.image, (255, 220, 180), (20, 12), 10)
        
        # Chapeau tricorne
        pygame.draw.rect(self.image, GameConfig.BLACK, (8, 2, 24, 6))
        pygame.draw.polygon(self.image, GameConfig.BLACK, [(10, 2), (20, -3), (30, 2)])
        
        # Yeux
        pygame.draw.circle(self.image, GameConfig.BLACK, (17, 11), 2)
        pygame.draw.circle(self.image, GameConfig.BLACK, (23, 11), 2)
        
        # Boutons
        for i in range(3):
            pygame.draw.circle(self.image, accent_color, (20, 25 + i * 6), 2)
        
        # Mousquet
        pygame.draw.rect(self.image, uniform_color, (28, 22, 8, 5))
        pygame.draw.rect(self.image, GameConfig.BROWN, (32, 20, 8, 3))
    
    def change_skin(self):
        """Change le skin du soldat."""
        self.skin_index = (self.skin_index + 1) % len(self.skins)
        self._draw_soldier()
    
    def update(self, platforms, sound_manager):
        """
        Met à jour le joueur.
        
        Args:
            platforms: Groupe de sprites des plateformes
            sound_manager: Gestionnaire de sons
        """
        # Gestion des power-ups
        if self.fire_rate_boost > 0:
            self.fire_rate_boost -= 1
            self.fire_rate = self.base_fire_rate // 2
        else:
            self.fire_rate = self.base_fire_rate
        
        if self.speed_boost > 0:
            self.speed_boost -= 1
            self.speed = self.base_speed * 1.5
        else:
            self.speed = self.base_speed
        
        if self.invincible > 0:
            self.invincible -= 1
        
        # Son de pas
        if self.vel_x != 0 and self.on_ground:
            self.step_counter += 1
            if self.step_counter >= 20:
                sound_manager.play('step')
                self.step_counter = 0
        
        # Gravité
        self.vel_y += self.gravity
        if self.vel_y > 15:
            self.vel_y = 15
        
        # Mouvement horizontal
        self.rect.x += self.vel_x
        
        # Collision horizontale
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:
                    self.rect.right = platform.rect.left
                elif self.vel_x < 0:
                    self.rect.left = platform.rect.right
        
        # Mouvement vertical
        self.rect.y += self.vel_y
        self.on_ground = False
        
        # Collision verticale
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
        
        # Limites (seulement à gauche)
        if self.rect.left < 0:
            self.rect.left = 0
        
        # Cooldown de tir
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def jump(self, sound_manager):
        """
        Fait sauter le joueur.
        
        Args:
            sound_manager: Gestionnaire de sons
        """
        if self.on_ground:
            self.vel_y = self.jump_power
            sound_manager.play('jump')
    
    def shoot(self, bullets, sound_manager):
        """
        Tire un projectile.
        
        Args:
            bullets: Groupe de sprites des balles
            sound_manager: Gestionnaire de sons
        """
        if self.shoot_cooldown <= 0:
            bullet_x = self.rect.right if self.direction == 1 else self.rect.left
            bullet = Bullet(bullet_x, self.rect.centery, self.direction, True)
            bullets.add(bullet)
            self.shoot_cooldown = self.fire_rate
            sound_manager.play('shoot')
    
    def take_damage(self, sound_manager):
        """
        Inflige des dégâts au joueur.
        
        Args:
            sound_manager: Gestionnaire de sons
            
        Returns:
            True si des dégâts ont été infligés, False sinon
        """
        if self.invincible <= 0:
            self.health -= 1
            self.invincible = 60
            sound_manager.play('hit')
            return True
        return False
    
    def collect_powerup(self, powerup, sound_manager):
        """
        Collecte un power-up.
        
        Args:
            powerup: Instance du power-up collecté
            sound_manager: Gestionnaire de sons
        """
        if powerup.powerup_type == "fire_rate":
            self.fire_rate_boost = 300
        elif powerup.powerup_type == "health":
            if self.health < self.max_health:
                self.health += 1
        elif powerup.powerup_type == "speed":
            self.speed_boost = 300
        sound_manager.play('powerup')
