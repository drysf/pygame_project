"""Armes du jeu"""

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

# Définition de toutes les armes disponibles dans le jeu
ALL_WEAPONS = {
    "handgun": {
        "name": "M9 Beretta",
        "animation_key": "handgun",
        "damage": 20,
        "fire_rate": 4,
        "bullet_speed": 700,
        "bullet_count": 1,
        "spread": 3,
        "auto_fire": False
    },
    "knife": {
        "name": "KA-BAR Knife",
        "animation_key": "knife",
        "damage": 50,
        "fire_rate": 2,
        "bullet_speed": 0,
        "bullet_count": 1,
        "spread": 0,
        "auto_fire": False
    },
    "rifle": {
        "name": "M4 Carbine",
        "animation_key": "rifle",
        "damage": 15,
        "fire_rate": 10,
        "bullet_speed": 800,
        "bullet_count": 1,
        "spread": 4,
        "auto_fire": True
    },
    "shotgun": {
        "name": "M870 Shotgun",
        "animation_key": "shotgun",
        "damage": 12,
        "fire_rate": 1.2,
        "bullet_speed": 600,
        "bullet_count": 8,
        "spread": 15,
        "auto_fire": False
    },
    "smg": {
        "name": "MP5 SMG",
        "animation_key": "rifle",  # Utilise les mêmes animations que le rifle
        "damage": 10,
        "fire_rate": 15,
        "bullet_speed": 750,
        "bullet_count": 1,
        "spread": 6,
        "auto_fire": True
    },
    "sniper": {
        "name": "M24 Sniper",
        "animation_key": "rifle",
        "damage": 80,
        "fire_rate": 0.8,
        "bullet_speed": 1200,
        "bullet_count": 1,
        "spread": 1,
        "auto_fire": False
    },
    "grenade": {
        "name": "M203 Grenade",
        "animation_key": "shotgun",
        "damage": 100,
        "fire_rate": 0.5,
        "bullet_speed": 400,
        "bullet_count": 1,
        "spread": 0,
        "auto_fire": False
    },
    "minigun": {
        "name": "M134 Minigun",
        "animation_key": "rifle",
        "damage": 8,
        "fire_rate": 25,
        "bullet_speed": 900,
        "bullet_count": 1,
        "spread": 8,
        "auto_fire": True
    },
    "flashlight": {
        "name": "Flashlight",
        "animation_key": "flashlight",
        "damage": 5,
        "fire_rate": 3,
        "bullet_speed": 0,
        "bullet_count": 1,
        "spread": 0,
        "auto_fire": False
    }
}

class WeaponManager:
    """Gestionnaire des armes"""
    
    def __init__(self, owned_weapons=None):
        self.weapons = []
        self.current_index = 0
        
        # Par défaut, seulement pistolet et couteau
        if owned_weapons is None:
            owned_weapons = {"handgun", "knife"}
        
        self._load_weapons(owned_weapons)
    
    def _load_weapons(self, owned_weapons):
        """Charge uniquement les armes possédées"""
        # Ordre préféré des armes
        weapon_order = ["handgun", "knife", "rifle", "shotgun", "smg", "sniper", "grenade", "minigun", "flashlight"]
        
        for weapon_key in weapon_order:
            if weapon_key in owned_weapons and weapon_key in ALL_WEAPONS:
                data = ALL_WEAPONS[weapon_key]
                self.weapons.append(Weapon(
                    name=data["name"],
                    animation_key=data["animation_key"],
                    damage=data["damage"],
                    fire_rate=data["fire_rate"],
                    bullet_speed=data["bullet_speed"],
                    bullet_count=data["bullet_count"],
                    spread=data["spread"],
                    auto_fire=data["auto_fire"]
                ))
        
        # S'assurer qu'il y a au moins une arme
        if not self.weapons:
            data = ALL_WEAPONS["handgun"]
            self.weapons.append(Weapon(
                name=data["name"],
                animation_key=data["animation_key"],
                damage=data["damage"],
                fire_rate=data["fire_rate"],
                bullet_speed=data["bullet_speed"],
                bullet_count=data["bullet_count"],
                spread=data["spread"],
                auto_fire=data["auto_fire"]
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
