"""Menu en cas de victoire"""
import pygame
import sys
import math
import random

# Initialisation
pygame.init()

# Constantes
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60

# Palette
COLORS = {
    'sky_top': (135, 206, 250),
    'sky_middle': (176, 226, 255),
    'sky_horizon': (255, 250, 205),
    'dawn_light': (255, 228, 181),
    'dawn_warm': (255, 193, 130),
    'cloud_white': (255, 255, 255),
    'cloud_shadow': (220, 220, 230),
    'cream': (255, 253, 208),
    'parchment': (245, 237, 218),
    'parchment_old': (220, 210, 180),
    'colonial_blue': (31, 58, 96),
    'royal_blue': (65, 105, 225),
    'deep_red': (139, 0, 0),
    'bright_red': (178, 34, 34),
    'warm_gold': (218, 165, 32),
    'brass': (181, 166, 66),
    'wood_brown': (139, 90, 43),
    'dark_wood': (92, 64, 51),
    'white': (255, 255, 255),
    'ivory': (255, 250, 240),
    'grass_green': (85, 107, 47),
    'dark_green': (34, 85, 34),
    'forest_green': (49, 87, 44),
    'shadow': (30, 30, 35),
}

class Confetti:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-SCREEN_HEIGHT, 0)
        self.speed_y = random.uniform(2, 5)
        self.speed_x = random.uniform(-1.5, 1.5)
        self.size = random.randint(4, 7)
        self.color = random.choice([
            COLORS['warm_gold'],
            COLORS['bright_red'],
            COLORS['royal_blue'],
            COLORS['grass_green'],
            COLORS['ivory']
        ])
        self.angle = random.uniform(0, 2 * math.pi)
        self.rotation_speed = random.uniform(-0.1, 0.1)

    def update(self):
        self.y += self.speed_y
        self.x += self.speed_x
        self.angle += self.rotation_speed

        if self.y > SCREEN_HEIGHT + 20:
            self.reset()

    def draw(self, screen):
        half = self.size // 2
        points = []
        for i in range(4):
            a = self.angle + i * math.pi / 2
            px = self.x + math.cos(a) * half
            py = self.y + math.sin(a) * half
            points.append((int(px), int(py)))
        pygame.draw.polygon(screen, self.color, points)

class RisingLight:
    def __init__(self):
        self.particles = [
            [random.randint(0, SCREEN_WIDTH),
             random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT),
             random.uniform(0.5, 1.5),
             random.randint(30, 80)]
            for _ in range(80)
        ]

    def update(self):
        for p in self.particles:
            p[1] -= p[2]
            p[3] -= 1
            if p[3] <= 0 or p[1] < SCREEN_HEIGHT // 2:
                p[0] = random.randint(0, SCREEN_WIDTH)
                p[1] = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
                p[2] = random.uniform(0.5, 1.5)
                p[3] = random.randint(30, 80)

    def draw(self, screen):
        for x, y, _, life in self.particles:
            alpha = max(0, min(255, life * 3))
            surf = pygame.Surface((4, 8), pygame.SRCALPHA)
            pygame.draw.ellipse(surf, (*COLORS['warm_gold'], alpha), (0, 0, 4, 8))
            screen.blit(surf, (int(x), int(y)))

class StandingSoldier:
    def __init__(self, x, y, facing_right=True):
        self.x = x
        self.y = y
        self.facing_right = facing_right
        self.breath_phase = random.uniform(0, 2 * math.pi)

    def update(self):
        self.breath_phase += 0.03

    def draw(self, screen):
        offset_y = math.sin(self.breath_phase) * 2

        shadow_surf = pygame.Surface((60, 20), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow_surf, (*COLORS['shadow'], 150), (0, 0, 60, 20))
        screen.blit(shadow_surf, (int(self.x - 30), int(self.y + 5)))

        body_points = []
        if self.facing_right:
            body_points = [
                (self.x - 10, self.y - 40 + offset_y),
                (self.x + 15, self.y - 35 + offset_y),
                (self.x + 18, self.y + 10 + offset_y),
                (self.x - 8, self.y + 5 + offset_y),
            ]
        else:
            body_points = [
                (self.x + 10, self.y - 40 + offset_y),
                (self.x - 15, self.y - 35 + offset_y),
                (self.x - 18, self.y + 10 + offset_y),
                (self.x + 8, self.y + 5 + offset_y),
            ]
        pygame.draw.polygon(
            screen,
            COLORS['colonial_blue'],
            [(int(px), int(py)) for px, py in body_points],
        )

        head_x = self.x + (-5 if self.facing_right else 5)
        head_y = self.y - 50 + offset_y
        pygame.draw.circle(screen, COLORS['parchment'], (int(head_x), int(head_y)), 8)

        hat_points = [
            (head_x - 10, head_y - 2),
            (head_x, head_y - 8),
            (head_x + 10, head_y - 2),
            (head_x + 6, head_y + 1),
            (head_x - 6, head_y + 1),
        ]
        pygame.draw.polygon(
            screen,
            COLORS['dark_wood'],
            [(int(px), int(py)) for px, py in hat_points],
        )

        leg_x = self.x + (5 if self.facing_right else -5)
        leg_y = self.y + 5 + offset_y
        pygame.draw.line(
            screen, COLORS['shadow'], (int(leg_x), int(leg_y)), (int(leg_x), int(leg_y + 20)), 4
        )

