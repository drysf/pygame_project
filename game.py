"""Gestion des éléments du jeu"""
import pygame
import random
import math
from player import Player
from enemy import Enemy, EliteEnemy
from bullet import Bullet
from camera import Camera
from level_manager import LevelManager

POWERUP_SOUND = None

def get_powerup_sound():
    """Charge le son de power-up si ce n'est pas déjà fait"""
    global POWERUP_SOUND
    if POWERUP_SOUND is None:
        try:
            POWERUP_SOUND = pygame.mixer.Sound("assets/Sons/powerup.mp3")
            POWERUP_SOUND.set_volume(10.0)  
        except Exception as e:
            print(f"Erreur chargement son power-up: {e}")
    return POWERUP_SOUND
class HealthPack(pygame.sprite.Sprite):
    """Power-up qui redonne de la vie"""
    
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)
        self.heal_amount = 30
        
        self.pulse_timer = 0
        self.size = 12
        
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self._draw_pack()
    
    def _draw_pack(self):
        """Dessine le power-up"""
        self.image.fill((0, 0, 0, 0))
        center = (15, 15)
        
        pulse = 1 + 0.2 * math.sin(self.pulse_timer)
        size = int(self.size * pulse)
        
        pygame.draw.circle(self.image, (255, 100, 100, 100), center, size + 5)
        pygame.draw.circle(self.image, (200, 50, 50), center, size)
        
        cross_w = size // 2
        cross_h = 3
        pygame.draw.rect(self.image, (255, 255, 255), 
                        (center[0] - cross_w, center[1] - cross_h, cross_w * 2, cross_h * 2))
        pygame.draw.rect(self.image, (255, 255, 255), 
                        (center[0] - cross_h, center[1] - cross_w, cross_h * 2, cross_w * 2))
        
        pygame.draw.circle(self.image, (255, 255, 255), center, size, 2)
    
    def update(self, dt):
        """Met à jour l'animation"""
        self.pulse_timer += dt * 5
        self._draw_pack()

