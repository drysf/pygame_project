"""Classe principale du jeu - Gestion du gameplay et boucle principale."""
import pygame
import random
from config import GameConfig
from managers import SoundManager, Camera
from entities import Player, Enemy, Bullet, Platform, Building, PowerUp


class Game:
    """Classe principale gérant toute la logique du jeu."""
    
    def __init__(self):
        """Initialise le jeu."""
        self.sound_manager = SoundManager()
        self.state = "menu"
        self.level = 1
        self.max_level = 5
        self.score = 0
        self.high_score = 0
        
        # Groupes de sprites
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()
        
        self.player = None
        self.camera = None
        self.camera_x = 0
        self.level_length = 3000
        self.game_speed = 1.0
        
        # Initialisation de Pygame display
        self.screen = pygame.display.set_mode((GameConfig.SCREEN_WIDTH, 
                                               GameConfig.SCREEN_HEIGHT))
        pygame.display.set_caption("Bataille de Philadelphie - Révolution Américaine")
        self.clock = pygame.time.Clock()
        
        # Polices
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        
        self.setup_level()
    
    def setup_level(self):
        """Configure un niveau complet."""
        # Nettoyer tous les groupes
        self.all_sprites.empty()
        self.platforms.empty()
        self.enemies.empty()
        self.player_bullets.empty()
        self.enemy_bullets.empty()
        self.powerups.empty()
        self.buildings.empty()
        
        self.camera_x = 0
        self.level_length = 2000 + (self.level * 1000)
        self.game_speed = 1.0
        
        # Créer le joueur
        self.player = Player(100, GameConfig.SCREEN_HEIGHT - 150)
        self.player.base_speed = 5 + (self.level - 1) * 0.5
        self.all_sprites.add(self.player)
        
        # Créer la caméra
        self.camera = Camera(self.level_length)
        
        # Générer le niveau
        self._create_ground()
        self._create_buildings()
        self._create_platforms()
        self._create_enemies()
        self._create_powerups()
    
    def _create_ground(self):
        """Crée le sol du niveau."""
        for i in range(self.level_length // 300 + 1):
            ground = Platform(i * 300, GameConfig.SCREEN_HEIGHT - 50, 300, 50, "ground")
            self.platforms.add(ground)
            self.all_sprites.add(ground)
    
    def _create_buildings(self):
        """Crée les bâtiments d'arrière-plan."""
        for i in range(self.level_length // 200):
            bx = i * 200 + random.randint(-20, 20)
            bw = random.randint(80, 150)
            bh = random.randint(150, 300)
            by = GameConfig.SCREEN_HEIGHT - 50 - bh
            building = Building(bx, by, bw, bh)
            self.buildings.add(building)
    
    def _create_platforms(self):
        """Crée les plateformes organisées par sections."""
        platform_positions = []
        section_width = 350
        num_sections = self.level_length // section_width
        
        for i in range(num_sections):
            section_x = i * section_width + 200
            heights = [
                GameConfig.SCREEN_HEIGHT - 150,
                GameConfig.SCREEN_HEIGHT - 230,
                GameConfig.SCREEN_HEIGHT - 310,
                GameConfig.SCREEN_HEIGHT - 390
            ]
            
            num_platforms_in_section = random.randint(1, 2)
            used_heights = []
            
            for j in range(num_platforms_in_section):
                available_heights = [h for h in heights if h not in used_heights]
                if not available_heights:
                    break
                    
                py = random.choice(available_heights)
                used_heights.append(py)
                pw = random.randint(100, 180)
                px = section_x + random.randint(-30, 30)
                
                if px > 200 and px + pw < self.level_length - 100:
                    platform = Platform(px, py, pw, 20, "brick")
                    self.platforms.add(platform)
                    self.all_sprites.add(platform)
                    platform_positions.append((px, py, pw))
        
        # Plateformes supplémentaires
        for i in range(self.level * 2):
            attempts = 0
            while attempts < 10:
                px = random.randint(400, self.level_length - 300)
                py = random.choice([GameConfig.SCREEN_HEIGHT - 180, 
                                  GameConfig.SCREEN_HEIGHT - 260, 
                                  GameConfig.SCREEN_HEIGHT - 340])
                pw = random.randint(80, 140)
                
                collision = False
                for (old_x, old_y, old_w) in platform_positions:
                    if (abs(py - old_y) < 30 and 
                        not (px + pw < old_x or px > old_x + old_w)):
                        collision = True
                        break
                
                if not collision:
                    platform = Platform(px, py, pw, 20, "brick")
                    self.platforms.add(platform)
                    self.all_sprites.add(platform)
                    platform_positions.append((px, py, pw))
                    break
                    
                attempts += 1
    
    def _create_enemies(self):
        """Crée les ennemis du niveau."""
        num_enemies = 3 + self.level * 2
        spacing = self.level_length // (num_enemies + 1)
        
        for i in range(num_enemies):
            ex = spacing * (i + 1) + random.randint(-50, 50)
            ey = GameConfig.SCREEN_HEIGHT - 120
            
            # Types d'ennemis selon le niveau
            rand = random.random()
            if self.level >= 4 and rand < 0.1:
                enemy_type = "tank"
            elif self.level >= 3 and rand < 0.25:
                enemy_type = "commander"
            elif self.level >= 2 and rand < 0.4:
                enemy_type = "officer"
            elif rand < 0.5:
                enemy_type = "elite"
            else:
                enemy_type = "regular"
            
            enemy = Enemy(ex, ey, enemy_type)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
    
    def _create_powerups(self):
        """Crée les power-ups du niveau."""
        powerup_types = ["fire_rate", "health", "speed"]
        for i in range(2 + self.level):
            px = random.randint(300, self.level_length - 100)
            py = random.randint(GameConfig.SCREEN_HEIGHT - 300, 
                              GameConfig.SCREEN_HEIGHT - 100)
            ptype = random.choice(powerup_types)
            powerup = PowerUp(px, py, ptype)
            self.powerups.add(powerup)
            self.all_sprites.add(powerup)
    
    def handle_events(self):
        """
        Gère les événements du jeu.
        
        Returns:
            False si le jeu doit se terminer, True sinon
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.state == "menu":
                    if event.key == pygame.K_RETURN:
                        self.state = "playing"
                    elif event.key == pygame.K_ESCAPE:
                        return False
                
                elif self.state == "playing":
                    if event.key == pygame.K_SPACE:
                        self.player.jump(self.sound_manager)
                    elif event.key == pygame.K_c:
                        self.player.change_skin()
                    elif event.key == pygame.K_ESCAPE:
                        self.state = "pause"
                
                elif self.state == "pause":
                    if event.key == pygame.K_ESCAPE:
                        self.state = "playing"
                    elif event.key == pygame.K_m:
                        self.state = "menu"
                
                elif self.state == "game_over":
                    if event.key == pygame.K_RETURN:
                        self.level = 1
                        self.score = 0
                        self.setup_level()
                        self.state = "playing"
                    elif event.key == pygame.K_ESCAPE:
                        self.state = "menu"
                
                elif self.state == "level_complete":
                    if event.key == pygame.K_RETURN:
                        if self.level < self.max_level:
                            self.level += 1
                            self.setup_level()
                            self.state = "playing"
                        else:
                            self.state = "victory"
                
                elif self.state == "victory":
                    if event.key == pygame.K_RETURN:
                        self.level = 1
                        self.score = 0
                        self.setup_level()
                        self.state = "menu"
        
        return True
    
    def update(self):
        """Met à jour la logique du jeu."""
        if self.state != "playing":
            return
        
        # Contrôles du joueur
        keys = pygame.key.get_pressed()
        self.player.vel_x = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.player.vel_x = -self.player.speed * self.game_speed
            self.player.direction = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.vel_x = self.player.speed * self.game_speed
            self.player.direction = 1
        
        # Tir continu horizontal
        self.player.shoot(self.player_bullets, self.sound_manager)
        
        # Mise à jour du joueur
        self.player.update(self.platforms, self.sound_manager)
        
        # Mise à jour de la caméra
        self.camera.update(self.player.rect.centerx)
        self.camera_x = self.camera.x
        
        # Augmentation de la vitesse
        progress = self.player.rect.x / self.level_length
        self.game_speed = 1.0 + (self.level - 1) * 0.1 + progress * 0.3
        
        # Mise à jour des ennemis
        for enemy in self.enemies:
            enemy.update(self.platforms, self.player.rect.x)
            if abs(enemy.rect.x - self.player.rect.x) < 500:
                enemy.shoot(self.enemy_bullets, self.player.rect.x)
        
        # Mise à jour des projectiles et power-ups
        self.player_bullets.update()
        self.enemy_bullets.update()
        self.powerups.update()
        
        # Collisions balles joueur -> ennemis
        for bullet in self.player_bullets:
            hits = pygame.sprite.spritecollide(bullet, self.enemies, False)
            for enemy in hits:
                bullet.kill()
                if enemy.take_damage():
                    enemy.kill()
                    # Points selon le type
                    points = {
                        "regular": 100,
                        "elite": 250,
                        "officer": 400,
                        "commander": 600,
                        "tank": 800
                    }
                    self.score += points.get(enemy.enemy_type, 100)
                    self.sound_manager.play('enemy_death')
        
        # Collisions balles ennemies -> joueur
        if self.player.invincible <= 0:
            hits = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
            for hit in hits:
                self.player.take_damage(self.sound_manager)
        
        # Collisions joueur -> ennemis
        if self.player.invincible <= 0:
            hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
            for hit in hits:
                self.player.take_damage(self.sound_manager)
        
        # Collisions power-ups
        hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
        for powerup in hits:
            self.player.collect_powerup(powerup, self.sound_manager)
            self.score += 50
        
        # Vérifier game over
        if self.player.health <= 0:
            if self.score > self.high_score:
                self.high_score = self.score
            self.state = "game_over"
        
        # Vérifier fin de niveau
        if self.player.rect.x >= self.level_length - 200:
            self.score += 500 * self.level
            self.state = "level_complete"
    
    def _draw_background(self):
        """Dessine l'arrière-plan."""
        self.screen.fill(GameConfig.LIGHT_BLUE)
        
        # Nuages
        for i in range(5):
            cloud_x = (i * 300 - self.camera_x * 0.2) % (GameConfig.SCREEN_WIDTH + 200) - 100
            pygame.draw.ellipse(self.screen, GameConfig.WHITE, 
                              (cloud_x, 50 + i * 20, 100, 40))
            pygame.draw.ellipse(self.screen, GameConfig.WHITE, 
                              (cloud_x + 30, 40 + i * 20, 80, 50))
            pygame.draw.ellipse(self.screen, GameConfig.WHITE, 
                              (cloud_x + 60, 50 + i * 20, 90, 40))
        
        # Bâtiments
        for building in self.buildings:
            draw_x = building.rect.x - self.camera_x * 0.5
            if -200 < draw_x < GameConfig.SCREEN_WIDTH + 200:
                self.screen.blit(building.image, (draw_x, building.rect.y))
    
    def _draw_hud(self):
        """Dessine l'interface utilisateur."""
        # Cœurs
        for i in range(self.player.max_health):
            heart_x = 20 + i * 40
            if i < self.player.health:
                pygame.draw.circle(self.screen, GameConfig.RED, (heart_x, 30), 10)
                pygame.draw.circle(self.screen, GameConfig.RED, (heart_x + 14, 30), 10)
                pygame.draw.polygon(self.screen, GameConfig.RED, 
                                  [(heart_x - 10, 33), (heart_x + 7, 50), (heart_x + 24, 33)])
            else:
                pygame.draw.circle(self.screen, GameConfig.GRAY, (heart_x, 30), 10, 2)
                pygame.draw.circle(self.screen, GameConfig.GRAY, (heart_x + 14, 30), 10, 2)
                pygame.draw.polygon(self.screen, GameConfig.GRAY, 
                                  [(heart_x - 10, 33), (heart_x + 7, 50), (heart_x + 24, 33)], 2)
        
        # Score et niveau
        score_text = self.font_small.render(f"Score: {self.score}", True, GameConfig.BLACK)
        self.screen.blit(score_text, (GameConfig.SCREEN_WIDTH - 200, 20))
        
        level_text = self.font_small.render(f"Niveau: {self.level}/{self.max_level}", 
                                            True, GameConfig.BLACK)
        self.screen.blit(level_text, (GameConfig.SCREEN_WIDTH - 200, 50))
        
        enemies_text = self.font_small.render(f"Ennemis: {len(self.enemies)}", 
                                              True, GameConfig.BLACK)
        self.screen.blit(enemies_text, (GameConfig.SCREEN_WIDTH - 200, 80))
        
        # Power-ups actifs
        powerup_y = 80
        if self.player.fire_rate_boost > 0:
            boost_text = self.font_small.render(
                f"Cadence x2: {self.player.fire_rate_boost // 60}s", 
                True, GameConfig.YELLOW)
            self.screen.blit(boost_text, (20, powerup_y))
            powerup_y += 25
        if self.player.speed_boost > 0:
            boost_text = self.font_small.render(
                f"Vitesse +: {self.player.speed_boost // 60}s", 
                True, GameConfig.LIGHT_BLUE)
            self.screen.blit(boost_text, (20, powerup_y))
        
        # Barre de progression
        progress = min(self.player.rect.x / self.level_length, 1.0)
        bar_width, bar_height = 200, 15
        bar_x = GameConfig.SCREEN_WIDTH // 2 - bar_width // 2
        bar_y = 20
        pygame.draw.rect(self.screen, GameConfig.GRAY, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(self.screen, GameConfig.GREEN, 
                        (bar_x, bar_y, bar_width * progress, bar_height))
        pygame.draw.rect(self.screen, GameConfig.BLACK, 
                        (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Contrôles
        controls = self.font_small.render("C: Changer Skin | ESPACE: Sauter | Tir Auto", 
                                         True, GameConfig.DARK_GRAY)
        self.screen.blit(controls, (GameConfig.SCREEN_WIDTH // 2 - controls.get_width() // 2, 
                                   GameConfig.SCREEN_HEIGHT - 30))
    
    def _draw_menu(self):
        """Dessine le menu principal."""
        self.screen.fill(GameConfig.DARK_BLUE)
        
        title = self.font_large.render("Bataille de Philadelphie", True, GameConfig.YELLOW)
        subtitle = self.font_medium.render("Revolution Americaine - 1776", True, GameConfig.WHITE)
        self.screen.blit(title, (GameConfig.SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        self.screen.blit(subtitle, (GameConfig.SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 180))
        
        instructions = [
            "ENTREE - Commencer",
            "FLECHES / Q,D - Se deplacer",
            "ESPACE - Sauter",
            "C - Changer de skin",
            "ESC - Pause / Menu",
            "",
            f"Meilleur Score: {self.high_score}"
        ]
        
        for i, text in enumerate(instructions):
            color = GameConfig.YELLOW if i == 0 else GameConfig.WHITE
            rendered = self.font_small.render(text, True, color)
            self.screen.blit(rendered, (GameConfig.SCREEN_WIDTH // 2 - rendered.get_width() // 2, 
                                       300 + i * 35))
    
    def _draw_pause(self):
        """Dessine l'écran de pause."""
        overlay = pygame.Surface((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))
        overlay.fill(GameConfig.BLACK)
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font_large.render("PAUSE", True, GameConfig.WHITE)
        resume_text = self.font_small.render("ESC - Reprendre | M - Menu", True, GameConfig.WHITE)
        
        self.screen.blit(pause_text, 
                        (GameConfig.SCREEN_WIDTH // 2 - pause_text.get_width() // 2, 
                         GameConfig.SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(resume_text, 
                        (GameConfig.SCREEN_WIDTH // 2 - resume_text.get_width() // 2, 
                         GameConfig.SCREEN_HEIGHT // 2 + 20))
    
    def _draw_game_over(self):
        """Dessine l'écran de game over."""
        self.screen.fill(GameConfig.DARK_GRAY)
        
        game_over = self.font_large.render("DEFAITE", True, GameConfig.RED)
        score_text = self.font_medium.render(f"Score Final: {self.score}", True, GameConfig.WHITE)
        high_score = self.font_small.render(f"Meilleur Score: {self.high_score}", 
                                           True, GameConfig.YELLOW)
        restart = self.font_small.render("ENTREE - Recommencer | ESC - Menu", True, GameConfig.WHITE)
        
        self.screen.blit(game_over, 
                        (GameConfig.SCREEN_WIDTH // 2 - game_over.get_width() // 2, 150))
        self.screen.blit(score_text, 
                        (GameConfig.SCREEN_WIDTH // 2 - score_text.get_width() // 2, 250))
        self.screen.blit(high_score, 
                        (GameConfig.SCREEN_WIDTH // 2 - high_score.get_width() // 2, 320))
        self.screen.blit(restart, 
                        (GameConfig.SCREEN_WIDTH // 2 - restart.get_width() // 2, 420))
    
    def _draw_level_complete(self):
        """Dessine l'écran de niveau terminé."""
        self.screen.fill(GameConfig.DARK_GREEN)
        
        complete = self.font_large.render(f"NIVEAU {self.level} TERMINE!", 
                                         True, GameConfig.YELLOW)
        score_text = self.font_medium.render(f"Score: {self.score}", True, GameConfig.WHITE)
        next_text = self.font_small.render("ENTREE - Niveau Suivant", True, GameConfig.WHITE)
        
        self.screen.blit(complete, 
                        (GameConfig.SCREEN_WIDTH // 2 - complete.get_width() // 2, 200))
        self.screen.blit(score_text, 
                        (GameConfig.SCREEN_WIDTH // 2 - score_text.get_width() // 2, 300))
        self.screen.blit(next_text, 
                        (GameConfig.SCREEN_WIDTH // 2 - next_text.get_width() // 2, 400))
    
    def _draw_victory(self):
        """Dessine l'écran de victoire."""
        self.screen.fill(GameConfig.DARK_BLUE)
        
        victory = self.font_large.render("VICTOIRE!", True, GameConfig.YELLOW)
        subtitle = self.font_medium.render("L'Independance est Declaree!", True, GameConfig.WHITE)
        score_text = self.font_medium.render(f"Score Final: {self.score}", True, GameConfig.YELLOW)
        restart = self.font_small.render("ENTREE - Menu Principal", True, GameConfig.WHITE)
        
        # Drapeau américain
        flag_x, flag_y = GameConfig.SCREEN_WIDTH // 2 - 60, 80
        for i in range(7):
            color = GameConfig.RED if i % 2 == 0 else GameConfig.WHITE
            pygame.draw.rect(self.screen, color, (flag_x, flag_y + i * 11, 120, 11))
        pygame.draw.rect(self.screen, GameConfig.DARK_BLUE, (flag_x, flag_y, 50, 44))
        
        self.screen.blit(victory, 
                        (GameConfig.SCREEN_WIDTH // 2 - victory.get_width() // 2, 200))
        self.screen.blit(subtitle, 
                        (GameConfig.SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 280))
        self.screen.blit(score_text, 
                        (GameConfig.SCREEN_WIDTH // 2 - score_text.get_width() // 2, 360))
        self.screen.blit(restart, 
                        (GameConfig.SCREEN_WIDTH // 2 - restart.get_width() // 2, 450))
    
    def draw(self):
        """Dessine le jeu selon l'état actuel."""
        if self.state == "menu":
            self._draw_menu()
        
        elif self.state == "playing":
            self._draw_background()
            
            # Plateformes
            for platform in self.platforms:
                draw_x = platform.rect.x - self.camera_x
                if -platform.rect.width < draw_x < GameConfig.SCREEN_WIDTH:
                    self.screen.blit(platform.image, (draw_x, platform.rect.y))
            
            # Power-ups
            for powerup in self.powerups:
                draw_x = powerup.rect.x - self.camera_x
                if -50 < draw_x < GameConfig.SCREEN_WIDTH + 50:
                    self.screen.blit(powerup.image, (draw_x, powerup.rect.y))
            
            # Ennemis avec barres de vie
            for enemy in self.enemies:
                draw_x = enemy.rect.x - self.camera_x
                if -enemy.rect.width < draw_x < GameConfig.SCREEN_WIDTH:
                    self.screen.blit(enemy.image, (draw_x, enemy.rect.y))
                    
                    # Barre de vie pour ennemis forts
                    if enemy.max_health > 3:
                        bar_width = enemy.width
                        bar_height = 5
                        bar_x = draw_x
                        bar_y = enemy.rect.y - 10
                        
                        pygame.draw.rect(self.screen, GameConfig.RED, 
                                       (bar_x, bar_y, bar_width, bar_height))
                        health_width = (enemy.health / enemy.max_health) * bar_width
                        pygame.draw.rect(self.screen, GameConfig.GREEN, 
                                       (bar_x, bar_y, health_width, bar_height))
                        pygame.draw.rect(self.screen, GameConfig.BLACK, 
                                       (bar_x, bar_y, bar_width, bar_height), 1)
            
            # Joueur (clignotement si invincible)
            player_x = self.player.rect.x - self.camera_x
            if self.player.invincible % 10 < 5:
                self.screen.blit(self.player.image, (player_x, self.player.rect.y))
            
            # Projectiles
            for bullet in self.player_bullets:
                draw_x = bullet.rect.x - self.camera_x
                if 0 < draw_x < GameConfig.SCREEN_WIDTH:
                    self.screen.blit(bullet.image, (draw_x, bullet.rect.y))
            
            for bullet in self.enemy_bullets:
                draw_x = bullet.rect.x - self.camera_x
                if 0 < draw_x < GameConfig.SCREEN_WIDTH:
                    self.screen.blit(bullet.image, (draw_x, bullet.rect.y))
            
            self._draw_hud()
        
        elif self.state == "pause":
            self._draw_background()
            for platform in self.platforms:
                draw_x = platform.rect.x - self.camera_x
                if -platform.rect.width < draw_x < GameConfig.SCREEN_WIDTH:
                    self.screen.blit(platform.image, (draw_x, platform.rect.y))
            player_x = self.player.rect.x - self.camera_x
            self.screen.blit(self.player.image, (player_x, self.player.rect.y))
            self._draw_hud()
            self._draw_pause()
        
        elif self.state == "game_over":
            self._draw_game_over()
        
        elif self.state == "level_complete":
            self._draw_level_complete()
        
        elif self.state == "victory":
            self._draw_victory()
        
        pygame.display.flip()
    
    def run(self):
        """Boucle principale du jeu."""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(GameConfig.FPS)
        
        pygame.quit()
