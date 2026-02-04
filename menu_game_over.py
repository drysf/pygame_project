import pygame
import sys
import math
import random
from typing import List, Tuple

# Initialisation
pygame.init()

# Constantes
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60

# Palette ultra-réaliste
COLORS = {
    'sky_top': (100, 149, 237),
    'sky_middle': (135, 206, 250),
    'sky_horizon': (255, 250, 205),
    'night_sky': (15, 24, 45),
    'night_dark': (8, 12, 25),
    'dusk_dark': (40, 30, 50),
    'dusk_red': (80, 40, 40),
    'dusk_purple': (60, 40, 70),
    'cloud_white': (255, 255, 255),
    'cloud_shadow': (220, 220, 230),
    'cloud_dark': (100, 100, 120),
    'cream': (255, 253, 208),
    'parchment': (245, 237, 218),
    'parchment_old': (220, 210, 180),
    'colonial_blue': (31, 58, 96),
    'royal_blue': (65, 105, 225),
    'deep_red': (139, 0, 0),
    'bright_red': (178, 34, 34),
    'blood_red': (100, 0, 0),
    'brick_red': (165, 42, 42),
    'warm_gold': (218, 165, 32),
    'brass': (181, 166, 66),
    'wood_brown': (139, 90, 43),
    'dark_wood': (92, 64, 51),
    'white': (255, 255, 255),
    'ivory': (255, 250, 240),
    'grass_green': (85, 107, 47),
    'dark_green': (34, 85, 34),
    'dead_grass': (100, 90, 60),
    'forest_green': (49, 87, 44),
    'shadow': (30, 30, 35),
    'dirt_brown': (115, 85, 45),
    'stone_gray': (169, 169, 169),
    'ash_gray': (128, 128, 128),
    'smoke_gray': (100, 100, 100),
    'gunpowder': (70, 70, 70),
}


class RainDrop:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-SCREEN_HEIGHT, 0)
        self.speed = random.uniform(15, 25)
        self.length = random.randint(10, 20)
    
    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-100, -10)
            self.x = random.randint(0, SCREEN_WIDTH)
    
    def draw(self, screen):
        pygame.draw.line(screen, (*COLORS['cloud_dark'], 120),
                        (int(self.x), int(self.y)),
                        (int(self.x - 2), int(self.y + self.length)), 2)


