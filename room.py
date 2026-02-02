"""
Classe représentant une salle avec des murs
"""
import pygame
import random


class Wall(pygame.sprite.Sprite):
    """Mur solid"""
    
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((80, 80, 80))
        pygame.draw.rect(self.image, (60, 60, 60), (0, 0, width, height), 3)
        self.rect = self.image.get_rect(topleft=(x, y))


class Room:
    """Grande carte avec plusieurs salles connectées"""
    
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Taille de la carte (beaucoup plus grande que l'écran)
        self.map_width = screen_width * 4
        self.map_height = screen_height * 3
        
        self.walls = pygame.sprite.Group()
        self._create_map()
    
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