class Game:
    """Gestionnaire principal du jeu"""

    def __init__(self, screen, level_config=None, player_data=None):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        self.level_config = level_config or {"name": "Default", "enemies": 20, "map_type": "warehouse"}
        self.player_data = player_data

        self.kills = 0
        self.gold_earned = 0
        self.gold_per_kill = 25

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.decorations = pygame.sprite.Group()
        self.health_packs = pygame.sprite.Group()

        level_manager = LevelManager(self.screen_width, self.screen_height)
        self.current_map = level_manager.create_level(self.level_config)

        self.walls.add(self.current_map.walls)
        self.all_sprites.add(self.current_map.walls)
        self.decorations.add(self.current_map.decorations)

        self.camera = Camera(self.screen_width, self.screen_height,
                            self.current_map.map_width, self.current_map.map_height)

        spawn_pos = self.current_map.get_spawn_position()
        owned_weapons = None
        if self.player_data:
            owned_weapons = self.player_data.owned_weapons
        self.player = Player(spawn_pos[0], spawn_pos[1], owned_weapons)
        self.all_sprites.add(self.player)

        enemy_count = self.level_config.get("enemies", 20)
        self._spawn_enemies(enemy_count)

        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        self.game_over = False
        self.victory = False

        self.gold_notifications = []
        self.heal_notifications = []

        self.health_pack_drop_chance = 0.6

    def _spawn_enemies(self, count):
        """Fait apparaître des ennemis répartis sur toute la carte (avec élites)"""
        for i in range(count):
            valid_position = False
            attempts = 0

            while not valid_position and attempts < 100:
                x = random.randint(100, self.current_map.map_width - 100)
                y = random.randint(100, self.current_map.map_height - 100)

                distance = ((x - self.player.pos.x) ** 2 + 
                           (y - self.player.pos.y) ** 2) ** 0.5

                if distance > 300:
                    if (i + 1) % 5 == 0:
                        enemy = EliteEnemy(x, y)
                    else:
                        enemy = Enemy(x, y)
                    
                    if not pygame.sprite.spritecollide(enemy, self.walls, False):
                        valid_position = True
                        self.enemies.add(enemy)
                        self.all_sprites.add(enemy)

                attempts += 1

    def _spawn_health_pack(self, x, y):
        """Fait apparaître un pack de vie à la position donnée"""
        health_pack = HealthPack(x, y)
        self.health_packs.add(health_pack)
        self.all_sprites.add(health_pack)

    def handle_event(self, event):
        """Gère les événements du jeu"""
        if self.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self._restart_game()
            return None

        if self.victory:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "next_level"
                elif event.key == pygame.K_m:
                    return "menu"
            return None

        self.player.handle_weapon_switch(event)
        return None
    
    def update(self, dt):
        """Met à jour tous les éléments du jeu"""
        if self.game_over or self.victory:
            return

        mouse_screen_pos = pygame.mouse.get_pos()
        mouse_world_pos = self.camera.screen_to_world(mouse_screen_pos)

        keys = pygame.key.get_pressed()
        self.player.update(dt, keys, mouse_world_pos, self.walls)

        self.camera.update(self.player)

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            weapon = self.player.current_weapon

            if weapon.bullet_speed == 0:
                if self.player.shoot_timer >= weapon.cooldown:
                    self.player.shoot_timer = 0
                    self.player.animations.trigger_shoot()
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

        for enemy in self.enemies:
            enemy.update(dt, self.player.pos, self.walls)

            bullet = enemy.shoot(self.player.pos)
            if bullet:
                self.enemy_bullets.add(bullet)
                self.all_sprites.add(bullet)

        for bullet in list(self.player_bullets):
            bullet.update(dt)

            if pygame.sprite.spritecollide(bullet, self.walls, False):
                bullet.kill()
                continue

            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            if hit_enemies:
                bullet.kill()
                for enemy in hit_enemies:
                    if enemy.take_damage(bullet.damage):
                        self._on_enemy_killed(enemy)
                        enemy.kill()

        for bullet in list(self.enemy_bullets):
            bullet.update(dt)

            if pygame.sprite.spritecollide(bullet, self.walls, False):
                bullet.kill()
                continue

            if pygame.sprite.collide_rect(bullet, self.player):
                bullet.kill()
                if self.player.take_damage(bullet.damage):
                    self.game_over = True
                    if self.player_data:
                        self.player_data.record_death()

        for health_pack in self.health_packs:
            health_pack.update(dt)

        collected_packs = pygame.sprite.spritecollide(self.player, self.health_packs, True)
        for pack in collected_packs:
            self._on_health_pack_collected(pack)

        self._update_gold_notifications(dt)
        self._update_heal_notifications(dt)

        if len(self.enemies) == 0 and not self.victory:
            self.victory = True
            self._on_level_complete()

    def _on_health_pack_collected(self, pack):
        """Appelé quand le joueur ramasse un pack de vie"""
        old_health = self.player.health
        self.player.health = min(self.player.max_health, self.player.health + pack.heal_amount)
        healed = self.player.health - old_health
        
        if healed > 0:
            sound = get_powerup_sound()
        if sound:
            sound.play()
        
            screen_pos = self.camera.apply_pos((self.player.pos.x, self.player.pos.y - 30))
            self.heal_notifications.append({
                'text': f'+{healed} HP',
                'pos': list(screen_pos),
                'timer': 1.0,
                'alpha': 255
            })

    def _update_heal_notifications(self, dt):
        """Met à jour les notifications de soin"""
        for notif in self.heal_notifications[:]:
            notif['timer'] -= dt
            notif['pos'][1] -= 50 * dt
            notif['alpha'] = int(255 * (notif['timer'] / 1.0))

            if notif['timer'] <= 0:
                self.heal_notifications.remove(notif)
    def draw(self):
        """Dessine tous les éléments du jeu"""
        self.screen.fill((40, 40, 45))

        self._draw_exterior_ground()

        for decoration in self.decorations:
            screen_rect = self.camera.apply(decoration)
            if screen_rect.right > 0 and screen_rect.left < self.screen_width and \
               screen_rect.bottom > 0 and screen_rect.top < self.screen_height:
                self.screen.blit(decoration.image, screen_rect)

        for health_pack in self.health_packs:
            screen_rect = self.camera.apply(health_pack)
            if screen_rect.right > 0 and screen_rect.left < self.screen_width and \
               screen_rect.bottom > 0 and screen_rect.top < self.screen_height:
                self.screen.blit(health_pack.image, screen_rect)

        for sprite in self.all_sprites:
            screen_rect = self.camera.apply(sprite)
            if screen_rect.right > 0 and screen_rect.left < self.screen_width and \
               screen_rect.bottom > 0 and screen_rect.top < self.screen_height:
                self.screen.blit(sprite.image, screen_rect)

        for enemy in self.enemies:
            enemy.draw_health_bar(self.screen, self.camera)

        self._draw_hud()
        self._draw_heal_notifications()

        if self.victory:
            self._draw_victory()

    def _draw_heal_notifications(self):
        """Dessine les notifications de soin"""
        for notif in self.heal_notifications:
            font = pygame.font.Font(None, 28)
            text = font.render(notif['text'], True, (100, 255, 100))
            text.set_alpha(notif['alpha'])
            self.screen.blit(text, notif['pos'])

    def _draw_exterior_ground(self):
        """Dessine le sol des zones extérieures"""
        ground_rect = pygame.Rect(0, 0, self.current_map.map_width, self.current_map.map_height)
        screen_rect = self.camera.apply_rect(ground_rect)
        
        if hasattr(self.current_map, 'ground_image') and self.current_map.ground_image:
            tile_width = self.current_map.ground_image.get_width()
            tile_height = self.current_map.ground_image.get_height()
            
            for x in range(0, self.current_map.map_width, tile_width):
                for y in range(0, self.current_map.map_height, tile_height):
                    tile_rect = pygame.Rect(x, y, tile_width, tile_height)
                    screen_tile_rect = self.camera.apply_rect(tile_rect)
                    if screen_tile_rect.colliderect(pygame.Rect(0, 0, self.screen_width, self.screen_height)):
                        self.screen.blit(self.current_map.ground_image, screen_tile_rect)
        elif hasattr(self.current_map, 'ground_color'):
            pygame.draw.rect(self.screen, self.current_map.ground_color, screen_rect)
        
        if hasattr(self.current_map, 'exterior_zones'):
            for zone_rect, color in self.current_map.exterior_zones:
                screen_rect = self.camera.apply_rect(zone_rect)
                if screen_rect.right > 0 and screen_rect.left < self.screen_width and \
                   screen_rect.bottom > 0 and screen_rect.top < self.screen_height:
                    pygame.draw.rect(self.screen, color, screen_rect)

    def _draw_hud(self):
        """Dessine l'interface utilisateur"""
        hud_bg = pygame.Surface((220, 200))
        hud_bg.set_alpha(180)
        hud_bg.fill((0, 0, 0))
        self.screen.blit(hud_bg, (5, 5))

        level_name = self.level_config.get("name", "Mission")
        level_text = self.small_font.render(level_name, True, (255, 215, 0))
        self.screen.blit(level_text, (10, 10))

        health_text = self.font.render(f"HP: {self.player.health}/{self.player.max_health}", 
                                       True, (255, 255, 255))
        self.screen.blit(health_text, (10, 35))

        enemies_text = self.font.render(f"Ennemis: {len(self.enemies)}", 
                                       True, (255, 255, 255))
        self.screen.blit(enemies_text, (10, 70))

        gold_text = self.font.render(f"$ +{self.gold_earned}", True, (255, 215, 0))
        self.screen.blit(gold_text, (10, 100))

        if self.player_data:
            total_gold = self.small_font.render(f"Total: ${self.player_data.gold + self.gold_earned}", 
                                                True, (200, 180, 100))
            self.screen.blit(total_gold, (10, 125))

        bar_width = 200
        bar_height = 20
        fill = (self.player.health / self.player.max_health) * bar_width
        fill = max(0, fill)
        outline_rect = pygame.Rect(10, 150, bar_width, bar_height)
        fill_rect = pygame.Rect(10, 150, fill, bar_height)

        if self.player.health > 60:
            color = (0, 255, 0)
        elif self.player.health > 30:
            color = (255, 255, 0)
        else:
            color = (255, 0, 0)

        pygame.draw.rect(self.screen, color, fill_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), outline_rect, 2)

        weapon = self.player.current_weapon
        weapon_text = self.small_font.render(f"Arme: {weapon.name}", True, (255, 200, 0))
        self.screen.blit(weapon_text, (10, 177))

        self._draw_gold_notifications()
        self._draw_minimap()

    def _draw_minimap(self):
        """Dessine une mini-carte"""
        minimap_width = 150
        minimap_height = 100
        minimap_x = self.screen_width - minimap_width - 10
        minimap_y = 10

        minimap = pygame.Surface((minimap_width, minimap_height))
        minimap.set_alpha(200)
        minimap.fill((20, 20, 20))

        scale_x = minimap_width / self.current_map.map_width
        scale_y = minimap_height / self.current_map.map_height

        for wall in self.walls:
            x = int(wall.rect.x * scale_x)
            y = int(wall.rect.y * scale_y)
            w = max(1, int(wall.rect.width * scale_x))
            h = max(1, int(wall.rect.height * scale_y))
            pygame.draw.rect(minimap, (80, 80, 80), (x, y, w, h))

        for pack in self.health_packs:
            x = int(pack.pos.x * scale_x)
            y = int(pack.pos.y * scale_y)
            pygame.draw.circle(minimap, (255, 150, 150), (x, y), 2)

        for enemy in self.enemies:
            x = int(enemy.pos.x * scale_x)
            y = int(enemy.pos.y * scale_y)
            if isinstance(enemy, EliteEnemy):
                pygame.draw.circle(minimap, (255, 150, 0), (x, y), 3)
            else:
                pygame.draw.circle(minimap, (255, 0, 0), (x, y), 2)

        player_x = int(self.player.pos.x * scale_x)
        player_y = int(self.player.pos.y * scale_y)
        pygame.draw.circle(minimap, (0, 255, 0), (player_x, player_y), 3)

        cam_x = int(self.camera.x * scale_x)
        cam_y = int(self.camera.y * scale_y)
        cam_w = int(self.screen_width * scale_x)
        cam_h = int(self.screen_height * scale_y)
        pygame.draw.rect(minimap, (255, 255, 255), (cam_x, cam_y, cam_w, cam_h), 1)

        self.screen.blit(minimap, (minimap_x, minimap_y))
        pygame.draw.rect(self.screen, (100, 100, 100), 
                        (minimap_x, minimap_y, minimap_width, minimap_height), 2)

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
        self.all_sprites.empty()
        self.enemies.empty()
        self.player_bullets.empty()
        self.enemy_bullets.empty()
        self.walls.empty()
        self.decorations.empty()
        self.health_packs.empty()

        if self.game_over and self.player_data:
            self.player_data.gold += self.gold_earned // 2

        self.kills = 0
        self.gold_earned = 0
        self.gold_notifications = []
        self.heal_notifications = []

        level_manager = LevelManager(self.screen_width, self.screen_height)
        self.current_map = level_manager.create_level(self.level_config)

        self.walls.add(self.current_map.walls)
        self.all_sprites.add(self.current_map.walls)
        self.decorations.add(self.current_map.decorations)

        spawn_pos = self.current_map.get_spawn_position()
        owned_weapons = None
        if self.player_data:
            owned_weapons = self.player_data.owned_weapons
        self.player = Player(spawn_pos[0], spawn_pos[1], owned_weapons)
        self.all_sprites.add(self.player)

        enemy_count = self.level_config.get("enemies", 20)
        self._spawn_enemies(enemy_count)

        self.camera = Camera(self.screen_width, self.screen_height,
                            self.current_map.map_width, self.current_map.map_height)

        self.game_over = False
        self.victory = False

    def _on_enemy_killed(self, enemy):
        """Appelé quand un ennemi est tué"""
        self.kills += 1
        
        gold = getattr(enemy, 'gold_reward', self.gold_per_kill)
        self.gold_earned += gold

        screen_pos = self.camera.apply_pos((enemy.pos.x, enemy.pos.y))
        self.gold_notifications.append({
            'text': f'+${gold}',
            'pos': list(screen_pos),
            'timer': 1.0,
            'alpha': 255
        })

        if isinstance(enemy, EliteEnemy):
            if random.random() < self.health_pack_drop_chance:
                self._spawn_health_pack(enemy.pos.x, enemy.pos.y)

    def _on_level_complete(self):
        """Appelé quand le niveau est terminé"""
        if self.player_data:
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
            notif['pos'][1] -= 50 * dt
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

