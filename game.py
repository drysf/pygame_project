"""
Classe principale du jeu gérant tous les éléments
"""
import pygame
import random
from player import Player
from enemy import Enemy
from bullet import Bullet
from room import Room
from camera import Camera


class Game:
    """Gestionnaire principal du jeu"""
    
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        # Groupes de sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        
        # Création de la salle (grande carte)
        self.room = Room(self.screen_width, self.screen_height)
        self.walls.add(self.room.walls)
        self.all_sprites.add(self.room.walls)
        
        # Création de la caméra
        self.camera = Camera(self.screen_width, self.screen_height,
                            self.room.map_width, self.room.map_height)
        
        # Création du joueur (dans la première salle)
        self.player = Player(self.screen_width // 2, self.screen_height // 2)
        self.all_sprites.add(self.player)
        
        # Création des ennemis répartis sur la carte
        self._spawn_enemies(20)
        
        # Police pour le HUD
        self.font = pygame.font.Font(None, 36)
        
        # État du jeu
        self.game_over = False
        self.victory = False
    
    def _spawn_enemies(self, count):
        """Fait apparaître des ennemis répartis sur toute la carte"""
        for _ in range(count):
            valid_position = False
            attempts = 0
            
            while not valid_position and attempts < 100:
                # Position aléatoire sur toute la carte
                x = random.randint(100, self.room.map_width - 100)
                y = random.randint(100, self.room.map_height - 100)
                
                # Vérifier que l'ennemi n'est pas trop proche du joueur
                distance = ((x - self.player.pos.x) ** 2 + 
                           (y - self.player.pos.y) ** 2) ** 0.5
                
                if distance > 300:
                    enemy = Enemy(x, y)
                    # Vérifier les collisions avec les murs
                    if not pygame.sprite.spritecollide(enemy, self.walls, False):
                        valid_position = True
                        self.enemies.add(enemy)
                        self.all_sprites.add(enemy)
                
                attempts += 1
    
    def handle_event(self, event):
        """Gère les événements du jeu"""
        if self.game_over or self.victory:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self._restart_game()
            return
        
        # Gérer le changement d'arme
        self.player.handle_weapon_switch(event)
    
    def update(self, dt):
        """Met à jour tous les éléments du jeu"""
        if self.game_over or self.victory:
            return
        
        # Convertir la position de la souris en coordonnées monde
        mouse_screen_pos = pygame.mouse.get_pos()
        mouse_world_pos = self.camera.screen_to_world(mouse_screen_pos)
        
        # Mise à jour du joueur
        keys = pygame.key.get_pressed()
        self.player.update(dt, keys, mouse_world_pos, self.walls)
        
        # Mise à jour de la caméra
        self.camera.update(self.player)
        
        # Tir avec clic gauche
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            weapon = self.player.current_weapon
            
            # Si c'est une arme de mêlée
            if weapon.bullet_speed == 0:
                if self.player.shoot_timer >= weapon.cooldown:
                    self.player.shoot_timer = 0
                    self.player.animations.trigger_shoot()
                    # Vérifier les ennemis dans la zone de mêlée
                    melee_rect = self.player.get_melee_rect()
                    for enemy in self.enemies:
                        if melee_rect.colliderect(enemy.rect):
                            if enemy.take_damage(weapon.damage):
                                enemy.kill()
            else:
                bullets = self.player.shoot(mouse_world_pos, True)
                for bullet in bullets:
                    self.player_bullets.add(bullet)
                    self.all_sprites.add(bullet)
        
        # Mise à jour des ennemis
        for enemy in self.enemies:
            enemy.update(dt, self.player.pos, self.walls)
            
            # Les ennemis tirent sur le joueur
            bullet = enemy.shoot(self.player.pos)
            if bullet:
                self.enemy_bullets.add(bullet)
                self.all_sprites.add(bullet)
        
        # Mise à jour des balles du joueur
        for bullet in self.player_bullets:
            bullet.update(dt)
            
            # Collision avec les murs
            if pygame.sprite.spritecollide(bullet, self.walls, False):
                bullet.kill()
            
            # Collision avec les ennemis
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            if hit_enemies:
                bullet.kill()
                for enemy in hit_enemies:
                    if enemy.take_damage(bullet.damage):
                        enemy.kill()
        
        # Mise à jour des balles ennemies
        for bullet in self.enemy_bullets:
            bullet.update(dt)
            
            # Collision avec les murs
            if pygame.sprite.spritecollide(bullet, self.walls, False):
                bullet.kill()
            
            # Collision avec le joueur
            if pygame.sprite.collide_rect(bullet, self.player):
                bullet.kill()
                if self.player.take_damage(bullet.damage):
                    self.game_over = True
        
        # Vérifier la victoire
        if len(self.enemies) == 0:
            self.victory = True
    
    def draw(self):
        """Dessine tous les éléments du jeu"""
        # Fond de la carte
        self.screen.fill((40, 40, 45))
        
        # Dessiner tous les sprites avec la caméra
        for sprite in self.all_sprites:
            screen_rect = self.camera.apply(sprite)
            # Ne dessiner que si visible à l'écran
            if screen_rect.right > 0 and screen_rect.left < self.screen_width and \
               screen_rect.bottom > 0 and screen_rect.top < self.screen_height:
                self.screen.blit(sprite.image, screen_rect)
        
        # Dessiner le HUD
        self._draw_hud()
        
        # Dessiner les messages de fin
        if self.game_over:
            self._draw_game_over()
        elif self.victory:
            self._draw_victory()
    
    def _draw_hud(self):
        """Dessine l'interface utilisateur"""
        # Fond du HUD
        hud_bg = pygame.Surface((220, 170))
        hud_bg.set_alpha(180)
        hud_bg.fill((0, 0, 0))
        self.screen.blit(hud_bg, (5, 5))
        
        # Barre de vie
        health_text = self.font.render(f"HP: {self.player.health}/{self.player.max_health}", 
                                       True, (255, 255, 255))
        self.screen.blit(health_text, (10, 10))
        
        # Compteur d'ennemis
        enemies_text = self.font.render(f"Ennemis: {len(self.enemies)}", 
                                       True, (255, 255, 255))
        self.screen.blit(enemies_text, (10, 50))
        
        # Barre de vie visuelle
        bar_width = 200
        bar_height = 20
        fill = (self.player.health / self.player.max_health) * bar_width
        fill = max(0, fill)
        outline_rect = pygame.Rect(10, 90, bar_width, bar_height)
        fill_rect = pygame.Rect(10, 90, fill, bar_height)
        
        # Couleur selon la vie
        if self.player.health > 60:
            color = (0, 255, 0)
        elif self.player.health > 30:
            color = (255, 255, 0)
        else:
            color = (255, 0, 0)
        
        pygame.draw.rect(self.screen, color, fill_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), outline_rect, 2)
        
        # Afficher l'arme actuelle
        weapon = self.player.current_weapon
        weapon_text = self.font.render(f"Arme: {weapon.name}", True, (255, 200, 0))
        self.screen.blit(weapon_text, (10, 120))
        
        # Instructions de changement d'arme
        small_font = pygame.font.Font(None, 24)
        switch_text = small_font.render("[1-5] ou molette pour changer", True, (150, 150, 150))
        self.screen.blit(switch_text, (10, 150))
        
        # Mini-carte
        self._draw_minimap()
    
    def _draw_minimap(self):
        """Dessine une mini-carte"""
        minimap_width = 150
        minimap_height = 100
        minimap_x = self.screen_width - minimap_width - 10
        minimap_y = 10
        
        # Fond de la mini-carte
        minimap = pygame.Surface((minimap_width, minimap_height))
        minimap.set_alpha(200)
        minimap.fill((20, 20, 20))
        
        # Échelle
        scale_x = minimap_width / self.room.map_width
        scale_y = minimap_height / self.room.map_height
        
        # Dessiner les murs sur la mini-carte
        for wall in self.walls:
            x = int(wall.rect.x * scale_x)
            y = int(wall.rect.y * scale_y)
            w = max(1, int(wall.rect.width * scale_x))
            h = max(1, int(wall.rect.height * scale_y))
            pygame.draw.rect(minimap, (80, 80, 80), (x, y, w, h))
        
        # Dessiner les ennemis
        for enemy in self.enemies:
            x = int(enemy.pos.x * scale_x)
            y = int(enemy.pos.y * scale_y)
            pygame.draw.circle(minimap, (255, 0, 0), (x, y), 2)
        
        # Dessiner le joueur
        player_x = int(self.player.pos.x * scale_x)
        player_y = int(self.player.pos.y * scale_y)
        pygame.draw.circle(minimap, (0, 255, 0), (player_x, player_y), 3)
        
        # Cadre de la caméra
        cam_x = int(self.camera.x * scale_x)
        cam_y = int(self.camera.y * scale_y)
        cam_w = int(self.screen_width * scale_x)
        cam_h = int(self.screen_height * scale_y)
        pygame.draw.rect(minimap, (255, 255, 255), (cam_x, cam_y, cam_w, cam_h), 1)
        
        self.screen.blit(minimap, (minimap_x, minimap_y))
        pygame.draw.rect(self.screen, (100, 100, 100), 
                        (minimap_x, minimap_y, minimap_width, minimap_height), 2)
    
    def _draw_game_over(self):
        """Dessine l'écran de game over"""
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        restart_text = self.font.render("Appuyez sur R pour recommencer", True, (255, 255, 255))
        
        text_rect = game_over_text.get_rect(center=(self.screen_width // 2, 
                                                     self.screen_height // 2 - 50))
        restart_rect = restart_text.get_rect(center=(self.screen_width // 2, 
                                                      self.screen_height // 2 + 50))
        
        self.screen.blit(game_over_text, text_rect)
        self.screen.blit(restart_text, restart_rect)
    
    def _draw_victory(self):
        """Dessine l'écran de victoire"""
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        victory_text = self.font.render("VICTOIRE!", True, (0, 255, 0))
        restart_text = self.font.render("Appuyez sur R pour recommencer", True, (255, 255, 255))
        
        text_rect = victory_text.get_rect(center=(self.screen_width // 2, 
                                                   self.screen_height // 2 - 50))
        restart_rect = restart_text.get_rect(center=(self.screen_width // 2, 
                                                      self.screen_height // 2 + 50))
        
        self.screen.blit(victory_text, text_rect)
        self.screen.blit(restart_text, restart_rect)
    
    def _restart_game(self):
        """Redémarre le jeu"""
        # Nettoyer tous les sprites
        self.all_sprites.empty()
        self.enemies.empty()
        self.player_bullets.empty()
        self.enemy_bullets.empty()
        self.walls.empty()
        
        # Recréer la salle
        self.room = Room(self.screen_width, self.screen_height)
        self.walls.add(self.room.walls)
        self.all_sprites.add(self.room.walls)
        
        # Recréer le joueur
        self.player = Player(self.screen_width // 2, self.screen_height // 2)
        self.all_sprites.add(self.player)
        
        # Recréer les ennemis
        self._spawn_enemies(20)
        
        # Réinitialiser l'état
        self.game_over = False
        self.victory = False
