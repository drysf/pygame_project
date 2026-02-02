"""Gestionnaire de caméra pour le défilement."""
from config import GameConfig


class Camera:
    """Gestion de la caméra pour suivre le joueur."""
    
    def __init__(self, level_length):
        """
        Initialise la caméra.
        
        Args:
            level_length: Longueur totale du niveau en pixels
        """
        self.x = 0
        self.level_length = level_length
    
    def update(self, target_x):
        """
        Met à jour la position de la caméra pour suivre le joueur.
        
        Args:
            target_x: Position x du joueur à suivre
        """
        target_camera = target_x - GameConfig.SCREEN_WIDTH // 3
        self.x = max(0, min(target_camera, self.level_length - GameConfig.SCREEN_WIDTH))
    
    def apply(self, rect):
        """
        Applique l'offset de la caméra à un rectangle.
        
        Args:
            rect: Rectangle pygame à décaler
            
        Returns:
            Tuple (x, y) avec les coordonnées décalées
        """
        return rect.x - self.x, rect.y
    
    def apply_x(self, x):
        """
        Applique l'offset de la caméra à une coordonnée x.
        
        Args:
            x: Coordonnée x à décaler
            
        Returns:
            Coordonnée x décalée
        """
        return x - self.x