class ProudFlag:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wave_phase = random.uniform(0, 2 * math.pi)
        self.sway = 0
        self.sway_direction = random.choice([-1, 1])

    def update(self):
        self.wave_phase += 0.05
        self.sway += 0.015 * self.sway_direction
        if abs(self.sway) > 0.25:
            self.sway_direction *= -1

    def draw(self, screen):
        pole_x = self.x + self.sway * 20
        pole_height = 200
        pygame.draw.rect(screen, COLORS['dark_wood'], (int(pole_x - 4), self.y, 8, pole_height))

        flag_width = 120
        flag_height = 72
        stripe_height = flag_height // 13
        flag_surf = pygame.Surface((flag_width, flag_height), pygame.SRCALPHA)

        for i in range(13):
            color = COLORS['bright_red'] if i % 2 == 0 else COLORS['ivory']
            y_pos = i * stripe_height
            for x in range(flag_width):
                wave = math.sin(self.wave_phase + x * 0.12 + self.sway) * 5
                pygame.draw.line(
                    flag_surf,
                    color,
                    (x, int(y_pos + wave)),
                    (x, int(y_pos + stripe_height + wave)),
                )

        canton_width = flag_width // 2
        canton_height = 7 * stripe_height
        for x in range(canton_width):
            for y in range(canton_height):
                wave = math.sin(self.wave_phase + x * 0.12 + self.sway) * 5
                flag_surf.set_at((x, int(y + wave)), COLORS['colonial_blue'])

        for row in range(2):
            for col in range(4):
                sx = col * 20 + 10
                sy = row * 20 + 12
                for i in range(10):
                    angle = i * 2 * math.pi / 10
                    radius = 4 if i % 2 == 0 else 2
                    px = int(sx + math.cos(angle) * radius)
                    py = int(sy + math.sin(angle) * radius)
                    if 0 <= px < canton_width and 0 <= py < canton_height:
                        wave = int(math.sin(self.wave_phase + px * 0.12 + self.sway) * 5)
                        if 0 <= py + wave < flag_height:
                            flag_surf.set_at((px, py + wave), COLORS['ivory'])

        screen.blit(flag_surf, (int(pole_x + 6), self.y + 25))

