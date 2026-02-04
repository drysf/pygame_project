"""
Classe représentant une salle avec des murs
"""
import os
import pygame
import random
import math
from room_auto import Wall as SpriteWall

ASSETS_ENV_PATH = os.path.join("assets", "Environnement")

def load_random_image(subfolder, scale=None):
    """Charge une image aléatoire dans assets/Environnement/<subfolder>"""
    folder_path = os.path.join(ASSETS_ENV_PATH, subfolder)
    files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
    if not files:
        raise FileNotFoundError(f"Aucun asset dans {folder_path}")
    filename = random.choice(files)
    full_path = os.path.join(folder_path, filename)
    image = pygame.image.load(full_path).convert_alpha()
    if scale is not None:
        image = pygame.transform.scale(image, scale)
    return image
class Wall(pygame.sprite.Sprite):
    """Mur simple gris"""
    
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((80, 80, 80))
        pygame.draw.rect(self.image, (60, 60, 60), (0, 0, width, height), 3)
        self.rect = self.image.get_rect(topleft=(x, y))


class Tree(pygame.sprite.Sprite):
    """Arbre décoratif (collision) basé sur un asset"""
    def __init__(self, x, y, size=50):
        super().__init__()
        # Par exemple on fixe la hauteur à size et on garde le ratio
        img = load_random_image("Arbres")  # assets/Environnement/Arbres
        w, h = img.get_size()
        new_h = size
        new_w = int(w * (new_h / h))
        self.image = pygame.transform.scale(img, (new_w, new_h))
        self.rect = self.image.get_rect(center=(x, y))


class Bush(pygame.sprite.Sprite):
    """Buisson décoratif (pas de collision) basé sur un asset"""
    def __init__(self, x, y, size=30):
        super().__init__()
        img = load_random_image("Bush")
        w, h = img.get_size()
        new_h = size
        new_w = int(w * (new_h / h))
        self.image = pygame.transform.scale(img, (new_w, new_h))
        self.rect = self.image.get_rect(center=(x, y))

class GrassPatch(pygame.sprite.Sprite):
    """Touffe d'herbe décorative basée sur un asset"""
    def __init__(self, x, y, size=20):
        super().__init__()
        img = load_random_image("Herbe")
        w, h = img.get_size()
        new_h = size
        new_w = int(w * (new_h / h))
        self.image = pygame.transform.scale(img, (new_w, new_h))
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
    """Fleur décorative basée sur un asset"""
    def __init__(self, x, y, size=15):
        super().__init__()
        img = load_random_image("Fleurs")
        w, h = img.get_size()
        new_h = size
        new_w = int(w * (new_h / h))
        self.image = pygame.transform.scale(img, (new_w, new_h))
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
        # SALLE 0,0 - Barils et cônes
        (room_width // 2 - 100, room_height // 2, 'apocalypsebarrelred1'),
        (150, 150, 'apocalypsebarrelblue1'),
        (room_width - 150, 150, 'apocalypsetrafficcone'),
        
        # SALLE 1,0 - Camion et barils
        (room_width + 400, 300, 'apocalypsecar7rustredtruck'),
        (room_width + 200, 200, 'apocalypsebarrelrustred2'),
        (room_width + 600, 400, 'apocalypsetrafficcone'),
        
        # SALLE 2,0 - Véhicules variés
        (2 * room_width + 300, room_height // 2, 'apocalypsecar7rustbluetruck'),
        (2 * room_width + 600, 300, 'apocalypsebarrelblue2'),
        
        # SALLE 3,0 - Zone de véhicules
        (3 * room_width + 300, 300, 'apocalypsecar4rustred'),
        (3 * room_width + 500, 400, 'apocalypsetrafficcone'),
        (3 * room_width + 200, 500, 'apocalypsebarrelred2'),
        
        # SALLE 0,1 - Barils et cônes
        (300, room_height + 300, 'apocalypsebarrelrustred1'),
        (500, room_height + 400, 'apocalypsetrafficcone'),
        (200, room_height + 200, 'apocalypsebarrelblue1'),
        
        # SALLE 1,1 - Camions
        (room_width + 400, room_height + 400, 'apocalypsecar7rustgreentruck'),
        (room_width + 200, room_height + 300, 'apocalypsebarrelred1'),
        
        # SALLE 2,1 - Véhicules endommagés
        (2 * room_width + 200, room_height + 200, 'apocalypsecar6rustredscrap'),
        (2 * room_width + 500, room_height + 400, 'apocalypsetrafficcone'),
        (2 * room_width + 700, room_height + 300, 'apocalypsebarrelrustred2'),
        
        # SALLE 3,1 - Camions apocalypse
        (3 * room_width + 300, room_height + 300, 'apocalypsecar7rustorangetruck'),
        (3 * room_width + 600, room_height + 500, 'apocalypsebarrelblue2'),
        
        # SALLE 0,2 - Barils multiples
        (200, 2 * room_height + 300, 'apocalypsebarrelred1'),
        (400, 2 * room_height + 400, 'apocalypsebarrelblue1'),
        (150, 2 * room_height + 150, 'apocalypsetrafficcone'),
        
        # SALLE 1,2 - Véhicules
        (room_width + 400, 2 * room_height + 400, 'apocalypsecar4rustblue'),
        (room_width + 600, 2 * room_height + 300, 'apocalypsebarrelrustred1'),
        
        # SALLE 2,2 - Arena avec camions
        (2 * room_width + 300, 2 * room_height + 300, 'apocalypsecar7rustyellowtruck'),
        (2 * room_width + room_width - 300, 2 * room_height + 300, 'apocalypsetrafficcone'),
        (2 * room_width + 500, 2 * room_height + 500, 'apocalypsebarrelred2'),
        
        # SALLE 3,2 - Boss avec véhicules
        (3 * room_width + room_width // 2 + 200, 2 * room_height + room_height // 2, 'apocalypsecar7rustdarkbluetruck'),
        (3 * room_width + 300, 2 * room_height + 300, 'apocalypsebarrelblue2'),
        (3 * room_width + 700, 2 * room_height + 400, 'apocalypsetrafficcone'),
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
        
       
