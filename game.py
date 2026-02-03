"""
Classe principale du jeu gérant tous les éléments
"""
import pygame
import random
from player import Player
from enemy import Enemy
from bullet import Bullet
from camera import Camera
from level_manager import LevelManager


class Game:
    """Gestionnaire principal du jeu"""
    
    def __init__(self, screen, level_config=None, player_data=None):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        # Configuration du niveau
        self.level_config = level_config or {"name": "Default", "enemies": 20, "map_type": "warehouse"}
        self.player_data = player_data
        
        # Statistiques de la partie
        self.kills = 0
        self.gold_earned = 0
        self.gold_per_kill = 25  # Or gagné par ennemi tué
        
        # Groupes de sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.decorations = pygame.sprite.Group()
        
        # Création du niveau
        level_manager = LevelManager(self.screen_width, self.screen_height)
        self.current_map = level_manager.create_level(self.level_config)
        
        self.walls.add(self.current_map.walls)
        self.all_sprites.add(self.current_map.walls)
        self.decorations.add(self.current_map.decorations)
        
        # Création de la caméra
        self.camera = Camera(self.screen_width, self.screen_height,
                            self.current_map.map_width, self.current_map.map_height)
        
        # Création du joueur avec ses armes possédées
        spawn_pos = self.current_map.get_spawn_position()
        owned_weapons = None
        if self.player_data:
            owned_weapons = self.player_data.owned_weapons
        self.player = Player(spawn_pos[0], spawn_pos[1], owned_weapons)
        self.all_sprites.add(self.player)
        
        # Création des ennemis
        enemy_count = self.level_config.get("enemies", 20)
        self._spawn_enemies(enemy_count)
        
        # Police pour le HUD
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # État du jeu
        self.game_over = False
        self.victory = False
        
        # Notifications de gain d'or
        self.gold_notifications = []
    
    def _spawn_enemies(self, count):
        """Fait apparaître des ennemis répartis sur toute la carte"""
        for _ in range(count):
            valid_position = False
            attempts = 0
            
            while not valid_position and attempts < 100:
                # Position aléatoire sur toute la carte
                x = random.randint(100, self.current_map.map_width - 100)
                y = random.randint(100, self.current_map.map_height - 100)
                
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
        if self.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self._restart_game()
                elif event.key == pygame.K_m:
                    return "menu"
            return None
        
        if self.victory:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "next_level"
                elif event.key == pygame.K_m:
                    return "menu"
            return None
        
        # Gérer le changement d'arme
        self.player.handle_weapon_switch(event)
        return None
    
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
                    for enemy in list(self.enemies):
                        if melee_rect.colliderect(enemy.rect):
                            if enemy.take_damage(weapon.damage):
                                self._on_enemy_killed(enemy)
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
        for bullet in list(self.player_bullets):
            bullet.update(dt)
            
            # Collision avec les murs
            if pygame.sprite.spritecollide(bullet, self.walls, False):
                bullet.kill()
                continue
            
            # Collision avec les ennemis
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            if hit_enemies:
                bullet.kill()
                for enemy in hit_enemies:
                    if enemy.take_damage(bullet.damage):
                        self._on_enemy_killed(enemy)
                        enemy.kill()
        
        # Mise à jour des balles ennemies
        for bullet in list(self.enemy_bullets):
            bullet.update(dt)
            
            # Collision avec les murs
            if pygame.sprite.spritecollide(bullet, self.walls, False):
                bullet.kill()
                continue
            
            # Collision avec le joueur
            if pygame.sprite.collide_rect(bullet, self.player):
                bullet.kill()
                if self.player.take_damage(bullet.damage):
                    self.game_over = True
                    if self.player_data:
                        self.player_data.record_death()
        
        # Mettre à jour les notifications d'or
        self._update_gold_notifications(dt)
        
        # Vérifier la victoire
        if len(self.enemies) == 0 and not self.victory:
            self.victory = True
            self._on_level_complete()
    
    def draw(self):
        """Dessine tous les éléments du jeu"""
        # Fond de la carte (intérieur sombre)
        self.screen.fill((40, 40, 45))
        
        # Dessiner les zones extérieures (herbe verte)
        self._draw_exterior_ground()
        
        # Dessiner les décorations d'abord (en arrière-plan)
        for decoration in self.decorations:
            screen_rect = self.camera.apply(decoration)
            if screen_rect.right > 0 and screen_rect.left < self.screen_width and \
               screen_rect.bottom > 0 and screen_rect.top < self.screen_height:
                self.screen.blit(decoration.image, screen_rect)
        
        # Dessiner tous les sprites avec la caméra
        for sprite in self.all_sprites:
            screen_rect = self.camera.apply(sprite)
            # Ne dessiner que si visible à l'écran
            if screen_rect.right > 0 and screen_rect.left < self.screen_width and \
               screen_rect.bottom > 0 and screen_rect.top < self.screen_height:
                self.screen.blit(sprite.image, screen_rect)
        
        # Dessiner les barres de vie des ennemis
        for enemy in self.enemies:
            enemy.draw_health_bar(self.screen, self.camera)
        
        # Dessiner le HUD
        self._draw_hud()
        
        # Dessiner les messages de fin
        if self.game_over:
            self._draw_game_over()
        elif self.victory:
            self._draw_victory()
    
    def _draw_exterior_ground(self):
        """Dessine le sol des zones extérieures"""
        # Dessiner le sol de base de la carte
        if hasattr(self.current_map, 'ground_color'):
            ground_rect = pygame.Rect(0, 0, self.current_map.map_width, self.current_map.map_height)
            screen_rect = self.camera.apply_rect(ground_rect)
            pygame.draw.rect(self.screen, self.current_map.ground_color, screen_rect)
        
        # Dessiner les zones extérieures spécifiques
        if hasattr(self.current_map, 'exterior_zones'):
            for zone_rect, color in self.current_map.exterior_zones:
                screen_rect = self.camera.apply_rect(zone_rect)
                if screen_rect.right > 0 and screen_rect.left < self.screen_width and \
                   screen_rect.bottom > 0 and screen_rect.top < self.screen_height:
                    pygame.draw.rect(self.screen, color, screen_rect)
    
    def _draw_hud(self):
        """Dessine l'interface utilisateur"""
        # Fond du HUD
        hud_bg = pygame.Surface((220, 200))
        hud_bg.set_alpha(180)
        hud_bg.fill((0, 0, 0))
        self.screen.blit(hud_bg, (5, 5))
        
        # Nom du niveau
        level_name = self.level_config.get("name", "Mission")
        level_text = self.small_font.render(level_name, True, (255, 215, 0))
        self.screen.blit(level_text, (10, 10))
        
        # Barre de vie
        health_text = self.font.render(f"HP: {self.player.health}/{self.player.max_health}", 
                                       True, (255, 255, 255))
        self.screen.blit(health_text, (10, 35))
        
        # Compteur d'ennemis
        enemies_text = self.font.render(f"Ennemis: {len(self.enemies)}", 
                                       True, (255, 255, 255))
        self.screen.blit(enemies_text, (10, 70))
        
        # Or gagné cette partie
        gold_text = self.font.render(f"$ +{self.gold_earned}", True, (255, 215, 0))
        self.screen.blit(gold_text, (10, 100))
        
        # Or total
        if self.player_data:
            total_gold = self.small_font.render(f"Total: ${self.player_data.gold + self.gold_earned}", 
                                                True, (200, 180, 100))
            self.screen.blit(total_gold, (10, 125))
        
        # Barre de vie visuelle
        bar_width = 200
        bar_height = 20
        fill = (self.player.health / self.player.max_health) * bar_width
        fill = max(0, fill)
        outline_rect = pygame.Rect(10, 150, bar_width, bar_height)
        fill_rect = pygame.Rect(10, 150, fill, bar_height)
        
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
        weapon_text = self.small_font.render(f"Arme: {weapon.name}", True, (255, 200, 0))
        self.screen.blit(weapon_text, (10, 177))
        
        # Dessiner les notifications d'or
        self._draw_gold_notifications()
        
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
        scale_x = minimap_width / self.current_map.map_width
        scale_y = minimap_height / self.current_map.map_height
        
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
        kills_text = self.font.render(f"Ennemis tués: {self.kills}", True, (255, 255, 255))
        gold_text = self.font.render(f"Or conservé: ${self.gold_earned // 2}", True, (255, 215, 0))
        restart_text = self.small_font.render("[R] Recommencer  |  [M] Menu", True, (200, 200, 200))
        
        text_rect = game_over_text.get_rect(center=(self.screen_width // 2, 
                                                     self.screen_height // 2 - 80))
        kills_rect = kills_text.get_rect(center=(self.screen_width // 2, 
                                                  self.screen_height // 2 - 20))
        gold_rect = gold_text.get_rect(center=(self.screen_width // 2, 
                                                self.screen_height // 2 + 20))
        restart_rect = restart_text.get_rect(center=(self.screen_width // 2, 
                                                      self.screen_height // 2 + 80))
        
        self.screen.blit(game_over_text, text_rect)
        self.screen.blit(kills_text, kills_rect)
        self.screen.blit(gold_text, gold_rect)
        self.screen.blit(restart_text, restart_rect)
    
    def _draw_victory(self):
        """Dessine l'écran de victoire"""
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        victory_text = self.font.render("MISSION ACCOMPLIE!", True, (0, 255, 0))
        level_name = self.level_config.get("name", "Mission")
        level_text = self.font.render(f"{level_name} terminé!", True, (255, 255, 255))
        kills_text = self.font.render(f"Ennemis tués: {self.kills}", True, (255, 255, 255))
        gold_text = self.font.render(f"Or gagné: ${self.gold_earned}", True, (255, 215, 0))
        continue_text = self.small_font.render("[ENTRÉE] Niveau suivant  |  [M] Menu", True, (200, 200, 200))
        
        text_rect = victory_text.get_rect(center=(self.screen_width // 2, 
                                                   self.screen_height // 2 - 100))
        level_rect = level_text.get_rect(center=(self.screen_width // 2, 
                                                  self.screen_height // 2 - 50))
        kills_rect = kills_text.get_rect(center=(self.screen_width // 2, 
                                                  self.screen_height // 2))
        gold_rect = gold_text.get_rect(center=(self.screen_width // 2, 
                                                self.screen_height // 2 + 50))
        continue_rect = continue_text.get_rect(center=(self.screen_width // 2, 
                                                        self.screen_height // 2 + 120))
        
        self.screen.blit(victory_text, text_rect)
        self.screen.blit(level_text, level_rect)
        self.screen.blit(kills_text, kills_rect)
        self.screen.blit(gold_text, gold_rect)
        self.screen.blit(continue_text, continue_rect)
    
    def _restart_game(self):
        """Redémarre le jeu"""
        # Nettoyer tous les sprites
        self.all_sprites.empty()
        self.enemies.empty()
        self.player_bullets.empty()
        self.enemy_bullets.empty()
        self.walls.empty()
        self.decorations.empty()
        
        # Réinitialiser les stats mais garder l'or partiel en cas de game over
        if self.game_over and self.player_data:
            self.player_data.gold += self.gold_earned // 2  # Garder la moitié de l'or
        
        self.kills = 0
        self.gold_earned = 0
        self.gold_notifications = []
        
        # Recréer la carte
        level_manager = LevelManager(self.screen_width, self.screen_height)
        self.current_map = level_manager.create_level(self.level_config)
        
        self.walls.add(self.current_map.walls)
        self.all_sprites.add(self.current_map.walls)
        self.decorations.add(self.current_map.decorations)
        
        # Recréer le joueur avec ses armes possédées
        spawn_pos = self.current_map.get_spawn_position()
        owned_weapons = None
        if self.player_data:
            owned_weapons = self.player_data.owned_weapons
        self.player = Player(spawn_pos[0], spawn_pos[1], owned_weapons)
        self.all_sprites.add(self.player)
        
        # Recréer les ennemis
        enemy_count = self.level_config.get("enemies", 20)
        self._spawn_enemies(enemy_count)
        
        # Réinitialiser la caméra
        self.camera = Camera(self.screen_width, self.screen_height,
                            self.current_map.map_width, self.current_map.map_height)
        
        # Réinitialiser l'état
        self.game_over = False
        self.victory = False
    
    def _on_enemy_killed(self, enemy):
        """Appelé quand un ennemi est tué"""
        self.kills += 1
        self.gold_earned += self.gold_per_kill
        
        # Ajouter une notification d'or
        screen_pos = self.camera.apply_pos((enemy.pos.x, enemy.pos.y))
        self.gold_notifications.append({
            'text': f'+${self.gold_per_kill}',
            'pos': list(screen_pos),
            'timer': 1.0,
            'alpha': 255
        })
    
    def _on_level_complete(self):
        """Appelé quand le niveau est terminé"""
        if self.player_data:
            # Trouver l'index du niveau actuel
            level_index = 0
            level_names = ["Entrepôt", "Base Militaire", "Forêt", "Bunker", "QG Ennemi"]
            level_name = self.level_config.get("name", "")
            if level_name in level_names:
                level_index = level_names.index(level_name)
            
            self.player_data.complete_level(level_index, self.gold_earned, self.kills)
            self.player_data.save()
    
    def _update_gold_notifications(self, dt):
        """Met à jour les notifications d'or"""
        for notif in self.gold_notifications[:]:
            notif['timer'] -= dt
            notif['pos'][1] -= 50 * dt  # Monte vers le haut
            notif['alpha'] = int(255 * (notif['timer'] / 1.0))
            
            if notif['timer'] <= 0:
                self.gold_notifications.remove(notif)
    
    def _draw_gold_notifications(self):
        """Dessine les notifications d'or"""
        for notif in self.gold_notifications:
            font = pygame.font.Font(None, 28)
            text = font.render(notif['text'], True, (255, 215, 0))
            text.set_alpha(notif['alpha'])
            self.screen.blit(text, notif['pos'])
