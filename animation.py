"""
Animations du joueur
"""
import pygame
import os


class Animation:
    """Gère une séquence d'animation"""
    
    def __init__(self, frames, frame_duration=0.05):
        self.frames = frames
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.timer = 0
    
    def update(self, dt):
        """Met à jour l'animation"""
        self.timer += dt
        if self.timer >= self.frame_duration:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def get_current_frame(self):
        """Retourne l'image actuelle"""
        return self.frames[self.current_frame]
    
    def reset(self):
        """Remet l'animation au début"""
        self.current_frame = 0
        self.timer = 0


class PlayerAnimations:
    """Gère toutes les animations du joueur"""
    
    ASSETS_PATH = "assets/player"
    SCALE = 0.4  # Échelle des sprites
    
    def __init__(self):
        self.weapons = {}
        self._load_all_animations()
        self.current_weapon = "rifle"
        self.current_state = "idle"
        self.is_shooting = False
        self.shoot_timer = 0
    
    def _load_frames(self, folder_path, prefix, count=None):
        """Charge les frames d'une animation"""
        frames = []
        
        # Lister tous les fichiers et trier
        if os.path.exists(folder_path):
            files = sorted([f for f in os.listdir(folder_path) if f.startswith(prefix) and f.endswith('.png')],
                          key=lambda x: int(x.split('_')[-1].replace('.png', '')))
            
            for filename in files:
                path = os.path.join(folder_path, filename)
                try:
                    image = pygame.image.load(path).convert_alpha()
                    # Redimensionner
                    new_size = (int(image.get_width() * self.SCALE), 
                               int(image.get_height() * self.SCALE))
                    image = pygame.transform.scale(image, new_size)
                    frames.append(image)
                except Exception as e:
                    print(f"Erreur de chargement {path}: {e}")
        
        return frames if frames else self._create_default_frames()
    
    def _create_default_frames(self):
        """Crée des frames par défaut si les images ne sont pas trouvées"""
        surface = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(surface, (0, 100, 200), (25, 25), 20)
        return [surface]
    
    def _load_all_animations(self):
        """Charge toutes les animations pour toutes les armes"""
        weapon_types = ["handgun", "rifle", "shotgun", "knife", "flashlight"]
        
        for weapon in weapon_types:
            weapon_path = os.path.join(self.ASSETS_PATH, weapon)
            
            self.weapons[weapon] = {
                "idle": Animation(
                    self._load_frames(
                        os.path.join(weapon_path, "idle"),
                        f"survivor-idle_{weapon}"
                    ),
                    frame_duration=0.1
                ),
                "move": Animation(
                    self._load_frames(
                        os.path.join(weapon_path, "move"),
                        f"survivor-move_{weapon}"
                    ),
                    frame_duration=0.05
                ),
            }
            
            # Charger l'animation de tir si elle existe
            shoot_path = os.path.join(weapon_path, "shoot")
            if os.path.exists(shoot_path):
                self.weapons[weapon]["shoot"] = Animation(
                    self._load_frames(shoot_path, f"survivor-shoot_{weapon}"),
                    frame_duration=0.05
                )
            
            # Charger l'animation de rechargement si elle existe
            reload_path = os.path.join(weapon_path, "reload")
            if os.path.exists(reload_path):
                self.weapons[weapon]["reload"] = Animation(
                    self._load_frames(reload_path, f"survivor-reload_{weapon}"),
                    frame_duration=0.08
                )
            
            # Charger l'animation de mêlée si elle existe
            melee_path = os.path.join(weapon_path, "meleeattack")
            if os.path.exists(melee_path):
                self.weapons[weapon]["melee"] = Animation(
                    self._load_frames(melee_path, f"survivor-meleeattack_{weapon}"),
                    frame_duration=0.04
                )
    
    def set_weapon(self, weapon_name):
        """Change l'arme actuelle"""
        if weapon_name in self.weapons:
            self.current_weapon = weapon_name
            # Reset les animations
            for anim in self.weapons[weapon_name].values():
                anim.reset()
    
    def set_state(self, state):
        """Change l'état d'animation (idle, move, shoot)"""
        if state != self.current_state:
            self.current_state = state
            if state in self.weapons[self.current_weapon]:
                self.weapons[self.current_weapon][state].reset()
    
    def trigger_shoot(self):
        """Déclenche l'animation de tir"""
        self.is_shooting = True
        self.shoot_timer = 0
        if "shoot" in self.weapons[self.current_weapon]:
            self.weapons[self.current_weapon]["shoot"].reset()
    
    def update(self, dt, is_moving):
        """Met à jour l'animation actuelle"""
        # Gérer l'animation de tir
        if self.is_shooting:
            self.shoot_timer += dt
            if "shoot" in self.weapons[self.current_weapon]:
                shoot_anim = self.weapons[self.current_weapon]["shoot"]
                shoot_anim.update(dt)
                # Terminer après un cycle complet
                if self.shoot_timer >= shoot_anim.frame_duration * len(shoot_anim.frames):
                    self.is_shooting = False
            else:
                if self.shoot_timer >= 0.1:
                    self.is_shooting = False
        
        # Déterminer l'état
        if self.is_shooting and "shoot" in self.weapons[self.current_weapon]:
            state = "shoot"
        elif is_moving:
            state = "move"
        else:
            state = "idle"
        
        # Mettre à jour l'animation appropriée
        if state in self.weapons[self.current_weapon]:
            self.weapons[self.current_weapon][state].update(dt)
    
    def get_current_frame(self):
        """Retourne l'image actuelle"""
        weapon_anims = self.weapons[self.current_weapon]
        
        if self.is_shooting and "shoot" in weapon_anims:
            return weapon_anims["shoot"].get_current_frame()
        elif self.current_state == "move" and "move" in weapon_anims:
            return weapon_anims["move"].get_current_frame()
        else:
            return weapon_anims["idle"].get_current_frame()
