"""
Gestionnaire de niveaux - Génère différentes cartes
"""
import pygame
import random
import os
from room import Wall, Tree, Bush, GrassPatch, Rock, Flower, WaterPuddle


class LevelManager:
    """Gestionnaire des différents niveaux"""
    
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def create_level(self, level_config):
        """Crée un niveau basé sur la configuration"""
        map_type = level_config.get("map_type", "warehouse")
        
        if map_type == "warehouse":
            return WarehouseMap(self.screen_width, self.screen_height)
        elif map_type == "military":
            return MilitaryBaseMap(self.screen_width, self.screen_height)
        elif map_type == "forest":
            return ForestMap(self.screen_width, self.screen_height)
        elif map_type == "bunker":
            return BunkerMap(self.screen_width, self.screen_height)
        elif map_type == "headquarters":
            return HeadquartersMap(self.screen_width, self.screen_height)
        else:
            return WarehouseMap(self.screen_width, self.screen_height)


class BaseMap:
    """Classe de base pour les cartes"""
    
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = screen_width * 2
        self.map_height = screen_height * 2
        
        self.walls = pygame.sprite.Group()
        self.decorations = pygame.sprite.Group()
        self.ground_color = (40, 40, 45)
        self.ground_image = None # Image de sol
        self.exterior_zones = []  # Liste de (rect, color) pour zones extérieures
        
        self._create_boundary_walls()
    
    def _create_boundary_walls(self):
        """Crée les murs de bordure"""
        wall_thickness = 25
        
        # Mur haut
        self.walls.add(Wall(0, 0, self.map_width, wall_thickness))
        # Mur bas
        self.walls.add(Wall(0, self.map_height - wall_thickness, self.map_width, wall_thickness))
        # Mur gauche
        self.walls.add(Wall(0, 0, wall_thickness, self.map_height))
        # Mur droit
        self.walls.add(Wall(self.map_width - wall_thickness, 0, wall_thickness, self.map_height))
    
    def get_spawn_position(self):
        """Retourne la position de spawn du joueur"""
        return (self.screen_width // 2, self.screen_height // 2)
    
    def get_enemy_spawn_zones(self):
        """Retourne les zones où les ennemis peuvent spawn"""
        return [(100, 100, self.map_width - 200, self.map_height - 200)]
        
    def _load_ground_image(self, level_number):
        """Charge l'image du sol pour un niveau spécifique"""
        try:
            asset_path = os.path.join("assets", "Environnement", "Sol", f"sol{level_number}.png")
            if os.path.exists(asset_path):
                self.ground_image = pygame.image.load(asset_path).convert()
                print(f"✓ Sol niveau {level_number} chargé: {asset_path}")
            else:
                print(f"✗ Image de sol non trouvée: {asset_path}")
        except Exception as e:
            print(f"✗ Erreur chargement sol {level_number}: {e}")

class WarehouseMap(BaseMap):
    """Carte: Entrepôt - Zone d'entraînement"""
    
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.map_width = int(screen_width * 2)
        self.map_height = int(screen_height * 1.5)
        self.ground_color = (50, 45, 40)
        self._load_ground_image(1) # Charger le sol du niveau 1

        # Recréer les murs de bordure avec la bonne taille
        self.walls.empty()
        self._create_boundary_walls()
        self._create_obstacles()
    
    def _create_obstacles(self):
        """Crée les obstacles de l'entrepôt"""
        # Caisses et étagères
        crate_positions = [
            (200, 200, 80, 80),
            (400, 150, 60, 60),
            (600, 300, 100, 50),
            (self.map_width - 300, 200, 80, 80),
            (self.map_width - 500, 350, 60, 120),
            (300, self.map_height - 300, 120, 60),
            (self.map_width // 2 - 50, self.map_height // 2 - 50, 100, 100),
            (self.map_width // 2 + 150, self.map_height // 2, 60, 60),
            (self.map_width // 2 - 200, self.map_height // 2 + 100, 60, 60),
        ]
        
        for x, y, w, h in crate_positions:
            try:
                crate = Wall(x, y, sprite_type='apocalypse_crate_wood_1')  # ← N'existe PAS !
                self.walls.add(crate)
                print(f"✓ Caisse créée en ({x}, {y})")
            except Exception as e:
                print(f"✗ Erreur caisse: {e}")


class MilitaryBaseMap(BaseMap):
    """Carte: Base Militaire"""
    
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.map_width = int(screen_width * 3)
        self.map_height = int(screen_height * 2)
        self.ground_color = (45, 50, 45)
        self._load_ground_image(2)  # Charge sol niveau 2

        self.walls.empty()
        self._create_boundary_walls()
        self._create_base_layout()
    
    def _create_base_layout(self):
        """Crée la disposition de la base militaire"""
        # Murs intérieurs formant des couloirs
        wall_thickness = 25
        room_w = self.screen_width
        room_h = self.screen_height
        
        # Mur horizontal central avec passage
        self.walls.add(Wall(0, room_h, room_w - 100, wall_thickness))
        self.walls.add(Wall(room_w, room_h, self.map_width - room_w, wall_thickness))
        
        # Mur vertical
        self.walls.add(Wall(room_w, 0, wall_thickness, room_h - 100))
        self.walls.add(Wall(room_w, room_h + 100, wall_thickness, room_h - 100))
        
        # Mur vertical droit
        self.walls.add(Wall(2 * room_w, room_h // 2, wall_thickness, room_h))
        
        # Obstacles - véhicules militaires (rectangles)
        vehicles = [
            (200, 200, 150, 80),
            (self.map_width - 400, 300, 150, 80),
            (room_w + 200, room_h + 200, 100, 60),
            (100, room_h + 300, 120, 70),
        ]
        
        for x, y, w, h in vehicles:
            vehicle = Wall(x, y, w, h)
            vehicle.image.fill((60, 80, 60))  # Vert militaire
            pygame.draw.rect(vehicle.image, (40, 60, 40), (0, 0, w, h), 3)
            self.walls.add(vehicle)
        
        # Barricades
        for i in range(5):
            x = 400 + i * 200
            barricade = Wall(x, room_h - 150, 60, 30)
            barricade.image.fill((80, 80, 80))
            self.walls.add(barricade)


class ForestMap(BaseMap):
    """Carte: Forêt - Extérieur"""
    
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.map_width = int(screen_width * 3)
        self.map_height = int(screen_height * 3)
        self.ground_color = (34, 85, 34)
        self._load_ground_image(3)  # Charge sol niveau 3
        
        self.walls.empty()
        self._create_boundary_walls()
        self._create_forest()
        
        # Toute la carte est extérieure
        self.exterior_zones = [
            (pygame.Rect(0, 0, self.map_width, self.map_height), (34, 85, 34))
        ]
    
    def _create_forest(self):
        """Crée la forêt avec arbres et végétation"""
        # Arbres (bloquent le passage)
        for _ in range(60):
            x = random.randint(100, self.map_width - 100)
            y = random.randint(100, self.map_height - 100)
            
            # Éviter la zone de spawn
            if abs(x - self.screen_width // 2) < 200 and abs(y - self.screen_height // 2) < 200:
                continue
            
            tree = Tree(x, y, random.randint(50, 80))
            self.walls.add(tree)
        
        # Rochers
        for _ in range(20):
            x = random.randint(100, self.map_width - 100)
            y = random.randint(100, self.map_height - 100)
            rock = Rock(x, y, random.randint(35, 55))
            self.walls.add(rock)
        
        # Buissons (décoratifs)
        for _ in range(80):
            x = random.randint(50, self.map_width - 50)
            y = random.randint(50, self.map_height - 50)
            bush = Bush(x, y, random.randint(25, 45))
            self.decorations.add(bush)
        
        # Herbe
        for _ in range(150):
            x = random.randint(50, self.map_width - 50)
            y = random.randint(50, self.map_height - 50)
            grass = GrassPatch(x, y, random.randint(15, 30))
            self.decorations.add(grass)
        
        # Fleurs
        for _ in range(60):
            x = random.randint(50, self.map_width - 50)
            y = random.randint(50, self.map_height - 50)
            flower = Flower(x, y, random.randint(12, 20))
            self.decorations.add(flower)
        
        # Quelques flaques d'eau
        for _ in range(8):
            x = random.randint(200, self.map_width - 200)
            y = random.randint(200, self.map_height - 200)
            puddle = WaterPuddle(x, y, random.randint(60, 100), random.randint(30, 50))
            self.decorations.add(puddle)


class BunkerMap(BaseMap):
    """Carte: Bunker - Espace confiné"""
    
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.map_width = int(screen_width * 2.5)
        self.map_height = int(screen_height * 2)
        self.ground_color = (35, 35, 40)
        self._load_ground_image(4)  # Charge sol niveau 4
        
        self.walls.empty()
        self._create_boundary_walls()
        self._create_bunker_layout()
    
    def _create_bunker_layout(self):
        """Crée le labyrinthe du bunker"""
        wall_thickness = 30
        
        # Labyrinthe de couloirs
        corridors = [
            # Couloirs horizontaux
            (200, 200, 400, wall_thickness),
            (0, 400, 300, wall_thickness),
            (400, 400, 600, wall_thickness),
            (200, 600, 500, wall_thickness),
            (800, 600, 400, wall_thickness),
            (100, 800, 600, wall_thickness),
            (800, 800, 400, wall_thickness),
            
            # Couloirs verticaux
            (300, 0, wall_thickness, 200),
            (600, 200, wall_thickness, 200),
            (300, 400, wall_thickness, 200),
            (700, 400, wall_thickness, 300),
            (200, 600, wall_thickness, 200),
            (500, 700, wall_thickness, 300),
            (900, 200, wall_thickness, 400),
            (1100, 500, wall_thickness, 400),
        ]
        
        for x, y, w, h in corridors:
            self.walls.add(Wall(x, y, w, h))
        
        # Piliers
        pillar_positions = [
            (450, 300), (750, 300), (450, 500), (900, 500),
            (300, 700), (600, 900), (1000, 700),
        ]
        
        for px, py in pillar_positions:
            pillar = Wall(px, py, 40, 40)
            pillar.image.fill((60, 60, 65))
            self.walls.add(pillar)
    
    def get_spawn_position(self):
        """Retourne une position de spawn dans une zone ouverte"""
        # Spawn au centre-droit de la carte, zone ouverte entre les murs
        return (self.map_width - 200, self.map_height - 150)


class HeadquartersMap(BaseMap):
    """Carte: QG Ennemi - Mission finale"""
    
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.map_width = int(screen_width * 4)
        self.map_height = int(screen_height * 3)
        self.ground_color = (40, 35, 35)
        self._load_ground_image(5)  # Charge sol niveau 5
        
        self.walls.empty()
        self._create_boundary_walls()
        self._create_headquarters()
        
        # Zone extérieure au sud
        self.exterior_zones = [
            (pygame.Rect(0, self.screen_height * 2, self.map_width, self.screen_height), (46, 80, 46))
        ]
    
    def _create_headquarters(self):
        """Crée le QG ennemi"""
        wall_thickness = 25
        room_w = self.screen_width
        room_h = self.screen_height
        
        # Structure de plusieurs salles
        # Murs horizontaux
        for row in range(1, 3):
            y = row * room_h
            # Segments avec passages
            for col in range(4):
                x_start = col * room_w
                passage_x = x_start + room_w // 2 - 50
                
                if passage_x - x_start > wall_thickness:
                    self.walls.add(Wall(x_start, y, passage_x - x_start, wall_thickness))
                
                passage_end = passage_x + 100
                if x_start + room_w - passage_end > wall_thickness:
                    self.walls.add(Wall(passage_end, y, x_start + room_w - passage_end, wall_thickness))
        
        # Murs verticaux
        for col in range(1, 4):
            x = col * room_w
            for row in range(3):
                y_start = row * room_h
                passage_y = y_start + room_h // 2 - 50
                
                if passage_y - y_start > wall_thickness:
                    self.walls.add(Wall(x, y_start, wall_thickness, passage_y - y_start))
                
                passage_end = passage_y + 100
                if y_start + room_h - passage_end > wall_thickness:
                    self.walls.add(Wall(x, passage_end, wall_thickness, y_start + room_h - passage_end))
        
        # Obstacles variés dans chaque salle
        obstacles = [
            # Salle de commandement (centre)
            (room_w * 2 - 100, room_h - 100, 200, 25),
            (room_w * 2 - 100, room_h + 75, 200, 25),
            (room_w * 2 - 100, room_h - 100, 25, 200),
            (room_w * 2 + 75, room_h - 100, 25, 200),
            
            # Armurerie
            (100, 100, 150, 30),
            (100, 200, 150, 30),
            (100, 300, 150, 30),
            
            # Baraquements
            (room_w + 100, 150, 200, 50),
            (room_w + 100, 300, 200, 50),
            (room_w + 400, 150, 200, 50),
            (room_w + 400, 300, 200, 50),
        ]
        
        for x, y, w, h in obstacles:
            self.walls.add(Wall(x, y, w, h))
        
        # Zone extérieure avec arbres
        for _ in range(30):
            x = random.randint(100, self.map_width - 100)
            y = random.randint(int(room_h * 2 + 100), int(self.map_height - 100))
            tree = Tree(x, y, random.randint(50, 70))
            self.walls.add(tree)
        
        # Buissons dans la zone extérieure
        for _ in range(40):
            x = random.randint(50, self.map_width - 50)
            y = random.randint(int(room_h * 2 + 50), int(self.map_height - 50))
            bush = Bush(x, y, random.randint(25, 40))
            self.decorations.add(bush)