class WinScreen:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.font_huge = pygame.font.Font(None, 140)
        self.font_large = pygame.font.Font(None, 70)
        self.font_medium = pygame.font.Font(None, 45)
        self.font_small = pygame.font.Font(None, 40)

        self.time = 0
        self.title_pulse = 0
        self.fade_alpha = 255

        self.confettis = [Confetti() for _ in range(120)]
        self.lights = RisingLight()
        self.soldiers = [
            StandingSoldier(220, 580, True),
            StandingSoldier(380, 590, False),
            StandingSoldier(640, 585, True),
            StandingSoldier(820, 595, False),
        ]
        self.flags = [
            ProudFlag(120, 380),
            ProudFlag(SCREEN_WIDTH - 120, 390),
        ]

        # Options en français
        self.options = ["NIVEAU SUIVANT", "MENU PRINCIPAL", "QUITTER"]
        self.selected = 0

    def update(self):
        self.time += 0.015
        self.title_pulse += 0.05

        for c in self.confettis:
            c.update()
        self.lights.update()
        for f in self.flags:
            f.update()
        for s in self.soldiers:
            s.update()

        if self.fade_alpha > 0:
            self.fade_alpha -= 3

    def draw_sky(self):
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            if ratio < 0.5:
                r = int(COLORS['sky_top'][0] + (COLORS['sky_middle'][0] - COLORS['sky_top'][0]) * (ratio / 0.5))
                g = int(COLORS['sky_top'][1] + (COLORS['sky_middle'][1] - COLORS['sky_top'][1]) * (ratio / 0.5))
                b = int(COLORS['sky_top'][2] + (COLORS['sky_middle'][2] - COLORS['sky_top'][2]) * (ratio / 0.5))
            else:
                local_ratio = (ratio - 0.5) / 0.5
                r = int(COLORS['sky_middle'][0] + (COLORS['dawn_warm'][0] - COLORS['sky_middle'][0]) * local_ratio)
                g = int(COLORS['sky_middle'][1] + (COLORS['dawn_warm'][1] - COLORS['sky_middle'][1]) * local_ratio)
                b = int(COLORS['sky_middle'][2] + (COLORS['dawn_warm'][2] - COLORS['sky_middle'][2]) * local_ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))

        for _ in range(35):
            cx = random.randint(0, SCREEN_WIDTH)
            cy = random.randint(0, SCREEN_HEIGHT // 2)
            radius = random.randint(10, 20)
            pygame.draw.circle(self.screen, COLORS['cloud_shadow'], (cx + 3, cy + 3), radius)
            pygame.draw.circle(self.screen, COLORS['cloud_white'], (cx, cy), radius)

    def draw_field(self):
        ground_y = 540
        for y in range(ground_y, SCREEN_HEIGHT):
            ratio = (y - ground_y) / (SCREEN_HEIGHT - ground_y)
            r = int(COLORS['grass_green'][0] + (COLORS['forest_green'][0] - COLORS['grass_green'][0]) * ratio)
            g = int(COLORS['grass_green'][1] + (COLORS['forest_green'][1] - COLORS['grass_green'][1]) * ratio)
            b = int(COLORS['grass_green'][2] + (COLORS['forest_green'][2] - COLORS['grass_green'][2]) * ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))

        for _ in range(80):
            gx = random.randint(0, SCREEN_WIDTH)
            gy = random.randint(ground_y, SCREEN_HEIGHT)
            pygame.draw.line(self.screen, COLORS['shadow'], (gx, gy), (gx, gy + 3), 1)

    def draw(self):
        self.draw_sky()
        self.draw_field()

        self.lights.draw(self.screen)
        for c in self.confettis:
            c.draw(self.screen)

        for f in self.flags:
            f.draw(self.screen)
        for s in self.soldiers:
            s.draw(self.screen)

        panel_y = 70
        panel_height = 540
        overlay = pygame.Surface((SCREEN_WIDTH - 120, panel_height), pygame.SRCALPHA)
        overlay.fill((*COLORS['parchment_old'], 220))

        for _ in range(25):
            spot_x = random.randint(0, SCREEN_WIDTH - 120)
            spot_y = random.randint(0, panel_height)
            spot_size = random.randint(3, 7)
            pygame.draw.circle(overlay, (*COLORS['shadow'], 40), (spot_x, spot_y), spot_size)

        for i in range(4):
            thickness = 10 - i * 2
            offset = i * 4
            pygame.draw.rect(
                overlay,
                COLORS['shadow'],
                (offset, offset, SCREEN_WIDTH - 120 - 2 * offset, panel_height - 2 * offset),
                thickness,
            )

        self.screen.blit(overlay, (60, panel_y))

        corner_positions = [
            (80, panel_y + 20),
            (SCREEN_WIDTH - 80, panel_y + 20),
            (80, panel_y + panel_height - 20),
            (SCREEN_WIDTH - 80, panel_y + panel_height - 20),
        ]
        for cx, cy in corner_positions:
            pygame.draw.circle(self.screen, COLORS['parchment_old'], (cx, cy), 8)
            pygame.draw.circle(self.screen, COLORS['shadow'], (cx, cy), 8, 2)
            pygame.draw.circle(self.screen, COLORS['shadow'], (cx - 3, cy - 1), 2)
            pygame.draw.circle(self.screen, COLORS['shadow'], (cx + 3, cy - 1), 2)
            pygame.draw.line(self.screen, COLORS['shadow'], (cx - 2, cy + 3), (cx + 2, cy + 3), 1)

        title_text = "VICTOIRE"
        title_y = panel_y + 120
        pulse = 1.02 + math.sin(self.title_pulse) * 0.06
        scaled_font = pygame.font.Font(None, int(140 * pulse))

        for offset in range(12, 0, -1):
            shadow_surf = scaled_font.render(title_text, True, COLORS['shadow'])
            shadow_rect = shadow_surf.get_rect(center=(SCREEN_WIDTH // 2 + offset, title_y + offset))
            s = pygame.Surface(shadow_surf.get_size(), pygame.SRCALPHA)
            s.fill((*COLORS['shadow'], 40))
            s.blit(shadow_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            self.screen.blit(s, shadow_rect)

        title_surf = scaled_font.render(title_text, True, COLORS['warm_gold'])
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, title_y))

        outline_surf = scaled_font.render(title_text, True, COLORS['shadow'])
        for angle in range(0, 360, 30):
            ox = math.cos(math.radians(angle)) * 4
            oy = math.sin(math.radians(angle)) * 4
            self.screen.blit(outline_surf, (title_rect.x + ox, title_rect.y + oy))
        self.screen.blit(title_surf, title_rect)

        subtitle_text = "Indépendance assurée, soldat."
        subtitle_surf = self.font_medium.render(subtitle_text, True, COLORS['shadow'])
        subtitle_rect = subtitle_surf.get_rect(center=(SCREEN_WIDTH // 2, panel_y + 215))
        self.screen.blit(subtitle_surf, subtitle_rect)

        line_y = panel_y + 260
        line_center = SCREEN_WIDTH // 2
        for i in range(3):
            y_off = i * 2
            alpha = 110 - i * 30
            pygame.draw.line(
                self.screen,
                (*COLORS['shadow'], alpha),
                (line_center - 280, line_y + y_off),
                (line_center + 280, line_y + y_off),
                3,
            )

        medal_positions = [line_center - 220, line_center, line_center + 220]
        for mx in medal_positions:
            pygame.draw.circle(self.screen, COLORS['warm_gold'], (mx, line_y), 14)
            pygame.draw.circle(self.screen, COLORS['shadow'], (mx, line_y), 14, 2)
            pygame.draw.circle(self.screen, COLORS['ivory'], (mx, line_y - 4), 4)
            pygame.draw.line(
                self.screen, COLORS['shadow'], (mx - 4, line_y + 5), (mx + 4, line_y + 5), 2
            )

        quote_y = panel_y + 310
        quote_text = "Le futur appartient aux libres."
        quote_surf = self.font_small.render(quote_text, True, COLORS['shadow'])
        quote_rect = quote_surf.get_rect(center=(SCREEN_WIDTH // 2, quote_y))
        self.screen.blit(quote_surf, quote_rect)

        # Options
        for i, option in enumerate(self.options):
            is_selected = (i == self.selected)
            option_y = panel_y + 420 + i * 45

            if is_selected:
                sel_width = 320
                sel_height = 50
                sel_rect = pygame.Rect(
                    SCREEN_WIDTH // 2 - sel_width // 2, option_y - 22, sel_width, sel_height
                )
                sel_surf = pygame.Surface((sel_width, sel_height), pygame.SRCALPHA)
                for sy in range(sel_height):
                    alpha = 150 - abs(sy - sel_height // 2) * 2
                    pygame.draw.line(
                        sel_surf,
                        (*COLORS['warm_gold'], max(0, alpha)),
                        (0, sy),
                        (sel_width, sy),
                    )
                self.screen.blit(sel_surf, sel_rect)
                pygame.draw.rect(self.screen, COLORS['shadow'], sel_rect, 3)

                arrow_left = [
                    (SCREEN_WIDTH // 2 - 175, option_y),
                    (SCREEN_WIDTH // 2 - 160, option_y - 8),
                    (SCREEN_WIDTH // 2 - 160, option_y + 8),
                ]
                arrow_right = [
                    (SCREEN_WIDTH // 2 + 175, option_y),
                    (SCREEN_WIDTH // 2 + 160, option_y - 8),
                    (SCREEN_WIDTH // 2 + 160, option_y + 8),
                ]
                pygame.draw.polygon(self.screen, COLORS['warm_gold'], arrow_left)
                pygame.draw.polygon(self.screen, COLORS['warm_gold'], arrow_right)
                color = COLORS['warm_gold']
            else:
                color = COLORS['shadow']

            shadow_surf = self.font_medium.render(option, True, COLORS['shadow'])
            shadow_rect = shadow_surf.get_rect(center=(SCREEN_WIDTH // 2 + 3, option_y + 3))
            s = pygame.Surface(shadow_surf.get_size(), pygame.SRCALPHA)
            s.fill((*COLORS['shadow'], 90))
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

        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            for i in range(len(self.options)):
                option_y = 70 + 420 + i * 45
                if (SCREEN_WIDTH // 2 - 160 < mouse_x < SCREEN_WIDTH // 2 + 160
                        and option_y - 25 < mouse_y < option_y + 25):
                    self.selected = i

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.options[self.selected]

        return None

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PHILADELPHIA LIBERTY VICTOIRE")
    win_screen = WinScreen(screen)
    running = True
    clock = pygame.time.Clock()

    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            action = win_screen.handle_input(event)
            if action == "NIVEAU SUIVANT":
                print("Prochain niveau sélectionné.")
            elif action == "MENU PRINCIPAL":
                print("Retour au menu principal.")
            elif action == "QUITTER":
                print("Mission accomplie, fermeture du jeu.")
                running = False

        win_screen.update()
        win_screen.draw()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
