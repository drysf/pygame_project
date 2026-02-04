"""
Classe représentant les ennemis
"""
import pygame
import math
import random
import os

class Enemy(pygame.sprite.Sprite):
    """Ennemi contrôlé par l'IA"""
    
    # Cache pour l'image du soldat
    _soldier_image = None
    
    @classmethod
    def _load_soldier_image(cls):
        """Charge l'image du soldat (une seule fois)"""
        if cls._soldier_image is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, 'assets', 'england_soldier', 'soldier.png')
            try:
                original = pygame.image.load(image_path).convert_alpha()
                # Redimensionner à 130x130
                scaled = pygame.transform.scale(original, (130, 130))
                # Retourner l'image (elle était à l'envers)
                cls._soldier_image = pygame.transform.flip(scaled, False, True)
            except Exception as e:
                print(f"[ERREUR] Chargement soldier.png: {e}")
                # Fallback: carré rouge
                cls._soldier_image = pygame.Surface((130, 130), pygame.SRCALPHA)
                cls._soldier_image.fill((200, 50, 50))
        return cls._soldier_image
    
    def __init__(self, x, y):
        super().__init__()
        
        # Apparence - charger l'image du soldat
        self.original_image = Enemy._load_soldier_image().copy()
        
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        
        # Position précise
        self.pos = pygame.math.Vector2(x, y)
        
        # Statistiques
        self.max_health = 50
        self.health = self.max_health
        self.speed = 120
        self.is_elite = False
        self.gold_reward = 10  # Or donné à la mort
        
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
    
    def draw_health_bar(self, screen, camera):
        """Dessine la barre de vie au-dessus de l'ennemi"""
        # Dimensions de la barre
        bar_width = 40
        bar_height = 5
        
        # Position au-dessus de l'ennemi (en coordonnées monde)
        bar_x = self.pos.x - bar_width // 2
        bar_y = self.pos.y - 30
        
        # Convertir en coordonnées écran via la caméra
        screen_x = bar_x - camera.x
        screen_y = bar_y - camera.y
        
        # Calcul du remplissage
        health_ratio = self.health / self.max_health
        fill_width = int(bar_width * health_ratio)
        
        # Couleur selon la vie
        if health_ratio > 0.6:
            fill_color = (0, 255, 0)  # Vert
        elif health_ratio > 0.3:
            fill_color = (255, 255, 0)  # Jaune
        else:
            fill_color = (255, 0, 0)  # Rouge
        
        # Dessiner le fond (noir)
        background_rect = pygame.Rect(screen_x, screen_y, bar_width, bar_height)
        pygame.draw.rect(screen, (0, 0, 0), background_rect)
        
        # Dessiner le remplissage
        if fill_width > 0:
            fill_rect = pygame.Rect(screen_x, screen_y, fill_width, bar_height)
            pygame.draw.rect(screen, fill_color, fill_rect)
        
        # Dessiner le contour
        pygame.draw.rect(screen, (255, 255, 255), background_rect, 1)


class EliteEnemy(Enemy):
    """Ennemi d'élite - Plus puissant, apparence noir et rouge"""
    
    def __init__(self, x, y):
        super().__init__(x, y)
        
        # Marquer comme élite
        self.is_elite = True
        
        # Statistiques améliorées
        self.max_health = 200  # 4x plus de vie
        self.health = self.max_health
        self.speed = 100  # Un peu plus lent mais tank
        self.gold_reward = 50  # Plus d'or
        
        # Apparence - soldat agrandi et teinté en rouge pour l'élite
        size = 160  # Plus grand
        base_image = Enemy._load_soldier_image()
        scaled = pygame.transform.scale(base_image, (size, size))
        
        # Teinter l'image en rouge pour l'élite
        self.original_image = scaled.copy()
        red_overlay = pygame.Surface((size, size), pygame.SRCALPHA)
        red_overlay.fill((255, 50, 50, 80))  # Teinte rouge semi-transparente
        self.original_image.blit(red_overlay, (0, 0))
        
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        
        # Tir plus rapide
        self.shoot_cooldown = 1.5
    
    def draw_health_bar(self, screen, camera):
        """Dessine une barre de vie plus grande pour l'élite"""
        # Dimensions de la barre (plus grande)
        bar_width = 60
        bar_height = 8
        
        # Position au-dessus de l'ennemi
        bar_x = self.pos.x - bar_width // 2
        bar_y = self.pos.y - 40
        
        # Convertir en coordonnées écran
        screen_x = bar_x - camera.x
        screen_y = bar_y - camera.y
        
        # Calcul du remplissage
        health_ratio = self.health / self.max_health
        fill_width = int(bar_width * health_ratio)
        
        # Fond noir
        background_rect = pygame.Rect(screen_x, screen_y, bar_width, bar_height)
        pygame.draw.rect(screen, (0, 0, 0), background_rect)
        
        # Remplissage dégradé rouge/orange pour élite
        if fill_width > 0:
            fill_rect = pygame.Rect(screen_x, screen_y, fill_width, bar_height)
            if health_ratio > 0.5:
                fill_color = (200, 50, 50)  # Rouge
            else:
                fill_color = (255, 100, 0)  # Orange
            pygame.draw.rect(screen, fill_color, fill_rect)
        
        # Contour doré pour élite
        pygame.draw.rect(screen, (255, 200, 0), background_rect, 2)
        
        # Indicateur "ELITE" au-dessus
        font = pygame.font.Font(None, 18)
        elite_text = font.render("ELITE", True, (255, 50, 50))
        text_rect = elite_text.get_rect(center=(screen_x + bar_width // 2, screen_y - 10))
        screen.blit(elite_text, text_rect)