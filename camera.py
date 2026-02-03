"""
Classe représentant la caméra qui suit le joueur
"""
import pygame


class Camera:
    """Caméra qui suit le joueur sur la carte"""
    
    def __init__(self, screen_width, screen_height, map_width, map_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height
        
        # Position de la caméra (coin supérieur gauche)
        self.x = 0
        self.y = 0
    
    def update(self, target):
        """Mise à jour de la position de la caméra pour suivre la cible"""
        # Centrer la caméra sur la cible
        self.x = target.pos.x - self.screen_width // 2
        self.y = target.pos.y - self.screen_height // 2
        
        # Limiter la caméra aux bords de la carte
        self.x = max(0, min(self.x, self.map_width - self.screen_width))
        self.y = max(0, min(self.y, self.map_height - self.screen_height))
    
    def apply(self, entity):
        """Retourne la position d'un sprite par rapport à la caméra"""
        return pygame.Rect(
            entity.rect.x - self.x,
            entity.rect.y - self.y,
            entity.rect.width,
            entity.rect.height
        )
    
    def apply_rect(self, rect):
        """Retourne un rectangle transformé par rapport à la caméra"""
        return pygame.Rect(
            rect.x - self.x,
            rect.y - self.y,
            rect.width,
            rect.height
        )
    
    def apply_pos(self, pos):
        """Convertit une position monde en position écran"""
        return (pos[0] - self.x, pos[1] - self.y)
    
    def screen_to_world(self, pos):
        """Convertit une position écran en position monde"""
        return (pos[0] + self.x, pos[1] + self.y)