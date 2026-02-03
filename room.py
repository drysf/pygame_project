"""
Classe représentant une salle avec des murs
"""
import pygame
import random
import math


class Wall(pygame.sprite.Sprite):
    """Mur solid"""
    
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
        leaf_color = (34, 139, 34)  # Vert forêt
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
        
        # Plusieurs cercles verts pour le buisson
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
        
        # Dessiner des brins d'herbe
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
        
        # Forme de rocher irrégulière avec polygone
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
        
        # Reflet
        pygame.draw.line(self.image, (130, 130, 130), (w // 3, h // 3), (w // 2, h // 4), 2)
        
        self.rect = self.image.get_rect(center=(x, y))


class Flower(pygame.sprite.Sprite):
    """Fleur décorative"""
    
    def __init__(self, x, y, size=15):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Tige
        pygame.draw.line(self.image, (34, 139, 34), (size // 2, size), (size // 2, size // 2), 2)
        
        # Pétales
        petal_colors = [(255, 182, 193), (255, 105, 180), (255, 255, 0), (255, 165, 0), (148, 0, 211)]
        color = random.choice(petal_colors)
        center = (size // 2, size // 3)
        for angle in range(0, 360, 72):
            rad = math.radians(angle)
            px = int(center[0] + 4 * math.cos(rad))
            py = int(center[1] + 4 * math.sin(rad))
            pygame.draw.circle(self.image, color, (px, py), 3)
        
        # Centre
        pygame.draw.circle(self.image, (255, 255, 0), center, 2)
        
        self.rect = self.image.get_rect(center=(x, y))


class WaterPuddle(pygame.sprite.Sprite):
    """Flaque d'eau décorative"""
    
    def __init__(self, x, y, width=60, height=30):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # Ellipse bleue pour l'eau
        pygame.draw.ellipse(self.image, (30, 144, 200, 150), (0, 0, width, height))
        pygame.draw.ellipse(self.image, (100, 180, 230, 100), (width // 4, height // 4, width // 2, height // 2))
        
        self.rect = self.image.get_rect(center=(x, y))


class Room:
    """Grande carte avec plusieurs salles connectées"""
    
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Taille de la carte (beaucoup plus grande que l'écran)
        self.map_width = screen_width * 5  # Agrandi pour zone extérieure
        self.map_height = screen_height * 4  # Agrandi pour zone extérieure
        
        self.walls = pygame.sprite.Group()
        self.decorations = pygame.sprite.Group()  # Décorations sans collision
        self.solid_decorations = pygame.sprite.Group()  # Décorations avec collision
        self._create_map()
        self._create_exterior_zone()
    
    def _create_map(self):
        """Crée la carte complète avec murs et obstacles"""
        wall_thickness = 25
        
        # Murs extérieurs de la carte
        # Mur haut
        self.walls.add(Wall(0, 0, self.map_width, wall_thickness))
        # Mur bas
        self.walls.add(Wall(0, self.map_height - wall_thickness, self.map_width, wall_thickness))
        # Mur gauche
        self.walls.add(Wall(0, 0, wall_thickness, self.map_height))
        # Mur droit
        self.walls.add(Wall(self.map_width - wall_thickness, 0, wall_thickness, self.map_height))
        
        # Créer une grille de salles
        room_width = self.screen_width
        room_height = self.screen_height
        
        # Murs intérieurs horizontaux avec des ouvertures
        for row in range(1, 3):
            y = row * room_height
            # Créer des segments de mur avec des passages
            for col in range(4):
                x_start = col * room_width
                # Laisser un passage au milieu
                passage_x = x_start + room_width // 2 - 60
                
                # Mur gauche du passage
                if passage_x - x_start > wall_thickness:
                    self.walls.add(Wall(x_start, y - wall_thickness // 2, 
                                       passage_x - x_start, wall_thickness))
                
                # Mur droit du passage
                passage_end = passage_x + 120
                if x_start + room_width - passage_end > wall_thickness:
                    self.walls.add(Wall(passage_end, y - wall_thickness // 2,
                                       x_start + room_width - passage_end, wall_thickness))
        
        # Murs intérieurs verticaux avec des ouvertures
        for col in range(1, 4):
            x = col * room_width
            for row in range(3):
                y_start = row * room_height
                # Laisser un passage au milieu
                passage_y = y_start + room_height // 2 - 60
                
                # Mur haut du passage
                if passage_y - y_start > wall_thickness:
                    self.walls.add(Wall(x - wall_thickness // 2, y_start,
                                       wall_thickness, passage_y - y_start))
                
                # Mur bas du passage
                passage_end = passage_y + 120
                if y_start + room_height - passage_end > wall_thickness:
                    self.walls.add(Wall(x - wall_thickness // 2, passage_end,
                                       wall_thickness, y_start + room_height - passage_end))
        
        # Ajouter des obstacles dans chaque salle
        self._add_obstacles()
    
    def _add_obstacles(self):
        """Ajoute des obstacles variés dans les salles"""
        room_width = self.screen_width
        room_height = self.screen_height
        
        obstacles = [
            # Salle 0,0 (spawn) - quelques piliers
            (room_width // 4, room_height // 4, 50, 50),
            (3 * room_width // 4, room_height // 4, 50, 50),
            
            # Salle 1,0 - mur en L
            (room_width + 200, 150, 150, 25),
            (room_width + 200, 150, 25, 150),
            (room_width + room_width - 350, room_height - 200, 150, 25),
            (room_width + room_width - 225, room_height - 200, 25, 150),
            
            # Salle 2,0 - piliers
            (2 * room_width + room_width // 3, room_height // 3, 60, 60),
            (2 * room_width + 2 * room_width // 3, room_height // 3, 60, 60),
            (2 * room_width + room_width // 3, 2 * room_height // 3, 60, 60),
            (2 * room_width + 2 * room_width // 3, 2 * room_height // 3, 60, 60),
            
            # Salle 3,0 - couloir
            (3 * room_width + 100, 100, 25, room_height - 300),
            (3 * room_width + room_width - 125, 200, 25, room_height - 300),
            
            # Salle 0,1 - croix
            (room_width // 2 - 100, room_height + room_height // 2 - 12, 200, 25),
            (room_width // 2 - 12, room_height + room_height // 2 - 100, 25, 200),
            
            # Salle 1,1 - murs diagonaux simulés
            (room_width + 150, room_height + 150, 80, 25),
            (room_width + 200, room_height + 200, 80, 25),
            (room_width + 250, room_height + 250, 80, 25),
            (room_width + room_width - 230, room_height + 150, 80, 25),
            (room_width + room_width - 280, room_height + 200, 80, 25),
            (room_width + room_width - 330, room_height + 250, 80, 25),
            
            # Salle 2,1 - labyrinthe simple
            (2 * room_width + 150, room_height + 100, 25, 200),
            (2 * room_width + 150, room_height + 100, 200, 25),
            (2 * room_width + room_width - 350, room_height + room_height - 300, 200, 25),
            (2 * room_width + room_width - 175, room_height + room_height - 300, 25, 200),
            
            # Salle 3,1 - nombreux petits piliers
            (3 * room_width + 150, room_height + 150, 40, 40),
            (3 * room_width + 300, room_height + 150, 40, 40),
            (3 * room_width + 450, room_height + 150, 40, 40),
            (3 * room_width + 150, room_height + 350, 40, 40),
            (3 * room_width + 300, room_height + 350, 40, 40),
            (3 * room_width + 450, room_height + 350, 40, 40),
            (3 * room_width + 150, room_height + 550, 40, 40),
            (3 * room_width + 300, room_height + 550, 40, 40),
            (3 * room_width + 450, room_height + 550, 40, 40),
            
            # Salle 0,2 - grands blocs
            (200, 2 * room_height + 200, 120, 120),
            (room_width - 320, 2 * room_height + room_height - 320, 120, 120),
            
            # Salle 1,2 - murs parallèles
            (room_width + 200, 2 * room_height + 150, 25, 250),
            (room_width + 400, 2 * room_height + room_height - 400, 25, 250),
            (room_width + 600, 2 * room_height + 150, 25, 250),
            
            # Salle 2,2 - enclos central
            (2 * room_width + room_width // 2 - 100, 2 * room_height + room_height // 2 - 100, 200, 25),
            (2 * room_width + room_width // 2 - 100, 2 * room_height + room_height // 2 + 75, 200, 25),
            (2 * room_width + room_width // 2 - 100, 2 * room_height + room_height // 2 - 100, 25, 100),
            (2 * room_width + room_width // 2 + 75, 2 * room_height + room_height // 2, 25, 100),
            
            # Salle 3,2 - arena finale
            (3 * room_width + 100, 2 * room_height + 100, 60, 60),
            (3 * room_width + room_width - 160, 2 * room_height + 100, 60, 60),
            (3 * room_width + 100, 2 * room_height + room_height - 160, 60, 60),
            (3 * room_width + room_width - 160, 2 * room_height + room_height - 160, 60, 60),
            (3 * room_width + room_width // 2 - 40, 2 * room_height + room_height // 2 - 40, 80, 80),
        ]
        
        for x, y, w, h in obstacles:
            self.walls.add(Wall(x, y, w, h))
    
    def _create_exterior_zone(self):
        """Crée une zone extérieure avec végétation et décor naturel"""
        room_width = self.screen_width
        room_height = self.screen_height
        
        # Zone extérieure commence après les salles intérieures
        exterior_start_x = 4 * room_width + 50
        exterior_start_y = 50
        exterior_width = room_width - 100
        exterior_height = 3 * room_height - 100
        
        # Passage vers l'extérieur (ouverture dans le mur est)
        # Déjà géré par les murs extérieurs redimensionnés
        
        # Zone sud (nouvelle rangée de salles extérieures)
        south_start_y = 3 * room_height + 50
        
        # --- ZONE EST (Forêt) ---
        # Arbres dispersés
        for _ in range(25):
            x = random.randint(int(exterior_start_x), int(exterior_start_x + exterior_width - 50))
            y = random.randint(int(exterior_start_y + 100), int(exterior_start_y + exterior_height - 50))
            tree = Tree(x, y, random.randint(45, 70))
            self.solid_decorations.add(tree)
            self.walls.add(tree)  # Les arbres bloquent le passage
        
        # Buissons
        for _ in range(40):
            x = random.randint(int(exterior_start_x), int(exterior_start_x + exterior_width))
            y = random.randint(int(exterior_start_y), int(exterior_start_y + exterior_height))
            bush = Bush(x, y, random.randint(25, 40))
            self.decorations.add(bush)
        
        # Herbe
        for _ in range(60):
            x = random.randint(int(exterior_start_x), int(exterior_start_x + exterior_width))
            y = random.randint(int(exterior_start_y), int(exterior_start_y + exterior_height))
            grass = GrassPatch(x, y, random.randint(15, 25))
            self.decorations.add(grass)
        
        # Rochers
        for _ in range(10):
            x = random.randint(int(exterior_start_x + 50), int(exterior_start_x + exterior_width - 50))
            y = random.randint(int(exterior_start_y + 100), int(exterior_start_y + exterior_height - 50))
            rock = Rock(x, y, random.randint(30, 50))
            self.solid_decorations.add(rock)
            self.walls.add(rock)  # Les rochers bloquent le passage
        
        # Fleurs
        for _ in range(30):
            x = random.randint(int(exterior_start_x), int(exterior_start_x + exterior_width))
            y = random.randint(int(exterior_start_y), int(exterior_start_y + exterior_height))
            flower = Flower(x, y, random.randint(12, 18))
            self.decorations.add(flower)
        
        # --- ZONE SUD (Jardin/Parc) ---
        # Arbres alignés (allée)
        for i in range(8):
            x = 200 + i * 250
            tree1 = Tree(x, south_start_y + 150, 55)
            tree2 = Tree(x, south_start_y + room_height - 200, 55)
            self.solid_decorations.add(tree1, tree2)
            self.walls.add(tree1, tree2)
        
        # Flaques d'eau
        for _ in range(5):
            x = random.randint(300, int(4 * room_width - 300))
            y = random.randint(int(south_start_y + 200), int(south_start_y + room_height - 200))
            puddle = WaterPuddle(x, y, random.randint(50, 80), random.randint(25, 40))
            self.decorations.add(puddle)
        
        # Massifs de fleurs
        flower_clusters = [
            (500, south_start_y + 400),
            (1200, south_start_y + 300),
            (2000, south_start_y + 500),
            (2800, south_start_y + 350),
        ]
        for cx, cy in flower_clusters:
            for _ in range(15):
                x = cx + random.randint(-60, 60)
                y = cy + random.randint(-40, 40)
                flower = Flower(x, y, random.randint(12, 18))
                self.decorations.add(flower)
        
        # Buissons décoratifs dans le parc
        for _ in range(30):
            x = random.randint(100, int(4 * room_width - 100))
            y = random.randint(int(south_start_y + 50), int(south_start_y + room_height - 50))
            bush = Bush(x, y, random.randint(30, 45))
            self.decorations.add(bush)
        
        # Herbe dans le parc
        for _ in range(80):
            x = random.randint(100, int(4 * room_width - 100))
            y = random.randint(int(south_start_y + 50), int(south_start_y + room_height - 50))
            grass = GrassPatch(x, y, random.randint(15, 25))
            self.decorations.add(grass)
        
        # Gros rochers décoratifs
        rock_positions = [
            (800, south_start_y + 600),
            (1800, south_start_y + 250),
            (3200, south_start_y + 550),
        ]
        for rx, ry in rock_positions:
            rock = Rock(rx, ry, random.randint(45, 60))
            self.solid_decorations.add(rock)
            self.walls.add(rock)
