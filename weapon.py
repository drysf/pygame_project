"""
Définition desarmes du jeu
"""


class Weapon:
    """Définition d'une arme"""
    
    def __init__(self, name, animation_key, damage, fire_rate, bullet_speed, 
                 bullet_count=1, spread=0, auto_fire=True):
        self.name = name
        self.animation_key = animation_key
        self.damage = damage
        self.fire_rate = fire_rate
        self.cooldown = 1.0 / fire_rate
        self.bullet_speed = bullet_speed
        self.bullet_count = bullet_count
        self.spread = spread
        self.auto_fire = auto_fire


class WeaponManager:
    """Gestionnaire des armes"""
    
    def __init__(self):
        self.weapons = []
        self.current_index = 0
        self._load_weapons()
    
    def _load_weapons(self):
        """Charge les armes disponibles"""
        # Handgun - Pistolet
        self.weapons.append(Weapon(
            name="Pistol",
            animation_key="handgun",
            damage=20,
            fire_rate=4,
            bullet_speed=700,
            bullet_count=1,
            spread=3,
            auto_fire=False
        ))
        
        # Rifle - Fusil d'assaut
        self.weapons.append(Weapon(
            name="Rifle",
            animation_key="rifle",
            damage=15,
            fire_rate=10,
            bullet_speed=800,
            bullet_count=1,
            spread=4,
            auto_fire=True
        ))
        
        # Shotgun - Fusil à pompe
        self.weapons.append(Weapon(
            name="Shotgun",
            animation_key="shotgun",
            damage=12,
            fire_rate=1.2,
            bullet_speed=600,
            bullet_count=8,
            spread=15,
            auto_fire=False
        ))
        
        # Knife - Couteau (mêlée)
        self.weapons.append(Weapon(
            name="Knife",
            animation_key="knife",
            damage=50,
            fire_rate=2,
            bullet_speed=0,  # Mêlée
            bullet_count=1,
            spread=0,
            auto_fire=False
        ))
        
        # Flashlight - Lampe torche (pour explorer)
        self.weapons.append(Weapon(
            name="Flashlight",
            animation_key="flashlight",
            damage=5,
            fire_rate=3,
            bullet_speed=0,  # Mêlée
            bullet_count=1,
            spread=0,
            auto_fire=False
        ))
    
    @property
    def current_weapon(self):
        return self.weapons[self.current_index]
    
    def next_weapon(self):
        self.current_index = (self.current_index + 1) % len(self.weapons)
        return self.current_weapon
    
    def previous_weapon(self):
        self.current_index = (self.current_index - 1) % len(self.weapons)
        return self.current_weapon
    
    def select_weapon(self, index):
        if 0 <= index < len(self.weapons):
            self.current_index = index
        return self.current_weapon
