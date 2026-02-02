"""
Projet PyGame - Groupe 9
Jeu de plateforme 2D : Soldat Américain vs Soldats Anglais à Philadelphie
Architecture Orientée Objet
"""

import pygame
import random
import math
from abc import ABC, abstractmethod

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()


class GameConfig:
    """Configuration globale du jeu - Pattern Singleton"""
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600
    FPS = 60
    
    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    BROWN = (139, 69, 19)
    GRAY = (128, 128, 128)
    DARK_GRAY = (64, 64, 64)
    LIGHT_BLUE = (135, 206, 235)
    DARK_BLUE = (0, 0, 139)
    BRICK_RED = (178, 34, 34)
    CREAM = (255, 253, 208)
    DARK_GREEN = (0, 100, 0)


class Display:
    """Gestionnaire d'affichage - Encapsulation de l'écran et des polices"""
    def __init__(self):
        self.screen = pygame.display.set_mode((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))
        pygame.display.set_caption("Bataille de Philadelphie - Révolution Américaine")
        self.clock = pygame.time.Clock()
        
        # Polices
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
    
    def get_screen(self):
        return self.screen
    
    def tick(self, fps):
        self.clock.tick(fps)
    
    def flip(self):
        pygame.display.flip()


class Camera:
    """Gestion de la caméra pour le défilement"""
    def __init__(self, level_length):
        self.x = 0
        self.level_length = level_length
    
    def update(self, target_x):
        """Met à jour la position de la caméra pour suivre le joueur"""
        target_camera = target_x - GameConfig.SCREEN_WIDTH // 3
        self.x = max(0, min(target_camera, self.level_length - GameConfig.SCREEN_WIDTH))
    
    def apply(self, rect):
        """Applique l'offset de la caméra à un rectangle"""
        return rect.x - self.x, rect.y
    
    def apply_x(self, x):
        """Applique l'offset de la caméra à une coordonnée x"""
        return x - self.x


class GameState(ABC):
    """Classe abstraite pour les différents états du jeu - Pattern State"""
    def __init__(self, game):
        self.game = game
    
    @abstractmethod
    def handle_events(self, events):
        """Gère les événements pour cet état"""
        pass
    
    @abstractmethod
    def update(self):
        """Met à jour la logique pour cet état"""
        pass
    
    @abstractmethod
    def draw(self, display):
        """Dessine cet état"""
        pass


