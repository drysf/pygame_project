"""
Classe représentant une salle avec des murs
"""
import pygame
import random
import math
from room_auto import Wall as SpriteWall


class Wall(pygame.sprite.Sprite):
    """Mur simple gris"""
    
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((80, 80, 80))
        pygame.draw.rect(self.image, (60, 60, 60), (0, 0, width, height), 3)
        self.rect = self.image.get_rect(topleft=(x, y))


class Tree(pygame.sprite.Sprite):
    """Arbre décoratif (collision)"""
    
    def __init__(self, x, y, size=50):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Tronc
        trunk_width = size // 5
        trunk_height = size // 2
        trunk_x = (size - trunk_width) // 2
        trunk_y = size - trunk_height
        pygame.draw.rect(self.image, (101, 67, 33), (trunk_x, trunk_y, trunk_width, trunk_height))
        
        # Feuillage (cercles verts)
        leaf_color = (34, 139, 34)
        leaf_radius = size // 3
        pygame.draw.circle(self.image, leaf_color, (size // 2, size // 3), leaf_radius)
        pygame.draw.circle(self.image, (46, 125, 50), (size // 3, size // 2), leaf_radius - 5)
        pygame.draw.circle(self.image, (56, 142, 60), (2 * size // 3, size // 2), leaf_radius - 5)
        
        self.rect = self.image.get_rect(center=(x, y))


class Bush(pygame.sprite.Sprite):
    """Buisson décoratif (pas de collision)"""
    
    def __init__(self, x, y, size=30):
        super().__init__()
        self.image = pygame.Surface((size, size // 2), pygame.SRCALPHA)
        
        colors = [(34, 139, 34), (46, 125, 50), (60, 160, 60)]
        for i in range(3):
            offset_x = i * (size // 4) + size // 6
            offset_y = size // 4
            radius = size // 4 + random.randint(-2, 2)
            pygame.draw.circle(self.image, colors[i % len(colors)], (offset_x, offset_y), radius)
        
        self.rect = self.image.get_rect(center=(x, y))


class GrassPatch(pygame.sprite.Sprite):
    """Touffe d'herbe décorative"""
    
    def __init__(self, x, y, size=20):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        
        grass_colors = [(34, 139, 34), (50, 150, 50), (76, 175, 80)]
        for i in range(5):
            start_x = i * (size // 5) + size // 10
            start_y = size
            end_x = start_x + random.randint(-3, 3)
            end_y = random.randint(2, size // 2)
            color = grass_colors[i % len(grass_colors)]
            pygame.draw.line(self.image, color, (start_x, start_y), (end_x, end_y), 2)
        
        self.rect = self.image.get_rect(center=(x, y))


class Rock(pygame.sprite.Sprite):
    """Rocher décoratif (collision)"""
    
    def __init__(self, x, y, size=35):
        super().__init__()
        self.image = pygame.Surface((size, size * 2 // 3), pygame.SRCALPHA)
        
        w, h = size, size * 2 // 3
        points = [
            (w // 4, h),
            (0, h * 2 // 3),
            (w // 6, h // 3),
            (w // 3, h // 6),
            (2 * w // 3, h // 6),
            (5 * w // 6, h // 3),
            (w, h * 2 // 3),
            (3 * w // 4, h)
        ]
        pygame.draw.polygon(self.image, (105, 105, 105), points)
        pygame.draw.polygon(self.image, (80, 80, 80), points, 2)
        pygame.draw.line(self.image, (130, 130, 130), (w // 3, h // 3), (w // 2, h // 4), 2)
        
        self.rect = self.image.get_rect(center=(x, y))


class Flower(pygame.sprite.Sprite):
    """Fleur décorative"""
    
    def __init__(self, x, y, size=15):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        
        pygame.draw.line(self.image, (34, 139, 34), (size // 2, size), (size // 2, size // 2), 2)
        
        petal_colors = [(255, 182, 193), (255, 105, 180), (255, 255, 0), (255, 165, 0), (148, 0, 211)]
        color = random.choice(petal_colors)
        center = (size // 2, size // 3)
        for angle in range(0, 360, 72):
            rad = math.radians(angle)
            px = int(center[0] + 4 * math.cos(rad))
            py = int(center[1] + 4 * math.sin(rad))
            pygame.draw.circle(self.image, color, (px, py), 3)
        
        pygame.draw.circle(self.image, (255, 255, 0), center, 2)
        self.rect = self.image.get_rect(center=(x, y))


class WaterPuddle(pygame.sprite.Sprite):
    """Flaque d'eau décorative"""
    
    def __init__(self, x, y, width=60, height=30):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        
        pygame.draw.ellipse(self.image, (30, 144, 200, 150), (0, 0, width, height))
        pygame.draw.ellipse(self.image, (100, 180, 230, 100), (width // 4, height // 4, width // 2, height // 2))
        
        self.rect = self.image.get_rect(center=(x, y))


class Room:
    """Grande carte avec plusieurs salles connectées"""
    
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = screen_width * 5
        self.map_height = screen_height * 4
        
        self.walls = pygame.sprite.Group()
        self.decorations = pygame.sprite.Group()
        self.solid_decorations = pygame.sprite.Group()
        self._create_map()
        self._add_sprite_decorations()  # NOUVEAUX SPRITES
        self._create_exterior_zone()
    
    def _create_map(self):
        """Crée la carte complète avec murs et obstacles"""
        wall_thickness = 25
        
        self.walls.add(Wall(0, 0, self.map_width, wall_thickness))
        self.walls.add(Wall(0, self.map_height - wall_thickness, self.map_width, wall_thickness))
        self.walls.add(Wall(0, 0, wall_thickness, self.map_height))
        self.walls.add(Wall(self.map_width - wall_thickness, 0, wall_thickness, self.map_height))
        
        room_width = self.screen_width
        room_height = self.screen_height
        
        for row in range(1, 3):
            y = row * room_height
            for col in range(4):
                x_start = col * room_width
                passage_x = x_start + room_width // 2 - 60
                
                if passage_x - x_start > wall_thickness:
                    self.walls.add(Wall(x_start, y - wall_thickness // 2, passage_x - x_start, wall_thickness))
                
                passage_end = passage_x + 120
                if x_start + room_width - passage_end > wall_thickness:
                    self.walls.add(Wall(passage_end, y - wall_thickness // 2, x_start + room_width - passage_end, wall_thickness))
        
        for col in range(1, 4):
            x = col * room_width
            for row in range(3):
                y_start = row * room_height
                passage_y = y_start + room_height // 2 - 60
                
                if passage_y - y_start > wall_thickness:
                    self.walls.add(Wall(x - wall_thickness // 2, y_start, wall_thickness, passage_y - y_start))
                
                passage_end = passage_y + 120
                if y_start + room_height - passage_end > wall_thickness:
                    self.walls.add(Wall(x - wall_thickness // 2, passage_end, wall_thickness, y_start + room_height - passage_end))
        
        self._add_obstacles()
    
    def _add_obstacles(self):
        """Ajoute des obstacles variés dans les salles (murs gris)"""
        room_width = self.screen_width
        room_height = self.screen_height
        
        obstacles = [
            (room_width // 4, room_height // 4, 50, 50),
            (3 * room_width // 4, room_height // 4, 50, 50),
            (room_width + 200, 150, 150, 25),
            (room_width + 200, 150, 25, 150),
            (room_width + room_width - 350, room_height - 200, 150, 25),
            (room_width + room_width - 225, room_height - 200, 25, 150),
            (2 * room_width + room_width // 3, room_height // 3, 60, 60),
            (2 * room_width + 2 * room_width // 3, room_height // 3, 60, 60),
            (2 * room_width + room_width // 3, 2 * room_height // 3, 60, 60),
            (2 * room_width + 2 * room_width // 3, 2 * room_height // 3, 60, 60),
            (3 * room_width + 100, 100, 25, room_height - 300),
            (3 * room_width + room_width - 125, 200, 25, room_height - 300),
            (room_width // 2 - 100, room_height + room_height // 2 - 12, 200, 25),
            (room_width // 2 - 12, room_height + room_height // 2 - 100, 25, 200),
            (room_width + 150, room_height + 150, 80, 25),
            (room_width + 200, room_height + 200, 80, 25),
            (room_width + 250, room_height + 250, 80, 25),
            (2 * room_width + 150, room_height + 100, 25, 200),
            (2 * room_width + 150, room_height + 100, 200, 25),
            (3 * room_width + 150, room_height + 150, 40, 40),
            (3 * room_width + 300, room_height + 150, 40, 40),
            (200, 2 * room_height + 200, 120, 120),
            (room_width + 200, 2 * room_height + 150, 25, 250),
            (2 * room_width + room_width // 2 - 100, 2 * room_height + room_height // 2 - 100, 200, 25),
            (3 * room_width + 100, 2 * room_height + 100, 60, 60),
        ]
        
        for x, y, w, h in obstacles:
            self.walls.add(Wall(x, y, w, h))
    
def _add_sprite_decorations(self):
    """Ajoute des sprites réels dans les salles"""
    room_width = self.screen_width
    room_height = self.screen_height
    
    sprite_obstacles = [
        # SALLE 0,0 - Spawn avec arbres et lampadaire
        (room_width // 2 - 100, room_height // 2, 'apocalypsetree1sprucegreen'),
        (150, 150, 'apocalypsetree3normalgreen'),
        (room_width - 150, 150, 'apocalypsebush1green'),
        (300, 200, 'apocalypsestreetlight1side'),
        
        # SALLE 1,0 - Zone avec camion
        (room_width + 400, 300, 'apocalypsecar7rustredtruck'),
        (room_width + 500, 500, 'apocalypsetree5biggreen'),
        (room_width + 200, 200, 'apocalypsestreetlight2up'),
        
        # SALLE 2,0 - Arbres et lampadaires
        (2 * room_width + 300, room_height // 2, 'apocalypsetree6pinebiggreen'),
        (2 * room_width + 600, 300, 'apocalypsestreetlight1side'),
        
        # SALLE 3,0 - Camion bleu
        (3 * room_width + 300, 300, 'apocalypsecar7rustbluetruck'),
        (3 * room_width + 500, 400, 'apocalypsetree2sprucesparsegreen'),
        
        # SALLE 0,1 - Nature
        (300, room_height + 300, 'apocalypsetree7birchgreen'),
        (500, room_height + 400, 'apocalypsebush2green'),
        (200, room_height + 200, 'apocalypsestreetlight3down'),
        
        # SALLE 1,1 - Zone urbaine
        (room_width + 400, room_height + 400, 'apocalypsestreetlight1side'),
        (room_width + 600, room_height + 300, 'apocalypsebarrelred1'),
        
        # SALLE 2,1 - Camion vert
        (2 * room_width + 200, room_height + 200, 'apocalypsecar7rustgreentruck'),
        (2 * room_width + 500, room_height + 400, 'apocalypsetree8birchgreen'),
        
        # SALLE 3,1 - Zone sombre
        (3 * room_width + 300, room_height + 300, 'apocalypsecar7rustorangetruck'),
        (3 * room_width + 500, room_height + 400, 'apocalypsestreetlight4sideovergrowndarkgreen'),
        
        # SALLE 0,2 - Forêt
        (200, 2 * room_height + 300, 'apocalypsetree9smalloakgreen'),
        (400, 2 * room_height + 400, 'apocalypsetree10smalloakgreen'),
        (150, 2 * room_height + 150, 'apocalypsebush1green'),
        
        # SALLE 1,2 - Village
        (room_width + 400, 2 * room_height + 400, 'apocalypsestreetlight5upovergrowngreen'),
        (room_width + 600, 2 * room_height + 300, 'apocalypsebarrelblue1'),
        
        # SALLE 2,2 - Arena avec camion jaune
        (2 * room_width + 300, 2 * room_height + 300, 'apocalypsecar7rustyellowtruck'),
        (2 * room_width + room_width - 300, 2 * room_height + 300, 'apocalypsetree5biggreen'),
        
        # SALLE 3,2 - Boss
        (3 * room_width + room_width // 2 + 200, 2 * room_height + room_height // 2, 'apocalypsecar7rustredtruck'),
        (3 * room_width + 300, 2 * room_height + 300, 'apocalypsestreetlight2up'),
    ]
    
    for x, y, sprite_type in sprite_obstacles:
        try:
            sprite = SpriteWall(x, y, sprite_type=sprite_type)
            self.walls.add(sprite)
            self.solid_decorations.add(sprite)
        except Exception as e:
            print(f"Sprite ignoré '{sprite_type}': {e}")

    def _create_exterior_zone(self):
        """Crée une zone extérieure avec végétation procédurale"""
        room_width = self.screen_width
        room_height = self.screen_height
        
        exterior_start_x = 4 * room_width + 50
        exterior_start_y = 50
        exterior_width = room_width - 100
        exterior_height = 3 * room_height - 100
        south_start_y = 3 * room_height + 50
        
        # ZONE EST (Forêt)
        for _ in range(25):
            x = random.randint(int(exterior_start_x), int(exterior_start_x + exterior_width - 50))
            y = random.randint(int(exterior_start_y + 100), int(exterior_start_y + exterior_height - 50))
            tree = Tree(x, y, random.randint(45, 70))
            self.solid_decorations.add(tree)
            self.walls.add(tree)
        
        for _ in range(40):
            x = random.randint(int(exterior_start_x), int(exterior_start_x + exterior_width))
            y = random.randint(int(exterior_start_y), int(exterior_start_y + exterior_height))
            bush = Bush(x, y, random.randint(25, 40))
            self.decorations.add(bush)
        
        for _ in range(60):
            x = random.randint(int(exterior_start_x), int(exterior_start_x + exterior_width))
            y = random.randint(int(exterior_start_y), int(exterior_start_y + exterior_height))
            grass = GrassPatch(x, y, random.randint(15, 25))
            self.decorations.add(grass)
        
        for _ in range(10):
            x = random.randint(int(exterior_start_x + 50), int(exterior_start_x + exterior_width - 50))
            y = random.randint(int(exterior_start_y + 100), int(exterior_start_y + exterior_height - 50))
            rock = Rock(x, y, random.randint(30, 50))
            self.solid_decorations.add(rock)
            self.walls.add(rock)
        
       
