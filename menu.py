"""
Menu principal du jeu - Philadelphia Liberty
Style colonial américain avec animations détaillées
"""
import pygame
import sys
import math
import random
from typing import List, Tuple

# Constantes
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60

# Palette ultra-réaliste
COLORS = {
    'sky_top': (100, 149, 237),
    'sky_middle': (135, 206, 250),
    'sky_horizon': (255, 250, 205),
    'sun_glow': (255, 248, 220),
    'cloud_white': (255, 255, 255),
    'cloud_shadow': (220, 220, 230),
    'cream': (255, 253, 208),
    'parchment': (245, 237, 218),
    'colonial_blue': (31, 58, 96),
    'royal_blue': (65, 105, 225),
    'deep_red': (139, 0, 0),
    'bright_red': (178, 34, 34),
    'brick_red': (165, 42, 42),
    'brick_shadow': (120, 30, 30),
    'warm_gold': (218, 165, 32),
    'brass': (181, 166, 66),
    'wood_brown': (139, 90, 43),
    'dark_wood': (92, 64, 51),
    'white': (255, 255, 255),
    'ivory': (255, 250, 240),
    'roof_gray': (105, 105, 105),
    'slate_blue': (112, 128, 144),
    'grass_green': (85, 107, 47),
    'dark_green': (34, 85, 34),
    'forest_green': (49, 87, 44),
    'smoke_gray': (128, 128, 128),
    'smoke_light': (192, 192, 192),
    'flash_yellow': (255, 255, 200),
    'flash_white': (255, 255, 255),
    'gunpowder': (70, 70, 70),
    'shadow': (30, 30, 35),
    'dirt_brown': (115, 85, 45),
    'stone_gray': (169, 169, 169),
}