class MenuState(GameState):
    """État du menu principal"""
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return PlayingState(self.game)
                elif event.key == pygame.K_ESCAPE:
                    return None  # Quitter
        return self
    
    def update(self):
        pass
    
    def draw(self, display):
        screen = display.get_screen()
        screen.fill(GameConfig.DARK_BLUE)
        
        title = display.font_large.render("Bataille de Philadelphie", True, GameConfig.YELLOW)
        subtitle = display.font_medium.render("Revolution Americaine - 1776", True, GameConfig.WHITE)
        screen.blit(title, (GameConfig.SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        screen.blit(subtitle, (GameConfig.SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 180))
        
        instructions = [
            "ENTREE - Commencer",
            "FLECHES / Q,D - Se deplacer",
            "ESPACE - Sauter",
            "C - Changer de skin",
            "ESC - Pause / Menu",
            "",
            f"Meilleur Score: {self.game.high_score}"
        ]
        
        for i, text in enumerate(instructions):
            color = GameConfig.YELLOW if i == 0 else GameConfig.WHITE
            rendered = display.font_small.render(text, True, color)
            screen.blit(rendered, (GameConfig.SCREEN_WIDTH // 2 - rendered.get_width() // 2, 300 + i * 35))


class PauseState(GameState):
    """État de pause"""
    def __init__(self, game, playing_state):
        super().__init__(game)
        self.playing_state = playing_state
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return self.playing_state
                elif event.key == pygame.K_m:
                    return MenuState(self.game)
        return self
    
    def update(self):
        pass
    
    def draw(self, display):
        # Dessiner d'abord l'état de jeu
        self.playing_state.draw(display)
        
        # Assombrir l'écran
        screen = display.get_screen()
        overlay = pygame.Surface((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))
        overlay.fill(GameConfig.BLACK)
        overlay.set_alpha(128)
        screen.blit(overlay, (0, 0))
        
        pause_text = display.font_large.render("PAUSE", True, GameConfig.WHITE)
        resume_text = display.font_small.render("ESC - Reprendre | M - Menu", True, GameConfig.WHITE)
        
        screen.blit(pause_text, (GameConfig.SCREEN_WIDTH // 2 - pause_text.get_width() // 2, GameConfig.SCREEN_HEIGHT // 2 - 50))
        screen.blit(resume_text, (GameConfig.SCREEN_WIDTH // 2 - resume_text.get_width() // 2, GameConfig.SCREEN_HEIGHT // 2 + 20))


class GameOverState(GameState):
    """État de game over"""
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.reset()
                    return PlayingState(self.game)
                elif event.key == pygame.K_ESCAPE:
                    return MenuState(self.game)
        return self
    
    def update(self):
        pass
    
    def draw(self, display):
        screen = display.get_screen()
        screen.fill(GameConfig.DARK_GRAY)
        
        game_over = display.font_large.render("DEFAITE", True, GameConfig.RED)
        score_text = display.font_medium.render(f"Score Final: {self.game.score}", True, GameConfig.WHITE)
        high_score = display.font_small.render(f"Meilleur Score: {self.game.high_score}", True, GameConfig.YELLOW)
        restart = display.font_small.render("ENTREE - Recommencer | ESC - Menu", True, GameConfig.WHITE)
        
        screen.blit(game_over, (GameConfig.SCREEN_WIDTH // 2 - game_over.get_width() // 2, 150))
        screen.blit(score_text, (GameConfig.SCREEN_WIDTH // 2 - score_text.get_width() // 2, 250))
        screen.blit(high_score, (GameConfig.SCREEN_WIDTH // 2 - high_score.get_width() // 2, 320))
        screen.blit(restart, (GameConfig.SCREEN_WIDTH // 2 - restart.get_width() // 2, 420))


class LevelCompleteState(GameState):
    """État de niveau complété"""
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game.level < self.game.max_level:
                        self.game.level += 1
                        return PlayingState(self.game)
                    else:
                        return VictoryState(self.game)
        return self
    
    def update(self):
        pass
    
    def draw(self, display):
        screen = display.get_screen()
        screen.fill(GameConfig.DARK_GREEN)
        
        complete = display.font_large.render(f"NIVEAU {self.game.level} TERMINE!", True, GameConfig.YELLOW)
        score_text = display.font_medium.render(f"Score: {self.game.score}", True, GameConfig.WHITE)
        next_text = display.font_small.render("ENTREE - Niveau Suivant", True, GameConfig.WHITE)
        
        screen.blit(complete, (GameConfig.SCREEN_WIDTH // 2 - complete.get_width() // 2, 200))
        screen.blit(score_text, (GameConfig.SCREEN_WIDTH // 2 - score_text.get_width() // 2, 300))
        screen.blit(next_text, (GameConfig.SCREEN_WIDTH // 2 - next_text.get_width() // 2, 400))


class VictoryState(GameState):
    """État de victoire finale"""
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.reset()
                    return MenuState(self.game)
        return self
    
    def update(self):
        pass
    
    def draw(self, display):
        screen = display.get_screen()
        screen.fill(GameConfig.DARK_BLUE)
        
        victory = display.font_large.render("VICTOIRE!", True, GameConfig.YELLOW)
        subtitle = display.font_medium.render("L'Independance est Declaree!", True, GameConfig.WHITE)
        score_text = display.font_medium.render(f"Score Final: {self.game.score}", True, GameConfig.YELLOW)
        restart = display.font_small.render("ENTREE - Menu Principal", True, GameConfig.WHITE)
        
        # Drapeau américain
        flag_x, flag_y = GameConfig.SCREEN_WIDTH // 2 - 60, 80
        for i in range(7):
            color = GameConfig.RED if i % 2 == 0 else GameConfig.WHITE
            pygame.draw.rect(screen, color, (flag_x, flag_y + i * 11, 120, 11))
        pygame.draw.rect(screen, GameConfig.DARK_BLUE, (flag_x, flag_y, 50, 44))
        
        screen.blit(victory, (GameConfig.SCREEN_WIDTH // 2 - victory.get_width() // 2, 200))
        screen.blit(subtitle, (GameConfig.SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 280))
        screen.blit(score_text, (GameConfig.SCREEN_WIDTH // 2 - score_text.get_width() // 2, 360))
        screen.blit(restart, (GameConfig.SCREEN_WIDTH // 2 - restart.get_width() // 2, 450))


class LevelManager:
    """Gestionnaire de niveaux - Génération et gestion des éléments du niveau"""
    def __init__(self, level, score):
        self.level = level
        self.level_length = 2000 + (level * 1000)
        self.game_speed = 1.0
        
        # Groupes de sprites
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()
        
        self.player = None
        self.camera = Camera(self.level_length)
        
        self._generate_level()
    
    def _generate_level(self):
        """Génère tous les éléments du niveau"""
        self._create_player()
        self._create_ground()
        self._create_buildings()
        self._create_platforms()
        self._create_enemies()
        self._create_powerups()
    
    def _create_player(self):
        """Crée le joueur"""
        self.player = Player(100, GameConfig.SCREEN_HEIGHT - 150)
        self.player.base_speed = 5 + (self.level - 1) * 0.5
        self.all_sprites.add(self.player)
    
    def _create_ground(self):
        """Crée le sol"""
        for i in range(self.level_length // 300 + 1):
            ground = Platform(i * 300, GameConfig.SCREEN_HEIGHT - 50, 300, 50, "ground")
            self.platforms.add(ground)
            self.all_sprites.add(ground)
    
    def _create_buildings(self):
        """Crée les bâtiments d'arrière-plan"""
        for i in range(self.level_length // 200):
            bx = i * 200 + random.randint(-20, 20)
            bw = random.randint(80, 150)
            bh = random.randint(150, 300)
            by = GameConfig.SCREEN_HEIGHT - 50 - bh
            building = Building(bx, by, bw, bh)
            self.buildings.add(building)
    
    def _create_platforms(self):
        """Crée les plateformes avec un système sans chevauchement"""
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
                py = random.choice([GameConfig.SCREEN_HEIGHT - 180, GameConfig.SCREEN_HEIGHT - 260, GameConfig.SCREEN_HEIGHT - 340])
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
        """Crée les ennemis"""
        num_enemies = 3 + self.level * 2
        spacing = self.level_length // (num_enemies + 1)
        
        for i in range(num_enemies):
            ex = spacing * (i + 1) + random.randint(-50, 50)
            ey = GameConfig.SCREEN_HEIGHT - 120
            
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
        """Crée les power-ups"""
        powerup_types = ["fire_rate", "health", "speed"]
        for i in range(2 + self.level):
            px = random.randint(300, self.level_length - 100)
            py = random.randint(GameConfig.SCREEN_HEIGHT - 300, GameConfig.SCREEN_HEIGHT - 100)
            ptype = random.choice(powerup_types)
            powerup = PowerUp(px, py, ptype)
            self.powerups.add(powerup)
            self.all_sprites.add(powerup)
    
    def update_game_speed(self):
        """Met à jour la vitesse du jeu selon la progression"""
        progress = self.player.rect.x / self.level_length
        self.game_speed = 1.0 + (self.level - 1) * 0.1 + progress * 0.3
        return self.game_speed
    
    def is_level_complete(self):
        """Vérifie si le niveau est terminé"""
        return self.player.rect.x >= self.level_length - 200


class SoundManager:
    """Gestionnaire de sons"""
    def __init__(self):
        self.sounds = {}
        self.create_sounds()
    
    def create_sounds(self):
        """Crée des sons synthétiques"""
        try:
            import array
            # Son de tir
            shoot_sound = pygame.mixer.Sound(buffer=self.generate_shoot_sound())
            shoot_sound.set_volume(0.3)
            self.sounds['shoot'] = shoot_sound
            
            # Son de saut
            jump_sound = pygame.mixer.Sound(buffer=self.generate_jump_sound())
            jump_sound.set_volume(0.4)
            self.sounds['jump'] = jump_sound
            
            # Son de pas/course
            step_sound = pygame.mixer.Sound(buffer=self.generate_step_sound())
            step_sound.set_volume(0.2)
            self.sounds['step'] = step_sound
            
            # Son de dégâts
            hit_sound = pygame.mixer.Sound(buffer=self.generate_hit_sound())
            hit_sound.set_volume(0.5)
            self.sounds['hit'] = hit_sound
            
            # Son de powerup
            powerup_sound = pygame.mixer.Sound(buffer=self.generate_powerup_sound())
            powerup_sound.set_volume(0.5)
            self.sounds['powerup'] = powerup_sound
            
            # Son de mort ennemi
            enemy_death = pygame.mixer.Sound(buffer=self.generate_enemy_death_sound())
            enemy_death.set_volume(0.4)
            self.sounds['enemy_death'] = enemy_death
            
        except Exception as e:
            print(f"Erreur lors de la création des sons: {e}")
    
    def generate_shoot_sound(self):
        """Génère un son de tir"""
        import array
        sample_rate = 22050
        duration = 0.1
        samples = int(sample_rate * duration)
        buf = array.array('h')
        for i in range(samples):
            t = i / sample_rate
            freq = 800 - (t * 5000)
            value = int(32767 * 0.5 * math.sin(2 * math.pi * freq * t) * (1 - t/duration))
            buf.append(value)
        return buf.tobytes()
    
    def generate_jump_sound(self):
        """Génère un son de saut"""
        import array
        sample_rate = 22050
        duration = 0.15
        samples = int(sample_rate * duration)
        buf = array.array('h')
        for i in range(samples):
            t = i / sample_rate
            freq = 200 + (t * 600)
            value = int(32767 * 0.4 * math.sin(2 * math.pi * freq * t) * (1 - t/duration))
            buf.append(value)
        return buf.tobytes()
    
    def generate_step_sound(self):
        """Génère un son de pas"""
        import array
        sample_rate = 22050
        duration = 0.08
        samples = int(sample_rate * duration)
        buf = array.array('h')
        for i in range(samples):
            t = i / sample_rate
            noise = random.randint(-8000, 8000)
            value = int(noise * (1 - t/duration))
            buf.append(max(-32767, min(32767, value)))
        return buf.tobytes()
    
    def generate_hit_sound(self):
        """Génère un son de dégâts"""
        import array
        sample_rate = 22050
        duration = 0.2
        samples = int(sample_rate * duration)
        buf = array.array('h')
        for i in range(samples):
            t = i / sample_rate
            freq = 150
            noise = random.randint(-5000, 5000)
            value = int((32767 * 0.3 * math.sin(2 * math.pi * freq * t) + noise) * (1 - t/duration))
            buf.append(max(-32767, min(32767, value)))
        return buf.tobytes()
    
    def generate_powerup_sound(self):
        """Génère un son de powerup"""
        import array
        sample_rate = 22050
        duration = 0.3
        samples = int(sample_rate * duration)
        buf = array.array('h')
        for i in range(samples):
            t = i / sample_rate
            freq = 400 + (t * 400)
            value = int(32767 * 0.4 * math.sin(2 * math.pi * freq * t))
            buf.append(value)
        return buf.tobytes()
    
    def generate_enemy_death_sound(self):
        """Génère un son de mort ennemi"""
        import array
        sample_rate = 22050
        duration = 0.25
        samples = int(sample_rate * duration)
        buf = array.array('h')
        for i in range(samples):
            t = i / sample_rate
            freq = 400 - (t * 300)
            value = int(32767 * 0.4 * math.sin(2 * math.pi * freq * t) * (1 - t/duration))
            buf.append(value)
        return buf.tobytes()
    
    def play(self, sound_name):
        """Joue un son"""
        if sound_name in self.sounds:
            self.sounds[sound_name].play()


class Bullet(pygame.sprite.Sprite):
    """Classe pour les balles"""
    def __init__(self, x, y, direction, is_player_bullet=True):
        super().__init__()
        self.image = pygame.Surface((12, 4))
        color = YELLOW if is_player_bullet else RED
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.direction = direction
        self.speed = 15 if is_player_bullet else 8
        self.is_player_bullet = is_player_bullet
    
    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right < -100 or self.rect.left > SCREEN_WIDTH + 1100:
            self.kill()


class Platform(pygame.sprite.Sprite):
    """Classe pour les plateformes"""
    def __init__(self, x, y, width, height, platform_type="ground"):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.platform_type = platform_type
        
        if platform_type == "ground":
            self.draw_cobblestone(width, height)
        elif platform_type == "brick":
            self.draw_brick(width, height)
        else:
            self.image.fill(BROWN)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw_cobblestone(self, width, height):
        """Dessine des pavés"""
        self.image.fill(GRAY)
        for i in range(0, width, 30):
            for j in range(0, height, 20):
                offset = 15 if (j // 20) % 2 else 0
                pygame.draw.rect(self.image, DARK_GRAY, (i + offset, j, 28, 18), 1)
    
    def draw_brick(self, width, height):
        """Dessine des briques"""
        self.image.fill(BRICK_RED)
        for i in range(0, width, 40):
            for j in range(0, height, 20):
                offset = 20 if (j // 20) % 2 else 0
                pygame.draw.rect(self.image, DARK_GRAY, (i + offset, j, 38, 18), 1)


class Building(pygame.sprite.Sprite):
    """Bâtiments de Philadelphie en arrière-plan"""
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.draw_building(width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw_building(self, width, height):
        """Dessine un bâtiment colonial"""
        colors = [BRICK_RED, CREAM, (200, 180, 160)]
        color = random.choice(colors)
        pygame.draw.rect(self.image, color, (0, 20, width, height - 20))
        
        # Toit
        pygame.draw.polygon(self.image, DARK_GRAY, 
                          [(0, 20), (width // 2, 0), (width, 20)])
        
        # Fenêtres
        window_width = width // 5
        window_height = height // 6
        for row in range(2):
            for col in range(2):
                wx = 10 + col * (width // 2)
                wy = 40 + row * (height // 3)
                if wx + window_width < width and wy + window_height < height:
                    pygame.draw.rect(self.image, LIGHT_BLUE, (wx, wy, window_width, window_height))
                    pygame.draw.rect(self.image, BROWN, (wx, wy, window_width, window_height), 2)
                    pygame.draw.line(self.image, BROWN, (wx + window_width//2, wy), 
                                   (wx + window_width//2, wy + window_height), 2)
                    pygame.draw.line(self.image, BROWN, (wx, wy + window_height//2), 
                                   (wx + window_width, wy + window_height//2), 2)
        
        # Porte
        door_width = width // 4
        door_height = height // 3
        pygame.draw.rect(self.image, BROWN, 
                        (width//2 - door_width//2, height - door_height, door_width, door_height))


class PowerUp(pygame.sprite.Sprite):
    """Classe pour les power-ups"""
    def __init__(self, x, y, powerup_type="fire_rate"):
        super().__init__()
        self.powerup_type = powerup_type
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        
        if powerup_type == "fire_rate":
            self.draw_star(YELLOW)
        elif powerup_type == "health":
            self.draw_heart(RED)
        elif powerup_type == "speed":
            self.draw_lightning(LIGHT_BLUE)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.float_offset = 0
        self.base_y = y
    
    def draw_star(self, color):
        """Dessine une étoile"""
        center = 15
        points = []
        for i in range(5):
            angle = math.radians(i * 72 - 90)
            points.append((center + 12 * math.cos(angle), center + 12 * math.sin(angle)))
            angle = math.radians(i * 72 - 90 + 36)
            points.append((center + 5 * math.cos(angle), center + 5 * math.sin(angle)))
        pygame.draw.polygon(self.image, color, points)
        pygame.draw.polygon(self.image, ORANGE, points, 2)
    
    def draw_heart(self, color):
        """Dessine un coeur"""
        pygame.draw.circle(self.image, color, (10, 12), 7)
        pygame.draw.circle(self.image, color, (20, 12), 7)
        pygame.draw.polygon(self.image, color, [(3, 14), (15, 27), (27, 14)])
    
    def draw_lightning(self, color):
        """Dessine un éclair"""
        points = [(15, 2), (8, 14), (13, 14), (10, 28), (22, 12), (16, 12), (20, 2)]
        pygame.draw.polygon(self.image, color, points)
        pygame.draw.polygon(self.image, BLUE, points, 2)
    
    def update(self):
        """Animation flottante"""
        self.float_offset += 0.1
        self.rect.y = self.base_y + math.sin(self.float_offset) * 5


class Player(pygame.sprite.Sprite):
    """Classe du joueur - Soldat Américain"""
    def __init__(self, x, y):
        super().__init__()
        self.skins = ["default", "general", "minuteman"]
        self.skin_index = 0
        
        self.width = 40
        self.height = 60
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.draw_soldier()
        
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
    
    def draw_soldier(self):
        """Dessine le soldat américain"""
        self.image.fill((0, 0, 0, 0))
        
        skin = self.skins[self.skin_index]
        if skin == "general":
            uniform_color = DARK_BLUE
            accent_color = YELLOW
        elif skin == "minuteman":
            uniform_color = BROWN
            accent_color = CREAM
        else:
            uniform_color = (0, 0, 139)
            accent_color = (255, 215, 0)
        
        # Corps
        pygame.draw.rect(self.image, uniform_color, (10, 20, 20, 25))
        
        # Jambes
        pygame.draw.rect(self.image, CREAM, (12, 45, 7, 15))
        pygame.draw.rect(self.image, CREAM, (21, 45, 7, 15))
        
        # Bottes
        pygame.draw.rect(self.image, BLACK, (11, 55, 8, 5))
        pygame.draw.rect(self.image, BLACK, (20, 55, 8, 5))
        
        # Tête
        pygame.draw.circle(self.image, (255, 220, 180), (20, 12), 10)
        
        # Chapeau tricorne
        pygame.draw.rect(self.image, BLACK, (8, 2, 24, 6))
        pygame.draw.polygon(self.image, BLACK, [(10, 2), (20, -3), (30, 2)])
        
        # Yeux
        pygame.draw.circle(self.image, BLACK, (17, 11), 2)
        pygame.draw.circle(self.image, BLACK, (23, 11), 2)
        
        # Boutons
        for i in range(3):
            pygame.draw.circle(self.image, accent_color, (20, 25 + i * 6), 2)
        
        # Mousquet
        pygame.draw.rect(self.image, uniform_color, (28, 22, 8, 5))
        pygame.draw.rect(self.image, BROWN, (32, 20, 8, 3))
    
    def change_skin(self):
        """Change le skin du soldat"""
        self.skin_index = (self.skin_index + 1) % len(self.skins)
        self.draw_soldier()
    
    def update(self, platforms, sound_manager):
        # Power-ups
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
        
        # Limites (seulement à gauche, pas de limite à droite pour avancer dans le niveau)
        if self.rect.left < 0:
            self.rect.left = 0
        
        # Cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def jump(self, sound_manager):
        if self.on_ground:
            self.vel_y = self.jump_power
            sound_manager.play('jump')
    
    def shoot(self, bullets, sound_manager):
        if self.shoot_cooldown <= 0:
            bullet_x = self.rect.right if self.direction == 1 else self.rect.left
            bullet = Bullet(bullet_x, self.rect.centery, self.direction, True)
            bullets.add(bullet)
            self.shoot_cooldown = self.fire_rate
            sound_manager.play('shoot')
    
    def take_damage(self, sound_manager):
        if self.invincible <= 0:
            self.health -= 1
            self.invincible = 60
            sound_manager.play('hit')
            return True
        return False
    
    def collect_powerup(self, powerup, sound_manager):
        if powerup.powerup_type == "fire_rate":
            self.fire_rate_boost = 300
        elif powerup.powerup_type == "health":
            if self.health < self.max_health:
                self.health += 1
        elif powerup.powerup_type == "speed":
            self.speed_boost = 300
        sound_manager.play('powerup')


class Enemy(pygame.sprite.Sprite):
    """Classe des ennemis - Soldats Anglais"""
    def __init__(self, x, y, enemy_type="regular"):
        super().__init__()
        self.enemy_type = enemy_type
        # Taille varie selon le type
        if enemy_type == "tank":
            self.width = 55
            self.height = 70
        elif enemy_type == "commander":
            self.width = 50
            self.height = 68
        elif enemy_type == "officer":
            self.width = 45
            self.height = 65
        else:
            self.width = 40
            self.height = 60
        
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.draw_british_soldier()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Physique
        self.vel_y = 0
        self.gravity = 0.8
        self.direction = -1
        
        # Combat (différents types d'ennemis)
        if enemy_type == "tank":  # Très résistant
            self.health = 8
            self.fire_rate = 80
            self.speed = 0.5
            self.max_health = 8
        elif enemy_type == "commander":  # Boss
            self.health = 6
            self.fire_rate = 30
            self.speed = 1.5
            self.max_health = 6
        elif enemy_type == "officer":  # Fort
            self.health = 4
            self.fire_rate = 45
            self.speed = 1.2
            self.max_health = 4
        elif enemy_type == "elite":  # Moyen
            self.health = 3
            self.fire_rate = 40
            self.speed = 2
            self.max_health = 3
        else:  # Regular
            self.health = 2
            self.fire_rate = 60
            self.speed = 1
            self.max_health = 2
        
        self.shoot_cooldown = random.randint(30, 60)
        self.patrol_direction = 1
        self.patrol_distance = 0
        self.max_patrol = 100
    
    def draw_british_soldier(self):
        """Dessine un soldat britannique avec apparence unique selon le type"""
        self.image.fill((0, 0, 0, 0))
        
        center_x = self.width // 2
        
        if self.enemy_type == "tank":
            # TANK : Soldat massif avec armure
            uniform_color = (80, 0, 0)
            accent_color = (200, 200, 200)
            
            # Corps très large
            pygame.draw.rect(self.image, uniform_color, (center_x - 15, 25, 30, 30))
            # Armure argentée
            pygame.draw.rect(self.image, accent_color, (center_x - 13, 27, 26, 26))
            pygame.draw.rect(self.image, uniform_color, (center_x - 11, 29, 22, 22))
            
            # Jambes épaisses
            pygame.draw.rect(self.image, WHITE, (center_x - 12, 55, 10, 15))
            pygame.draw.rect(self.image, WHITE, (center_x + 2, 55, 10, 15))
            
            # Bottes renforcées
            pygame.draw.rect(self.image, BLACK, (center_x - 13, 65, 11, 5))
            pygame.draw.rect(self.image, BLACK, (center_x + 1, 65, 11, 5))
            
            # Tête large
            pygame.draw.circle(self.image, (255, 220, 180), (center_x, 15), 13)
            
            # Casque lourd
            pygame.draw.rect(self.image, BLACK, (center_x - 10, 0, 20, 15))
            pygame.draw.polygon(self.image, BLACK, [(center_x - 12, 14), (center_x, -5), (center_x + 12, 14)])
            pygame.draw.circle(self.image, accent_color, (center_x, 10), 3)
            
            # Yeux méchants
            pygame.draw.line(self.image, BLACK, (center_x - 6, 12), (center_x - 3, 15), 3)
            pygame.draw.line(self.image, BLACK, (center_x + 3, 15), (center_x + 6, 12), 3)
            
            # Cicatrices
            pygame.draw.line(self.image, RED, (center_x + 5, 12), (center_x + 8, 18), 2)
            
            # Mousquet lourd
            pygame.draw.rect(self.image, BROWN, (0, 28, 15, 5))
            pygame.draw.circle(self.image, DARK_GRAY, (3, 30), 4)
            
        elif self.enemy_type == "commander":
            # COMMANDER : Officier avec décorations
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
            pygame.draw.rect(self.image, WHITE, (center_x - 2, 24, 4, 28))
            pygame.draw.rect(self.image, WHITE, (center_x - 12, 35, 24, 4))
            
            # Jambes
            pygame.draw.rect(self.image, WHITE, (center_x - 10, 52, 8, 16))
            pygame.draw.rect(self.image, WHITE, (center_x + 2, 52, 8, 16))
            
            # Bottes cirées
            pygame.draw.rect(self.image, BLACK, (center_x - 11, 63, 9, 5))
            pygame.draw.rect(self.image, BLACK, (center_x + 1, 63, 9, 5))
            pygame.draw.circle(self.image, accent_color, (center_x - 6, 65), 2)
            pygame.draw.circle(self.image, accent_color, (center_x + 6, 65), 2)
            
            # Tête
            pygame.draw.circle(self.image, (255, 220, 180), (center_x, 14), 11)
            
            # Chapeau à plume
            pygame.draw.rect(self.image, BLACK, (center_x - 9, 0, 18, 10))
            pygame.draw.ellipse(self.image, BLACK, (center_x - 12, 8, 24, 5))
            # Plume rouge
            pygame.draw.ellipse(self.image, RED, (center_x + 5, -5, 8, 15))
            pygame.draw.ellipse(self.image, (200, 0, 0), (center_x + 7, -3, 4, 12))
            
            # Yeux et moustache
            pygame.draw.circle(self.image, BLACK, (center_x - 4, 13), 2)
            pygame.draw.circle(self.image, BLACK, (center_x + 4, 13), 2)
            pygame.draw.arc(self.image, BLACK, (center_x - 6, 16, 12, 6), 0, 3.14, 2)
            pygame.draw.line(self.image, BLACK, (center_x - 8, 18), (center_x - 2, 19), 2)
            pygame.draw.line(self.image, BLACK, (center_x + 2, 19), (center_x + 8, 18), 2)
            
            # Médailles
            for i in range(3):
                pygame.draw.circle(self.image, accent_color, (center_x - 8 + i * 8, 30 + i * 5), 3)
            
            # Sabre au lieu de mousquet
            pygame.draw.rect(self.image, (192, 192, 192), (2, 27, 12, 2))
            pygame.draw.circle(self.image, accent_color, (14, 28), 3)
            
        elif self.enemy_type == "officer":
            # OFFICER : Soldat avec galons
            uniform_color = (170, 0, 0)
            accent_color = (255, 223, 0)
            
            # Corps
            pygame.draw.rect(self.image, uniform_color, (center_x - 11, 23, 22, 26))
            
            # Galons sur les épaules
            for i in range(3):
                pygame.draw.rect(self.image, accent_color, (center_x - 12, 22 + i * 2, 6, 1))
                pygame.draw.rect(self.image, accent_color, (center_x + 6, 22 + i * 2, 6, 1))
            
            # Croix
            pygame.draw.rect(self.image, WHITE, (center_x - 2, 23, 4, 26))
            pygame.draw.rect(self.image, WHITE, (center_x - 11, 34, 22, 4))
            
            # Jambes
            pygame.draw.rect(self.image, WHITE, (center_x - 9, 49, 8, 16))
            pygame.draw.rect(self.image, WHITE, (center_x + 1, 49, 8, 16))
            
            # Bottes
            pygame.draw.rect(self.image, BLACK, (center_x - 10, 60, 9, 5))
            pygame.draw.rect(self.image, BLACK, (center_x, 60, 9, 5))
            
            # Tête
            pygame.draw.circle(self.image, (255, 220, 180), (center_x, 13), 10)
            
            # Chapeau officier
            pygame.draw.rect(self.image, BLACK, (center_x - 8, -1, 16, 11))
            pygame.draw.rect(self.image, BLACK, (center_x - 10, 9, 20, 3))
            pygame.draw.circle(self.image, accent_color, (center_x, 4), 2)
            
            # Yeux sévères
            pygame.draw.line(self.image, BLACK, (center_x - 5, 11), (center_x - 2, 13), 2)
            pygame.draw.line(self.image, BLACK, (center_x + 2, 13), (center_x + 5, 11), 2)
            
            # Insigne
            pygame.draw.circle(self.image, accent_color, (center_x, 28), 4)
            pygame.draw.circle(self.image, uniform_color, (center_x, 28), 2)
            
            # Mousquet
            pygame.draw.rect(self.image, BROWN, (1, 25, 10, 3))
            
        elif self.enemy_type == "elite":
            # ELITE : Soldat entraîné
            uniform_color = (150, 0, 0)
            accent_color = YELLOW
            
            # Corps athlétique
            pygame.draw.rect(self.image, uniform_color, (center_x - 10, 22, 20, 25))
            
            # Croix blanche proéminente
            pygame.draw.rect(self.image, WHITE, (center_x - 2, 22, 4, 25))
            pygame.draw.rect(self.image, WHITE, (center_x - 10, 32, 20, 5))
            
            # Jambes
            pygame.draw.rect(self.image, WHITE, (center_x - 8, 47, 7, 13))
            pygame.draw.rect(self.image, WHITE, (center_x + 1, 47, 7, 13))
            
            # Bottes
            pygame.draw.rect(self.image, BLACK, (center_x - 9, 57, 8, 3))
            pygame.draw.rect(self.image, BLACK, (center_x, 57, 8, 3))
            
            # Tête
            pygame.draw.circle(self.image, (255, 220, 180), (center_x, 12), 9)
            
            # Chapeau haut de forme
            pygame.draw.rect(self.image, BLACK, (center_x - 7, -1, 14, 11))
            pygame.draw.rect(self.image, BLACK, (center_x - 9, 9, 18, 3))
            
            # Yeux concentrés
            pygame.draw.line(self.image, BLACK, (center_x - 4, 10), (center_x - 2, 12), 2)
            pygame.draw.line(self.image, BLACK, (center_x + 2, 12), (center_x + 4, 10), 2)
            
            # Boutons dorés
            for i in range(3):
                pygame.draw.circle(self.image, accent_color, (center_x, 26 + i * 6), 2)
            
            # Mousquet
            pygame.draw.rect(self.image, BROWN, (2, 24, 9, 3))
            
        else:
            # REGULAR : Soldat standard
            uniform_color = RED
            accent_color = WHITE
            
            # Corps basique
            pygame.draw.rect(self.image, uniform_color, (center_x - 10, 20, 20, 25))
            
            # Croix blanche simple
            pygame.draw.rect(self.image, WHITE, (center_x - 2, 20, 4, 25))
            pygame.draw.rect(self.image, WHITE, (center_x - 10, 30, 20, 4))
            
            # Jambes
            pygame.draw.rect(self.image, WHITE, (center_x - 8, 45, 7, 15))
            pygame.draw.rect(self.image, WHITE, (center_x + 1, 45, 7, 15))
            
            # Bottes simples
            pygame.draw.rect(self.image, BLACK, (center_x - 9, 55, 8, 5))
            pygame.draw.rect(self.image, BLACK, (center_x, 55, 8, 5))
            
            # Tête
            pygame.draw.circle(self.image, (255, 220, 180), (center_x, 12), 10)
            
            # Chapeau basique
            pygame.draw.rect(self.image, BLACK, (center_x - 8, -2, 16, 12))
            pygame.draw.rect(self.image, BLACK, (center_x - 10, 8, 20, 3))
            
            # Yeux
            pygame.draw.line(self.image, BLACK, (center_x - 5, 9), (center_x - 2, 11), 2)
            pygame.draw.line(self.image, BLACK, (center_x + 2, 11), (center_x + 5, 9), 2)
            
            # Boutons
            for i in range(3):
                pygame.draw.circle(self.image, accent_color, (center_x, 25 + i * 6), 2)
            
            # Mousquet
            pygame.draw.rect(self.image, BROWN, (2, 22, 10, 3))
    
    def update(self, platforms, player_x):
        # Gravité
        self.vel_y += self.gravity
        if self.vel_y > 15:
            self.vel_y = 15
        
        # Direction
        if player_x < self.rect.centerx:
            self.direction = -1
        else:
            self.direction = 1
        
        # Patrouille
        self.patrol_distance += self.speed * self.patrol_direction
        if abs(self.patrol_distance) > self.max_patrol:
            self.patrol_direction *= -1
        
        new_x = self.rect.x + self.speed * self.patrol_direction
        # Empêcher les ennemis de sortir des limites
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
        if self.shoot_cooldown <= 0:
            direction = -1 if player_x < self.rect.centerx else 1
            bullet_x = self.rect.left if direction == -1 else self.rect.right
            bullet = Bullet(bullet_x, self.rect.centery, direction, False)
            bullets.add(bullet)
            self.shoot_cooldown = self.fire_rate
    
    def take_damage(self):
        self.health -= 1
        return self.health <= 0


class Game:
    """Classe principale du jeu"""
    def __init__(self):
        self.sound_manager = SoundManager()
        self.state = "menu"
        self.level = 1
        self.max_level = 5
        self.score = 0
        self.high_score = 0
        
        # Groupes
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()
        
        self.player = None
        self.camera_x = 0
        self.level_length = 3000
        self.game_speed = 1.0
        
        self.setup_level()
    
    def setup_level(self):
        """Configure un niveau"""
        # Nettoyer
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
        
        # Joueur
        self.player = Player(100, SCREEN_HEIGHT - 150)
        self.player.base_speed = 5 + (self.level - 1) * 0.5
        self.all_sprites.add(self.player)
        
        # Sol
        for i in range(self.level_length // 300 + 1):
            ground = Platform(i * 300, SCREEN_HEIGHT - 50, 300, 50, "ground")
            self.platforms.add(ground)
            self.all_sprites.add(ground)
        
        # Bâtiments
        for i in range(self.level_length // 200):
            bx = i * 200 + random.randint(-20, 20)
            bw = random.randint(80, 150)
            bh = random.randint(150, 300)
            by = SCREEN_HEIGHT - 50 - bh
            building = Building(bx, by, bw, bh)
            self.buildings.add(building)
        
        # Plateformes organisées par sections (sans chevauchement)
        platform_positions = []  # Pour vérifier les chevauchements
        
        # Créer des plateformes en sections régulières
        section_width = 350
        num_sections = self.level_length // section_width
        
        for i in range(num_sections):
            section_x = i * section_width + 200
            
            # Hauteurs variées pour créer du relief
            heights = [
                SCREEN_HEIGHT - 150,  # Bas
                SCREEN_HEIGHT - 230,  # Moyen-bas
                SCREEN_HEIGHT - 310,  # Moyen-haut
                SCREEN_HEIGHT - 390   # Haut
            ]
            
            # Choisir 1-2 plateformes par section
            num_platforms_in_section = random.randint(1, 2)
            used_heights = []
            
            for j in range(num_platforms_in_section):
                # Choisir une hauteur non utilisée
                available_heights = [h for h in heights if h not in used_heights]
                if not available_heights:
                    break
                    
                py = random.choice(available_heights)
                used_heights.append(py)
                
                # Largeur aléatoire mais raisonnable
                pw = random.randint(100, 180)
                px = section_x + random.randint(-30, 30)
                
                # Vérifier qu'on ne sort pas des limites
                if px > 200 and px + pw < self.level_length - 100:
                    platform = Platform(px, py, pw, 20, "brick")
                    self.platforms.add(platform)
                    self.all_sprites.add(platform)
                    platform_positions.append((px, py, pw))
        
        # Ajouter quelques plateformes supplémentaires pour le défi
        for i in range(self.level * 2):
            attempts = 0
            while attempts < 10:  # Essayer 10 fois de placer la plateforme
                px = random.randint(400, self.level_length - 300)
                py = random.choice([SCREEN_HEIGHT - 180, SCREEN_HEIGHT - 260, SCREEN_HEIGHT - 340])
                pw = random.randint(80, 140)
                
                # Vérifier qu'elle ne chevauche pas une autre
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
        
        # Ennemis (mieux espacés avec variété)
        num_enemies = 3 + self.level * 2
        spacing = self.level_length // (num_enemies + 1)
        
        for i in range(num_enemies):
            ex = spacing * (i + 1) + random.randint(-50, 50)
            ey = SCREEN_HEIGHT - 120
            
            # Types d'ennemis selon le niveau et la position
            rand = random.random()
            if self.level >= 4 and rand < 0.1:  # Tank (rare)
                enemy_type = "tank"
            elif self.level >= 3 and rand < 0.25:  # Commander
                enemy_type = "commander"
            elif self.level >= 2 and rand < 0.4:  # Officer
                enemy_type = "officer"
            elif rand < 0.5:  # Elite
                enemy_type = "elite"
            else:  # Regular
                enemy_type = "regular"
            
            enemy = Enemy(ex, ey, enemy_type)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
        
        # Power-ups
        powerup_types = ["fire_rate", "health", "speed"]
        for i in range(2 + self.level):
            px = random.randint(300, self.level_length - 100)
            py = random.randint(SCREEN_HEIGHT - 300, SCREEN_HEIGHT - 100)
            ptype = random.choice(powerup_types)
            powerup = PowerUp(px, py, ptype)
            self.powerups.add(powerup)
            self.all_sprites.add(powerup)
    
    def handle_events(self):
        """Gère les événements"""
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
        """Met à jour le jeu"""
        if self.state != "playing":
            return
        
        # Contrôles
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
        
        # Mise à jour
        self.player.update(self.platforms, self.sound_manager)
        
        # Caméra
        target_camera = self.player.rect.centerx - SCREEN_WIDTH // 3
        self.camera_x = max(0, min(target_camera, self.level_length - SCREEN_WIDTH))
        
        # Vitesse augmente
        progress = self.player.rect.x / self.level_length
        self.game_speed = 1.0 + (self.level - 1) * 0.1 + progress * 0.3
        
        # Ennemis
        for enemy in self.enemies:
            enemy.update(self.platforms, self.player.rect.x)
            if abs(enemy.rect.x - self.player.rect.x) < 500:
                enemy.shoot(self.enemy_bullets, self.player.rect.x)
        
        # Balles
        self.player_bullets.update()
        self.enemy_bullets.update()
        self.powerups.update()
        
        # Collisions balles->ennemis
        for bullet in self.player_bullets:
            hits = pygame.sprite.spritecollide(bullet, self.enemies, False)
            for enemy in hits:
                bullet.kill()
                if enemy.take_damage():
                    enemy.kill()
                    # Points selon le type d'ennemi
                    points = {
                        "regular": 100,
                        "elite": 250,
                        "officer": 400,
                        "commander": 600,
                        "tank": 800
                    }
                    self.score += points.get(enemy.enemy_type, 100)
                    self.sound_manager.play('enemy_death')
        
        # Collisions balles->joueur
        if self.player.invincible <= 0:
            hits = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
            for hit in hits:
                self.player.take_damage(self.sound_manager)
        
        # Collisions joueur->ennemis
        if self.player.invincible <= 0:
            hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
            for hit in hits:
                self.player.take_damage(self.sound_manager)
        
        # Collisions powerups
        hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
        for powerup in hits:
            self.player.collect_powerup(powerup, self.sound_manager)
            self.score += 50
        
        # Game over
        if self.player.health <= 0:
            if self.score > self.high_score:
                self.high_score = self.score
            self.state = "game_over"
        
        # Fin de niveau
        if self.player.rect.x >= self.level_length - 200:
            self.score += 500 * self.level
            self.state = "level_complete"
    
    def draw_background(self):
        """Dessine l'arrière-plan"""
        screen.fill(LIGHT_BLUE)
        
        # Nuages
        for i in range(5):
            cloud_x = (i * 300 - self.camera_x * 0.2) % (SCREEN_WIDTH + 200) - 100
            pygame.draw.ellipse(screen, WHITE, (cloud_x, 50 + i * 20, 100, 40))
            pygame.draw.ellipse(screen, WHITE, (cloud_x + 30, 40 + i * 20, 80, 50))
            pygame.draw.ellipse(screen, WHITE, (cloud_x + 60, 50 + i * 20, 90, 40))
        
        # Bâtiments
        for building in self.buildings:
            draw_x = building.rect.x - self.camera_x * 0.5
            if -200 < draw_x < SCREEN_WIDTH + 200:
                screen.blit(building.image, (draw_x, building.rect.y))
    
    def draw_hud(self):
        """Dessine l'interface"""
        # Coeurs
        for i in range(self.player.max_health):
            heart_x = 20 + i * 40
            if i < self.player.health:
                pygame.draw.circle(screen, RED, (heart_x, 30), 10)
                pygame.draw.circle(screen, RED, (heart_x + 14, 30), 10)
                pygame.draw.polygon(screen, RED, [(heart_x - 10, 33), (heart_x + 7, 50), (heart_x + 24, 33)])
            else:
                pygame.draw.circle(screen, GRAY, (heart_x, 30), 10, 2)
                pygame.draw.circle(screen, GRAY, (heart_x + 14, 30), 10, 2)
                pygame.draw.polygon(screen, GRAY, [(heart_x - 10, 33), (heart_x + 7, 50), (heart_x + 24, 33)], 2)
        
        # Score
        score_text = font_small.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (SCREEN_WIDTH - 200, 20))
        
        # Niveau
        level_text = font_small.render(f"Niveau: {self.level}/{self.max_level}", True, BLACK)
        screen.blit(level_text, (SCREEN_WIDTH - 200, 50))
        
        # Ennemis restants (pour debug)
        enemies_text = font_small.render(f"Ennemis: {len(self.enemies)}", True, BLACK)
        screen.blit(enemies_text, (SCREEN_WIDTH - 200, 80))
        
        # Power-ups actifs
        powerup_y = 80
        if self.player.fire_rate_boost > 0:
            boost_text = font_small.render(f"Cadence x2: {self.player.fire_rate_boost // 60}s", True, YELLOW)
            screen.blit(boost_text, (20, powerup_y))
            powerup_y += 25
        if self.player.speed_boost > 0:
            boost_text = font_small.render(f"Vitesse +: {self.player.speed_boost // 60}s", True, LIGHT_BLUE)
            screen.blit(boost_text, (20, powerup_y))
        
        # Barre de progression
        progress = min(self.player.rect.x / self.level_length, 1.0)
        bar_width, bar_height = 200, 15
        bar_x = SCREEN_WIDTH // 2 - bar_width // 2
        bar_y = 20
        pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, bar_width * progress, bar_height))
        pygame.draw.rect(screen, BLACK, (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Contrôles
        controls = font_small.render("C: Changer Skin | ESPACE: Sauter | Tir Auto", True, DARK_GRAY)
        screen.blit(controls, (SCREEN_WIDTH // 2 - controls.get_width() // 2, SCREEN_HEIGHT - 30))
    
    def draw_menu(self):
        """Menu principal"""
        screen.fill(DARK_BLUE)
        
        title = font_large.render("Bataille de Philadelphie", True, YELLOW)
        subtitle = font_medium.render("Revolution Americaine - 1776", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 180))
        
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
            color = YELLOW if i == 0 else WHITE
            rendered = font_small.render(text, True, color)
            screen.blit(rendered, (SCREEN_WIDTH // 2 - rendered.get_width() // 2, 300 + i * 35))
    
    def draw_pause(self):
        """Écran de pause"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(128)
        screen.blit(overlay, (0, 0))
        
        pause_text = font_large.render("PAUSE", True, WHITE)
        resume_text = font_small.render("ESC - Reprendre | M - Menu", True, WHITE)
        
        screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
    
    def draw_game_over(self):
        """Game over"""
        screen.fill(DARK_GRAY)
        
        game_over = font_large.render("DEFAITE", True, RED)
        score_text = font_medium.render(f"Score Final: {self.score}", True, WHITE)
        high_score = font_small.render(f"Meilleur Score: {self.high_score}", True, YELLOW)
        restart = font_small.render("ENTREE - Recommencer | ESC - Menu", True, WHITE)
        
        screen.blit(game_over, (SCREEN_WIDTH // 2 - game_over.get_width() // 2, 150))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 250))
        screen.blit(high_score, (SCREEN_WIDTH // 2 - high_score.get_width() // 2, 320))
        screen.blit(restart, (SCREEN_WIDTH // 2 - restart.get_width() // 2, 420))
    
    def draw_level_complete(self):
        """Fin de niveau"""
        screen.fill(DARK_GREEN)
        
        complete = font_large.render(f"NIVEAU {self.level} TERMINE!", True, YELLOW)
        score_text = font_medium.render(f"Score: {self.score}", True, WHITE)
        next_text = font_small.render("ENTREE - Niveau Suivant", True, WHITE)
        
        screen.blit(complete, (SCREEN_WIDTH // 2 - complete.get_width() // 2, 200))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 300))
        screen.blit(next_text, (SCREEN_WIDTH // 2 - next_text.get_width() // 2, 400))
    
    def draw_victory(self):
        """Victoire"""
        screen.fill(DARK_BLUE)
        
        victory = font_large.render("VICTOIRE!", True, YELLOW)
        subtitle = font_medium.render("L'Independance est Declaree!", True, WHITE)
        score_text = font_medium.render(f"Score Final: {self.score}", True, YELLOW)
        restart = font_small.render("ENTREE - Menu Principal", True, WHITE)
        
        # Drapeau américain
        flag_x, flag_y = SCREEN_WIDTH // 2 - 60, 80
        for i in range(7):
            color = RED if i % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, (flag_x, flag_y + i * 11, 120, 11))
        pygame.draw.rect(screen, DARK_BLUE, (flag_x, flag_y, 50, 44))
        
        screen.blit(victory, (SCREEN_WIDTH // 2 - victory.get_width() // 2, 200))
        screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 280))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 360))
        screen.blit(restart, (SCREEN_WIDTH // 2 - restart.get_width() // 2, 450))
    
    def draw(self):
        """Dessine le jeu"""
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "playing":
            self.draw_background()
            
            # Plateformes
            for platform in self.platforms:
                draw_x = platform.rect.x - self.camera_x
                if -platform.rect.width < draw_x < SCREEN_WIDTH:
                    screen.blit(platform.image, (draw_x, platform.rect.y))
            
            # Power-ups
            for powerup in self.powerups:
                draw_x = powerup.rect.x - self.camera_x
                if -50 < draw_x < SCREEN_WIDTH + 50:
                    screen.blit(powerup.image, (draw_x, powerup.rect.y))
            
            # Ennemis
            for enemy in self.enemies:
                draw_x = enemy.rect.x - self.camera_x
                if -enemy.rect.width < draw_x < SCREEN_WIDTH:
                    screen.blit(enemy.image, (draw_x, enemy.rect.y))
                    
                    # Barre de vie pour les ennemis avec beaucoup de PV
                    if enemy.max_health > 3:
                        bar_width = enemy.width
                        bar_height = 5
                        bar_x = draw_x
                        bar_y = enemy.rect.y - 10
                        
                        # Fond de la barre
                        pygame.draw.rect(screen, RED, (bar_x, bar_y, bar_width, bar_height))
                        # Vie restante
                        health_width = (enemy.health / enemy.max_health) * bar_width
                        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, health_width, bar_height))
                        # Contour
                        pygame.draw.rect(screen, BLACK, (bar_x, bar_y, bar_width, bar_height), 1)
            
            # Joueur
            player_x = self.player.rect.x - self.camera_x
            if self.player.invincible % 10 < 5:
                screen.blit(self.player.image, (player_x, self.player.rect.y))
            
            # Balles joueur
            for bullet in self.player_bullets:
                draw_x = bullet.rect.x - self.camera_x
                if 0 < draw_x < SCREEN_WIDTH:
                    screen.blit(bullet.image, (draw_x, bullet.rect.y))
            
            # Balles ennemies
            for bullet in self.enemy_bullets:
                draw_x = bullet.rect.x - self.camera_x
                if 0 < draw_x < SCREEN_WIDTH:
                    screen.blit(bullet.image, (draw_x, bullet.rect.y))
            
            self.draw_hud()
        
        elif self.state == "pause":
            self.draw_background()
            for platform in self.platforms:
                draw_x = platform.rect.x - self.camera_x
                if -platform.rect.width < draw_x < SCREEN_WIDTH:
                    screen.blit(platform.image, (draw_x, platform.rect.y))
            player_x = self.player.rect.x - self.camera_x
            screen.blit(self.player.image, (player_x, self.player.rect.y))
            self.draw_hud()
            self.draw_pause()
        
        elif self.state == "game_over":
            self.draw_game_over()
        
        elif self.state == "level_complete":
            self.draw_level_complete()
        
        elif self.state == "victory":
            self.draw_victory()
        
        pygame.display.flip()
    
    def run(self):
        """Boucle principale"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            clock.tick(FPS)
        
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
