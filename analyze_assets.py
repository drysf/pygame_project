"""
Script pour analyser automatiquement les assets et générer le code
Lance ce script UNE FOIS pour analyser tes images
"""
import os
from PIL import Image


def analyze_sprite(image_path):
    """Analyse une image et retourne ses dimensions"""
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        # Détecter la zone non-transparente (si PNG avec alpha)
        if img.mode in ('RGBA', 'LA'):
            bbox = img.getbbox()
            if bbox:
                actual_width = bbox[2] - bbox[0]
                actual_height = bbox[3] - bbox[1]
                offset_x = bbox[0]
                offset_y = bbox[1]
                return {
                    'full_width': width,
                    'full_height': height,
                    'sprite_width': actual_width,
                    'sprite_height': actual_height,
                    'offset_x': offset_x,
                    'offset_y': offset_y
                }
        
        return {
            'full_width': width,
            'full_height': height,
            'sprite_width': width,
            'sprite_height': height,
            'offset_x': 0,
            'offset_y': 0
        }
    except Exception as e:
        print(f" Erreur avec {image_path}: {e}")
        return None


def scan_assets_folder(base_path, folder_name):
    """Scanne tous les fichiers PNG dans un dossier"""
    sprites = {}
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.png'):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, 'assets')
                
                # Créer un nom propre pour le sprite avec préfixe du dossier
                sprite_name = os.path.splitext(file)[0]
                sprite_name = sprite_name.lower().replace(' ', '_').replace('-', '_')
                
                # Ajouter le préfixe du dossier pour éviter les conflits
                sprite_name = f"{folder_name}_{sprite_name}"
                
                info = analyze_sprite(full_path)
                if info:
                    sprites[sprite_name] = {
                        'path': relative_path,
                        'info': info
                    }
                    print(f"  ✓ {sprite_name}: {info['sprite_width']}x{info['sprite_height']}px")
    
    return sprites


def generate_code(sprites):
    """Génère le code Python pour Pygame"""
    code = '''"""
Code auto-généré pour les assets
Généré automatiquement - NE PAS MODIFIER MANUELLEMENT
"""
import pygame
import os


class SpriteSheet:
    """Classe pour charger des sprites individuels"""
    
    def __init__(self, filename):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, 'assets', filename)
        
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image non trouvée: {image_path}")
        
        self.sheet = pygame.image.load(image_path).convert_alpha()
    
    def get_full_image(self):
        """Retourne l'image complète"""
        return self.sheet


class Wall(pygame.sprite.Sprite):
    """Mur avec sprites automatiques"""
    
    sprites_cache = {}
    
    @classmethod
    def load_assets(cls):
        """Charge tous les assets automatiquement"""
        if not cls.sprites_cache:
            print("Chargement des assets...")
'''
    
    # Générer le chargement de chaque sprite
    for name, data in sprites.items():
        code += f"            cls.sprites_cache['{name}'] = {{\n"
        code += f"                'sheet': SpriteSheet('{data['path']}'),\n"
        code += f"                'width': {data['info']['sprite_width']},\n"
        code += f"                'height': {data['info']['sprite_height']}\n"
        code += f"            }}\n"
    
    code += '''            print(f"✓ {len(cls.sprites_cache)} sprites chargés")
    
    def __init__(self, x, y, width=None, height=None, sprite_type=None):
        super().__init__()
        Wall.load_assets()
        
        if sprite_type and sprite_type in Wall.sprites_cache:
            # Utiliser le sprite avec sa taille native
            sprite_data = Wall.sprites_cache[sprite_type]
            self.image = sprite_data['sheet'].get_full_image()
            
            # Redimensionner si width/height sont fournis
            if width and height:
                self.image = pygame.transform.scale(self.image, (width, height))
        else:
            # Fallback: rectangle gris
            w = width if width else 32
            h = height if height else 32
            self.image = pygame.Surface((w, h))
            self.image.fill((80, 80, 80))
            pygame.draw.rect(self.image, (60, 60, 60), (0, 0, w, h), 3)
        
        self.rect = self.image.get_rect(topleft=(x, y))


# Références des sprites disponibles
# Utilisez ces noms dans sprite_type='nom_du_sprite'
#
'''
    
    # Ajouter la liste des sprites disponibles en commentaire
    for name, data in sorted(sprites.items()):
        code += f"# '{name}' - {data['info']['sprite_width']}x{data['info']['sprite_height']}px - {data['path']}\n"
    
    return code


# Execution du script
if __name__ == "__main__":
    print("=" * 60)
    print("ANALYSE AUTOMATIQUE DES ASSETS")
    print("=" * 60)
    print()
    
    # Liste de tous vos dossiers d'assets
    folders_to_scan = ["apocalypse", "bullet", "pixel_village", "player"]
    
    all_sprites = {}
    
    for folder in folders_to_scan:
        assets_path = os.path.join("assets", folder)
        
        if os.path.exists(assets_path):
            print(f"📁 Analyse de: {folder}/")
            folder_sprites = scan_assets_folder(assets_path, folder)
            all_sprites.update(folder_sprites)
            print(f"   → {len(folder_sprites)} sprites trouvés")
            print()
        else:
            print(f"  Dossier ignoré (non trouvé): {assets_path}")
            print()
    
    print("=" * 60)
    print(f"✓ TOTAL: {len(all_sprites)} sprites analysés")
    print("=" * 60)
    print()
    
    if all_sprites:
        # Générer le code
        generated_code = generate_code(all_sprites)
        
        # Sauvegarder dans un fichier
        output_file = "room_auto.py"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generated_code)
        
        print(f"✓ Code généré dans: {output_file}")
        print()
        print("PROCHAINES ÉTAPES:")
        print("  1. Dans game.py, remplacez:")
        print("     from room import Room")
        print("     par:")
        print("     from room_auto import Wall, Room")
        print()
        print("  2. Utilisez Wall avec sprite_type:")
        print("     Wall(100, 100, sprite_type='pixel_village_tree')")
        print("     Wall(200, 200, sprite_type='player_idle')")
        print()
        print("  3. Consultez room_auto.py pour voir tous les noms disponibles")
        print()
    else:
        print(" Aucun sprite trouvé !")
