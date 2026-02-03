"""
Données persistantes du joueur (or, armes, progression)
"""
import json
import os


class PlayerData:
    """Données de progression du joueur"""
    
    SAVE_FILE = "save_data.json"
    
    def __init__(self):
        self.gold = 100  # Or de départ
        self.owned_weapons = {"handgun", "knife"}  # Armes de base
        self.unlocked_levels = {0, 1}  # Niveaux débloqués (0 et 1 par défaut)
        self.completed_levels = set()  # Niveaux terminés
        self.total_kills = 0
        self.total_deaths = 0
        self.highest_level = 0
        
        # Charger les données sauvegardées
        self.load()
    
    def add_gold(self, amount):
        """Ajoute de l'or"""
        self.gold += amount
    
    def spend_gold(self, amount):
        """Dépense de l'or si possible"""
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    def unlock_weapon(self, weapon_key):
        """Débloque une arme"""
        self.owned_weapons.add(weapon_key)
    
    def unlock_level(self, level_index):
        """Débloque un niveau"""
        self.unlocked_levels.add(level_index)
    
    def complete_level(self, level_index, gold_earned, kills):
        """Marque un niveau comme terminé"""
        self.completed_levels.add(level_index)
        self.gold += gold_earned
        self.total_kills += kills
        
        # Débloquer le niveau suivant
        if level_index + 1 not in self.unlocked_levels:
            self.unlocked_levels.add(level_index + 1)
        
        if level_index > self.highest_level:
            self.highest_level = level_index
    
    def record_death(self):
        """Enregistre une mort"""
        self.total_deaths += 1
    
    def save(self):
        """Sauvegarde les données"""
        data = {
            "gold": self.gold,
            "owned_weapons": list(self.owned_weapons),
            "unlocked_levels": list(self.unlocked_levels),
            "completed_levels": list(self.completed_levels),
            "total_kills": self.total_kills,
            "total_deaths": self.total_deaths,
            "highest_level": self.highest_level
        }
        
        try:
            with open(self.SAVE_FILE, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Erreur de sauvegarde: {e}")
    
    def load(self):
        """Charge les données sauvegardées"""
        if not os.path.exists(self.SAVE_FILE):
            return
        
        try:
            with open(self.SAVE_FILE, 'r') as f:
                data = json.load(f)
            
            self.gold = data.get("gold", 100)
            self.owned_weapons = set(data.get("owned_weapons", ["handgun", "knife"]))
            self.unlocked_levels = set(data.get("unlocked_levels", [0, 1]))
            self.completed_levels = set(data.get("completed_levels", []))
            self.total_kills = data.get("total_kills", 0)
            self.total_deaths = data.get("total_deaths", 0)
            self.highest_level = data.get("highest_level", 0)
            
        except Exception as e:
            print(f"Erreur de chargement: {e}")
    
    def reset(self):
        """Réinitialise toutes les données"""
        self.gold = 100
        self.owned_weapons = {"handgun", "knife"}
        self.unlocked_levels = {0, 1}
        self.completed_levels = set()
        self.total_kills = 0
        self.total_deaths = 0
        self.highest_level = 0
        self.save()