class Ember:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-2, -0.5)
        self.lifetime = random.randint(60, 120)
        self.max_lifetime = self.lifetime
        self.size = random.randint(2, 5)
        self.flicker_phase = random.uniform(0, 2 * math.pi)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.02
        self.lifetime -= 1
        self.flicker_phase += 0.2
    
    def draw(self, screen):
        if self.lifetime > 0:
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            flicker = 0.7 + math.sin(self.flicker_phase) * 0.3
            
            glow_surf = pygame.Surface((self.size * 6, self.size * 6), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*COLORS['bright_red'], int(alpha * 0.3 * flicker)),
                             (self.size * 3, self.size * 3), self.size * 3)
            screen.blit(glow_surf, (int(self.x - self.size * 3), int(self.y - self.size * 3)))
            
            pygame.draw.circle(screen, (*COLORS['bright_red'], int(alpha * flicker)),
                             (int(self.x), int(self.y)), self.size)
            pygame.draw.circle(screen, (*COLORS['white'], int(alpha * 0.5 * flicker)),
                             (int(self.x), int(self.y)), max(1, self.size // 2))


class Smoke:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.3, 0.3)
        self.vy = random.uniform(-0.8, -0.3)
        self.lifetime = random.randint(100, 200)
        self.max_lifetime = self.lifetime
        self.size = random.randint(8, 15)
        self.rotation = random.uniform(0, 2 * math.pi)
        self.rotation_speed = random.uniform(-0.02, 0.02)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.99
        self.vy *= 0.98
        self.lifetime -= 1
        self.size += 0.2
        self.rotation += self.rotation_speed
    
    def draw(self, screen):
        if self.lifetime > 0:
            alpha = int(100 * (self.lifetime / self.max_lifetime))
            smoke_surf = pygame.Surface((int(self.size * 3), int(self.size * 3)), pygame.SRCALPHA)
            
            for i in range(3):
                offset_x = math.cos(self.rotation + i * 2.1) * self.size * 0.3
                offset_y = math.sin(self.rotation + i * 2.1) * self.size * 0.3
                pygame.draw.circle(smoke_surf, (*COLORS['smoke_gray'], alpha // (i + 1)),
                                 (int(self.size * 1.5 + offset_x),
                                  int(self.size * 1.5 + offset_y)),
                                 int(self.size * (1 + i * 0.2)))
            
            screen.blit(smoke_surf, (int(self.x - self.size * 1.5), int(self.y - self.size * 1.5)))


class BattlefieldFire:
    def __init__(self, x, y, scale=1.0):
        self.x = x
        self.y = y
        self.scale = scale
        self.embers = []
        self.smoke = []
        self.ember_timer = 0
        self.smoke_timer = 0
        self.flame_phase = random.uniform(0, 2 * math.pi)
    
    def update(self):
        self.flame_phase += 0.15
        self.ember_timer += 1
        self.smoke_timer += 1
        
        if self.ember_timer > 8:
            self.ember_timer = 0
            self.embers.append(Ember(
                self.x + random.uniform(-15, 15) * self.scale,
                self.y
            ))
        
        if self.smoke_timer > 12:
            self.smoke_timer = 0
            self.smoke.append(Smoke(
                self.x + random.uniform(-10, 10) * self.scale,
                self.y - 20 * self.scale
            ))
        
        for ember in self.embers[:]:
            ember.update()
            if ember.lifetime <= 0:
                self.embers.remove(ember)
        
        for smoke in self.smoke[:]:
            smoke.update()
            if smoke.lifetime <= 0:
                self.smoke.remove(smoke)
    
    def draw(self, screen):
        for smoke in self.smoke:
            smoke.draw(screen)
        
        flame_height = (30 + math.sin(self.flame_phase) * 10) * self.scale
        flame_width = 25 * self.scale
        
        flame_surf = pygame.Surface((int(flame_width * 2), int(flame_height * 1.5)), pygame.SRCALPHA)
        
        for i in range(3):
            wave = math.sin(self.flame_phase + i) * 5 * self.scale
            points = [
                (flame_width + wave, flame_height * 1.5),
                (flame_width * 0.7 + wave, flame_height * 0.7),
                (flame_width + wave * 0.5, flame_height * 0.3),
                (flame_width * 1.3 + wave, flame_height * 0.7),
            ]
            if i == 0:
                color = (*COLORS['bright_red'], 200)
            elif i == 1:
                color = (*COLORS['bright_red'], 150)
            else:
                color = (*COLORS['white'], 100)
            
            pygame.draw.polygon(flame_surf, color, [(int(p[0]), int(p[1])) for p in points])
        
        screen.blit(flame_surf, (int(self.x - flame_width), int(self.y - flame_height * 1.5)))
        
        for ember in self.embers:
            ember.draw(screen)


class FallenSoldier:
    def __init__(self, x, y, facing_right=True):
        self.x = x
        self.y = y
        self.facing_right = facing_right
        self.tattered = random.choice([True, False])
    
    def draw(self, screen):
        shadow_surf = pygame.Surface((80, 30), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow_surf, (*COLORS['shadow'], 150), (0, 0, 80, 30))
        screen.blit(shadow_surf, (int(self.x - 40), int(self.y)))
        
        if self.facing_right:
            body_points = [
                (self.x - 30, self.y),
                (self.x - 20, self.y - 15),
                (self.x + 10, self.y - 10),
                (self.x + 20, self.y + 5)
            ]
        else:
            body_points = [
                (self.x + 30, self.y),
                (self.x + 20, self.y - 15),
                (self.x - 10, self.y - 10),
                (self.x - 20, self.y + 5)
            ]
        
        pygame.draw.polygon(screen, COLORS['colonial_blue'], [(int(p[0]), int(p[1])) for p in body_points])
        
        if self.tattered:
            for _ in range(5):
                tear_x = random.randint(int(min(p[0] for p in body_points)), int(max(p[0] for p in body_points)))
                tear_y = random.randint(int(min(p[1] for p in body_points)), int(max(p[1] for p in body_points)))
                pygame.draw.circle(screen, COLORS['shadow'], (tear_x, tear_y), 2)
        
        head_x = self.x + (-15 if self.facing_right else 15)
        head_y = self.y - 18
        pygame.draw.circle(screen, COLORS['parchment'], (int(head_x), int(head_y)), 8)
        
        hat_x = head_x + random.randint(-5, 5)
        hat_y = self.y + random.randint(-5, 5)
        tricorne_points = [
            (hat_x - 10, hat_y),
            (hat_x, hat_y - 6),
            (hat_x + 10, hat_y),
            (hat_x + 5, hat_y + 2),
            (hat_x - 5, hat_y + 2)
        ]
        pygame.draw.polygon(screen, (0, 0, 0), [(int(p[0]), int(p[1])) for p in tricorne_points])
        
        musket_angle = random.uniform(-0.5, 0.5) + (0.3 if self.facing_right else 2.8)
        musket_length = 60
        musket_x = self.x + (5 if self.facing_right else -5)
        musket_y = self.y - 5
        musket_end_x = musket_x + math.cos(musket_angle) * musket_length
        musket_end_y = musket_y + math.sin(musket_angle) * musket_length
        
        pygame.draw.line(screen, COLORS['gunpowder'],
                        (int(musket_x), int(musket_y)),
                        (int(musket_end_x), int(musket_end_y)), 4)


class TatteredFlag:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wave_phase = random.uniform(0, 2 * math.pi)
        self.sway = 0
        self.sway_direction = random.choice([-1, 1])
    
    def update(self):
        self.wave_phase += 0.05
        self.sway += 0.02 * self.sway_direction
        if abs(self.sway) > 0.3:
            self.sway_direction *= -1
    
    def draw(self, screen):
        pole_x = self.x + self.sway * 20
        pole_height = 180
        
        pygame.draw.rect(screen, COLORS['dark_wood'],
                        (int(pole_x - 3), self.y, 6, pole_height))
        
        flag_width = 90
        flag_height = 60
        stripe_height = flag_height // 13
        
        flag_surf = pygame.Surface((flag_width, flag_height), pygame.SRCALPHA)
        
        for i in range(13):
            color = COLORS['blood_red'] if i % 2 == 0 else COLORS['parchment_old']
            y_pos = i * stripe_height
            
            for x in range(flag_width):
                if random.random() > 0.95:
                    continue
                
                wave = math.sin(self.wave_phase + x * 0.1 + self.sway) * 4
                if x < flag_width - 10 or random.random() > 0.3:
                    pygame.draw.line(flag_surf, color,
                                   (x, int(y_pos + wave)),
                                   (x, int(y_pos + stripe_height + wave)))
        
        canton_width = flag_width // 2
        canton_height = 7 * stripe_height
        
        for x in range(canton_width):
            for y in range(canton_height):
                if random.random() > 0.92:
                    continue
                wave = math.sin(self.wave_phase + x * 0.1 + self.sway) * 4
                flag_surf.set_at((x, int(y + wave)), COLORS['colonial_blue'])
        
        for row in range(2):
            for col in range(3):
                if random.random() > 0.7:
                    sx = col * 25 + 12
                    sy = row * 20 + 15
                    star_points = []
                    for i in range(10):
                        angle = i * 2 * math.pi / 10
                        radius = 5 if i % 2 == 0 else 2
                        px = sx + math.cos(angle) * radius
                        py = sy + math.sin(angle) * radius
                        star_points.append((int(px), int(py)))
                    
                    for px, py in star_points:
                        if 0 <= px < canton_width and 0 <= py < canton_height:
                            wave = int(math.sin(self.wave_phase + px * 0.1 + self.sway) * 4)
                            if 0 <= py + wave < flag_height:
                                flag_surf.set_at((px, py + wave), COLORS['parchment_old'])
        
        screen.blit(flag_surf, (int(pole_x + 5), self.y + 30))


class Crow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.speed = random.uniform(1.0, 2.0)
        self.wing_phase = random.uniform(0, 2 * math.pi)
        self.perched = random.choice([True, False])
        self.perch_timer = random.randint(60, 180)
    
    def update(self):
        self.wing_phase += 0.2
        
        if self.perched:
            self.perch_timer -= 1
            if self.perch_timer <= 0:
                self.perched = False
                self.target_x = random.randint(100, SCREEN_WIDTH - 100)
                self.target_y = random.randint(100, 300)
        else:
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            dist = math.sqrt(dx**2 + dy**2)
            
            if dist < 5:
                self.perched = True
                self.perch_timer = random.randint(60, 180)
            else:
                self.x += (dx / dist) * self.speed
                self.y += (dy / dist) * self.speed
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), 5)
        
        if not self.perched:
            wing_angle = math.sin(self.wing_phase) * 0.6
            wing_length = 10
            
            left_wing = (
                int(self.x - wing_length * math.cos(wing_angle)),
                int(self.y - wing_length * abs(math.sin(wing_angle)))
            )
            right_wing = (
                int(self.x + wing_length * math.cos(wing_angle)),
                int(self.y - wing_length * abs(math.sin(wing_angle)))
            )
            
            pygame.draw.line(screen, (0, 0, 0), (int(self.x), int(self.y)), left_wing, 2)
            pygame.draw.line(screen, (0, 0, 0), (int(self.x), int(self.y)), right_wing, 2)


