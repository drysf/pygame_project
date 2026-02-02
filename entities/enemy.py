"""Entité des ennemis."""
import pygame
import random
from config import GameConfig
from .bullet import Bullet


class Enemy(pygame.sprite.Sprite):
    """Représente un soldat britannique ennemi."""
    
    # Configurations des types d'ennemis
    ENEMY_TYPES = {
        "regular": {
            "health": 2,
            "fire_rate": 60,
            "speed": 1,
            "width": 40,
            "height": 60
        },
        "elite": {
            "health": 3,
            "fire_rate": 40,
            "speed": 2,
            "width": 40,
            "height": 60
        },
        "officer": {
            "health": 4,
            "fire_rate": 45,
            "speed": 1.2,
            "width": 45,
            "height": 65
        },
        "commander": {
            "health": 6,
            "fire_rate": 30,
            "speed": 1.5,
            "width": 50,
            "height": 68
        },
        "tank": {
            "health": 8,
            "fire_rate": 80,
            "speed": 0.5,
            "width": 55,
            "height": 70
        }
    }
    
    def __init__(self, x, y, enemy_type="regular"):
        """
        Initialise un ennemi.
        
        Args:
            x: Position x initiale
            y: Position y initiale
            enemy_type: Type d'ennemi (regular, elite, officer, commander, tank)
        """
        super().__init__()
        self.enemy_type = enemy_type
        
        # Récupérer la configuration du type
        config = self.ENEMY_TYPES.get(enemy_type, self.ENEMY_TYPES["regular"])
        
        self.width = config["width"]
        self.height = config["height"]
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._draw_british_soldier()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Physique
        self.vel_y = 0
        self.gravity = 0.8
        self.direction = -1
        
        # Combat
        self.max_health = config["health"]
        self.health = config["health"]
        self.fire_rate = config["fire_rate"]
        self.speed = config["speed"]
        self.shoot_cooldown = random.randint(30, 60)
        self.patrol_direction = 1
        self.patrol_distance = 0
        self.max_patrol = 100
    
    def _draw_british_soldier(self):
        """Dessine un soldat britannique selon son type."""
        self.image.fill((0, 0, 0, 0))
        center_x = self.width // 2
        
        if self.enemy_type == "tank":
            self._draw_tank(center_x)
        elif self.enemy_type == "commander":
            self._draw_commander(center_x)
        elif self.enemy_type == "officer":
            self._draw_officer(center_x)
        elif self.enemy_type == "elite":
            self._draw_elite(center_x)
        else:
            self._draw_regular(center_x)
    
    def _draw_tank(self, center_x):
        """Dessine un soldat tank (massif avec armure)."""
        uniform_color = (80, 0, 0)
        accent_color = (200, 200, 200)
        
        # Corps très large
        pygame.draw.rect(self.image, uniform_color, (center_x - 15, 25, 30, 30))
        pygame.draw.rect(self.image, accent_color, (center_x - 13, 27, 26, 26))
        pygame.draw.rect(self.image, uniform_color, (center_x - 11, 29, 22, 22))
        
        # Jambes épaisses
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 12, 55, 10, 15))
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x + 2, 55, 10, 15))
        
        # Bottes renforcées
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 13, 65, 11, 5))
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x + 1, 65, 11, 5))
        
        # Tête large
        pygame.draw.circle(self.image, (255, 220, 180), (center_x, 15), 13)
        
        # Casque lourd
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 10, 0, 20, 15))
        pygame.draw.polygon(self.image, GameConfig.BLACK, 
                          [(center_x - 12, 14), (center_x, -5), (center_x + 12, 14)])
        pygame.draw.circle(self.image, accent_color, (center_x, 10), 3)
        
        # Yeux méchants
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x - 6, 12), (center_x - 3, 15), 3)
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x + 3, 15), (center_x + 6, 12), 3)
        
        # Cicatrice
        pygame.draw.line(self.image, GameConfig.RED, 
                        (center_x + 5, 12), (center_x + 8, 18), 2)
        
        # Mousquet lourd
        pygame.draw.rect(self.image, GameConfig.BROWN, (0, 28, 15, 5))
        pygame.draw.circle(self.image, GameConfig.DARK_GRAY, (3, 30), 4)
    
    def _draw_commander(self, center_x):
        """Dessine un commandant (officier décoré)."""
        uniform_color = (120, 0, 0)
        accent_color = (255, 215, 0)
        
        # Corps décoré
        pygame.draw.rect(self.image, uniform_color, (center_x - 12, 24, 24, 28))
        
        # Épaulettes dorées
        pygame.draw.rect(self.image, accent_color, (center_x - 15, 22, 8, 5))
        pygame.draw.rect(self.image, accent_color, (center_x + 7, 22, 8, 5))
        pygame.draw.circle(self.image, accent_color, (center_x - 11, 24), 3)
        pygame.draw.circle(self.image, accent_color, (center_x + 11, 24), 3)
        
        # Croix blanche
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 2, 24, 4, 28))
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 12, 35, 24, 4))
        
        # Jambes
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 10, 52, 8, 16))
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x + 2, 52, 8, 16))
        
        # Bottes cirées
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 11, 63, 9, 5))
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x + 1, 63, 9, 5))
        pygame.draw.circle(self.image, accent_color, (center_x - 6, 65), 2)
        pygame.draw.circle(self.image, accent_color, (center_x + 6, 65), 2)
        
        # Tête
        pygame.draw.circle(self.image, (255, 220, 180), (center_x, 14), 11)
        
        # Chapeau à plume
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 9, 0, 18, 10))
        pygame.draw.ellipse(self.image, GameConfig.BLACK, (center_x - 12, 8, 24, 5))
        pygame.draw.ellipse(self.image, GameConfig.RED, (center_x + 5, -5, 8, 15))
        pygame.draw.ellipse(self.image, (200, 0, 0), (center_x + 7, -3, 4, 12))
        
        # Yeux et moustache
        pygame.draw.circle(self.image, GameConfig.BLACK, (center_x - 4, 13), 2)
        pygame.draw.circle(self.image, GameConfig.BLACK, (center_x + 4, 13), 2)
        pygame.draw.arc(self.image, GameConfig.BLACK, 
                       (center_x - 6, 16, 12, 6), 0, 3.14, 2)
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x - 8, 18), (center_x - 2, 19), 2)
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x + 2, 19), (center_x + 8, 18), 2)
        
        # Médailles
        for i in range(3):
            pygame.draw.circle(self.image, accent_color, 
                             (center_x - 8 + i * 8, 30 + i * 5), 3)
        
        # Sabre
        pygame.draw.rect(self.image, (192, 192, 192), (2, 27, 12, 2))
        pygame.draw.circle(self.image, accent_color, (14, 28), 3)
    
    def _draw_officer(self, center_x):
        """Dessine un officier (avec galons)."""
        uniform_color = (170, 0, 0)
        accent_color = (255, 223, 0)
        
        # Corps
        pygame.draw.rect(self.image, uniform_color, (center_x - 11, 23, 22, 26))
        
        # Galons
        for i in range(3):
            pygame.draw.rect(self.image, accent_color, 
                           (center_x - 12, 22 + i * 2, 6, 1))
            pygame.draw.rect(self.image, accent_color, 
                           (center_x + 6, 22 + i * 2, 6, 1))
        
        # Croix
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 2, 23, 4, 26))
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 11, 34, 22, 4))
        
        # Jambes
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 9, 49, 8, 16))
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x + 1, 49, 8, 16))
        
        # Bottes
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 10, 60, 9, 5))
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x, 60, 9, 5))
        
        # Tête
        pygame.draw.circle(self.image, (255, 220, 180), (center_x, 13), 10)
        
        # Chapeau officier
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 8, -1, 16, 11))
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 10, 9, 20, 3))
        pygame.draw.circle(self.image, accent_color, (center_x, 4), 2)
        
        # Yeux sévères
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x - 5, 11), (center_x - 2, 13), 2)
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x + 2, 13), (center_x + 5, 11), 2)
        
        # Insigne
        pygame.draw.circle(self.image, accent_color, (center_x, 28), 4)
        pygame.draw.circle(self.image, uniform_color, (center_x, 28), 2)
        
        # Mousquet
        pygame.draw.rect(self.image, GameConfig.BROWN, (1, 25, 10, 3))
    
    def _draw_elite(self, center_x):
        """Dessine un soldat d'élite (entraîné)."""
        uniform_color = (150, 0, 0)
        accent_color = GameConfig.YELLOW
        
        # Corps athlétique
        pygame.draw.rect(self.image, uniform_color, (center_x - 10, 22, 20, 25))
        
        # Croix blanche proéminente
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 2, 22, 4, 25))
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 10, 32, 20, 5))
        
        # Jambes
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 8, 47, 7, 13))
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x + 1, 47, 7, 13))
        
        # Bottes
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 9, 57, 8, 3))
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x, 57, 8, 3))
        
        # Tête
        pygame.draw.circle(self.image, (255, 220, 180), (center_x, 12), 9)
        
        # Chapeau haut de forme
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 7, -1, 14, 11))
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 9, 9, 18, 3))
        
        # Yeux concentrés
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x - 4, 10), (center_x - 2, 12), 2)
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x + 2, 12), (center_x + 4, 10), 2)
        
        # Boutons dorés
        for i in range(3):
            pygame.draw.circle(self.image, accent_color, (center_x, 26 + i * 6), 2)
        
        # Mousquet
        pygame.draw.rect(self.image, GameConfig.BROWN, (2, 24, 9, 3))
    
    def _draw_regular(self, center_x):
        """Dessine un soldat régulier (standard)."""
        uniform_color = GameConfig.RED
        accent_color = GameConfig.WHITE
        
        # Corps basique
        pygame.draw.rect(self.image, uniform_color, (center_x - 10, 20, 20, 25))
        
        # Croix blanche simple
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 2, 20, 4, 25))
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 10, 30, 20, 4))
        
        # Jambes
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x - 8, 45, 7, 15))
        pygame.draw.rect(self.image, GameConfig.WHITE, (center_x + 1, 45, 7, 15))
        
        # Bottes simples
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 9, 55, 8, 5))
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x, 55, 8, 5))
        
        # Tête
        pygame.draw.circle(self.image, (255, 220, 180), (center_x, 12), 10)
        
        # Chapeau basique
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 8, -2, 16, 12))
        pygame.draw.rect(self.image, GameConfig.BLACK, (center_x - 10, 8, 20, 3))
        
        # Yeux
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x - 5, 9), (center_x - 2, 11), 2)
        pygame.draw.line(self.image, GameConfig.BLACK, 
                        (center_x + 2, 11), (center_x + 5, 9), 2)
        
        # Boutons
        for i in range(3):
            pygame.draw.circle(self.image, accent_color, (center_x, 25 + i * 6), 2)
        
        # Mousquet
        pygame.draw.rect(self.image, GameConfig.BROWN, (2, 22, 10, 3))
    
    def update(self, platforms, player_x):
        """
        Met à jour l'ennemi.
        
        Args:
            platforms: Groupe de sprites des plateformes
            player_x: Position x du joueur
        """
        # Gravité
        self.vel_y += self.gravity
        if self.vel_y > 15:
            self.vel_y = 15
        
        # Direction vers le joueur
        if player_x < self.rect.centerx:
            self.direction = -1
        else:
            self.direction = 1
        
        # Patrouille
        self.patrol_distance += self.speed * self.patrol_direction
        if abs(self.patrol_distance) > self.max_patrol:
            self.patrol_direction *= -1
        
        new_x = self.rect.x + self.speed * self.patrol_direction
        if 0 < new_x < 10000:
            self.rect.x = new_x
        
        # Mouvement vertical
        self.rect.y += self.vel_y
        
        # Collision
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
        
        # Cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def shoot(self, bullets, player_x):
        """
        Tire un projectile vers le joueur.
        
        Args:
            bullets: Groupe de sprites des balles
            player_x: Position x du joueur
        """
        if self.shoot_cooldown <= 0:
            direction = -1 if player_x < self.rect.centerx else 1
            bullet_x = self.rect.left if direction == -1 else self.rect.right
            bullet = Bullet(bullet_x, self.rect.centery, direction, False)
            bullets.add(bullet)
            self.shoot_cooldown = self.fire_rate
    
    def take_damage(self):
        """
        Inflige des dégâts à l'ennemi.
        
        Returns:
            True si l'ennemi est mort, False sinon
        """
        self.health -= 1
        return self.health <= 0
