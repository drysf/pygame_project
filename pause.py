import pygame
import sys
import math
import random
from typing import List, Tuple

# Initialisation
pygame.init()

# Constantes
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
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

class Pause :
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.Font(None, 140)
        self.font_large = pygame.font.Font(None, 80)
        self.font_medium = pygame.font.Font(None, 60)
        self.font_small = pygame.font.Font(None, 45)
        self.options = ["RESUME", "RESTART", "QUIT"]
        self.selected = 0
        self.clouds = [
            Cloud(100, 100, 1.2, 0.15),
            Cloud(400, 80, 1.5, 0.1),
            Cloud(800, 120, 1.0, 0.2),
            Cloud(1100, 90, 1.3, 0.12),
        ]
        self.birds = [Bird(random.randint(0, SCREEN_WIDTH), random.randint(50, 250)) for _ in range(8)]
        self.houses = []
        for i in range(7):
            x = i * 250 + random.randint(-50, 50)
            y = 500 + random.randint(-30, 30)
            scale = random.uniform(0.9, 1.3)
            house_type = random.randint(0, 3)
            self.houses.append(ColonialHouse(x, y, house_type, scale))
        self.soldiers = [
            DetailedSoldier(180, 540, 1.4, True, 'blue', 'officer'),
            DetailedSoldier(320, 550, 1.2, True, 'blue', 'soldier'),
            DetailedSoldier(450, 545, 1.3, True, 'blue', 'sergeant'),
            DetailedSoldier(600, 548, 1.1, False, 'red', 'soldier'),
            DetailedSoldier(SCREEN_WIDTH - 450, 550, 1.2, False, 'blue', 'soldier'),
            DetailedSoldier(SCREEN_WIDTH - 300, 540, 1.3, False, 'red', 'sergeant'),
            DetailedSoldier(SCREEN_WIDTH - 150, 545, 1.1, False, 'blue', 'soldier'),
        ]
        self.muzzle_flashes = []
        self.smoke_particles = []
        self.time = 0
        self.sun_position = 0
        
    def fire_musket(self, soldier_index):
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
    
    def update(self):
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
        for y in range(SCREEN_HEIGHT // 2 + 50):
            ratio = y / (SCREEN_HEIGHT // 2 + 50)
            if ratio < 0.6:
                r = int(COLORS['sky_top'][0] + (COLORS['sky_middle'][0] - COLORS['sky_top'][0]) * (ratio / 0.6))
                g = int(COLORS['sky_top'][1] + (COLORS['sky_middle'][1] - COLORS['sky_top'][1]) * (ratio / 0.6))
                b = int(COLORS['sky_top'][2] + (COLORS['sky_middle'][2] - COLORS['sky_top'][2]) * (ratio / 0.6))
            else:
                local_ratio = (ratio - 0.6) / 0.4
                r = int(COLORS['sky_middle'][0] + (COLORS['sky_horizon'][0] - COLORS['sky_middle'][0]) * local_ratio)
                g = int(COLORS['sky_middle'][1] + (COLORS['sky_horizon'][1] - COLORS['sky_middle'][1]) * local_ratio)
                b = int(COLORS['sky_middle'][2] + (COLORS['sky_horizon'][2] - COLORS['sky_middle'][2]) * local_ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        sun_x = SCREEN_WIDTH - 200
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
        self.draw_sky()
        for cloud in self.clouds:
            cloud.draw(self.screen)
        for bird in self.birds:
            bird.draw(self.screen)
        hill_layers = [
            (420, COLORS['forest_green'], 35),
            (390, COLORS['dark_green'], 30),
            (360, (49, 107, 64), 25),
        ]
        for base_y, color, amplitude in hill_layers:
            hill_points = []
            for x in range(0, SCREEN_WIDTH + 30, 20):
                y = base_y + math.sin(x * 0.008 + self.time + amplitude) * amplitude
                hill_points.append((x, y))
            hill_points.append((SCREEN_WIDTH, SCREEN_HEIGHT // 2))
            hill_points.append((0, SCREEN_HEIGHT // 2))
            pygame.draw.polygon(self.screen, color, hill_points)
        grass_base = SCREEN_HEIGHT // 2
        pygame.draw.rect(self.screen, COLORS['grass_green'],
                        (0, grass_base, SCREEN_WIDTH, SCREEN_HEIGHT // 2))
        for _ in range(200):
            gx = random.randint(0, SCREEN_WIDTH)
            gy = random.randint(grass_base, SCREEN_HEIGHT // 2 + 100)
            grass_color = random.choice([COLORS['grass_green'], COLORS['dark_green'], COLORS['forest_green']])
            pygame.draw.line(self.screen, grass_color, (gx, gy), (gx, gy + 3), 1)
        road_y = 600
        road_height = 70
        pygame.draw.rect(self.screen, COLORS['dirt_brown'],
                        (0, road_y, SCREEN_WIDTH, road_height))
        for _ in range(150):
            rx = random.randint(0, SCREEN_WIDTH)
            ry = random.randint(road_y, road_y + road_height)
            pygame.draw.circle(self.screen, COLORS['dark_wood'], (rx, ry), 1)
        for x in range(0, SCREEN_WIDTH, 50):
            pygame.draw.line(self.screen, COLORS['shadow'],
                           (x, road_y + 20), (x + 40, road_y + 20), 3)
            pygame.draw.line(self.screen, COLORS['shadow'],
                           (x, road_y + 50), (x + 40, road_y + 50), 3)
        for x in range(0, SCREEN_WIDTH, 8):
            sway = math.sin(self.time * 2 + x * 0.08) * 3
            height = random.randint(18, 40)
            grass_color = random.choice([COLORS['dark_green'], COLORS['forest_green']])
            pygame.draw.line(self.screen, grass_color,
                           (x, road_y),
                           (x + sway, road_y - height), 2)
            pygame.draw.circle(self.screen, grass_color,
                             (int(x + sway), int(road_y - height)), 1)
    
    def draw(self):
        self.draw_background()
        for house in self.houses:
            house.draw(self.screen)
        for soldier in self.soldiers:
            soldier.draw(self.screen)
        for smoke in self.smoke_particles:
            smoke.draw(self.screen)
        for flash in self.muzzle_flashes:
            flash.draw(self.screen)

        # === PANNEAU DE MENU ===
        panel_y = 10
        panel_height = 500  # *** AGRANDI de 420 -> 500 pour loger les options espacées ***

        overlay = pygame.Surface((SCREEN_WIDTH - 40, panel_height), pygame.SRCALPHA)
        overlay.fill((*COLORS['parchment'], 245))
        for i in range(3):
            thickness = 8 - i * 2
            offset = i * 3
            pygame.draw.rect(overlay, COLORS['warm_gold'],
                           (offset, offset, 
                            SCREEN_WIDTH - 40 - 2 * offset, 
                            panel_height - 2 * offset), thickness)
        self.screen.blit(overlay, (20, panel_y))

        # Coins décorés
        corner_positions = [
            (35, 25), (SCREEN_WIDTH - 65, 25),
            (35, panel_y + panel_height - 25), (SCREEN_WIDTH - 65, panel_y + panel_height - 25)
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

        # === TITRE "PAUSED" ===
        title_text = "⚔ PAUSED ⚔"
        for offset in range(8, 0, -1):
            shadow_alpha = 50 - offset * 5
            shadow_surf = self.font_title.render(title_text, True, COLORS['shadow'])
            shadow_rect = shadow_surf.get_rect(center=(SCREEN_WIDTH // 2 + offset, 95 + offset))
            s = pygame.Surface(shadow_surf.get_size(), pygame.SRCALPHA)
            s.fill((*COLORS['shadow'], shadow_alpha))
            s.blit(shadow_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            self.screen.blit(s, shadow_rect)
        title_surf = self.font_title.render(title_text, True, COLORS['deep_red'])
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, 95))
        outline_surf = self.font_title.render(title_text, True, COLORS['warm_gold'])
        for angle in range(0, 360, 30):
            offset_x = math.cos(math.radians(angle)) * 4
            offset_y = math.sin(math.radians(angle)) * 4
            self.screen.blit(outline_surf, (title_rect.x + offset_x, title_rect.y + offset_y))
        self.screen.blit(title_surf, title_rect)

        # Ligne décorative ornementale
        line_y = 175
        line_center = SCREEN_WIDTH // 2
        pygame.draw.line(self.screen, COLORS['warm_gold'],
                        (line_center - 350, line_y),
                        (line_center + 350, line_y), 4)
        for ornament_x in [line_center - 300, line_center, line_center + 300]:
            pygame.draw.circle(self.screen, COLORS['warm_gold'], (ornament_x, line_y), 8)
            pygame.draw.circle(self.screen, COLORS['deep_red'], (ornament_x, line_y), 5)
        for direction, x_pos in [(-1, line_center - 370), (1, line_center + 370)]:
            arrow_points = [
                (x_pos, line_y),
                (x_pos + direction * 15, line_y - 8),
                (x_pos + direction * 15, line_y + 8)
            ]
            pygame.draw.polygon(self.screen, COLORS['warm_gold'], arrow_points)

        # === OPTIONS DU MENU — espacées de 70px au lieu de 42px ===
        for i, option in enumerate(self.options):
            is_selected = (i == self.selected)
            option_y = 240 + i * 70  # *** ESPACE AUGMENTÉ : 42 -> 70 ***

            if is_selected:
                sel_width = 450
                sel_height = 60
                sel_rect = pygame.Rect(SCREEN_WIDTH // 2 - sel_width // 2, option_y - 25, sel_width, sel_height)
                sel_surf = pygame.Surface((sel_width, sel_height), pygame.SRCALPHA)
                for sy in range(sel_height):
                    alpha = 180 - abs(sy - sel_height // 2) * 2
                    pygame.draw.line(sel_surf, (*COLORS['warm_gold'], alpha),
                                   (0, sy), (sel_width, sy))
                self.screen.blit(sel_surf, sel_rect)
                pygame.draw.rect(self.screen, COLORS['brass'], sel_rect, 3)

                star_positions = [
                    (SCREEN_WIDTH // 2 - 250, option_y),
                    (SCREEN_WIDTH // 2 + 250, option_y)
                ]
                for star_x, star_y in star_positions:
                    star_points = []
                    for j in range(10):
                        angle = j * 2 * math.pi / 10 + self.time * 3
                        radius = 18 if j % 2 == 0 else 8
                        sx = star_x + math.cos(angle) * radius
                        sy = star_y + math.sin(angle) * radius
                        star_points.append((sx, sy))
                    pygame.draw.polygon(self.screen, COLORS['deep_red'], star_points)
                    pygame.draw.polygon(self.screen, COLORS['warm_gold'], star_points, 2)

                arrow_left = [
                    (SCREEN_WIDTH // 2 - 210, option_y),
                    (SCREEN_WIDTH // 2 - 195, option_y - 8),
                    (SCREEN_WIDTH // 2 - 195, option_y + 8)
                ]
                arrow_right = [
                    (SCREEN_WIDTH // 2 + 210, option_y),
                    (SCREEN_WIDTH // 2 + 195, option_y - 8),
                    (SCREEN_WIDTH // 2 + 195, option_y + 8)
                ]
                pygame.draw.polygon(self.screen, COLORS['deep_red'], arrow_left)
                pygame.draw.polygon(self.screen, COLORS['deep_red'], arrow_right)
                color = COLORS['deep_red']
            else:
                color = COLORS['colonial_blue']

            # Ombre du texte
            shadow_surf = self.font_large.render(option, True, COLORS['shadow'])
            shadow_rect = shadow_surf.get_rect(center=(SCREEN_WIDTH // 2 + 3, option_y + 3))
            s = pygame.Surface(shadow_surf.get_size(), pygame.SRCALPHA)
            s.fill((*COLORS['shadow'], 120))
            s.blit(shadow_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            self.screen.blit(s, shadow_rect)

            # Texte principal
            option_surf = self.font_large.render(option, True, color)
            option_rect = option_surf.get_rect(center=(SCREEN_WIDTH // 2, option_y))
            self.screen.blit(option_surf, option_rect)

            if is_selected:
                outline_option = self.font_large.render(option, True, COLORS['warm_gold'])
                for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    self.screen.blit(outline_option, (option_rect.x + dx, option_rect.y + dy))
                self.screen.blit(option_surf, option_rect)
    
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                for i in range(len(self.soldiers)):
                    self.fire_musket(i)
                return self.options[self.selected]
            elif event.key == pygame.K_ESCAPE:
                return "RESUME"
        return None


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("1776 REVOLUTIONARY MENU")
    menu = HistoricalMenu(screen)
    running = True
    paused = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if paused:
                action = menu.handle_input(event)
                if action == "RESUME":
                    print("Returning to the battlefield!")
                    paused = False
                elif action == "RESTART":
                    print("Restarting the revolution!")
                elif action == "QUIT":
                    print("Honorable retreat!")
                    running = False
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    paused = True
        if paused:
            menu.update()
            menu.draw()
        else:
            screen.fill(COLORS['grass_green'])
            title_font = pygame.font.Font(None, 100)
            title_surf = title_font.render("BATTLE IN PROGRESS", True, COLORS['colonial_blue'])
            title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
            screen.blit(title_surf, title_rect)
        pygame.display.flip()
        menu.clock.tick(FPS)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()