class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font_huge = pygame.font.Font(None, 140)
        self.font_large = pygame.font.Font(None, 70)
        self.font_medium = pygame.font.Font(None, 45)
        self.font_small = pygame.font.Font(None, 45)
        
        self.time = 0
        self.rain = [RainDrop() for _ in range(100)]
        
        self.fires = [
            BattlefieldFire(200, 520, 0.8),
            BattlefieldFire(450, 530, 1.0),
            BattlefieldFire(780, 515, 0.9),
        ]
        
        self.fallen_soldiers = [
            FallenSoldier(150, 580, True),
            FallenSoldier(320, 590, False),
            FallenSoldier(550, 585, True),
            FallenSoldier(720, 595, False),
            FallenSoldier(880, 580, True),
        ]
        
        self.flags = [
            TatteredFlag(100, 400),
            TatteredFlag(SCREEN_WIDTH - 100, 410)
        ]
        
        self.crows = [
            Crow(random.randint(100, SCREEN_WIDTH - 100), random.randint(100, 300))
            for _ in range(5)
        ]
        
        self.options = ["RETRY", "MAIN MENU", "QUIT"]
        self.selected = 0
        
        self.title_pulse = 0
        self.fade_alpha = 255
    
    def update(self):
        self.time += 0.015
        self.title_pulse += 0.05
        
        for drop in self.rain:
            drop.update()
        
        for fire in self.fires:
            fire.update()
        
        for flag in self.flags:
            flag.update()
        
        for crow in self.crows:
            crow.update()
        
        if self.fade_alpha > 0:
            self.fade_alpha -= 2
    
    def draw_sky(self):
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            
            if ratio < 0.5:
                r = int(COLORS['dusk_dark'][0] + (COLORS['dusk_purple'][0] - COLORS['dusk_dark'][0]) * (ratio / 0.5))
                g = int(COLORS['dusk_dark'][1] + (COLORS['dusk_purple'][1] - COLORS['dusk_dark'][1]) * (ratio / 0.5))
                b = int(COLORS['dusk_dark'][2] + (COLORS['dusk_purple'][2] - COLORS['dusk_dark'][2]) * (ratio / 0.5))
            else:
                local_ratio = (ratio - 0.5) / 0.5
                r = int(COLORS['dusk_purple'][0] + (COLORS['dusk_red'][0] - COLORS['dusk_purple'][0]) * local_ratio)
                g = int(COLORS['dusk_purple'][1] + (COLORS['dusk_red'][1] - COLORS['dusk_purple'][1]) * local_ratio)
                b = int(COLORS['dusk_purple'][2] + (COLORS['dusk_red'][2] - COLORS['dusk_purple'][2]) * local_ratio)
            
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        for _ in range(80):
            sx = random.randint(0, SCREEN_WIDTH)
            sy = random.randint(0, SCREEN_HEIGHT // 3)
            brightness = random.randint(50, 100)
            pygame.draw.circle(self.screen, (brightness, brightness, brightness), (sx, sy), 1)
    
    def draw_battlefield(self):
        ground_y = 550
        
        for y in range(ground_y, SCREEN_HEIGHT):
            ratio = (y - ground_y) / (SCREEN_HEIGHT - ground_y)
            r = int(COLORS['dead_grass'][0] + (COLORS['dirt_brown'][0] - COLORS['dead_grass'][0]) * ratio)
            g = int(COLORS['dead_grass'][1] + (COLORS['dirt_brown'][1] - COLORS['dead_grass'][1]) * ratio)
            b = int(COLORS['dead_grass'][2] + (COLORS['dirt_brown'][2] - COLORS['dead_grass'][2]) * ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        for _ in range(60):
            gx = random.randint(0, SCREEN_WIDTH)
            gy = random.randint(ground_y, SCREEN_HEIGHT)
            pygame.draw.line(self.screen, COLORS['shadow'], (gx, gy), (gx, gy + 2), 1)
    
    def draw(self):
        self.draw_sky()
        
        for drop in self.rain:
            drop.draw(self.screen)
        
        self.draw_battlefield()
        
        for flag in self.flags:
            flag.draw(self.screen)
        
        for fire in self.fires:
            fire.draw(self.screen)
        
        for soldier in self.fallen_soldiers:
            soldier.draw(self.screen)
        
        for crow in self.crows:
            crow.draw(self.screen)
        
        panel_y = 60
        panel_height = 550
        
        overlay = pygame.Surface((SCREEN_WIDTH - 120, panel_height), pygame.SRCALPHA)
        overlay.fill((*COLORS['parchment_old'], 200))
        
        tear_surf = pygame.Surface((SCREEN_WIDTH - 120, panel_height), pygame.SRCALPHA)
        for _ in range(30):
            tear_x = random.randint(0, SCREEN_WIDTH - 120)
            tear_y = random.randint(0, panel_height)
            tear_size = random.randint(3, 8)
            pygame.draw.circle(tear_surf, (*COLORS['shadow'], 60), (tear_x, tear_y), tear_size)
        overlay.blit(tear_surf, (0, 0))
        
        for i in range(4):
            thickness = 10 - i * 2
            offset = i * 4
            pygame.draw.rect(overlay, COLORS['shadow'],
                           (offset, offset,
                            SCREEN_WIDTH - 120 - 2 * offset,
                            panel_height - 2 * offset), thickness)
        
        self.screen.blit(overlay, (60, panel_y))
        
        corner_positions = [
            (80, panel_y + 20), (SCREEN_WIDTH - 80, panel_y + 20),
            (80, panel_y + panel_height - 20), (SCREEN_WIDTH - 80, panel_y + panel_height - 20)
        ]
        for corner_x, corner_y in corner_positions:
            pygame.draw.circle(self.screen, COLORS['parchment_old'], (corner_x, corner_y), 8)
            pygame.draw.circle(self.screen, COLORS['shadow'], (corner_x, corner_y), 8, 2)
            pygame.draw.circle(self.screen, COLORS['shadow'], (corner_x - 3, corner_y - 1), 2)
            pygame.draw.circle(self.screen, COLORS['shadow'], (corner_x + 3, corner_y - 1), 2)
            pygame.draw.line(self.screen, COLORS['shadow'],
                           (corner_x - 2, corner_y + 3),
                           (corner_x + 2, corner_y + 3), 1)
        
        title_text = "DEFEAT"
        title_y = panel_y + 120
        
        pulse = 0.95 + math.sin(self.title_pulse) * 0.05
        scaled_font = pygame.font.Font(None, int(140 * pulse))
        
        for offset in range(12, 0, -1):
            shadow_surf = scaled_font.render(title_text, True, COLORS['shadow'])
            shadow_rect = shadow_surf.get_rect(center=(SCREEN_WIDTH // 2 + offset, title_y + offset))
            s = pygame.Surface(shadow_surf.get_size(), pygame.SRCALPHA)
            s.fill((*COLORS['shadow'], 50 - offset * 3))
            s.blit(shadow_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            self.screen.blit(s, shadow_rect)
        
        title_surf = scaled_font.render(title_text, True, COLORS['blood_red'])
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, title_y))
        
        outline_surf = scaled_font.render(title_text, True, COLORS['shadow'])
        for angle in range(0, 360, 30):
            offset_x = math.cos(math.radians(angle)) * 4
            offset_y = math.sin(math.radians(angle)) * 4
            self.screen.blit(outline_surf, (title_rect.x + offset_x, title_rect.y + offset_y))
        
        self.screen.blit(title_surf, title_rect)
        
        subtitle_text = "The battle is lost..."
        subtitle_surf = self.font_medium.render(subtitle_text, True, COLORS['shadow'])
        subtitle_rect = subtitle_surf.get_rect(center=(SCREEN_WIDTH // 2, panel_y + 210))
        self.screen.blit(subtitle_surf, subtitle_rect)
        
        line_y = panel_y + 260
        line_center = SCREEN_WIDTH // 2
        
        for i in range(3):
            y_offset = i * 2
            alpha = 100 - i * 30
            pygame.draw.line(self.screen, (*COLORS['shadow'], alpha),
                           (line_center - 300, line_y + y_offset),
                           (line_center + 300, line_y + y_offset), 3)
        
        skull_positions = [line_center - 240, line_center, line_center + 240]
        for skull_x in skull_positions:
            pygame.draw.circle(self.screen, COLORS['parchment_old'], (skull_x, line_y), 12)
            pygame.draw.circle(self.screen, COLORS['shadow'], (skull_x, line_y), 12, 2)
            
            pygame.draw.circle(self.screen, COLORS['shadow'], (skull_x - 4, line_y - 2), 3)
            pygame.draw.circle(self.screen, COLORS['shadow'], (skull_x + 4, line_y - 2), 3)
            
            pygame.draw.line(self.screen, COLORS['shadow'],
                           (skull_x - 3, line_y + 4),
                           (skull_x + 3, line_y + 4), 2)
        
        quote_y = panel_y + 310
        quote_text = '"These are the times that try men\'s souls"'
        quote_surf = self.font_small.render(quote_text, True, COLORS['shadow'])
        quote_rect = quote_surf.get_rect(center=(SCREEN_WIDTH // 2, quote_y))
        self.screen.blit(quote_surf, quote_rect)
        
        author_text = "- Thomas Paine"
        author_surf = self.font_small.render(author_text, True, COLORS['shadow'])
        author_rect = author_surf.get_rect(center=(SCREEN_WIDTH // 2, quote_y + 40))
        self.screen.blit(author_surf, author_rect)
        
        for i, option in enumerate(self.options):
            is_selected = (i == self.selected)
            option_y = panel_y + 425 + i * 45  # Changé à 45 pixels d'espacement
            
            if is_selected:
                sel_width = 280
                sel_height = 50
                sel_rect = pygame.Rect(SCREEN_WIDTH // 2 - sel_width // 2, option_y - 22, sel_width, sel_height)
                
                sel_surf = pygame.Surface((sel_width, sel_height), pygame.SRCALPHA)
                for sy in range(sel_height):
                    alpha = 120 - abs(sy - sel_height // 2) * 2
                    pygame.draw.line(sel_surf, (*COLORS['blood_red'], alpha),
                                   (0, sy), (sel_width, sy))
                self.screen.blit(sel_surf, sel_rect)
                
                pygame.draw.rect(self.screen, COLORS['shadow'], sel_rect, 3)
                
                arrow_left = [
                    (SCREEN_WIDTH // 2 - 155, option_y),
                    (SCREEN_WIDTH // 2 - 140, option_y - 8),
                    (SCREEN_WIDTH // 2 - 140, option_y + 8)
                ]
                arrow_right = [
                    (SCREEN_WIDTH // 2 + 155, option_y),
                    (SCREEN_WIDTH // 2 + 140, option_y - 8),
                    (SCREEN_WIDTH // 2 + 140, option_y + 8)
                ]
                pygame.draw.polygon(self.screen, COLORS['blood_red'], arrow_left)
                pygame.draw.polygon(self.screen, COLORS['blood_red'], arrow_right)
                
                color = COLORS['blood_red']
            else:
                color = COLORS['shadow']
            
            shadow_surf = self.font_medium.render(option, True, COLORS['shadow'])
            shadow_rect = shadow_surf.get_rect(center=(SCREEN_WIDTH // 2 + 3, option_y + 3))
            s = pygame.Surface(shadow_surf.get_size(), pygame.SRCALPHA)
            s.fill((*COLORS['shadow'], 100))
            s.blit(shadow_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            self.screen.blit(s, shadow_rect)
            
            option_surf = self.font_medium.render(option, True, color)
            option_rect = option_surf.get_rect(center=(SCREEN_WIDTH // 2, option_y))
            self.screen.blit(option_surf, option_rect)
        
        if self.fade_alpha > 0:
            fade_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            fade_surf.fill((*COLORS['shadow'], self.fade_alpha))
            self.screen.blit(fade_surf, (0, 0))
    
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected]
        return None


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("🎖️ PHILADELPHIA LIBERTY - DEFEAT 🎖️")
    game_over = GameOverScreen(screen)
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            action = game_over.handle_input(event)
            if action == "RETRY":
                print("⚔️ Rising again to fight!")
            elif action == "MAIN MENU":
                print("📜 Returning to main menu...")
            elif action == "QUIT":
                print("🏳️ Farewell, soldier...")
                running = False
        
        game_over.update()
        game_over.draw()
        
        pygame.display.flip()
        game_over.clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()