class Cloud:
    def __init__(self, x, y, scale=1.0, speed=0.2):
        self.x = x
        self.y = y
        self.scale = scale
        self.speed = speed
        self.puffs = []
        num_puffs = random.randint(5, 9)
        for i in range(num_puffs):
            offset_x = random.uniform(-60, 60) * scale
            offset_y = random.uniform(-20, 20) * scale
            radius = random.uniform(30, 60) * scale
            self.puffs.append((offset_x, offset_y, radius))
    
    def update(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH + 200:
            self.x = -200
    
    def draw(self, screen):
        for offset_x, offset_y, radius in self.puffs:
            shadow_surf = pygame.Surface((int(radius * 2.5), int(radius * 2.5)), pygame.SRCALPHA)
            pygame.draw.circle(shadow_surf, (*COLORS['cloud_shadow'], 60),
                             (int(radius * 1.25), int(radius * 1.25)), int(radius))
            screen.blit(shadow_surf, (int(self.x + offset_x - radius * 1.25), 
                                      int(self.y + offset_y - radius * 1.25 + 5)))
            cloud_surf = pygame.Surface((int(radius * 2.5), int(radius * 2.5)), pygame.SRCALPHA)
            pygame.draw.circle(cloud_surf, (*COLORS['cloud_white'], 200),
                             (int(radius * 1.25), int(radius * 1.25)), int(radius))
            screen.blit(cloud_surf, (int(self.x + offset_x - radius * 1.25), 
                                     int(self.y + offset_y - radius * 1.25)))


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.uniform(1.5, 3.0)
        self.wing_phase = random.uniform(0, 2 * math.pi)
        self.wing_speed = random.uniform(0.15, 0.25)
        self.altitude_wave = random.uniform(0, 2 * math.pi)
    
    def update(self):
        self.x += self.speed
        self.wing_phase += self.wing_speed
        self.altitude_wave += 0.02
        self.y += math.sin(self.altitude_wave) * 0.5
        if self.x > SCREEN_WIDTH + 50:
            self.x = -50
            self.y = random.randint(50, 250)
    
    def draw(self, screen):
        wing_angle = math.sin(self.wing_phase) * 0.5
        pygame.draw.circle(screen, COLORS['shadow'], (int(self.x), int(self.y)), 3)
        wing_length = 12
        left_wing = (
            int(self.x - wing_length * math.cos(wing_angle)),
            int(self.y - wing_length * abs(math.sin(wing_angle)))
        )
        right_wing = (
            int(self.x + wing_length * math.cos(wing_angle)),
            int(self.y - wing_length * abs(math.sin(wing_angle)))
        )
        pygame.draw.line(screen, COLORS['shadow'], (int(self.x), int(self.y)), left_wing, 2)
        pygame.draw.line(screen, COLORS['shadow'], (int(self.x), int(self.y)), right_wing, 2)


class MuzzleFlash:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.lifetime = 12
        self.max_lifetime = 12
        self.size = 50
        self.rays = []
        for _ in range(12):
            ray_angle = random.uniform(0, 2 * math.pi)
            ray_length = random.uniform(0.6, 1.2)
            self.rays.append((ray_angle, ray_length))
    
    def update(self):
        self.lifetime -= 1
    
    def draw(self, screen):
        if self.lifetime > 0:
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            flash_surf = pygame.Surface((self.size * 3, self.size * 3), pygame.SRCALPHA)
            center_x = self.size * 1.5
            center_y = self.size * 1.5
            pygame.draw.circle(flash_surf, (*COLORS['flash_white'], alpha),
                             (int(center_x), int(center_y)), int(self.size * 0.3))
            pygame.draw.circle(flash_surf, (*COLORS['flash_yellow'], alpha // 2),
                             (int(center_x), int(center_y)), int(self.size * 0.6))
            for ray_angle, ray_length in self.rays:
                angle = self.angle + ray_angle
                length = self.size * ray_length
                num_segments = 8
                for i in range(num_segments):
                    ratio = i / num_segments
                    seg_x = center_x + math.cos(angle) * length * ratio
                    seg_y = center_y + math.sin(angle) * length * ratio
                    color = COLORS['flash_yellow'] if i < 4 else COLORS['smoke_gray']
                    seg_alpha = alpha // (i + 1)
                    seg_size = int(self.size * 0.2 * (1 - ratio * 0.8))
                    pygame.draw.circle(flash_surf, (*color, seg_alpha),
                                     (int(seg_x), int(seg_y)), seg_size)
            screen.blit(flash_surf, (int(self.x - self.size * 1.5), int(self.y - self.size * 1.5)))


class SmokeParticle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx + random.uniform(-0.5, 0.5)
        self.vy = vy + random.uniform(-0.5, 0.5)
        self.lifetime = random.randint(50, 100)
        self.max_lifetime = self.lifetime
        self.size = random.randint(4, 10)
        self.rotation = random.uniform(0, 2 * math.pi)
        self.rotation_speed = random.uniform(-0.05, 0.05)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy -= 0.08
        self.vx *= 0.97
        self.vy *= 0.98
        self.lifetime -= 1
        self.size += 0.15
        self.rotation += self.rotation_speed
    
    def draw(self, screen):
        if self.lifetime > 0:
            alpha = int(150 * (self.lifetime / self.max_lifetime))
            smoke_surf = pygame.Surface((int(self.size * 3), int(self.size * 3)), pygame.SRCALPHA)
            for i in range(3):
                offset_x = math.cos(self.rotation + i * 2.1) * self.size * 0.3
                offset_y = math.sin(self.rotation + i * 2.1) * self.size * 0.3
                color_choice = COLORS['smoke_gray'] if i < 2 else COLORS['smoke_light']
                pygame.draw.circle(smoke_surf, (*color_choice, alpha // (i + 1)),
                                 (int(self.size * 1.5 + offset_x), 
                                  int(self.size * 1.5 + offset_y)), 
                                 int(self.size * (1 + i * 0.2)))
            screen.blit(smoke_surf, (int(self.x - self.size * 1.5), int(self.y - self.size * 1.5)))


class DetailedWindow:
    @staticmethod
    def draw(screen, x, y, width, height, has_light=False):
        pygame.draw.rect(screen, COLORS['dark_wood'], (x-2, y-2, width+4, height+4))
        if has_light:
            pygame.draw.rect(screen, COLORS['warm_gold'], (x, y, width, height))
            light_surf = pygame.Surface((width + 20, height + 20), pygame.SRCALPHA)
            pygame.draw.rect(light_surf, (*COLORS['warm_gold'], 60), 
                           (10, 10, width, height))
            screen.blit(light_surf, (x - 10, y - 10))
        else:
            pygame.draw.rect(screen, COLORS['colonial_blue'], (x, y, width, height))
        reflet_surf = pygame.Surface((width, height // 3), pygame.SRCALPHA)
        reflet_surf.fill((*COLORS['sky_middle'], 80))
        screen.blit(reflet_surf, (x, y))
        pygame.draw.line(screen, COLORS['white'], 
                        (x, y + height // 2), (x + width, y + height // 2), 2)
        pygame.draw.line(screen, COLORS['white'], 
                        (x + width // 2, y), (x + width // 2, y + height), 2)
        pygame.draw.line(screen, COLORS['shadow'], 
                        (x + 1, y + height // 2 + 1), (x + width + 1, y + height // 2 + 1), 1)
        pygame.draw.line(screen, COLORS['shadow'], 
                        (x + width // 2 + 1, y + 1), (x + width // 2 + 1, y + height + 1), 1)


class ColonialHouse:
    def __init__(self, x, y, house_type=0, scale=1.0):
        self.x = x
        self.y = y
        self.scale = scale
        self.house_type = house_type
        self.scroll_speed = 0.3
        self.has_lights = random.choice([True, False, False])
        self.smoke_timer = random.randint(0, 120)
        self.smoke_particles = []
    
    def update(self):
        self.x -= self.scroll_speed
        if self.x < -400 * self.scale:
            self.x = SCREEN_WIDTH + random.randint(200, 400)
            self.house_type = random.randint(0, 3)
            self.has_lights = random.choice([True, False, False])
        self.smoke_timer += 1
        if self.smoke_timer > 30:
            self.smoke_timer = 0
            if self.house_type in [0, 1]:
                chimney_x = self.x + (120 if self.house_type == 0 else 140) * self.scale
                chimney_y = self.y - 60 * self.scale
                self.smoke_particles.append(
                    SmokeParticle(chimney_x, chimney_y, 
                                random.uniform(-0.3, 0.3), -random.uniform(0.5, 1.2))
                )
        for smoke in self.smoke_particles[:]:
            smoke.update()
            if smoke.lifetime <= 0:
                self.smoke_particles.remove(smoke)
    
    def draw(self, screen):
        shadow_surf = pygame.Surface((int(200 * self.scale), int(150 * self.scale)), pygame.SRCALPHA)
        shadow_surf.fill((*COLORS['shadow'], 60))
        screen.blit(shadow_surf, (int(self.x + 10), int(self.y + 10)))
        if self.house_type == 0:
            self.draw_farmhouse(screen)
        elif self.house_type == 1:
            self.draw_colonial_mansion(screen)
        elif self.house_type == 2:
            self.draw_cottage(screen)
        else:
            self.draw_stone_house(screen)
        for smoke in self.smoke_particles:
            smoke.draw(screen)
    
    def draw_farmhouse(self, screen):
        base_x = int(self.x)
        base_y = int(self.y)
        house_width = int(140 * self.scale)
        house_height = int(90 * self.scale)
        pygame.draw.rect(screen, COLORS['wood_brown'], (base_x, base_y, house_width, house_height))
        for i in range(0, house_width, int(12 * self.scale)):
            pygame.draw.line(screen, COLORS['dark_wood'],
                           (base_x + i, base_y), (base_x + i, base_y + house_height), 3)
            pygame.draw.line(screen, COLORS['shadow'],
                           (base_x + i + 2, base_y), (base_x + i + 2, base_y + house_height), 1)
        pygame.draw.rect(screen, COLORS['stone_gray'],
                        (base_x - 5, base_y + house_height, house_width + 10, 8))
        roof_points = [
            (base_x - 15 * self.scale, base_y),
            (base_x + house_width // 2, base_y - 50 * self.scale),
            (base_x + house_width + 15 * self.scale, base_y)
        ]
        pygame.draw.polygon(screen, COLORS['slate_blue'], roof_points)
        for row in range(5):
            y_pos = base_y - 45 * self.scale + row * 10 * self.scale
            x_start = base_x - 10 * self.scale + row * 8 * self.scale
            x_end = base_x + house_width + 10 * self.scale - row * 8 * self.scale
            pygame.draw.line(screen, COLORS['roof_gray'], (x_start, y_pos), (x_end, y_pos), 2)
        chimney_x = base_x + house_width - 30 * self.scale
        chimney_y = base_y - 60 * self.scale
        chimney_width = int(18 * self.scale)
        chimney_height = int(40 * self.scale)
        pygame.draw.rect(screen, COLORS['brick_red'],
                        (chimney_x, chimney_y, chimney_width, chimney_height))
        for brick_y in range(int(chimney_y), int(chimney_y + chimney_height), int(6 * self.scale)):
            for brick_x in range(int(chimney_x), int(chimney_x + chimney_width), int(9 * self.scale)):
                pygame.draw.rect(screen, COLORS['brick_shadow'],
                               (brick_x, brick_y, 8 * self.scale, 5 * self.scale), 1)
        pygame.draw.rect(screen, COLORS['shadow'],
                        (chimney_x - 2 * self.scale, chimney_y, chimney_width + 4 * self.scale, 3 * self.scale))
        window_size = int(18 * self.scale)
        for i, wx in enumerate([base_x + 25 * self.scale, base_x + 60 * self.scale, base_x + 95 * self.scale]):
            has_light = self.has_lights and i == 1
            DetailedWindow.draw(screen, int(wx), int(base_y + 30 * self.scale), window_size, window_size, has_light)
        door_x = base_x + 20 * self.scale
        door_y = base_y + 50 * self.scale
        door_width = int(22 * self.scale)
        door_height = int(40 * self.scale)
        pygame.draw.rect(screen, COLORS['dark_wood'], (door_x, door_y, door_width, door_height))
        panel_margin = 3 * self.scale
        pygame.draw.rect(screen, COLORS['wood_brown'],
                        (door_x + panel_margin, door_y + panel_margin,
                         door_width - 2 * panel_margin, door_height // 2 - 1.5 * panel_margin))
        pygame.draw.rect(screen, COLORS['wood_brown'],
                        (door_x + panel_margin, door_y + door_height // 2 + 0.5 * panel_margin,
                         door_width - 2 * panel_margin, door_height // 2 - 1.5 * panel_margin))
        pygame.draw.circle(screen, COLORS['brass'],
                         (int(door_x + door_width - 6 * self.scale), int(door_y + door_height // 2)),
                         int(3 * self.scale))
    
    def draw_colonial_mansion(self, screen):
        base_x = int(self.x)
        base_y = int(self.y)
        house_width = int(180 * self.scale)
        house_height = int(110 * self.scale)
        pygame.draw.rect(screen, COLORS['brick_red'], (base_x, base_y, house_width, house_height))
        brick_height = int(6 * self.scale)
        brick_width = int(25 * self.scale)
        for row in range(0, int(house_height), brick_height):
            offset = (row // brick_height) % 2 * (brick_width // 2)
            for col in range(-brick_width, int(house_width) + brick_width, brick_width):
                brick_x = base_x + col + offset
                brick_y = base_y + row
                pygame.draw.rect(screen, COLORS['bright_red'],
                               (brick_x + 1, brick_y + 1, brick_width - 2, brick_height - 2))
                pygame.draw.rect(screen, COLORS['parchment'],
                               (brick_x, brick_y, brick_width, brick_height), 1)
        pygame.draw.rect(screen, COLORS['stone_gray'],
                        (base_x - 8, base_y + house_height, house_width + 16, 12))
        quoin_width = int(8 * self.scale)
        for i in range(0, int(house_height), int(15 * self.scale)):
            pygame.draw.rect(screen, COLORS['parchment'],
                           (base_x - quoin_width, base_y + i, quoin_width, 12 * self.scale))
            pygame.draw.rect(screen, COLORS['parchment'],
                           (base_x + house_width, base_y + i, quoin_width, 12 * self.scale))
        roof_height = int(60 * self.scale)
        roof_points = [
            (base_x - 20 * self.scale, base_y),
            (base_x + house_width // 2, base_y - roof_height),
            (base_x + house_width + 20 * self.scale, base_y)
        ]
        pygame.draw.polygon(screen, COLORS['slate_blue'], roof_points)
        for row in range(8):
            y_pos = base_y - roof_height + row * 8 * self.scale
            x_start = base_x - 18 * self.scale + row * 12 * self.scale
            x_end = base_x + house_width + 18 * self.scale - row * 12 * self.scale
            pygame.draw.line(screen, COLORS['roof_gray'], (x_start, y_pos), (x_end, y_pos), 2)
        for side, chimney_x in enumerate([base_x + 45 * self.scale, base_x + house_width - 63 * self.scale]):
            chimney_width = int(20 * self.scale)
            chimney_height = int(45 * self.scale)
            chimney_y = base_y - roof_height - 12 * self.scale
            pygame.draw.rect(screen, COLORS['brick_red'],
                           (chimney_x, chimney_y, chimney_width, chimney_height))
            for brick_y in range(int(chimney_y), int(chimney_y + chimney_height), int(6 * self.scale)):
                for brick_x in range(int(chimney_x), int(chimney_x + chimney_width), int(10 * self.scale)):
                    pygame.draw.rect(screen, COLORS['brick_shadow'],
                                   (brick_x, brick_y, 9 * self.scale, 5 * self.scale), 1)
            pygame.draw.rect(screen, COLORS['shadow'],
                           (chimney_x - 2 * self.scale, chimney_y, chimney_width + 4 * self.scale, 4 * self.scale))
        window_width = int(22 * self.scale)
        window_height = int(35 * self.scale)
        window_positions = [
            base_x + 30 * self.scale,
            base_x + 79 * self.scale,
            base_x + 128 * self.scale
        ]
        for i, wx in enumerate(window_positions):
            has_light = self.has_lights and i == 1
            DetailedWindow.draw(screen, int(wx), int(base_y + 25 * self.scale),
                              window_width, window_height, has_light)
        door_x = base_x + house_width // 2 - 18 * self.scale
        door_y = base_y + 60 * self.scale
        door_width = int(36 * self.scale)
        door_height = int(50 * self.scale)
        col_width = int(10 * self.scale)
        col_height = door_height + 5 * self.scale
        for col_x in [door_x - 18 * self.scale, door_x + door_width + 8 * self.scale]:
            pygame.draw.rect(screen, COLORS['ivory'], (col_x, door_y - 5 * self.scale, col_width, col_height))
            for i in range(3):
                pygame.draw.line(screen, COLORS['shadow'],
                               (col_x + (i + 1) * col_width // 4, door_y - 5 * self.scale),
                               (col_x + (i + 1) * col_width // 4, door_y + col_height - 5 * self.scale), 1)
            pygame.draw.rect(screen, COLORS['ivory'],
                           (col_x - 2 * self.scale, door_y - 8 * self.scale, col_width + 4 * self.scale, 4 * self.scale))
        pediment_points = [
            (door_x - 22 * self.scale, door_y - 8 * self.scale),
            (door_x + door_width // 2, door_y - 20 * self.scale),
            (door_x + door_width + 22 * self.scale, door_y - 8 * self.scale)
        ]
        pygame.draw.polygon(screen, COLORS['ivory'], pediment_points)
        pygame.draw.polygon(screen, COLORS['shadow'], pediment_points, 2)
        pygame.draw.rect(screen, COLORS['dark_wood'], (door_x, door_y, door_width, door_height))
        panel_margin = 4 * self.scale
        panels = [
            (door_y + panel_margin, door_height // 3 - panel_margin),
            (door_y + door_height // 3 + panel_margin, door_height // 3 - 2 * panel_margin),
            (door_y + 2 * door_height // 3 + panel_margin, door_height // 3 - panel_margin - 4 * self.scale)
        ]
        for panel_y, panel_height in panels:
            pygame.draw.rect(screen, COLORS['wood_brown'],
                           (door_x + panel_margin, panel_y,
                            door_width - 2 * panel_margin, panel_height))
            pygame.draw.rect(screen, COLORS['shadow'],
                           (door_x + panel_margin, panel_y,
                            door_width - 2 * panel_margin, panel_height), 2)
        knocker_x = int(door_x + door_width // 2)
        knocker_y = int(door_y + door_height // 2)
        pygame.draw.circle(screen, COLORS['brass'], (knocker_x, knocker_y), int(4 * self.scale))
        pygame.draw.circle(screen, COLORS['warm_gold'], (knocker_x, knocker_y), int(4 * self.scale), 1)
    
    def draw_cottage(self, screen):
        base_x = int(self.x)
        base_y = int(self.y)
        house_width = int(95 * self.scale)
        house_height = int(70 * self.scale)
        pygame.draw.rect(screen, COLORS['parchment'], (base_x, base_y, house_width, house_height))
        for _ in range(30):
            tx = base_x + random.randint(0, int(house_width))
            ty = base_y + random.randint(0, int(house_height))
            pygame.draw.circle(screen, COLORS['cream'], (tx, ty), 1)
        beam_positions = [house_height // 3, 2 * house_height // 3]
        for beam_y in beam_positions:
            pygame.draw.rect(screen, COLORS['dark_wood'],
                           (base_x, base_y + beam_y, house_width, 4 * self.scale))
        pygame.draw.rect(screen, COLORS['dark_wood'],
                        (base_x + house_width // 2, base_y, 4 * self.scale, house_height))
        pygame.draw.rect(screen, COLORS['dark_wood'], (base_x, base_y, house_width, house_height), 3)
        roof_points = [
            (base_x - 10 * self.scale, base_y + 8 * self.scale),
            (base_x + house_width // 2, base_y - 42 * self.scale),
            (base_x + house_width + 10 * self.scale, base_y + 8 * self.scale)
        ]
        pygame.draw.polygon(screen, COLORS['wood_brown'], roof_points)
        for layer in range(7):
            y_offset = layer * 7 * self.scale
            num_straws = 15
            for i in range(num_straws):
                ratio = i / num_straws
                x_pos = base_x + house_width * ratio
                y_base = base_y + 8 * self.scale - y_offset
                y_peak = base_y - 42 * self.scale + y_offset
                if ratio < 0.5:
                    y_pos = y_base + (y_peak - y_base) * (ratio * 2)
                else:
                    y_pos = y_peak + (y_base - y_peak) * ((ratio - 0.5) * 2)
                pygame.draw.line(screen, COLORS['dark_wood'],
                               (x_pos, y_pos),
                               (x_pos + random.uniform(-2, 2), y_pos + 5 * self.scale), 1)
        window_center_x = int(base_x + house_width // 2)
        window_center_y = int(base_y + 35 * self.scale)
        window_radius = int(14 * self.scale)
        pygame.draw.circle(screen, COLORS['dark_wood'], (window_center_x, window_center_y), window_radius + 2)
        pygame.draw.circle(screen, COLORS['colonial_blue'], (window_center_x, window_center_y), window_radius)
        pygame.draw.line(screen, COLORS['white'],
                        (window_center_x - window_radius, window_center_y),
                        (window_center_x + window_radius, window_center_y), 2)
        pygame.draw.line(screen, COLORS['white'],
                        (window_center_x, window_center_y - window_radius),
                        (window_center_x, window_center_y + window_radius), 2)
        reflet_surf = pygame.Surface((window_radius * 2, window_radius), pygame.SRCALPHA)
        reflet_surf.fill((*COLORS['sky_middle'], 80))
        screen.blit(reflet_surf, (window_center_x - window_radius, window_center_y - window_radius))
        door_x = base_x + house_width // 2 - 12 * self.scale
        door_y = base_y + 43 * self.scale
        door_width = int(24 * self.scale)
        door_height = int(27 * self.scale)
        pygame.draw.rect(screen, COLORS['dark_wood'], (door_x, door_y, door_width, door_height))
        for i in range(5):
            plank_y = door_y + i * 6 * self.scale
            pygame.draw.line(screen, COLORS['wood_brown'],
                           (door_x, plank_y),
                           (door_x + door_width, plank_y), 2)
        pygame.draw.circle(screen, (50, 50, 50),
                         (int(door_x + door_width - 5 * self.scale), int(door_y + door_height // 2)),
                         int(2 * self.scale))
    
    def draw_stone_house(self, screen):
        base_x = int(self.x)
        base_y = int(self.y)
        house_width = int(130 * self.scale)
        house_height = int(85 * self.scale)
        pygame.draw.rect(screen, COLORS['stone_gray'], (base_x, base_y, house_width, house_height))
        stone_pattern = [
            (0, 0, 35, 12), (37, 0, 28, 12), (67, 0, 30, 12),
            (5, 14, 30, 10), (37, 14, 25, 10), (64, 14, 33, 10),
            (0, 26, 32, 11), (34, 26, 29, 11), (65, 26, 32, 11),
        ]
        for row in range(0, int(house_height), int(40 * self.scale)):
            for stone_x, stone_y, stone_w, stone_h in stone_pattern:
                sx = base_x + stone_x * self.scale
                sy = base_y + stone_y * self.scale + row
                sw = stone_w * self.scale
                sh = stone_h * self.scale
                pygame.draw.rect(screen, COLORS['stone_gray'], (sx, sy, sw, sh))
                pygame.draw.rect(screen, COLORS['parchment'], (sx, sy, sw, sh), 2)
                shadow_surf = pygame.Surface((int(sw), int(sh)), pygame.SRCALPHA)
                shadow_surf.fill((*COLORS['shadow'], 30))
                screen.blit(shadow_surf, (int(sx + 2), int(sy + 2)))
        roof_points = [
            (base_x - 12 * self.scale, base_y),
            (base_x + house_width // 2, base_y - 45 * self.scale),
            (base_x + house_width + 12 * self.scale, base_y)
        ]
        pygame.draw.polygon(screen, COLORS['roof_gray'], roof_points)
        for row in range(6):
            y_pos = base_y - 40 * self.scale + row * 7 * self.scale
            x_start = base_x - 10 * self.scale + row * 10 * self.scale
            x_end = base_x + house_width + 10 * self.scale - row * 10 * self.scale
            pygame.draw.line(screen, COLORS['shadow'], (x_start, y_pos), (x_end, y_pos), 2)
        chimney_x = base_x + house_width - 25 * self.scale
        chimney_y = base_y - 55 * self.scale
        pygame.draw.rect(screen, COLORS['stone_gray'],
                        (chimney_x, chimney_y, 16 * self.scale, 35 * self.scale))
        for i in range(4):
            pygame.draw.line(screen, COLORS['parchment'],
                           (chimney_x, chimney_y + i * 9 * self.scale),
                           (chimney_x + 16 * self.scale, chimney_y + i * 9 * self.scale), 2)
        window_width = int(20 * self.scale)
        window_height = int(28 * self.scale)
        for wx in [base_x + 25 * self.scale, base_x + 85 * self.scale]:
            wy = base_y + 30 * self.scale
            arc_points = []
            for angle in range(180, 361, 10):
                rad = math.radians(angle)
                ax = wx + window_width // 2 + math.cos(rad) * (window_width // 2 + 2)
                ay = wy + math.sin(rad) * (window_height // 3)
                arc_points.append((ax, ay))
            if len(arc_points) > 2:
                pygame.draw.polygon(screen, COLORS['parchment'], arc_points)
            has_light = self.has_lights
            DetailedWindow.draw(screen, int(wx), int(wy), window_width, window_height, has_light)
        door_x = base_x + house_width // 2 - 14 * self.scale
        door_y = base_y + 50 * self.scale
        door_width = int(28 * self.scale)
        door_height = int(35 * self.scale)
        arc_points = []
        for angle in range(180, 361, 10):
            rad = math.radians(angle)
            ax = door_x + door_width // 2 + math.cos(rad) * (door_width // 2 + 3)
            ay = door_y + math.sin(rad) * (door_height // 3)
            arc_points.append((ax, ay))
        if len(arc_points) > 2:
            pygame.draw.polygon(screen, COLORS['parchment'], arc_points)
        pygame.draw.rect(screen, COLORS['dark_wood'], (door_x, door_y, door_width, door_height))
        for nail_y in range(int(door_y + 5 * self.scale), int(door_y + door_height), int(8 * self.scale)):
            for nail_x in [door_x + 5 * self.scale, door_x + door_width - 5 * self.scale]:
                pygame.draw.circle(screen, (50, 50, 50), (int(nail_x), int(nail_y)), 2)


class DetailedSoldier:
    def __init__(self, x, y, scale=1.0, facing_right=True, uniform_color='blue', rank='soldier'):
        self.x = x
        self.y = y
        self.scale = scale
        self.facing_right = facing_right
        self.march_phase = random.uniform(0, 2 * math.pi)
        self.march_speed = 0.04
        self.uniform_color = COLORS['colonial_blue'] if uniform_color == 'blue' else COLORS['deep_red']
        self.rank = rank
        self.breathing_phase = random.uniform(0, 2 * math.pi)
        
    def update(self):
        self.march_phase += self.march_speed
        self.breathing_phase += 0.03
    
    def draw(self, screen):
        base_x = int(self.x)
        base_y = int(self.y)
        leg_swing = math.sin(self.march_phase) * 18 * self.scale
        arm_swing = math.sin(self.march_phase + math.pi) * 10 * self.scale
        body_bob = abs(math.sin(self.march_phase * 2)) * 4 * self.scale
        breathing = math.sin(self.breathing_phase) * 1 * self.scale
        shadow_surf = pygame.Surface((int(60 * self.scale), int(20 * self.scale)), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow_surf, (*COLORS['shadow'], 80), (0, 0, int(60 * self.scale), int(20 * self.scale)))
        screen.blit(shadow_surf, (int(base_x - 30 * self.scale), int(base_y + 75 * self.scale)))
        leg_width = int(9 * self.scale)
        leg_height = int(38 * self.scale)
        back_leg_x = base_x - 7 * self.scale
        back_leg_y = base_y + 47 * self.scale - body_bob
        pygame.draw.rect(screen, COLORS['white'],
                        (int(back_leg_x - leg_swing // 2), int(back_leg_y),
                         leg_width, leg_height))
        shadow_rect = pygame.Surface((leg_width, leg_height), pygame.SRCALPHA)
        shadow_rect.fill((*COLORS['shadow'], 40))
        screen.blit(shadow_rect, (int(back_leg_x - leg_swing // 2 + 1), int(back_leg_y + 1)))
        boot_height = int(12 * self.scale)
        pygame.draw.rect(screen, (20, 20, 20),
                        (int(back_leg_x - leg_swing // 2), int(back_leg_y + leg_height - boot_height),
                         leg_width, boot_height))
        pygame.draw.line(screen, (60, 60, 60),
                        (int(back_leg_x - leg_swing // 2 + 2), int(back_leg_y + leg_height - boot_height + 2)),
                        (int(back_leg_x - leg_swing // 2 + 2), int(back_leg_y + leg_height - 2)), 1)
        front_leg_x = base_x + 3 * self.scale
        pygame.draw.rect(screen, COLORS['white'],
                        (int(front_leg_x + leg_swing // 2), int(back_leg_y),
                         leg_width, leg_height))
        shadow_rect = pygame.Surface((leg_width, leg_height), pygame.SRCALPHA)
        shadow_rect.fill((*COLORS['shadow'], 40))
        screen.blit(shadow_rect, (int(front_leg_x + leg_swing // 2 + 1), int(back_leg_y + 1)))
        pygame.draw.rect(screen, (20, 20, 20),
                        (int(front_leg_x + leg_swing // 2), int(back_leg_y + leg_height - boot_height),
                         leg_width, boot_height))
        pygame.draw.line(screen, (60, 60, 60),
                        (int(front_leg_x + leg_swing // 2 + 2), int(back_leg_y + leg_height - boot_height + 2)),
                        (int(front_leg_x + leg_swing // 2 + 2), int(back_leg_y + leg_height - 2)), 1)
        body_x = base_x - 14 * self.scale
        body_y = base_y + 17 * self.scale - body_bob + breathing
        body_width = int(28 * self.scale)
        body_height = int(38 * self.scale)
        pygame.draw.rect(screen, self.uniform_color,
                        (int(body_x), int(body_y), body_width, body_height))
        shadow_body = pygame.Surface((body_width, body_height), pygame.SRCALPHA)
        shadow_body.fill((*COLORS['shadow'], 50))
        screen.blit(shadow_body, (int(body_x + 2), int(body_y + 2)))
        lapel_points_left = [
            (int(body_x + 4 * self.scale), int(body_y)),
            (int(body_x + 4 * self.scale), int(body_y + 18 * self.scale)),
            (int(body_x + 10 * self.scale), int(body_y + 12 * self.scale)),
            (int(body_x + 10 * self.scale), int(body_y))
        ]
        pygame.draw.polygon(screen, COLORS['white'], lapel_points_left)
        lapel_points_right = [
            (int(body_x + body_width - 4 * self.scale), int(body_y)),
            (int(body_x + body_width - 4 * self.scale), int(body_y + 18 * self.scale)),
            (int(body_x + body_width - 10 * self.scale), int(body_y + 12 * self.scale)),
            (int(body_x + body_width - 10 * self.scale), int(body_y))
        ]
        pygame.draw.polygon(screen, COLORS['white'], lapel_points_right)
        button_positions = [10, 17, 24, 31]
        for i, button_y_offset in enumerate(button_positions):
            button_y = body_y + button_y_offset * self.scale
            pygame.draw.circle(screen, COLORS['brass'],
                             (int(base_x), int(button_y)), int(3 * self.scale))
            pygame.draw.circle(screen, COLORS['warm_gold'],
                             (int(base_x - 1 * self.scale), int(button_y - 1 * self.scale)), int(1 * self.scale))
        pygame.draw.rect(screen, COLORS['white'],
                        (int(body_x), int(body_y + 20 * self.scale),
                         body_width, int(4 * self.scale)))
        pygame.draw.rect(screen, COLORS['brass'],
                        (int(base_x - 4 * self.scale), int(body_y + 19 * self.scale),
                         8 * self.scale, 6 * self.scale))
        pygame.draw.rect(screen, self.uniform_color,
                        (int(base_x - 3 * self.scale), int(body_y + 20 * self.scale),
                         6 * self.scale, 4 * self.scale))
        if self.rank in ['officer', 'sergeant']:
            pygame.draw.rect(screen, COLORS['warm_gold'],
                           (int(body_x + 2 * self.scale), int(body_y),
                            10 * self.scale, 4 * self.scale))
            for i in range(5):
                pygame.draw.line(screen, COLORS['warm_gold'],
                               (int(body_x + 2 * self.scale + i * 2 * self.scale), int(body_y + 4 * self.scale)),
                               (int(body_x + 2 * self.scale + i * 2 * self.scale), int(body_y + 8 * self.scale)), 1)
            pygame.draw.rect(screen, COLORS['warm_gold'],
                           (int(body_x + body_width - 12 * self.scale), int(body_y),
                            10 * self.scale, 4 * self.scale))
            for i in range(5):
                pygame.draw.line(screen, COLORS['warm_gold'],
                               (int(body_x + body_width - 12 * self.scale + i * 2 * self.scale), int(body_y + 4 * self.scale)),
                               (int(body_x + body_width - 12 * self.scale + i * 2 * self.scale), int(body_y + 8 * self.scale)), 1)
        arm_width = int(8 * self.scale)
        arm_length = int(32 * self.scale)
        back_arm_x = base_x - 17 * self.scale
        back_arm_y = body_y + 10 * self.scale
        pygame.draw.rect(screen, self.uniform_color,
                        (int(back_arm_x), int(back_arm_y + arm_swing),
                         arm_width, arm_length))
        pygame.draw.circle(screen, COLORS['parchment'],
                         (int(back_arm_x + arm_width // 2),
                          int(back_arm_y + arm_length + arm_swing)),
                         int(5 * self.scale))
        musket_length = int(70 * self.scale)
        musket_angle = -0.7 if self.facing_right else -2.4
        musket_x = base_x
        musket_y = body_y + 18 * self.scale
        stock_length = int(20 * self.scale)
        stock_end_x = musket_x - math.cos(musket_angle) * stock_length
        stock_end_y = musket_y - math.sin(musket_angle) * stock_length
        pygame.draw.line(screen, COLORS['wood_brown'],
                        (musket_x, musket_y),
                        (stock_end_x, stock_end_y),
                        int(6 * self.scale))
        musket_end_x = musket_x + math.cos(musket_angle) * musket_length
        musket_end_y = musket_y + math.sin(musket_angle) * musket_length
        pygame.draw.line(screen, COLORS['gunpowder'],
                        (musket_x, musket_y),
                        (musket_end_x, musket_end_y),
                        int(4 * self.scale))
        highlight_length = musket_length * 0.7
        highlight_end_x = musket_x + math.cos(musket_angle) * highlight_length
        highlight_end_y = musket_y + math.sin(musket_angle) * highlight_length
        pygame.draw.line(screen, (120, 120, 120),
                        (musket_x, musket_y - 1),
                        (highlight_end_x, highlight_end_y - 1),
                        1)
        bayonet_length = int(15 * self.scale)
        bayonet_end_x = musket_end_x + math.cos(musket_angle) * bayonet_length
        bayonet_end_y = musket_end_y + math.sin(musket_angle) * bayonet_length
        pygame.draw.line(screen, (200, 200, 200),
                        (musket_end_x, musket_end_y),
                        (bayonet_end_x, bayonet_end_y),
                        2)
        flint_x = musket_x + math.cos(musket_angle) * 15 * self.scale
        flint_y = musket_y + math.sin(musket_angle) * 15 * self.scale
        pygame.draw.circle(screen, (80, 80, 80), (int(flint_x), int(flint_y)), int(3 * self.scale))
        front_arm_x = base_x + 6 * self.scale
        front_arm_y = body_y + 10 * self.scale
        pygame.draw.rect(screen, self.uniform_color,
                        (int(front_arm_x), int(front_arm_y - arm_swing),
                         arm_width, arm_length))
        hand_on_musket_x = musket_x + math.cos(musket_angle) * 30 * self.scale
        hand_on_musket_y = musket_y + math.sin(musket_angle) * 30 * self.scale
        pygame.draw.circle(screen, COLORS['parchment'],
                         (int(hand_on_musket_x), int(hand_on_musket_y)),
                         int(5 * self.scale))
        head_x = base_x
        head_y = body_y - 10 * self.scale + breathing
        head_radius = int(11 * self.scale)
        pygame.draw.rect(screen, COLORS['parchment'],
                        (int(head_x - 3 * self.scale), int(body_y - 2 * self.scale),
                         6 * self.scale, 5 * self.scale))
        pygame.draw.circle(screen, COLORS['parchment'], (head_x, int(head_y)), head_radius)
        shadow_face = pygame.Surface((head_radius * 2, head_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(shadow_face, (*COLORS['shadow'], 30),
                         (head_radius, head_radius), head_radius)
        screen.blit(shadow_face, (int(head_x - head_radius + 2), int(head_y - head_radius + 2)))
        pygame.draw.circle(screen, (0, 0, 0),
                         (head_x, int(head_y - 4 * self.scale)),
                         int(14 * self.scale))
        tricorne_points = [
            (head_x - 18 * self.scale, head_y - 10 * self.scale),
            (head_x - 3 * self.scale, head_y - 22 * self.scale),
            (head_x, head_y - 24 * self.scale),
            (head_x + 3 * self.scale, head_y - 22 * self.scale),
            (head_x + 18 * self.scale, head_y - 10 * self.scale),
            (head_x + 10 * self.scale, head_y - 4 * self.scale),
            (head_x - 10 * self.scale, head_y - 4 * self.scale)
        ]
        pygame.draw.polygon(screen, (0, 0, 0),
                          [(int(p[0]), int(p[1])) for p in tricorne_points])
        pygame.draw.polygon(screen, COLORS['warm_gold'],
                          [(int(p[0]), int(p[1])) for p in tricorne_points], 2)
        if self.rank == 'officer':
            pygame.draw.circle(screen, COLORS['warm_gold'],
                             (int(head_x - 10 * self.scale), int(head_y - 10 * self.scale)), int(4 * self.scale))
            pygame.draw.circle(screen, COLORS['deep_red'],
                             (int(head_x - 10 * self.scale), int(head_y - 10 * self.scale)), int(2 * self.scale))
        else:
            pygame.draw.circle(screen, COLORS['warm_gold'],
                             (int(head_x - 10 * self.scale), int(head_y - 10 * self.scale)), int(3 * self.scale))
        eye_y = int(head_y - 2 * self.scale)
        pygame.draw.circle(screen, (0, 0, 0),
                         (int(head_x - 4 * self.scale), eye_y), 2)
        pygame.draw.circle(screen, (0, 0, 0),
                         (int(head_x + 4 * self.scale), eye_y), 2)
        pygame.draw.line(screen, COLORS['wood_brown'],
                        (int(head_x - 6 * self.scale), int(eye_y - 2 * self.scale)),
                        (int(head_x - 2 * self.scale), int(eye_y - 3 * self.scale)), 1)
        pygame.draw.line(screen, COLORS['wood_brown'],
                        (int(head_x + 2 * self.scale), int(eye_y - 3 * self.scale)),
                        (int(head_x + 6 * self.scale), int(eye_y - 2 * self.scale)), 1)
        pygame.draw.line(screen, COLORS['shadow'],
                        (int(head_x), int(eye_y + 1)),
                        (int(head_x), int(eye_y + 5)), 1)
        pygame.draw.line(screen, COLORS['shadow'],
                        (int(head_x - 3 * self.scale), int(head_y + 5 * self.scale)),
                        (int(head_x + 3 * self.scale), int(head_y + 5 * self.scale)), 1)


class Button:
    """Bouton interactif pour le menu"""
    
    def __init__(self, x, y, width, height, text, font_size=36, 
                 color=(178, 34, 52), hover_color=(220, 50, 70)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.is_hovered = False
    
    def update(self, mouse_pos):
        """Met à jour l'état du bouton"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.current_color = self.hover_color if self.is_hovered else self.color
    
    def draw(self, screen):
        """Dessine le bouton"""
        shadow_rect = self.rect.copy()
        shadow_rect.x += 4
        shadow_rect.y += 4
        pygame.draw.rect(screen, (20, 20, 40), shadow_rect, border_radius=10)
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)
        pygame.draw.rect(screen, (255, 215, 0), self.rect, 3, border_radius=10)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, event):
        """Vérifie si le bouton est cliqué"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False


class MainMenu:
    """Menu principal colonial du jeu"""
    
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.clock = pygame.time.Clock()
        
        # Polices
        self.font_title = pygame.font.Font(None, 80)
        self.font_subtitle = pygame.font.Font(None, 45)
        self.font_large = pygame.font.Font(None, 60)
        self.font_medium = pygame.font.Font(None, 45)
        self.font_small = pygame.font.Font(None, 35)
        
        # Options du menu
        self.options = ["NOUVELLE PARTIE", "BOUTIQUE", "CREDITS", "QUITTER"]
        self.selected = 0
        
        # Éléments animés
        self.clouds = [
            Cloud(100, 100, 1.2, 0.15),
            Cloud(400, 80, 1.5, 0.1),
            Cloud(800, 120, 1.0, 0.2),
            Cloud(1100, 90, 1.3, 0.12),
        ]
        self.birds = [Bird(random.randint(0, self.screen_width), random.randint(50, 250)) for _ in range(8)]
        
        # Maisons coloniales
        self.houses = []
        for i in range(5):
            x = i * 220 + random.randint(-40, 40)
            y = 450 + random.randint(-25, 25)
            scale = random.uniform(0.8, 1.1)
            house_type = random.randint(0, 3)
            self.houses.append(ColonialHouse(x, y, house_type, scale))
        
        # Soldats
        self.soldiers = [
            DetailedSoldier(130, 490, 1.2, True, 'blue', 'officer'),
            DetailedSoldier(240, 495, 1.0, True, 'blue', 'soldier'),
            DetailedSoldier(350, 493, 1.1, True, 'blue', 'sergeant'),
            DetailedSoldier(460, 494, 0.9, False, 'red', 'soldier'),
            DetailedSoldier(self.screen_width - 350, 495, 1.0, False, 'blue', 'soldier'),
            DetailedSoldier(self.screen_width - 240, 490, 1.1, False, 'red', 'sergeant'),
            DetailedSoldier(self.screen_width - 130, 493, 0.9, False, 'blue', 'soldier'),
        ]
        
        # Effets visuels
        self.muzzle_flashes = []
        self.smoke_particles = []
        self.time = 0
        self.sun_position = 0
        
        # Données du joueur
        self.player_data = None
    
    def set_player_data(self, player_data):
        """Définit les données du joueur"""
        self.player_data = player_data
    
    def fire_musket(self, soldier_index):
        """Fait tirer un soldat"""
        soldier = self.soldiers[soldier_index]
        musket_angle = -0.7 if soldier.facing_right else -2.4
        flash_distance = 60 * soldier.scale
        flash_x = soldier.x + math.cos(musket_angle) * flash_distance
        flash_y = soldier.y + 18 * soldier.scale - 10 * soldier.scale + math.sin(musket_angle) * flash_distance
        self.muzzle_flashes.append(MuzzleFlash(flash_x, flash_y, musket_angle))
        for _ in range(25):
            angle = musket_angle + random.uniform(-0.4, 0.4)
            speed = random.uniform(2.5, 6.0)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            self.smoke_particles.append(SmokeParticle(flash_x, flash_y, vx, vy))
    
    def update(self, dt=None):
        """Met à jour le menu"""
        self.time += 0.015
        self.sun_position = (self.sun_position + 0.1) % 360
        
        for cloud in self.clouds:
            cloud.update()
        for bird in self.birds:
            bird.update()
        for house in self.houses:
            house.update()
        for soldier in self.soldiers:
            soldier.update()
        for flash in self.muzzle_flashes[:]:
            flash.update()
            if flash.lifetime <= 0:
                self.muzzle_flashes.remove(flash)
        for smoke in self.smoke_particles[:]:
            smoke.update()
            if smoke.lifetime <= 0:
                self.smoke_particles.remove(smoke)
    
    def draw_sky(self):
        """Dessine le ciel avec dégradé"""
        for y in range(self.screen_height // 2 + 50):
            ratio = y / (self.screen_height // 2 + 50)
            if ratio < 0.6:
                r = int(COLORS['sky_top'][0] + (COLORS['sky_middle'][0] - COLORS['sky_top'][0]) * (ratio / 0.6))
                g = int(COLORS['sky_top'][1] + (COLORS['sky_middle'][1] - COLORS['sky_top'][1]) * (ratio / 0.6))
                b = int(COLORS['sky_top'][2] + (COLORS['sky_middle'][2] - COLORS['sky_top'][2]) * (ratio / 0.6))
            else:
                local_ratio = (ratio - 0.6) / 0.4
                r = int(COLORS['sky_middle'][0] + (COLORS['sky_horizon'][0] - COLORS['sky_middle'][0]) * local_ratio)
                g = int(COLORS['sky_middle'][1] + (COLORS['sky_horizon'][1] - COLORS['sky_middle'][1]) * local_ratio)
                b = int(COLORS['sky_middle'][2] + (COLORS['sky_horizon'][2] - COLORS['sky_middle'][2]) * local_ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (self.screen_width, y))
        
        # Soleil avec halo
        sun_x = self.screen_width - 200
        sun_y = 150
        for i in range(5, 0, -1):
            halo_surf = pygame.Surface((120 + i * 20, 120 + i * 20), pygame.SRCALPHA)
            pygame.draw.circle(halo_surf, (*COLORS['sun_glow'], 20 // i),
                             ((120 + i * 20) // 2, (120 + i * 20) // 2),
                             (120 + i * 20) // 2)
            self.screen.blit(halo_surf, (sun_x - (120 + i * 20) // 2, sun_y - (120 + i * 20) // 2))
        pygame.draw.circle(self.screen, COLORS['flash_yellow'], (sun_x, sun_y), 45)
        pygame.draw.circle(self.screen, COLORS['sun_glow'], (sun_x, sun_y), 40)
        pygame.draw.circle(self.screen, COLORS['white'], (sun_x - 10, sun_y - 10), 12)
    
    def draw_background(self):
        """Dessine le fond avec collines et route"""
        self.draw_sky()
        
        for cloud in self.clouds:
            cloud.draw(self.screen)
        for bird in self.birds:
            bird.draw(self.screen)
        
        # Collines
        hill_layers = [
            (420, COLORS['forest_green'], 35),
            (390, COLORS['dark_green'], 30),
            (360, (49, 107, 64), 25),
        ]
        for base_y, color, amplitude in hill_layers:
            hill_points = []
            for x in range(0, self.screen_width + 30, 20):
                y = base_y + math.sin(x * 0.008 + self.time + amplitude) * amplitude
                hill_points.append((x, y))
            hill_points.append((self.screen_width, self.screen_height // 2))
            hill_points.append((0, self.screen_height // 2))
            pygame.draw.polygon(self.screen, color, hill_points)
        
        # Herbe
        grass_base = self.screen_height // 2
        pygame.draw.rect(self.screen, COLORS['grass_green'],
                        (0, grass_base, self.screen_width, self.screen_height // 2))
        for _ in range(200):
            gx = random.randint(0, self.screen_width)
            gy = random.randint(grass_base, self.screen_height // 2 + 100)
            grass_color = random.choice([COLORS['grass_green'], COLORS['dark_green'], COLORS['forest_green']])
            pygame.draw.line(self.screen, grass_color, (gx, gy), (gx, gy + 3), 1)
        
        # Route
        road_y = 600
        road_height = 70
        pygame.draw.rect(self.screen, COLORS['dirt_brown'],
                        (0, road_y, self.screen_width, road_height))
        for _ in range(150):
            rx = random.randint(0, self.screen_width)
            ry = random.randint(road_y, road_y + road_height)
            pygame.draw.circle(self.screen, COLORS['dark_wood'], (rx, ry), 1)
        for x in range(0, self.screen_width, 50):
            pygame.draw.line(self.screen, COLORS['shadow'],
                           (x, road_y + 20), (x + 40, road_y + 20), 3)
            pygame.draw.line(self.screen, COLORS['shadow'],
                           (x, road_y + 50), (x + 40, road_y + 50), 3)
        
        # Herbes devant la route
        for x in range(0, self.screen_width, 8):
            sway = math.sin(self.time * 2 + x * 0.08) * 3
            height = random.randint(18, 40)
            grass_color = random.choice([COLORS['dark_green'], COLORS['forest_green']])
            pygame.draw.line(self.screen, grass_color,
                           (x, road_y),
                           (x + sway, road_y - height), 2)
            pygame.draw.circle(self.screen, grass_color,
                             (int(x + sway), int(road_y - height)), 1)
    
    def draw(self):
        """Dessine le menu complet"""
        self.draw_background()
        
        for house in self.houses:
            house.draw(self.screen)
        for soldier in self.soldiers:
            soldier.draw(self.screen)
        for smoke in self.smoke_particles:
            smoke.draw(self.screen)
        for flash in self.muzzle_flashes:
            flash.draw(self.screen)

        # === PANNEAU DE TITRE ===
        panel_y = 15
        panel_height = 180
        
        overlay = pygame.Surface((self.screen_width - 40, panel_height), pygame.SRCALPHA)
        overlay.fill((*COLORS['parchment'], 250))
        for i in range(3):
            thickness = 10 - i * 2
            offset = i * 3
            pygame.draw.rect(overlay, COLORS['warm_gold'],
                           (offset, offset, 
                            self.screen_width - 40 - 2 * offset, 
                            panel_height - 2 * offset), thickness)
        self.screen.blit(overlay, (20, panel_y))

        # Coins décorés (étoiles)
        corner_positions = [
            (35, panel_y + 15), (self.screen_width - 65, panel_y + 15),
            (35, panel_y + panel_height - 15), (self.screen_width - 65, panel_y + panel_height - 15)
        ]
        for corner_x, corner_y in corner_positions:
            star_points = []
            for i in range(16):
                angle = i * math.pi / 8 + self.time * 2
                radius = 15 if i % 2 == 0 else 7
                sx = corner_x + math.cos(angle) * radius
                sy = corner_y + math.sin(angle) * radius
                star_points.append((sx, sy))
            pygame.draw.polygon(self.screen, COLORS['warm_gold'], star_points)
            pygame.draw.polygon(self.screen, COLORS['brass'], star_points, 2)

        # === TITRE PRINCIPAL ===
        title_text = "PHILADELPHIA LIBERTY"
        title_y = panel_y + 50
        
        # Ombre portée du titre
        for offset_val in range(10, 0, -1):
            shadow_alpha = 60 - offset_val * 4
            shadow_surf = self.font_title.render(title_text, True, COLORS['shadow'])
            shadow_rect = shadow_surf.get_rect(center=(self.screen_width // 2 + offset_val, title_y + offset_val))
            s = pygame.Surface(shadow_surf.get_size(), pygame.SRCALPHA)
            s.fill((*COLORS['shadow'], shadow_alpha))
            s.blit(shadow_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            self.screen.blit(s, shadow_rect)
        
        # Contour doré
        title_surf = self.font_title.render(title_text, True, COLORS['deep_red'])
        title_rect = title_surf.get_rect(center=(self.screen_width // 2, title_y))
        outline_surf = self.font_title.render(title_text, True, COLORS['warm_gold'])
        for ang in range(0, 360, 25):
            offset_x = math.cos(math.radians(ang)) * 5
            offset_y = math.sin(math.radians(ang)) * 5
            self.screen.blit(outline_surf, (title_rect.x + offset_x, title_rect.y + offset_y))
        self.screen.blit(title_surf, title_rect)

        # === SOUS-TITRE ===
        subtitle_text = "250ème Anniversaire de l'Indépendance"
        subtitle_y = panel_y + 105
        
        subtitle_surf = self.font_subtitle.render(subtitle_text, True, COLORS['colonial_blue'])
        subtitle_rect = subtitle_surf.get_rect(center=(self.screen_width // 2, subtitle_y))
        outline_subtitle = self.font_subtitle.render(subtitle_text, True, COLORS['warm_gold'])
        for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (-2, 0), (2, 0), (0, -2), (0, 2)]:
            self.screen.blit(outline_subtitle, (subtitle_rect.x + dx, subtitle_rect.y + dy))
        self.screen.blit(subtitle_surf, subtitle_rect)

        # Ligne décorative
        line_y = panel_y + 145
        line_center = self.screen_width // 2
        pygame.draw.line(self.screen, COLORS['warm_gold'],
                        (line_center - 350, line_y),
                        (line_center + 350, line_y), 5)
        
        for ornament_x in [line_center - 300, line_center - 150, line_center, line_center + 150, line_center + 300]:
            pygame.draw.circle(self.screen, COLORS['warm_gold'], (ornament_x, line_y), 8)
            pygame.draw.circle(self.screen, COLORS['deep_red'], (ornament_x, line_y), 5)

        # === PANNEAU DE MENU (OPTIONS) ===
        menu_panel_y = 210
        menu_panel_height = 380
        
        menu_overlay = pygame.Surface((self.screen_width - 40, menu_panel_height), pygame.SRCALPHA)
        menu_overlay.fill((*COLORS['parchment'], 245))
        for i in range(3):
            thickness = 8 - i * 2
            offset = i * 3
            pygame.draw.rect(menu_overlay, COLORS['warm_gold'],
                           (offset, offset, 
                            self.screen_width - 40 - 2 * offset, 
                            menu_panel_height - 2 * offset), thickness)
        self.screen.blit(menu_overlay, (20, menu_panel_y))

        # Coins décorés du panneau menu
        menu_corner_positions = [
            (35, menu_panel_y + 15), (self.screen_width - 65, menu_panel_y + 15),
            (35, menu_panel_y + menu_panel_height - 15), (self.screen_width - 65, menu_panel_y + menu_panel_height - 15)
        ]
        for corner_x, corner_y in menu_corner_positions:
            star_points = []
            for i in range(16):
                angle = i * math.pi / 8 - self.time * 2
                radius = 15 if i % 2 == 0 else 7
                sx = corner_x + math.cos(angle) * radius
                sy = corner_y + math.sin(angle) * radius
                star_points.append((sx, sy))
            pygame.draw.polygon(self.screen, COLORS['warm_gold'], star_points)
            pygame.draw.polygon(self.screen, COLORS['brass'], star_points, 2)

        # === OPTIONS DU MENU ===
        for i, option in enumerate(self.options):
            is_selected = (i == self.selected)
            option_y = menu_panel_y + 55 + i * 62
            
            if is_selected:
                sel_width = 420
                sel_height = 50
                sel_rect = pygame.Rect(self.screen_width // 2 - sel_width // 2, option_y - 20, sel_width, sel_height)
                sel_surf = pygame.Surface((sel_width, sel_height), pygame.SRCALPHA)
                for sy in range(sel_height):
                    alpha = 200 - abs(sy - sel_height // 2) * 2
                    pygame.draw.line(sel_surf, (*COLORS['warm_gold'], alpha),
                                   (0, sy), (sel_width, sy))
                self.screen.blit(sel_surf, sel_rect)
                pygame.draw.rect(self.screen, COLORS['brass'], sel_rect, 4)

                # Étoiles de sélection
                star_positions = [
                    (self.screen_width // 2 - 230, option_y),
                    (self.screen_width // 2 + 230, option_y)
                ]
                for star_x, star_y in star_positions:
                    star_pts = []
                    for j in range(10):
                        ang = j * 2 * math.pi / 10 + self.time * 3
                        rad = 18 if j % 2 == 0 else 8
                        spx = star_x + math.cos(ang) * rad
                        spy = star_y + math.sin(ang) * rad
                        star_pts.append((spx, spy))
                    pygame.draw.polygon(self.screen, COLORS['deep_red'], star_pts)
                    pygame.draw.polygon(self.screen, COLORS['warm_gold'], star_pts, 2)

                # Flèches de sélection
                arrow_left = [
                    (self.screen_width // 2 - 195, option_y),
                    (self.screen_width // 2 - 180, option_y - 8),
                    (self.screen_width // 2 - 180, option_y + 8)
                ]
                arrow_right = [
                    (self.screen_width // 2 + 195, option_y),
                    (self.screen_width // 2 + 180, option_y - 8),
                    (self.screen_width // 2 + 180, option_y + 8)
                ]
                pygame.draw.polygon(self.screen, COLORS['deep_red'], arrow_left)
                pygame.draw.polygon(self.screen, COLORS['deep_red'], arrow_right)
                color = COLORS['deep_red']
            else:
                color = COLORS['colonial_blue']

            # Ombre du texte
            shadow_surf = self.font_large.render(option, True, COLORS['shadow'])
            shadow_rect = shadow_surf.get_rect(center=(self.screen_width // 2 + 4, option_y + 4))
            s = pygame.Surface(shadow_surf.get_size(), pygame.SRCALPHA)
            s.fill((*COLORS['shadow'], 140))
            s.blit(shadow_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            self.screen.blit(s, shadow_rect)

            # Texte principal
            option_surf = self.font_large.render(option, True, color)
            option_rect = option_surf.get_rect(center=(self.screen_width // 2, option_y))
            self.screen.blit(option_surf, option_rect)

            if is_selected:
                outline_option = self.font_large.render(option, True, COLORS['warm_gold'])
                for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
                    self.screen.blit(outline_option, (option_rect.x + dx, option_rect.y + dy))
                self.screen.blit(option_surf, option_rect)
        
        # Afficher l'or si disponible
        if self.player_data:
            self._draw_gold_display()
    
    def _draw_gold_display(self):
        """Affiche l'or du joueur"""
        gold_bg = pygame.Rect(self.screen_width - 180, 15, 160, 45)
        pygame.draw.rect(self.screen, (20, 40, 20, 200), gold_bg, border_radius=8)
        pygame.draw.rect(self.screen, COLORS['warm_gold'], gold_bg, 2, border_radius=8)
        
        gold_font = pygame.font.Font(None, 36)
        gold_text = gold_font.render(f"$ {self.player_data.gold:,}", True, COLORS['warm_gold'])
        self.screen.blit(gold_text, (self.screen_width - 170, 25))
    
    def handle_event(self, event):
        """Gère les événements du menu"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                for i in range(len(self.soldiers)):
                    self.fire_musket(i)
                return self.get_action()
       
        # Support souris
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            menu_panel_y = 210
            for i, option in enumerate(self.options):
                option_y = menu_panel_y + 55 + i * 62
                option_rect = pygame.Rect(self.screen_width // 2 - 210, option_y - 25, 420, 50)
                if option_rect.collidepoint(mouse_pos):
                    self.selected = i
                    for j in range(len(self.soldiers)):
                        self.fire_musket(j)
                    return self.get_action()
        
        # Survol souris
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            menu_panel_y = 210
            for i, option in enumerate(self.options):
                option_y = menu_panel_y + 55 + i * 62
                option_rect = pygame.Rect(self.screen_width // 2 - 210, option_y - 25, 420, 50)
                if option_rect.collidepoint(mouse_pos):
                    self.selected = i
        
        return None
    
    def get_action(self):
        """Retourne l'action correspondant à l'option sélectionnée"""
        option = self.options[self.selected]
        if option == "NOUVELLE PARTIE":
            return "play"
        elif option == "BOUTIQUE":
            return "shop"
        elif option == "CREDITS":
            return "credits"
        elif option == "QUITTER":
            return "quit"
        return None
 
class LevelSelectMenu:
    """Menu de sélection des niveaux"""
    
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        self.title_font = pygame.font.Font(None, 60)
        self.font = pygame.font.Font(None, 32)
        
        # Définition des niveaux
        self.levels = [
            {"name": "Camp de Lexington", "description": "Zone d'entraînement - 10 ennemis", 
            "enemies": 10, "unlocked": True, "map_type": "warehouse"},
            {"name": "Fort Ticonderoga", "description": "Base militaire - 20 ennemis", 
            "enemies": 20, "unlocked": True, "map_type": "military"},
            {"name": "Forêt de Saratoga", "description": "Bataille tournante - 25 ennemis", 
            "enemies": 25, "unlocked": False, "required_gold": 500, "map_type": "forest"},
            {"name": "Bunker de Yorktown", "description": "Siège décisif - 30 ennemis", 
            "enemies": 30, "unlocked": False, "required_gold": 1000, "map_type": "bunker"},
            {"name": "QG de Washington", "description": "Mission finale - 40 ennemis", 
            "enemies": 40, "unlocked": False, "required_gold": 2000, "map_type": "headquarters"},
]

        
        self.level_buttons = []
        self._create_level_buttons()
        
        self.back_button = Button(20, self.screen_height - 70, 150, 50, "RETOUR",
                                  color=(100, 100, 100), hover_color=(130, 130, 130))
        
        self.player_data = None
        self.selected_level = None
        self.time = 0
    
    def set_player_data(self, player_data):
        """Met à jour les données joueur"""
        self.player_data = player_data
        self._update_unlocked_levels()
    
    def _update_unlocked_levels(self):
        """Met à jour les niveaux déverrouillés"""
        if not self.player_data:
            return
        
        for i, level in enumerate(self.levels):
            if i < 2:
                level["unlocked"] = True
            elif i in self.player_data.unlocked_levels:
                level["unlocked"] = True
    
    def _create_level_buttons(self):
        """Crée les boutons de niveau"""
        self.level_buttons = []
        start_y = 150
        
        for i, level in enumerate(self.levels):
            x = 100 + (i % 3) * 280
            y = start_y + (i // 3) * 200
            
            color = (70, 130, 180) if level["unlocked"] else (80, 80, 80)
            hover_color = (100, 160, 210) if level["unlocked"] else (100, 100, 100)
            
            button = Button(x, y, 250, 150, "", color=color, hover_color=hover_color)
            self.level_buttons.append((button, level, i))
    
    def update(self, dt):
        """Met à jour le menu"""
        self.time += dt
        mouse_pos = pygame.mouse.get_pos()
        
        for button, _, _ in self.level_buttons:
            button.update(mouse_pos)
        
        self.back_button.update(mouse_pos)
        
        for button, level, _ in self.level_buttons:
            if level["unlocked"]:
                button.color = (70, 130, 180)
                button.hover_color = (100, 160, 210)
            else:
                button.color = (80, 80, 80)
                button.hover_color = (100, 100, 100)
    
    def handle_event(self, event):
        """Gère les événements"""
        if self.back_button.is_clicked(event):
            return "back"
        
        for button, level, index in self.level_buttons:
            if button.is_clicked(event):
                if level["unlocked"]:
                    self.selected_level = index
                    return "play"
                elif self.player_data and "required_gold" in level:
                    if self.player_data.gold >= level["required_gold"]:
                        self.player_data.gold -= level["required_gold"]
                        self.player_data.unlocked_levels.add(index)
                        level["unlocked"] = True
                        return "unlocked"
        
        return None
    
    def draw(self):
        """Dessine le menu de sélection de niveau"""
        # Fond avec dégradé colonial
        for y in range(self.screen_height):
            ratio = y / self.screen_height
            r = int(COLORS['parchment'][0] * (1 - ratio * 0.3))
            g = int(COLORS['parchment'][1] * (1 - ratio * 0.3))
            b = int(COLORS['parchment'][2] * (1 - ratio * 0.3))
            pygame.draw.line(self.screen, (r, g, b), (0, y), (self.screen_width, y))
        
        # Titre
        title = self.title_font.render("SÉLECTION DE MISSION", True, COLORS['colonial_blue'])
        title_rect = title.get_rect(center=(self.screen_width // 2, 60))
        
        # Contour doré du titre
        outline = self.title_font.render("SÉLECTION DE MISSION", True, COLORS['warm_gold'])
        for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
            self.screen.blit(outline, (title_rect.x + dx, title_rect.y + dy))
        self.screen.blit(title, title_rect)
        
        # Afficher l'or
        if self.player_data:
            gold_bg = pygame.Rect(self.screen_width - 170, 15, 155, 40)
            pygame.draw.rect(self.screen, (20, 40, 20), gold_bg, border_radius=8)
            pygame.draw.rect(self.screen, COLORS['warm_gold'], gold_bg, 2, border_radius=8)
            gold_text = self.font.render(f"$ {self.player_data.gold:,}", True, COLORS['warm_gold'])
            self.screen.blit(gold_text, (self.screen_width - 160, 22))
        
        # Dessiner les boutons de niveau
        for button, level, i in self.level_buttons:
            if level["unlocked"]:
                button.color = COLORS['colonial_blue']
                button.hover_color = (50, 80, 130)
            else:
                button.color = (60, 60, 60)
                button.hover_color = (80, 80, 80)
            
            button.draw(self.screen)
            
            # Nom du niveau
            name_font = pygame.font.Font(None, 30)
            name_text = name_font.render(level["name"], True, COLORS['white'])
            name_rect = name_text.get_rect(center=(button.rect.centerx, button.rect.y + 35))
            self.screen.blit(name_text, name_rect)
            
            # Description
            desc_font = pygame.font.Font(None, 20)
            desc_text = desc_font.render(level["description"], True, (180, 180, 180))
            desc_rect = desc_text.get_rect(center=(button.rect.centerx, button.rect.y + 65))
            self.screen.blit(desc_text, desc_rect)
            
            # Statut
            if level["unlocked"]:
                status_text = desc_font.render("PRÊT", True, (100, 255, 100))
            else:
                required = level.get("required_gold", 0)
                status_text = desc_font.render(f"VERROUILLÉ - ${required:,}", True, (255, 100, 100))
            
            status_rect = status_text.get_rect(center=(button.rect.centerx, button.rect.y + 95))
            self.screen.blit(status_text, status_rect)
            
            # Badge de mission
            badge_font = pygame.font.Font(None, 24)
            badge_text = badge_font.render(f"OP-{i + 1}", True, COLORS['warm_gold'])
            self.screen.blit(badge_text, (button.rect.x + 10, button.rect.y + 120))
        
        # Bouton retour
        self.back_button.draw(self.screen)
    
    def get_selected_level(self):
        """Retourne le niveau sélectionné"""
        if self.selected_level is not None:
            return self.levels[self.selected_level]
        return None


class PauseMenu:
    """Menu de pause - Style Colonial"""
    
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        # Polices
        self.font_title = pygame.font.Font(None, 80)
        self.font_large = pygame.font.Font(None, 50)
        
        # Options du menu pause
        self.options = ["REPRENDRE", "MENU PRINCIPAL", "QUITTER"]
        self.selected = 0
        self.time = 0
    
    def update(self, dt):
        """Met à jour le menu"""
        self.time += 0.02
    
    def handle_event(self, event):
        """Gère les événements"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self._get_action()
            elif event.key == pygame.K_ESCAPE:
                return 'resume'
        
        # Support souris
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            panel_y = self.screen_height // 2 - 120
            for i, option in enumerate(self.options):
                option_y = panel_y + 80 + i * 70
                option_rect = pygame.Rect(self.screen_width // 2 - 180, option_y - 25, 360, 50)
                if option_rect.collidepoint(mouse_pos):
                    self.selected = i
                    return self._get_action()
        
        # Survol souris
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            panel_y = self.screen_height // 2 - 120
            for i, option in enumerate(self.options):
                option_y = panel_y + 80 + i * 70
                option_rect = pygame.Rect(self.screen_width // 2 - 180, option_y - 25, 360, 50)
                if option_rect.collidepoint(mouse_pos):
                    self.selected = i
        
        return None
    
    def _get_action(self):
        """Retourne l'action correspondant à l'option sélectionnée"""
        option = self.options[self.selected]
        if option == "REPRENDRE":
            return 'resume'
        elif option == "MENU PRINCIPAL":
            return 'menu'
        elif option == "QUITTER":
            return 'quit'
        return None
    
    def draw(self):
        """Dessine le menu de pause - Style Colonial"""
        # Overlay semi-transparent
        overlay = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        
        # Panneau central parchemin
        panel_width = 500
        panel_height = 350
        panel_x = self.screen_width // 2 - panel_width // 2
        panel_y = self.screen_height // 2 - panel_height // 2
        
        panel_surf = pygame.Surface((panel_width, panel_height), pygame.SRCALPHA)
        panel_surf.fill((*COLORS['parchment'], 250))
        
        # Bordures dorées
        for i in range(3):
            thickness = 8 - i * 2
            offset = i * 3
            pygame.draw.rect(panel_surf, COLORS['warm_gold'],
                           (offset, offset, panel_width - 2 * offset, panel_height - 2 * offset), thickness)
        self.screen.blit(panel_surf, (panel_x, panel_y))
        
        # Étoiles dans les coins
        corner_positions = [
            (panel_x + 25, panel_y + 25),
            (panel_x + panel_width - 25, panel_y + 25),
            (panel_x + 25, panel_y + panel_height - 25),
            (panel_x + panel_width - 25, panel_y + panel_height - 25)
        ]
        for corner_x, corner_y in corner_positions:
            star_points = []
            for i in range(16):
                angle = i * math.pi / 8 + self.time * 2
                radius = 12 if i % 2 == 0 else 5
                sx = corner_x + math.cos(angle) * radius
                sy = corner_y + math.sin(angle) * radius
                star_points.append((sx, sy))
            pygame.draw.polygon(self.screen, COLORS['warm_gold'], star_points)
            pygame.draw.polygon(self.screen, COLORS['brass'], star_points, 2)
        
        # Titre PAUSE
        title_text = "PAUSE"
        title_surf = self.font_title.render(title_text, True, COLORS['deep_red'])
        title_rect = title_surf.get_rect(center=(self.screen_width // 2, panel_y + 45))
        
        # Contour doré du titre
        outline_surf = self.font_title.render(title_text, True, COLORS['warm_gold'])
        for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (-3, 0), (3, 0), (0, -3), (0, 3)]:
            self.screen.blit(outline_surf, (title_rect.x + dx, title_rect.y + dy))
        self.screen.blit(title_surf, title_rect)
        
        # Ligne décorative
        line_y = panel_y + 75
        pygame.draw.line(self.screen, COLORS['warm_gold'],
                        (panel_x + 50, line_y), (panel_x + panel_width - 50, line_y), 3)
        pygame.draw.circle(self.screen, COLORS['warm_gold'], (self.screen_width // 2, line_y), 6)
        pygame.draw.circle(self.screen, COLORS['deep_red'], (self.screen_width // 2, line_y), 4)
        
        # Options du menu
        for i, option in enumerate(self.options):
            is_selected = (i == self.selected)
            option_y = panel_y + 120 + i * 70
            
            if is_selected:
                # Fond de sélection
                sel_width = 360
                sel_height = 45
                sel_rect = pygame.Rect(self.screen_width // 2 - sel_width // 2, option_y - 18, sel_width, sel_height)
                sel_surf = pygame.Surface((sel_width, sel_height), pygame.SRCALPHA)
                for sy in range(sel_height):
                    alpha = 180 - abs(sy - sel_height // 2) * 3
                    pygame.draw.line(sel_surf, (*COLORS['warm_gold'], alpha), (0, sy), (sel_width, sy))
                self.screen.blit(sel_surf, sel_rect)
                pygame.draw.rect(self.screen, COLORS['brass'], sel_rect, 3)
                
                # Étoiles de sélection
                for star_x in [self.screen_width // 2 - 170, self.screen_width // 2 + 170]:
                    star_pts = []
                    for j in range(10):
                        ang = j * 2 * math.pi / 10 + self.time * 3
                        rad = 14 if j % 2 == 0 else 6
                        spx = star_x + math.cos(ang) * rad
                        spy = option_y + math.sin(ang) * rad
                        star_pts.append((spx, spy))
                    pygame.draw.polygon(self.screen, COLORS['deep_red'], star_pts)
                    pygame.draw.polygon(self.screen, COLORS['warm_gold'], star_pts, 2)
                
                color = COLORS['deep_red']
            else:
                color = COLORS['colonial_blue']
            
            # Ombre du texte
            shadow_surf = self.font_large.render(option, True, COLORS['shadow'])
            shadow_rect = shadow_surf.get_rect(center=(self.screen_width // 2 + 3, option_y + 3))
            s = pygame.Surface(shadow_surf.get_size(), pygame.SRCALPHA)
            s.fill((*COLORS['shadow'], 120))
            s.blit(shadow_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            self.screen.blit(s, shadow_rect)
            
            # Texte principal
            option_surf = self.font_large.render(option, True, color)
            option_rect = option_surf.get_rect(center=(self.screen_width // 2, option_y))
            self.screen.blit(option_surf, option_rect)
            
            if is_selected:
                outline_option = self.font_large.render(option, True, COLORS['warm_gold'])
                for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
                    self.screen.blit(outline_option, (option_rect.x + dx, option_rect.y + dy))
                self.screen.blit(option_surf, option_rect)
