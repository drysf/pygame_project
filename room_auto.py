"""
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
            cls.sprites_cache['apocalypse_heart_full'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/Heart_Full.png'),
                'width': 13,
                'height': 12
            }
            cls.sprites_cache['apocalypse_heart_half'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/Heart_Half.png'),
                'width': 13,
                'height': 12
            }
            cls.sprites_cache['apocalypse_heart_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/Heart_Empty.png'),
                'width': 13,
                'height': 12
            }
            cls.sprites_cache['apocalypse_hp_bar'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/HP-Bar.png'),
                'width': 55,
                'height': 12
            }
            cls.sprites_cache['apocalypse_hp'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/HP.png'),
                'width': 43,
                'height': 4
            }
            cls.sprites_cache['apocalypse_heart_small_half'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/Small/Heart_Small_Half.png'),
                'width': 11,
                'height': 10
            }
            cls.sprites_cache['apocalypse_heart_small_full'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/Small/Heart_Small_Full.png'),
                'width': 11,
                'height': 10
            }
            cls.sprites_cache['apocalypse_hp_small'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/Small/HP_Small.png'),
                'width': 43,
                'height': 2
            }
            cls.sprites_cache['apocalypse_heart_small_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/Small/Heart_Small_Empty.png'),
                'width': 11,
                'height': 10
            }
            cls.sprites_cache['apocalypse_hp_bar_small'] = {
                'sheet': SpriteSheet('apocalypse/UI/HP/Small/HP-Bar_Small.png'),
                'width': 53,
                'height': 10
            }
            cls.sprites_cache['apocalypse_inventory_close_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Inventory_Close-Sheet2.png'),
                'width': 14,
                'height': 7
            }
            cls.sprites_cache['apocalypse_inventory_1_scrollbar'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Inventory_1_Scrollbar.png'),
                'width': 146,
                'height': 91
            }
            cls.sprites_cache['apocalypse_inventory_2'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Inventory_2.png'),
                'width': 143,
                'height': 91
            }
            cls.sprites_cache['apocalypse_inventory_chosen'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Inventory-Chosen.png'),
                'width': 19,
                'height': 19
            }
            cls.sprites_cache['apocalypse_inventory_cell'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Inventory-Cell.png'),
                'width': 19,
                'height': 20
            }
            cls.sprites_cache['apocalypse_inventory_1'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Inventory_1.png'),
                'width': 143,
                'height': 91
            }
            cls.sprites_cache['apocalypse_quick_access_inventory'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Quick-Access-Inventory.png'),
                'width': 124,
                'height': 19
            }
            cls.sprites_cache['apocalypse_inventory_close_not_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Inventory_Close_Not-Pressed.png'),
                'width': 7,
                'height': 7
            }
            cls.sprites_cache['apocalypse_inventory_scrollbox_1'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Inventory_Scrollbox_1.png'),
                'width': 4,
                'height': 28
            }
            cls.sprites_cache['apocalypse_inventory_close_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Inventory_Close_Pressed.png'),
                'width': 7,
                'height': 6
            }
            cls.sprites_cache['apocalypse_icon_bat'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Bat.png'),
                'width': 14,
                'height': 14
            }
            cls.sprites_cache['apocalypse_icon_pistol'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Pistol.png'),
                'width': 11,
                'height': 9
            }
            cls.sprites_cache['apocalypse_icon_wooden_wall_gate'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Wooden-wall_Gate.png'),
                'width': 14,
                'height': 13
            }
            cls.sprites_cache['apocalypse_icon_bullet_box_blue'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Bullet-box_Blue.png'),
                'width': 14,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_reinforced_wooden_wall'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Reinforced-wooden-wall.png'),
                'width': 13,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_bullet_crate_green'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Bullet-crate_Green.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_first_aid_kit_red'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_First-Aid-Kit_Red.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_wooden_wall'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Wooden-wall.png'),
                'width': 13,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_bullet_crate_red'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Bullet-crate_Red.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_shotgun'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Shotgun.png'),
                'width': 15,
                'height': 11
            }
            cls.sprites_cache['apocalypse_icon_bullet_crate_blue'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Bullet-crate_Blue.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_canned_soup'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Canned-soup.png'),
                'width': 9,
                'height': 14
            }
            cls.sprites_cache['apocalypse_icon_bandage'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Bandage.png'),
                'width': 12,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_bullet_box_green'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Bullet-box_Green.png'),
                'width': 14,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_rock'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Rock.png'),
                'width': 11,
                'height': 8
            }
            cls.sprites_cache['apocalypse_icon_gun'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Gun.png'),
                'width': 15,
                'height': 10
            }
            cls.sprites_cache['apocalypse_icon_canned_food'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Canned-food.png'),
                'width': 12,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_first_aid_kit_white'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_First-Aid-Kit_White.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_icon_reinforced_wooden_wall_gate'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Reinforced-wooden-wall_Gate.png'),
                'width': 14,
                'height': 13
            }
            cls.sprites_cache['apocalypse_icon_bullet_box_red'] = {
                'sheet': SpriteSheet('apocalypse/UI/Inventory/Objects/Icon_Bullet-box_Red.png'),
                'width': 14,
                'height': 12
            }
            cls.sprites_cache['apocalypse_cursor'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Cursor.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_button_no_not_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Button_No_Not-Pressed.png'),
                'width': 9,
                'height': 9
            }
            cls.sprites_cache['apocalypse_button_no_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Button_No_Pressed.png'),
                'width': 9,
                'height': 8
            }
            cls.sprites_cache['apocalypse_checkmark'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Checkmark.png'),
                'width': 7,
                'height': 5
            }
            cls.sprites_cache['apocalypse_checkmark_sheet5'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Checkmark-Sheet5.png'),
                'width': 35,
                'height': 5
            }
            cls.sprites_cache['apocalypse_scrollbar_scrollbox'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Scrollbar_Scrollbox.png'),
                'width': 4,
                'height': 9
            }
            cls.sprites_cache['apocalypse_button_no_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Button_No-Sheet2.png'),
                'width': 18,
                'height': 9
            }
            cls.sprites_cache['apocalypse_button_yes_not_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Button_Yes_Not-Pressed.png'),
                'width': 10,
                'height': 9
            }
            cls.sprites_cache['apocalypse_checkmark_body'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Checkmark-Body.png'),
                'width': 7,
                'height': 7
            }
            cls.sprites_cache['apocalypse_scrollbar_scrollbox_1'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Scrollbar_Scrollbox_1.png'),
                'width': 4,
                'height': 9
            }
            cls.sprites_cache['apocalypse_scrollbar'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Scrollbar.png'),
                'width': 54,
                'height': 7
            }
            cls.sprites_cache['apocalypse_button_yes_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Button_Yes_Pressed.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_button_yes_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Button_Yes-Sheet2.png'),
                'width': 20,
                'height': 9
            }
            cls.sprites_cache['apocalypse_load_not_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Load_Not-Pressed.png'),
                'width': 76,
                'height': 21
            }
            cls.sprites_cache['apocalypse_load_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Load_Pressed.png'),
                'width': 76,
                'height': 19
            }
            cls.sprites_cache['apocalypse_play_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Play_Pressed.png'),
                'width': 76,
                'height': 19
            }
            cls.sprites_cache['apocalypse_settings_not_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Settings_Not-Pressed.png'),
                'width': 76,
                'height': 21
            }
            cls.sprites_cache['apocalypse_play_not_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Play_Not-Pressed.png'),
                'width': 76,
                'height': 21
            }
            cls.sprites_cache['apocalypse_blank_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Blank_Pressed.png'),
                'width': 76,
                'height': 19
            }
            cls.sprites_cache['apocalypse_settings_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Settings_Pressed.png'),
                'width': 76,
                'height': 19
            }
            cls.sprites_cache['apocalypse_save_not_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Save_Not-Pressed.png'),
                'width': 76,
                'height': 21
            }
            cls.sprites_cache['apocalypse_blank_not_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Blank_Not-Pressed.png'),
                'width': 76,
                'height': 21
            }
            cls.sprites_cache['apocalypse_quit_not_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Quit_Not-Pressed.png'),
                'width': 76,
                'height': 21
            }
            cls.sprites_cache['apocalypse_quit_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Quit_Pressed.png'),
                'width': 76,
                'height': 19
            }
            cls.sprites_cache['apocalypse_save_pressed'] = {
                'sheet': SpriteSheet('apocalypse/UI/Menu/Main Menu/Save_Pressed.png'),
                'width': 76,
                'height': 19
            }
            cls.sprites_cache['apocalypse_shotgun_bullet'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Bullets/Shotgun-bullet.png'),
                'width': 3,
                'height': 1
            }
            cls.sprites_cache['apocalypse_gun_bullet_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Gun-Bullet_Empty.png'),
                'width': 7,
                'height': 25
            }
            cls.sprites_cache['apocalypse_gun_bullet'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Gun-Bullet.png'),
                'width': 7,
                'height': 25
            }
            cls.sprites_cache['apocalypse_pistol_bullet_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Pistol-Bullet_Empty.png'),
                'width': 7,
                'height': 13
            }
            cls.sprites_cache['apocalypse_shotgun_bullet_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Shotgun-Bullet_Empty.png'),
                'width': 9,
                'height': 14
            }
            cls.sprites_cache['apocalypse_pistol_bullet'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Pistol-Bullet.png'),
                'width': 7,
                'height': 13
            }
            cls.sprites_cache['apocalypse_gun_bullet_small_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Small/Gun-Bullet_Small_Empty.png'),
                'width': 5,
                'height': 16
            }
            cls.sprites_cache['apocalypse_pistol_bullet_small'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Small/Pistol-Bullet_Small.png'),
                'width': 6,
                'height': 10
            }
            cls.sprites_cache['apocalypse_pistol_bullet_small_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Small/Pistol-Bullet_Small_Empty.png'),
                'width': 6,
                'height': 10
            }
            cls.sprites_cache['apocalypse_shotgun_bullet_small'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Small/Shotgun-Bullet_Small.png'),
                'width': 8,
                'height': 10
            }
            cls.sprites_cache['apocalypse_gun_bullet_small'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Small/Gun-Bullet_Small.png'),
                'width': 5,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_bullet_small_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/Bullet Indicators/Small/Shotgun-Bullet_Small_Empty.png'),
                'width': 8,
                'height': 10
            }
            cls.sprites_cache['apocalypse_crafting_scrollbox'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting_Scrollbox.png'),
                'width': 4,
                'height': 28
            }
            cls.sprites_cache['apocalypse_crafting_1_1'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting_1_1.png'),
                'width': 47,
                'height': 22
            }
            cls.sprites_cache['apocalypse_crafting_1_2'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting_1_2.png'),
                'width': 70,
                'height': 22
            }
            cls.sprites_cache['apocalypse_crafting_cell'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting-cell.png'),
                'width': 21,
                'height': 22
            }
            cls.sprites_cache['apocalypse_crafting_plus'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting_Plus.png'),
                'width': 10,
                'height': 11
            }
            cls.sprites_cache['apocalypse_crafting_arrow'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting_Arrow.png'),
                'width': 7,
                'height': 11
            }
            cls.sprites_cache['apocalypse_crafting_2_1'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting_2_1.png'),
                'width': 49,
                'height': 22
            }
            cls.sprites_cache['apocalypse_crafting_equal'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting_Equal.png'),
                'width': 9,
                'height': 8
            }
            cls.sprites_cache['apocalypse_crafting_2_2'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting_2_2.png'),
                'width': 72,
                'height': 22
            }
            cls.sprites_cache['apocalypse_crafting_main_menu'] = {
                'sheet': SpriteSheet('apocalypse/UI/Crafting/Crafting-main-menu.png'),
                'width': 85,
                'height': 91
            }
            cls.sprites_cache['apocalypse_hunger_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/Hunger/Hunger_Empty.png'),
                'width': 13,
                'height': 13
            }
            cls.sprites_cache['apocalypse_hunger_full'] = {
                'sheet': SpriteSheet('apocalypse/UI/Hunger/Hunger_Full.png'),
                'width': 13,
                'height': 13
            }
            cls.sprites_cache['apocalypse_hunger_bar'] = {
                'sheet': SpriteSheet('apocalypse/UI/Hunger/Hunger-Bar.png'),
                'width': 50,
                'height': 13
            }
            cls.sprites_cache['apocalypse_hunger_half'] = {
                'sheet': SpriteSheet('apocalypse/UI/Hunger/Hunger_Half.png'),
                'width': 13,
                'height': 13
            }
            cls.sprites_cache['apocalypse_hunger'] = {
                'sheet': SpriteSheet('apocalypse/UI/Hunger/Hunger.png'),
                'width': 37,
                'height': 2
            }
            cls.sprites_cache['apocalypse_hunger_bar_small'] = {
                'sheet': SpriteSheet('apocalypse/UI/Hunger/Small/Hunger-Bar_Small.png'),
                'width': 48,
                'height': 11
            }
            cls.sprites_cache['apocalypse_hunger_small_full'] = {
                'sheet': SpriteSheet('apocalypse/UI/Hunger/Small/Hunger_Small_Full.png'),
                'width': 11,
                'height': 11
            }
            cls.sprites_cache['apocalypse_hunger_small_half'] = {
                'sheet': SpriteSheet('apocalypse/UI/Hunger/Small/Hunger_Small_Half.png'),
                'width': 11,
                'height': 11
            }
            cls.sprites_cache['apocalypse_hunger_small_empty'] = {
                'sheet': SpriteSheet('apocalypse/UI/Hunger/Small/Hunger_Small_Empty.png'),
                'width': 11,
                'height': 11
            }
            cls.sprites_cache['apocalypse_helmet_side_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side_Pick-up-Sheet3.png'),
                'width': 30,
                'height': 8
            }
            cls.sprites_cache['apocalypse_helmet_up_and_down_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_Up-and-Down_Idle-and-Run-Sheet6.png'),
                'width': 60,
                'height': 9
            }
            cls.sprites_cache['apocalypse_helmet_up_and_down_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_Up-and-Down_Punch-Sheet4.png'),
                'width': 40,
                'height': 10
            }
            cls.sprites_cache['apocalypse_helmet_side_left_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side-left_Idle-and-Run-Sheet6.png'),
                'width': 60,
                'height': 8
            }
            cls.sprites_cache['apocalypse_helmet_side_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side_Idle-and-Run-Sheet6.png'),
                'width': 60,
                'height': 8
            }
            cls.sprites_cache['apocalypse_helmet_side_left_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side-left_Punch-Sheet4.png'),
                'width': 52,
                'height': 8
            }
            cls.sprites_cache['apocalypse_helmet_side_left_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side-left_Death-Sheet6.png'),
                'width': 126,
                'height': 18
            }
            cls.sprites_cache['apocalypse_helmet_side_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side_Death-Sheet6.png'),
                'width': 126,
                'height': 18
            }
            cls.sprites_cache['apocalypse_helmet_side_left_idle_and_run_sprite'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side-left_Idle-and-Run_Sprite.png'),
                'width': 10,
                'height': 7
            }
            cls.sprites_cache['apocalypse_helmet_up_and_down_idle_and_run_sprite'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_Up-and-Down_Idle-and-Run-Sprite.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_helmet_side_left_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side-left_Pick-up-Sheet3.png'),
                'width': 30,
                'height': 8
            }
            cls.sprites_cache['apocalypse_helmet_side_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side_Punch-Sheet4.png'),
                'width': 50,
                'height': 8
            }
            cls.sprites_cache['apocalypse_helmet_up_and_down_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_Up-and-Down_Pick-up-Sheet3.png'),
                'width': 30,
                'height': 9
            }
            cls.sprites_cache['apocalypse_helmet_side_idle_and_run_sprite'] = {
                'sheet': SpriteSheet('apocalypse/Character/Helmet/Helmet_side_Idle-and-Run_Sprite.png'),
                'width': 10,
                'height': 7
            }
            cls.sprites_cache['apocalypse_gun_bullet_casing'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Bullets/Gun-bullet_Casing.png'),
                'width': 2,
                'height': 1
            }
            cls.sprites_cache['apocalypse_pistol_bullet_whole'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Bullets/Pistol-bullet_Whole.png'),
                'width': 2,
                'height': 1
            }
            cls.sprites_cache['apocalypse_pistol_bullet_casting'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Bullets/Pistol-bullet_Casting.png'),
                'width': 1,
                'height': 1
            }
            cls.sprites_cache['apocalypse_gun_bullet_whole'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Bullets/Gun-bullet_Whole.png'),
                'width': 4,
                'height': 1
            }
            cls.sprites_cache['apocalypse_pistol_bullet_bullet'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Bullets/Pistol-bullet_Bullet.png'),
                'width': 1,
                'height': 1
            }
            cls.sprites_cache['apocalypse_gun_bullet_bullet'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Bullets/Gun-bullet_Bullet.png'),
                'width': 2,
                'height': 1
            }
            cls.sprites_cache['apocalypse_shotgun_side_reload_second_part_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_reload_second-part-Sheet3.png'),
                'width': 33,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_reload_first_part_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_reload_first-part-Sheet4.png'),
                'width': 60,
                'height': 15
            }
            cls.sprites_cache['apocalypse_shotgun_side_reload_third_part_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_reload_third-part-Sheet2.png'),
                'width': 30,
                'height': 12
            }
            cls.sprites_cache['apocalypse_shotgun_side_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_idle-and-run-Sheet6.png'),
                'width': 90,
                'height': 8
            }
            cls.sprites_cache['apocalypse_shotgun_side_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_shoot-Sheet3.png'),
                'width': 54,
                'height': 8
            }
            cls.sprites_cache['apocalypse_shotgun_up_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_shoot-Sheet3.png'),
                'width': 18,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_side_racking_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_racking-Sheet2.png'),
                'width': 32,
                'height': 7
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_1reload_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_1reload-Sheet9.png'),
                'width': 135,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_up_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_idle-and-run-Sheet6.png'),
                'width': 36,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_Death-Sheet6.png'),
                'width': 96,
                'height': 9
            }
            cls.sprites_cache['apocalypse_shotgun_down_3reload_sheet15'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_3reload-Sheet15.png'),
                'width': 174,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_down_2reload_sheet12'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_2reload-Sheet12.png'),
                'width': 138,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_side_2reload_sheet12'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_2reload-Sheet12.png'),
                'width': 180,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_side_1reload_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_1reload-Sheet9.png'),
                'width': 135,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_down_reload_second_part_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_reload_second-part-Sheet3.png'),
                'width': 26,
                'height': 14
            }
            cls.sprites_cache['apocalypse_shotgun_down_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_idle-and-run-Sheet6.png'),
                'width': 36,
                'height': 14
            }
            cls.sprites_cache['apocalypse_shotgun_up_4reload_sheet18'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_4reload-Sheet18.png'),
                'width': 270,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_4reload_sheet18'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_4reload-Sheet18.png'),
                'width': 270,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_side_3reload_sheet15'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_3reload-Sheet15.png'),
                'width': 225,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_reload_third_part_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_reload_third-part-Sheet2.png'),
                'width': 30,
                'height': 12
            }
            cls.sprites_cache['apocalypse_shotgun_side_reload_first_part_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_reload_first-part-Sheet4.png'),
                'width': 60,
                'height': 15
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_racking_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_racking-Sheet2.png'),
                'width': 32,
                'height': 7
            }
            cls.sprites_cache['apocalypse_shotgun_down_reload_third_part_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_reload_third-part-Sheet2.png'),
                'width': 14,
                'height': 12
            }
            cls.sprites_cache['apocalypse_shotgun_down_1reload_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_1reload-Sheet9.png'),
                'width': 102,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_down_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_shoot-Sheet3.png'),
                'width': 18,
                'height': 15
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_reload_second_part_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_reload_second-part-Sheet3.png'),
                'width': 33,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_up_1reload_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_1reload-Sheet9.png'),
                'width': 135,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_side_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_Death-Sheet6.png'),
                'width': 95,
                'height': 9
            }
            cls.sprites_cache['apocalypse_shotgun_up_reload_second_part_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_reload_second-part-Sheet3.png'),
                'width': 33,
                'height': 13
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_idle-and-run-Sheet6.png'),
                'width': 90,
                'height': 8
            }
            cls.sprites_cache['apocalypse_shotgun_up_reload_third_part_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_reload_third-part-Sheet2.png'),
                'width': 12,
                'height': 14
            }
            cls.sprites_cache['apocalypse_shotgun_down_racking_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_racking-Sheet2.png'),
                'width': 12,
                'height': 14
            }
            cls.sprites_cache['apocalypse_shotgun_side_4reload_sheet18'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side_4reload-Sheet18.png'),
                'width': 270,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_3reload_sheet15'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_3reload-Sheet15.png'),
                'width': 225,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_up_reload_first_part_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_reload_first-part-Sheet4.png'),
                'width': 56,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_up_3reload_sheet15'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_3reload-Sheet15.png'),
                'width': 225,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_up_2reload_sheet12'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_2reload-Sheet12.png'),
                'width': 180,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_2reload_sheet12'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_2reload-Sheet12.png'),
                'width': 180,
                'height': 17
            }
            cls.sprites_cache['apocalypse_shotgun_up_racking_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_up_racking-Sheet2.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_side_left_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_side-left_shoot-Sheet3.png'),
                'width': 54,
                'height': 8
            }
            cls.sprites_cache['apocalypse_shotgun_down_reload_first_part_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_reload_first-part-Sheet4.png'),
                'width': 42,
                'height': 16
            }
            cls.sprites_cache['apocalypse_shotgun_down_4reload_sheet18'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Shotgun/Shotgun_down_4reload-Sheet18.png'),
                'width': 210,
                'height': 17
            }
            cls.sprites_cache['apocalypse_pistol_up_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_up_idle-and-run-Sheet6.png'),
                'width': 30,
                'height': 11
            }
            cls.sprites_cache['apocalypse_pistol_side_reload_sheet11'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_side_Reload-Sheet11.png'),
                'width': 132,
                'height': 13
            }
            cls.sprites_cache['apocalypse_pistol_side_left_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_side-left_Death-Sheet6.png'),
                'width': 78,
                'height': 9
            }
            cls.sprites_cache['apocalypse_pistol_side_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_side_shoot-Sheet3.png'),
                'width': 30,
                'height': 8
            }
            cls.sprites_cache['apocalypse_pistol_up_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_up_shoot-Sheet3.png'),
                'width': 15,
                'height': 11
            }
            cls.sprites_cache['apocalypse_pistol_side_left_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_side-left_idle-and-run-Sheet6.png'),
                'width': 48,
                'height': 9
            }
            cls.sprites_cache['apocalypse_pistol_down_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_down_idle-and-run-Sheet6.png'),
                'width': 30,
                'height': 11
            }
            cls.sprites_cache['apocalypse_pistol_side_left_reload_sheet11'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_side-left_Reload-Sheet11.png'),
                'width': 132,
                'height': 13
            }
            cls.sprites_cache['apocalypse_pistol_up_reload_sheet11'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_up_Reload-Sheet11.png'),
                'width': 196,
                'height': 19
            }
            cls.sprites_cache['apocalypse_pistol_side_left_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_side-left_shoot-Sheet3.png'),
                'width': 30,
                'height': 8
            }
            cls.sprites_cache['apocalypse_pistol_down_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_down_shoot-Sheet3.png'),
                'width': 15,
                'height': 11
            }
            cls.sprites_cache['apocalypse_pistol_side_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_side_idle-and-run-Sheet6.png'),
                'width': 48,
                'height': 9
            }
            cls.sprites_cache['apocalypse_pistol_down_reload_sheet11'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_down_Reload-Sheet11.png'),
                'width': 194,
                'height': 12
            }
            cls.sprites_cache['apocalypse_pistol_side_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Pistol/Pistol_side_Death-Sheet6.png'),
                'width': 78,
                'height': 9
            }
            cls.sprites_cache['apocalypse_fire_down_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Fire/Fire_Down-Sheet3.png'),
                'width': 20,
                'height': 10
            }
            cls.sprites_cache['apocalypse_fire_side_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Fire/Fire_side-Sheet3.png'),
                'width': 30,
                'height': 7
            }
            cls.sprites_cache['apocalypse_fire_side_left_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Fire/Fire_side-left-Sheet3.png'),
                'width': 30,
                'height': 7
            }
            cls.sprites_cache['apocalypse_fire_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Fire/Fire_Up-Sheet3.png'),
                'width': 20,
                'height': 10
            }
            cls.sprites_cache['apocalypse_gun_side_left_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_side-left_Death-Sheet6.png'),
                'width': 108,
                'height': 10
            }
            cls.sprites_cache['apocalypse_gun_up_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_up_idle-and-run-Sheet6.png'),
                'width': 30,
                'height': 16
            }
            cls.sprites_cache['apocalypse_gun_side_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_side_Death-Sheet6.png'),
                'width': 107,
                'height': 10
            }
            cls.sprites_cache['apocalypse_gun_down_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_down_shoot-Sheet3.png'),
                'width': 15,
                'height': 17
            }
            cls.sprites_cache['apocalypse_gun_side_reload_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_side_reload-Sheet8.png'),
                'width': 155,
                'height': 11
            }
            cls.sprites_cache['apocalypse_gun_side_left_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_side-left_idle-and-run-Sheet6.png'),
                'width': 96,
                'height': 10
            }
            cls.sprites_cache['apocalypse_gun_up_reload_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_up_reload-Sheet8.png'),
                'width': 163,
                'height': 19
            }
            cls.sprites_cache['apocalypse_gun_down_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_down_idle-and-run-Sheet6.png'),
                'width': 30,
                'height': 16
            }
            cls.sprites_cache['apocalypse_gun_side_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_side_shoot-Sheet3.png'),
                'width': 54,
                'height': 10
            }
            cls.sprites_cache['apocalypse_gun_down_reload_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_down_reload-Sheet8.png'),
                'width': 120,
                'height': 15
            }
            cls.sprites_cache['apocalypse_gun_side_left_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_side-left_shoot-Sheet3.png'),
                'width': 54,
                'height': 10
            }
            cls.sprites_cache['apocalypse_gun_up_shoot_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_up_shoot-Sheet3.png'),
                'width': 15,
                'height': 17
            }
            cls.sprites_cache['apocalypse_gun_side_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_side_idle-and-run-Sheet6.png'),
                'width': 96,
                'height': 10
            }
            cls.sprites_cache['apocalypse_gun_side_left_reload_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Character/Guns/Gun/Gun_side-left_Reload-Sheet8.png'),
                'width': 160,
                'height': 11
            }
            cls.sprites_cache['apocalypse_bat_down_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_down_idle-and-run-Sheet6.png'),
                'width': 102,
                'height': 11
            }
            cls.sprites_cache['apocalypse_bat_side_left_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_side-left_idle-and-run-Sheet6.png'),
                'width': 96,
                'height': 13
            }
            cls.sprites_cache['apocalypse_bat_side_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_side_idle-and-run-Sheet6.png'),
                'width': 96,
                'height': 13
            }
            cls.sprites_cache['apocalypse_bat_side_attack_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_side_attack-Sheet4.png'),
                'width': 105,
                'height': 16
            }
            cls.sprites_cache['apocalypse_bat_down_attack_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_down_attack-Sheet4.png'),
                'width': 78,
                'height': 25
            }
            cls.sprites_cache['apocalypse_bat_side_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_side_Death-Sheet6.png'),
                'width': 106,
                'height': 13
            }
            cls.sprites_cache['apocalypse_bat_up_idle_and_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_up_idle-and-run-Sheet6.png'),
                'width': 96,
                'height': 14
            }
            cls.sprites_cache['apocalypse_bat_side_left_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_side-left_Death-Sheet6.png'),
                'width': 108,
                'height': 13
            }
            cls.sprites_cache['apocalypse_bat_side_left_attack_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_side-left_attack-Sheet4.png'),
                'width': 112,
                'height': 16
            }
            cls.sprites_cache['apocalypse_bat_up_attack_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Bat/Bat_up_attack-Sheet4.png'),
                'width': 77,
                'height': 25
            }
            cls.sprites_cache['apocalypse_hands_side_left_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Hands_Side-left_idle-Sheet6.png'),
                'width': 72,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_idle_no_hands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Character_side-left_idle_no-hands-Sheet6.png'),
                'width': 60,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Character_side-left_idle-Sheet6.png'),
                'width': 72,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Character_side_idle-Sheet6.png'),
                'width': 72,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_down_idle_no_hands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Character_down_idle_no-hands-Sheet6.png'),
                'width': 66,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_down_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Character_down_idle-Sheet6.png'),
                'width': 78,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hands_up_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Hands_Up_idle-Sheet6.png'),
                'width': 66,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_idle_no_hands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Character_side_idle_no-hands-Sheet6.png'),
                'width': 60,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_up_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Character_up_idle-Sheet6.png'),
                'width': 66,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hands_side_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Hands_Side_idle-Sheet6.png'),
                'width': 72,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hands_down_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Hands_down_idle-Sheet6.png'),
                'width': 78,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_up_idle_no_hands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Idle/Character_up_idle_no-hands-Sheet6.png'),
                'width': 66,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_down_pick_up_nohands_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Character_down_Pick-up_NoHands-Sheet3.png'),
                'width': 33,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hands_down_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Hands_down_Pick-up-Sheet3.png'),
                'width': 36,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_up_pick_up_nohands_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Character_up_Pick-up_NoHands-Sheet3.png'),
                'width': 33,
                'height': 15
            }
            cls.sprites_cache['apocalypse_character_side_left_pick_up_nohands_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Character_side-left_Pick-up_NoHands-Sheet3.png'),
                'width': 30,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_down_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Character_down_Pick-up-Sheet3.png'),
                'width': 36,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Character_side_Pick-up-Sheet3.png'),
                'width': 33,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Character_side-left_Pick-up-Sheet3.png'),
                'width': 33,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hands_up_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Hands_Up_Pick-up-Sheet3.png'),
                'width': 33,
                'height': 15
            }
            cls.sprites_cache['apocalypse_character_up_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Character_up_Pick-up-Sheet3.png'),
                'width': 33,
                'height': 15
            }
            cls.sprites_cache['apocalypse_character_side_pick_up_nohands_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Character_side_Pick-up_NoHands-Sheet3.png'),
                'width': 30,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hands_side_pick_up_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Pick-up/Hands_side_Pick-up-Sheet3.png'),
                'width': 33,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hands_side_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Hands_side_death-Sheet6.png'),
                'width': 126,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_death1_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side_death1-Sheet6.png'),
                'width': 126,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_death2_nohands_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side-left_death2_NoHands-Sheet7.png'),
                'width': 147,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_death1_nohands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side-left_death1_NoHands-Sheet6.png'),
                'width': 126,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_death3_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side-left_death3-Sheet7.png'),
                'width': 147,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_death2_nohands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side_death2_NoHands-Sheet6.png'),
                'width': 146,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_death3_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side_death3-Sheet6.png'),
                'width': 147,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_death1_nohands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side_death1_NoHands-Sheet6.png'),
                'width': 124,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_death1_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side-left_death1-Sheet6.png'),
                'width': 126,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_death2_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side-left_death2-Sheet7.png'),
                'width': 147,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_death3_nohands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side_death3_NoHands-Sheet6.png'),
                'width': 145,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_death2_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side_death2-Sheet6.png'),
                'width': 147,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hands_side_left_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Hands_side-left_death-Sheet6.png'),
                'width': 126,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_death3_nohands_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Death/Character_side-left_death3_NoHands-Sheet7.png'),
                'width': 147,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Character_side_punch-Sheet4.png'),
                'width': 73,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hands_side_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Hands_side_punch-Sheet4.png'),
                'width': 72,
                'height': 10
            }
            cls.sprites_cache['apocalypse_character_side_punch_no_hands_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Character_side_punch_no-hands-Sheet4.png'),
                'width': 50,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_side_left_punch_no_hands_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Character_side-left_punch_no-hands-Sheet4.png'),
                'width': 52,
                'height': 16
            }
            cls.sprites_cache['apocalypse_character_up_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Character_up_punch-Sheet4.png'),
                'width': 48,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_down_punch_no_hands_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Character_down_punch_no-hands-Sheet4.png'),
                'width': 44,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_down_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Character_down_punch-Sheet4.png'),
                'width': 48,
                'height': 18
            }
            cls.sprites_cache['apocalypse_hands_down_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Hands_Down_punch-Sheet4.png'),
                'width': 48,
                'height': 10
            }
            cls.sprites_cache['apocalypse_character_side_left_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Character_side-left_punch-Sheet4.png'),
                'width': 80,
                'height': 18
            }
            cls.sprites_cache['apocalypse_hands_side_left_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Hands_side-left_punch-Sheet4.png'),
                'width': 72,
                'height': 10
            }
            cls.sprites_cache['apocalypse_character_up_punch_no_hands_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Character_up_punch_no-hands-Sheet4.png'),
                'width': 44,
                'height': 17
            }
            cls.sprites_cache['apocalypse_hands_up_punch_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Punch/Hands_Up_punch-Sheet4.png'),
                'width': 48,
                'height': 17
            }
            cls.sprites_cache['apocalypse_hands_down_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Hands_down_run-Sheet6.png'),
                'width': 78,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_side_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Character_side_run-Sheet6.png'),
                'width': 81,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_down_run_no_hands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Character_down_run_no-hands-Sheet6.png'),
                'width': 66,
                'height': 17
            }
            cls.sprites_cache['apocalypse_hands_up_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Hands_Up_run-Sheet6.png'),
                'width': 77,
                'height': 6
            }
            cls.sprites_cache['apocalypse_hands_side_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Hands_Side_run-Sheet6.png'),
                'width': 84,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_side_left_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Character_side-left_run-Sheet6.png'),
                'width': 84,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_down_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Character_down_run-Sheet6.png'),
                'width': 77,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_side_run_no_hands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Character_side_run_no-hands-Sheet6.png'),
                'width': 60,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_up_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Character_up_run-Sheet6.png'),
                'width': 77,
                'height': 17
            }
            cls.sprites_cache['apocalypse_hands_side_left_run_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Hands_side-left_run-Sheet6.png'),
                'width': 84,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_up_run_no_hands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Character_up_run_no-hands-Sheet6.png'),
                'width': 66,
                'height': 17
            }
            cls.sprites_cache['apocalypse_character_side_left_run_no_hands_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Character/Main/Run/Character_side-left_run_no-hands-Sheet6.png'),
                'width': 60,
                'height': 17
            }
            cls.sprites_cache['apocalypse_stop_sign_up_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Up_5.png'),
                'width': 15,
                'height': 24
            }
            cls.sprites_cache['apocalypse_trash_can_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Trash-can_2.png'),
                'width': 13,
                'height': 12
            }
            cls.sprites_cache['apocalypse_bench_4_side_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_4_side_Overgrown_Green.png'),
                'width': 13,
                'height': 28
            }
            cls.sprites_cache['apocalypse_bench_6_up_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_6_up_Overgrown_Dark-Green.png'),
                'width': 32,
                'height': 14
            }
            cls.sprites_cache['apocalypse_gray_brick'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Gray-brick.png'),
                'width': 8,
                'height': 10
            }
            cls.sprites_cache['apocalypse_street_light_4_side_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_4_Side_Overgrown_Dark-Green.png'),
                'width': 26,
                'height': 40
            }
            cls.sprites_cache['apocalypse_trash_can_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Trash-can_1.png'),
                'width': 13,
                'height': 13
            }
            cls.sprites_cache['apocalypse_tire_2_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Tire_2_Grass_Dark-Green.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_chips_pack_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Chips-pack_Red.png'),
                'width': 10,
                'height': 10
            }
            cls.sprites_cache['apocalypse_barrel_rust_red_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Barrel_rust_red_2.png'),
                'width': 15,
                'height': 10
            }
            cls.sprites_cache['apocalypse_manhole'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Manhole.png'),
                'width': 16,
                'height': 16
            }
            cls.sprites_cache['apocalypse_stop_sign_side_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Side_3.png'),
                'width': 7,
                'height': 25
            }
            cls.sprites_cache['apocalypse_stop_sign_up_6_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Up_6_Overgrown_Green.png'),
                'width': 15,
                'height': 24
            }
            cls.sprites_cache['apocalypse_bench_1_down'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_1_down.png'),
                'width': 32,
                'height': 15
            }
            cls.sprites_cache['apocalypse_hydrant_1_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Hydrant_1_red.png'),
                'width': 10,
                'height': 15
            }
            cls.sprites_cache['apocalypse_barrel_rust_red_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Barrel_rust_red_1.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_iron_beam'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Iron-beam.png'),
                'width': 15,
                'height': 5
            }
            cls.sprites_cache['apocalypse_street_light_1_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_1_Side.png'),
                'width': 23,
                'height': 38
            }
            cls.sprites_cache['apocalypse_stop_sign_down_2_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Down_2_Overgrown_Green.png'),
                'width': 14,
                'height': 25
            }
            cls.sprites_cache['apocalypse_stop_sign_side_4_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Side_4_Overgrown_Bleak-Yellow.png'),
                'width': 9,
                'height': 25
            }
            cls.sprites_cache['apocalypse_stop_sign_down_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Down_1.png'),
                'width': 16,
                'height': 25
            }
            cls.sprites_cache['apocalypse_garbage_bin_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Garbage-Bin_3.png'),
                'width': 20,
                'height': 28
            }
            cls.sprites_cache['apocalypse_bench_4_side_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_4_side_Overgrown_Bleak-Yellow.png'),
                'width': 13,
                'height': 28
            }
            cls.sprites_cache['apocalypse_hydrant_1_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Hydrant_1_yellow.png'),
                'width': 10,
                'height': 15
            }
            cls.sprites_cache['apocalypse_bench_6_up_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_6_up_Overgrown_Green.png'),
                'width': 32,
                'height': 14
            }
            cls.sprites_cache['apocalypse_garbage_bin_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Garbage-Bin_2.png'),
                'width': 27,
                'height': 20
            }
            cls.sprites_cache['apocalypse_vending_machine_red_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vending-machine_Red_Overgrown_Bleak-Yellow.png'),
                'width': 19,
                'height': 26
            }
            cls.sprites_cache['apocalypse_street_light_6_down_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_6_Down_Overgrown_Dark-Green.png'),
                'width': 10,
                'height': 37
            }
            cls.sprites_cache['apocalypse_vending_machine_blue_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vending-machine_Blue_Overgrown_Dark-Green.png'),
                'width': 19,
                'height': 26
            }
            cls.sprites_cache['apocalypse_garbage_bin_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Garbage-Bin_1.png'),
                'width': 29,
                'height': 23
            }
            cls.sprites_cache['apocalypse_tire_2_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Tire_2_Grass_Bleak-Yellow.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_bench_2_down_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_2_down_Overgrown_Dark-Green.png'),
                'width': 32,
                'height': 15
            }
            cls.sprites_cache['apocalypse_street_light_4_side_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_4_Side_Overgrown_Green.png'),
                'width': 26,
                'height': 40
            }
            cls.sprites_cache['apocalypse_pallet_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pallet_1.png'),
                'width': 13,
                'height': 14
            }
            cls.sprites_cache['apocalypse_2_tires_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/2-Tires_Grass_Dark-Green.png'),
                'width': 16,
                'height': 16
            }
            cls.sprites_cache['apocalypse_garbage_bin_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Garbage-Bin_4.png'),
                'width': 16,
                'height': 27
            }
            cls.sprites_cache['apocalypse_tire_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Tire_1.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_tire_2_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Tire_2_Grass_Green.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_stop_sign_up_6_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Up_6_Overgrown_Dark-Green.png'),
                'width': 15,
                'height': 24
            }
            cls.sprites_cache['apocalypse_pallet_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pallet_2.png'),
                'width': 14,
                'height': 10
            }
            cls.sprites_cache['apocalypse_stop_sign_side_4_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Side_4_Overgrown_Green.png'),
                'width': 9,
                'height': 25
            }
            cls.sprites_cache['apocalypse_bench_3_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_3_side.png'),
                'width': 11,
                'height': 28
            }
            cls.sprites_cache['apocalypse_barrel_rust_blue_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Barrel_rust_blue_1.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_vending_machine_red_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vending-machine_Red_Overgrown_Dark-Green.png'),
                'width': 19,
                'height': 26
            }
            cls.sprites_cache['apocalypse_bench_5_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_5_up.png'),
                'width': 32,
                'height': 13
            }
            cls.sprites_cache['apocalypse_street_light_6_down_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_6_Down_Overgrown_Green.png'),
                'width': 10,
                'height': 37
            }
            cls.sprites_cache['apocalypse_street_light_3_down'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_3_Down.png'),
                'width': 6,
                'height': 37
            }
            cls.sprites_cache['apocalypse_stop_sign_down_2_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Down_2_Overgrown_Dark-Green.png'),
                'width': 14,
                'height': 25
            }
            cls.sprites_cache['apocalypse_vending_machine_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vending-machine_Blue.png'),
                'width': 14,
                'height': 23
            }
            cls.sprites_cache['apocalypse_shopping_cart'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Shopping-cart.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_2_tires_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/2-Tires_Grass_Green.png'),
                'width': 16,
                'height': 16
            }
            cls.sprites_cache['apocalypse_vending_machine_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vending-machine_Red.png'),
                'width': 14,
                'height': 23
            }
            cls.sprites_cache['apocalypse_chips_pack_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Chips-pack_Yellow.png'),
                'width': 11,
                'height': 11
            }
            cls.sprites_cache['apocalypse_barrel_rust_blue_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Barrel_rust_blue_2.png'),
                'width': 15,
                'height': 10
            }
            cls.sprites_cache['apocalypse_washing_machine'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Washing-machine.png'),
                'width': 14,
                'height': 15
            }
            cls.sprites_cache['apocalypse_stop_sign_side_4_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Side_4_Overgrown_Dark-Green.png'),
                'width': 9,
                'height': 25
            }
            cls.sprites_cache['apocalypse_trash_bag_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Trash-bag_2.png'),
                'width': 10,
                'height': 12
            }
            cls.sprites_cache['apocalypse_refrigerator'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Refrigerator.png'),
                'width': 16,
                'height': 28
            }
            cls.sprites_cache['apocalypse_cardboard_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Cardboard_1.png'),
                'width': 11,
                'height': 9
            }
            cls.sprites_cache['apocalypse_barrel_blue_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Barrel_blue_1.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_metal_plates'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Metal-Plates.png'),
                'width': 23,
                'height': 18
            }
            cls.sprites_cache['apocalypse_trash_bag_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Trash-bag_1.png'),
                'width': 11,
                'height': 11
            }
            cls.sprites_cache['apocalypse_street_light_4_side_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_4_Side_Overgrown_Bleak-Yellow.png'),
                'width': 26,
                'height': 40
            }
            cls.sprites_cache['apocalypse_street_light_2_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_2_Up.png'),
                'width': 6,
                'height': 49
            }
            cls.sprites_cache['apocalypse_cardboard_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Cardboard_2.png'),
                'width': 12,
                'height': 10
            }
            cls.sprites_cache['apocalypse_barrel_blue_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Barrel_blue_2.png'),
                'width': 15,
                'height': 10
            }
            cls.sprites_cache['apocalypse_gray_brick_debris'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Gray-brick_Debris.png'),
                'width': 17,
                'height': 15
            }
            cls.sprites_cache['apocalypse_street_light_5_up_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_5_Up_Overgrown_Bleak-Yellow.png'),
                'width': 11,
                'height': 50
            }
            cls.sprites_cache['apocalypse_traffic_cone'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Traffic-cone.png'),
                'width': 9,
                'height': 11
            }
            cls.sprites_cache['apocalypse_barrel_red_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Barrel_red_2.png'),
                'width': 15,
                'height': 10
            }
            cls.sprites_cache['apocalypse_vending_machine_blue_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vending-machine_Blue_Overgrown_Bleak-Yellow.png'),
                'width': 19,
                'height': 26
            }
            cls.sprites_cache['apocalypse_bench_2_down_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_2_down_Overgrown_Bleak-Yellow.png'),
                'width': 32,
                'height': 15
            }
            cls.sprites_cache['apocalypse_vending_machine_blue_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vending-machine_Blue_Overgrown_Green.png'),
                'width': 19,
                'height': 26
            }
            cls.sprites_cache['apocalypse_bench_6_up_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_6_up_Overgrown_Bleak-Yellow.png'),
                'width': 32,
                'height': 14
            }
            cls.sprites_cache['apocalypse_barrel_red_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Barrel_red_1.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_street_light_5_up_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_5_Up_Overgrown_Dark-Green.png'),
                'width': 11,
                'height': 50
            }
            cls.sprites_cache['apocalypse_stop_sign_down_2_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Down_2_Overgrown_Bleak-Yellow.png'),
                'width': 14,
                'height': 25
            }
            cls.sprites_cache['apocalypse_bench_2_down_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_2_down_Overgrown_Green.png'),
                'width': 32,
                'height': 15
            }
            cls.sprites_cache['apocalypse_vending_machine_red_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vending-machine_Red_Overgrown_Green.png'),
                'width': 19,
                'height': 26
            }
            cls.sprites_cache['apocalypse_2_tires_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/2-Tires_Grass_Bleak-Yellow.png'),
                'width': 16,
                'height': 16
            }
            cls.sprites_cache['apocalypse_bench_4_side_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Bench_4_side_Overgrown_Dark-Green.png'),
                'width': 13,
                'height': 28
            }
            cls.sprites_cache['apocalypse_exhaust_pipe'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Exhaust-pipe.png'),
                'width': 5,
                'height': 11
            }
            cls.sprites_cache['apocalypse_street_light_5_up_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_5_Up_Overgrown_Green.png'),
                'width': 11,
                'height': 50
            }
            cls.sprites_cache['apocalypse_street_light_6_down_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Street-Light_6_Down_Overgrown_Bleak-Yellow.png'),
                'width': 10,
                'height': 37
            }
            cls.sprites_cache['apocalypse_stop_sign_up_6_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Stop-sign_Up_6_Overgrown_Bleak-Yellow.png'),
                'width': 15,
                'height': 24
            }
            cls.sprites_cache['apocalypse_awning_blue_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_blue_2.png'),
                'width': 48,
                'height': 16
            }
            cls.sprites_cache['apocalypse_brick_wall_1_lying'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Brick-wall_1_Lying.png'),
                'width': 13,
                'height': 12
            }
            cls.sprites_cache['apocalypse_awning_blue_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_blue_3.png'),
                'width': 64,
                'height': 16
            }
            cls.sprites_cache['apocalypse_roof_hole_1_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Roof-hole_1_Gray.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_destroyed_wall_not_corner'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Destroyed-wall_not-corner.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_awning_blue_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_blue_1.png'),
                'width': 32,
                'height': 16
            }
            cls.sprites_cache['apocalypse_layered_posters_2_for_ground_and_walls'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/layered-posters_2_For-ground-and-walls.png'),
                'width': 14,
                'height': 12
            }
            cls.sprites_cache['apocalypse_awning_blue_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_blue_4.png'),
                'width': 80,
                'height': 16
            }
            cls.sprites_cache['apocalypse_awning_blue_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_blue_5.png'),
                'width': 96,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hatch_1_open'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Hatch_1_Open.png'),
                'width': 13,
                'height': 18
            }
            cls.sprites_cache['apocalypse_enterance_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Enterance_Green.png'),
                'width': 31,
                'height': 27
            }
            cls.sprites_cache['apocalypse_hvac_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/HVAC_Overgrown_Green.png'),
                'width': 16,
                'height': 15
            }
            cls.sprites_cache['apocalypse_hvac'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/HVAC.png'),
                'width': 16,
                'height': 12
            }
            cls.sprites_cache['apocalypse_door_5_rusty_metal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Door_5_Rusty_Metal.png'),
                'width': 16,
                'height': 25
            }
            cls.sprites_cache['apocalypse_balcony_3_left_ladder_hole'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Balcony_3_Left_Ladder-hole.png'),
                'width': 40,
                'height': 32
            }
            cls.sprites_cache['apocalypse_enterance_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Enterance_Bleak-Yellow.png'),
                'width': 31,
                'height': 27
            }
            cls.sprites_cache['apocalypse_hvac_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/HVAC_Overgrown_Dark-Green.png'),
                'width': 16,
                'height': 15
            }
            cls.sprites_cache['apocalypse_duct_1_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Duct_1_side.png'),
                'width': 9,
                'height': 10
            }
            cls.sprites_cache['apocalypse_hvac_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/HVAC_Overgrown_Bleak-Yellow.png'),
                'width': 16,
                'height': 15
            }
            cls.sprites_cache['apocalypse_door_1_beige'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Door_1_Beige.png'),
                'width': 16,
                'height': 25
            }
            cls.sprites_cache['apocalypse_balcony_2_right'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Balcony_2_Right.png'),
                'width': 40,
                'height': 32
            }
            cls.sprites_cache['apocalypse_balcony_1_left'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Balcony_1_Left.png'),
                'width': 40,
                'height': 32
            }
            cls.sprites_cache['apocalypse_air_vent_4_rusty'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Air-vent_4_rusty.png'),
                'width': 9,
                'height': 12
            }
            cls.sprites_cache['apocalypse_door_4_metal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Door_4_Metal.png'),
                'width': 16,
                'height': 25
            }
            cls.sprites_cache['apocalypse_destroyed_wall_corner'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Destroyed-wall_corner.png'),
                'width': 14,
                'height': 13
            }
            cls.sprites_cache['apocalypse_air_vent_2_rusty'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Air-vent_2_rusty.png'),
                'width': 13,
                'height': 9
            }
            cls.sprites_cache['apocalypse_layered_posters_1_for_ground_and_walls'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/layered-posters_1_For-ground-and-walls.png'),
                'width': 15,
                'height': 14
            }
            cls.sprites_cache['apocalypse_ladder_balcony_metal_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Ladder_Balcony_Metal_1.png'),
                'width': 21,
                'height': 14
            }
            cls.sprites_cache['apocalypse_door_6_boarded_up_metal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Door_6_Boarded-up_Metal.png'),
                'width': 16,
                'height': 25
            }
            cls.sprites_cache['apocalypse_door_3_boarded_up_beige'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Door_3_Boarded-up_Beige.png'),
                'width': 16,
                'height': 25
            }
            cls.sprites_cache['apocalypse_awning_orange_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_orange_1.png'),
                'width': 32,
                'height': 16
            }
            cls.sprites_cache['apocalypse_balcony_4_right_ladder_hole'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Balcony_4_Right_Ladder-hole.png'),
                'width': 40,
                'height': 32
            }
            cls.sprites_cache['apocalypse_enterance_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Enterance_Dark-Green.png'),
                'width': 31,
                'height': 27
            }
            cls.sprites_cache['apocalypse_antenna_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Antenna_1.png'),
                'width': 14,
                'height': 15
            }
            cls.sprites_cache['apocalypse_brick_wall_2_lying'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Brick-wall_2_Lying.png'),
                'width': 11,
                'height': 7
            }
            cls.sprites_cache['apocalypse_awning_orange_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_orange_2.png'),
                'width': 48,
                'height': 16
            }
            cls.sprites_cache['apocalypse_door_2_ajar_beige'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Door_2_Ajar_Beige.png'),
                'width': 16,
                'height': 27
            }
            cls.sprites_cache['apocalypse_antenna_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Antenna_2.png'),
                'width': 14,
                'height': 14
            }
            cls.sprites_cache['apocalypse_awning_orange_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_orange_3.png'),
                'width': 64,
                'height': 16
            }
            cls.sprites_cache['apocalypse_duct_2_down'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Duct_2_down.png'),
                'width': 9,
                'height': 8
            }
            cls.sprites_cache['apocalypse_duct_3_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Duct_3_up.png'),
                'width': 9,
                'height': 10
            }
            cls.sprites_cache['apocalypse_ladder_balcony_metal_1_rusty'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Ladder_Balcony_Metal_1_Rusty.png'),
                'width': 21,
                'height': 14
            }
            cls.sprites_cache['apocalypse_air_vent_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Air-vent_1.png'),
                'width': 13,
                'height': 9
            }
            cls.sprites_cache['apocalypse_air_vent_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Air-vent_3.png'),
                'width': 9,
                'height': 12
            }
            cls.sprites_cache['apocalypse_roof_hole_2_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Roof-hole_2_Red.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_awning_orange_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_orange_4.png'),
                'width': 80,
                'height': 16
            }
            cls.sprites_cache['apocalypse_hatch_1_closed'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Hatch_1_Closed.png'),
                'width': 13,
                'height': 10
            }
            cls.sprites_cache['apocalypse_awning_orange_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildings/Awning_orange_5.png'),
                'width': 96,
                'height': 16
            }
            cls.sprites_cache['apocalypse_canned_food'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Canned-food.png'),
                'width': 7,
                'height': 7
            }
            cls.sprites_cache['apocalypse_bullet_box_1_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Bullet-box_1_Green.png'),
                'width': 6,
                'height': 4
            }
            cls.sprites_cache['apocalypse_bandage'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Bandage.png'),
                'width': 5,
                'height': 7
            }
            cls.sprites_cache['apocalypse_ammo_crate_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Ammo-crate_Blue.png'),
                'width': 9,
                'height': 7
            }
            cls.sprites_cache['apocalypse_gun'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Gun.png'),
                'width': 16,
                'height': 8
            }
            cls.sprites_cache['apocalypse_canned_soup'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Canned-soup.png'),
                'width': 5,
                'height': 7
            }
            cls.sprites_cache['apocalypse_pistol'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Pistol.png'),
                'width': 8,
                'height': 7
            }
            cls.sprites_cache['apocalypse_ammo_crate_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Ammo-crate_Green.png'),
                'width': 9,
                'height': 7
            }
            cls.sprites_cache['apocalypse_bullet_box_1_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Bullet-box_1_Blue.png'),
                'width': 6,
                'height': 4
            }
            cls.sprites_cache['apocalypse_bat'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Bat.png'),
                'width': 11,
                'height': 12
            }
            cls.sprites_cache['apocalypse_shotgun'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Shotgun.png'),
                'width': 15,
                'height': 6
            }
            cls.sprites_cache['apocalypse_ammo_crate_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Ammo-crate_Red.png'),
                'width': 9,
                'height': 7
            }
            cls.sprites_cache['apocalypse_bullet_box_1_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Pickable/Bullet-box_1_Red.png'),
                'width': 6,
                'height': 4
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_right_side_left&down_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Right-side_Left&Down-connect.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_horizontal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Horizontal.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_left_side_right&down_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Left-side_Right&Down-connect.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_vertical'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Vertical.png'),
                'width': 8,
                'height': 16
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_gate_horizontal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Gate_Horizontal.png'),
                'width': 16,
                'height': 15
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_gate_vertical'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Gate_Vertical.png'),
                'width': 3,
                'height': 23
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_left_side_right&up_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Left-side_Right&Up-connect.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_middle_right&left&down_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Middle_Right&Left&Down-connect.png'),
                'width': 16,
                'height': 16
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_right_side_left&up_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Right-side_Left&Up-connect.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_vertical_for_gate'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Vertical_For-gate.png'),
                'width': 7,
                'height': 10
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_gates_closingh_openingv_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Animation/Reinforced-wooden-wall_Gates-closingH_openingV-Sheet7.png'),
                'width': 112,
                'height': 25
            }
            cls.sprites_cache['apocalypse_reinforced_wooden_wall_gates_openingh_closingv_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Reinforced/Animation/Reinforced-wooden-wall_Gates-openingH_closingV-Sheet7.png'),
                'width': 99,
                'height': 25
            }
            cls.sprites_cache['apocalypse_wooden_wall_vertical'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Vertical.png'),
                'width': 8,
                'height': 16
            }
            cls.sprites_cache['apocalypse_wooden_wall_horizontal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Horizontal.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_wooden_wall_right_side_left&up_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Right-side_Left&Up-connect.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_wooden_wall_vertical_for_gate'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Vertical_For-gate.png'),
                'width': 7,
                'height': 10
            }
            cls.sprites_cache['apocalypse_wooden_wall_left_side_right&up_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Left-side_Right&Up-connect.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_wooden_wall_middle_right&left&down_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Middle_Right&Left&Down-connect.png'),
                'width': 16,
                'height': 16
            }
            cls.sprites_cache['apocalypse_wooden_wall_gate_vertical'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Gate_Vertical.png'),
                'width': 3,
                'height': 23
            }
            cls.sprites_cache['apocalypse_wooden_wall_left_side_right&down_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Left-side_Right&Down-connect.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_wooden_wall_gate_horizontal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Gate_Horizontal.png'),
                'width': 16,
                'height': 15
            }
            cls.sprites_cache['apocalypse_wooden_wall_right_side_left&down_connect'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Wooden-wall_Right-side_Left&Down-connect.png'),
                'width': 12,
                'height': 16
            }
            cls.sprites_cache['apocalypse_wooden_wall_gates_openingh_closingv_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Animations/Wooden-wall_Gates-openingH_closingV-Sheet7.png'),
                'width': 99,
                'height': 25
            }
            cls.sprites_cache['apocalypse_wooden_wall_gates_closingh_openingv_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Buildable/Wooden/Animations/Wooden-wall_Gates-closingH_openingV-Sheet7.png'),
                'width': 112,
                'height': 25
            }
            cls.sprites_cache['apocalypse_grass_1_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass_1_Green.png'),
                'width': 7,
                'height': 5
            }
            cls.sprites_cache['apocalypse_grass_5_stepping_on_animation_green_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass_5_Stepping-On-Animation_Green-Sheet2.png'),
                'width': 32,
                'height': 14
            }
            cls.sprites_cache['apocalypse_tree_1_spruce_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree_1_Spruce_Green.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_tree_10_small_oak_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree_10_Small-oak_Green.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_grass_3_stepping_on_animation_green_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass_3_Stepping-On-Animation_Green-Sheet2.png'),
                'width': 32,
                'height': 15
            }
            cls.sprites_cache['apocalypse_tree_3_normal_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree_3_Normal_Green.png'),
                'width': 21,
                'height': 30
            }
            cls.sprites_cache['apocalypse_bush_2_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Bush_2_Green.png'),
                'width': 28,
                'height': 13
            }
            cls.sprites_cache['apocalypse_tree_5_big_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree_5_Big_Green.png'),
                'width': 34,
                'height': 52
            }
            cls.sprites_cache['apocalypse_tree_trunk_2_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree-trunk_2_grass_Green.png'),
                'width': 32,
                'height': 12
            }
            cls.sprites_cache['apocalypse_tree_2_spruce_sparse_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree_2_Spruce-Sparse_Green.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_bush_1_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Bush_1_Green.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_grass_3_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass_3_Green.png'),
                'width': 16,
                'height': 15
            }
            cls.sprites_cache['apocalypse_grass_5_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass_5_Green.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_grass_2_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass_2_Green.png'),
                'width': 12,
                'height': 10
            }
            cls.sprites_cache['apocalypse_tree_6_pine_big_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree_6_Pine_Big_Green.png'),
                'width': 27,
                'height': 49
            }
            cls.sprites_cache['apocalypse_grass_4_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass_4_Green.png'),
                'width': 16,
                'height': 11
            }
            cls.sprites_cache['apocalypse_tree_8_birch_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree_8_Birch_Green.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_grass_4_stepping_on_animation_green_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass_4_Stepping-On-Animation_Green-Sheet2.png'),
                'width': 32,
                'height': 11
            }
            cls.sprites_cache['apocalypse_tree_7_birch_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree_7_Birch_Green.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_tree_9_small_oak_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Tree_9_Small-oak_Green.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_rock_grass'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Rocks/Rock-grass.png'),
                'width': 13,
                'height': 9
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_1.png'),
                'width': 5,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_2.png'),
                'width': 5,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_3.png'),
                'width': 8,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_7.png'),
                'width': 10,
                'height': 9
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_6'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_6.png'),
                'width': 9,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_4.png'),
                'width': 8,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_5.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_13'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_13.png'),
                'width': 9,
                'height': 15
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_12'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_12.png'),
                'width': 13,
                'height': 10
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_10'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_10.png'),
                'width': 11,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_11'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_11.png'),
                'width': 15,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_8'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_8.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_9'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_9.png'),
                'width': 10,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_9_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_9_Lighter.png'),
                'width': 10,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_5_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_5_Lighter.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_11_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_11_Lighter.png'),
                'width': 15,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_12_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_12_Lighter.png'),
                'width': 13,
                'height': 10
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_6_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_6_Lighter.png'),
                'width': 9,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_3_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_3_Lighter.png'),
                'width': 8,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_4_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_4_Lighter.png'),
                'width': 8,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_10_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_10_Lighter.png'),
                'width': 11,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_1_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_1_Lighter.png'),
                'width': 5,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_8_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_8_Lighter.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_2_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_2_Lighter.png'),
                'width': 5,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_13_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_13_Lighter.png'),
                'width': 9,
                'height': 15
            }
            cls.sprites_cache['apocalypse_moss_on_top_green_7_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_7_Lighter.png'),
                'width': 10,
                'height': 9
            }
            cls.sprites_cache['apocalypse_tree_9_small_oak_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Tree_9_Small-oak_Red.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_tree_7_birch_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Tree_7_Birch_Red.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_bush_1_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Bush_1_Red.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_bush_2_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Bush_2_Red.png'),
                'width': 28,
                'height': 13
            }
            cls.sprites_cache['apocalypse_tree_3_normal_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Tree_3_Normal_Red.png'),
                'width': 21,
                'height': 30
            }
            cls.sprites_cache['apocalypse_tree_5_big_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Tree_5_Big_Red.png'),
                'width': 34,
                'height': 52
            }
            cls.sprites_cache['apocalypse_tree_8_birch_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Tree_8_Birch_Red.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_tree_1_spruce_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Tree_1_Spruce_Red.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_tree_2_spruce_sparse_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Tree_2_Spruce-Sparse_Red.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_tree_10_small_oak_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Tree_10_Small-oak_Red.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_tree_6_big_pine_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Red/Tree_6_Big-pine_Red.png'),
                'width': 27,
                'height': 49
            }
            cls.sprites_cache['apocalypse_flowers_2_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_2_red.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_mushroom'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Mushroom.png'),
                'width': 9,
                'height': 8
            }
            cls.sprites_cache['apocalypse_flower_2_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_2_blue.png'),
                'width': 8,
                'height': 11
            }
            cls.sprites_cache['apocalypse_flower_2_purple'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_2_purple.png'),
                'width': 8,
                'height': 11
            }
            cls.sprites_cache['apocalypse_flowers_1_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_1_yellow.png'),
                'width': 14,
                'height': 12
            }
            cls.sprites_cache['apocalypse_flowers_3_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_3_red.png'),
                'width': 9,
                'height': 9
            }
            cls.sprites_cache['apocalypse_flower_2_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_2_red.png'),
                'width': 8,
                'height': 11
            }
            cls.sprites_cache['apocalypse_rain_drop_2_long_white'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rain-Drop_2_Long_White.png'),
                'width': 1,
                'height': 7
            }
            cls.sprites_cache['apocalypse_flowers_1_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_1_red.png'),
                'width': 14,
                'height': 12
            }
            cls.sprites_cache['apocalypse_flowers_3_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_3_yellow.png'),
                'width': 9,
                'height': 9
            }
            cls.sprites_cache['apocalypse_flowers_1_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_1_blue.png'),
                'width': 14,
                'height': 12
            }
            cls.sprites_cache['apocalypse_stick'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Stick.png'),
                'width': 10,
                'height': 6
            }
            cls.sprites_cache['apocalypse_flower_1_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_1_red.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_rain_drop_1_white'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rain-Drop_1_White.png'),
                'width': 1,
                'height': 3
            }
            cls.sprites_cache['apocalypse_rain_drop_2_long_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rain-Drop_2_Long_Blue.png'),
                'width': 1,
                'height': 7
            }
            cls.sprites_cache['apocalypse_flower_1_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_1_yellow.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_flowers_2_purple'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_2_purple.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_mushrooms_1_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Mushrooms_1_Yellow.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_mushrooms_2_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Mushrooms_2_Red.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_flowers_1_purple'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_1_purple.png'),
                'width': 14,
                'height': 12
            }
            cls.sprites_cache['apocalypse_flower_2_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_2_yellow.png'),
                'width': 8,
                'height': 11
            }
            cls.sprites_cache['apocalypse_flower_1_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_1_blue.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_rain_drop_1_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rain-Drop_1_Blue.png'),
                'width': 1,
                'height': 3
            }
            cls.sprites_cache['apocalypse_flowers_2_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_2_yellow.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_flower_1_purple'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_1_purple.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_stump_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Stump_1.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_flowers_2_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_2_blue.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_flowers_3_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_3_blue.png'),
                'width': 9,
                'height': 9
            }
            cls.sprites_cache['apocalypse_tree_trunk_1_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Tree-trunk_1_Green.png'),
                'width': 30,
                'height': 11
            }
            cls.sprites_cache['apocalypse_flowers_3_purple'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_3_purple.png'),
                'width': 9,
                'height': 9
            }
            cls.sprites_cache['apocalypse_stick_leaves'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Stick_leaves.png'),
                'width': 12,
                'height': 12
            }
            cls.sprites_cache['apocalypse_stump_2_mushrooms'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Stump_2_Mushrooms.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_tree_4_dry_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Tree_4_Dry_Green.png'),
                'width': 23,
                'height': 32
            }
            cls.sprites_cache['apocalypse_rock_7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_7.png'),
                'width': 14,
                'height': 13
            }
            cls.sprites_cache['apocalypse_rock_6'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_6.png'),
                'width': 10,
                'height': 7
            }
            cls.sprites_cache['apocalypse_rock_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_4.png'),
                'width': 5,
                'height': 4
            }
            cls.sprites_cache['apocalypse_rock_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_5.png'),
                'width': 4,
                'height': 2
            }
            cls.sprites_cache['apocalypse_rock_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_1.png'),
                'width': 8,
                'height': 4
            }
            cls.sprites_cache['apocalypse_rock_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_2.png'),
                'width': 7,
                'height': 4
            }
            cls.sprites_cache['apocalypse_rock_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_3.png'),
                'width': 6,
                'height': 4
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_6'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_6.png'),
                'width': 11,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_3_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_3_Grass_Green.png'),
                'width': 14,
                'height': 15
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_7.png'),
                'width': 10,
                'height': 4
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_5.png'),
                'width': 17,
                'height': 7
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_4.png'),
                'width': 18,
                'height': 10
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_3_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_3_Grass_Dark-Green.png'),
                'width': 14,
                'height': 15
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_1.png'),
                'width': 22,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_6_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_6_Grass_Dark-Green.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_3.png'),
                'width': 12,
                'height': 12
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_4_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_4_Grass_Green.png'),
                'width': 18,
                'height': 13
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_2.png'),
                'width': 28,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_5_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_5_Grass_Green.png'),
                'width': 20,
                'height': 10
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_2_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_2_Grass_Green.png'),
                'width': 30,
                'height': 13
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_2_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_2_Grass_Dark-Green.png'),
                'width': 30,
                'height': 13
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_7_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_7_Grass_Dark-Green.png'),
                'width': 14,
                'height': 8
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_4_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_4_Grass_Dark-Green.png'),
                'width': 19,
                'height': 13
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_1_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_1_Grass_Dark-Green.png'),
                'width': 25,
                'height': 13
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_7_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_7_Grass_Bleak-Yellow.png'),
                'width': 14,
                'height': 8
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_7_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_7_Grass_Green.png'),
                'width': 14,
                'height': 8
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_4_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_4_Grass_Bleak-Yellow.png'),
                'width': 19,
                'height': 13
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_3_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_3_Grass_Bleak-Yellow.png'),
                'width': 14,
                'height': 15
            }
            cls.sprites_cache['apocalypse_puddle_on_dry_ground_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_2.png'),
                'width': 28,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_1_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_1_Grass_Green.png'),
                'width': 25,
                'height': 13
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_2_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_2_Grass_Bleak-Yellow.png'),
                'width': 30,
                'height': 13
            }
            cls.sprites_cache['apocalypse_puddle_on_mud_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_2.png'),
                'width': 28,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_on_mud_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_3.png'),
                'width': 12,
                'height': 12
            }
            cls.sprites_cache['apocalypse_puddle_on_dry_ground_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_3.png'),
                'width': 12,
                'height': 12
            }
            cls.sprites_cache['apocalypse_puddle_on_dry_ground_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_1.png'),
                'width': 22,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_5_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_5_Grass_Dark-Green.png'),
                'width': 20,
                'height': 10
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_5_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_5_Grass_Bleak-Yellow.png'),
                'width': 20,
                'height': 10
            }
            cls.sprites_cache['apocalypse_puddle_on_mud_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_1.png'),
                'width': 22,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_on_dry_ground_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_4.png'),
                'width': 18,
                'height': 10
            }
            cls.sprites_cache['apocalypse_puddle_on_mud_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_4.png'),
                'width': 18,
                'height': 10
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_6_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_6_Grass_Bleak-Yellow.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_puddle_on_mud_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_5.png'),
                'width': 17,
                'height': 7
            }
            cls.sprites_cache['apocalypse_puddle_on_dry_ground_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_5.png'),
                'width': 17,
                'height': 7
            }
            cls.sprites_cache['apocalypse_puddle_on_dry_ground_7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_7.png'),
                'width': 10,
                'height': 4
            }
            cls.sprites_cache['apocalypse_puddle_on_mud_7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_7.png'),
                'width': 10,
                'height': 4
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_1_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_1_Grass_Bleak-Yellow.png'),
                'width': 25,
                'height': 13
            }
            cls.sprites_cache['apocalypse_puddle_on_mud_6'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_6.png'),
                'width': 11,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_on_dry_ground_6'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_6.png'),
                'width': 11,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_on_grass_6_grass_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_6_Grass_Green.png'),
                'width': 15,
                'height': 12
            }
            cls.sprites_cache['apocalypse_downspout_rainwater_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Downspout_Rainwater-Sheet3.png'),
                'width': 29,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_splash_2_squished_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Puddle-Splash_2_Squished-Sheet4.png'),
                'width': 24,
                'height': 5
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_2_big_sheet5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Rain-drop-splash_2_Big-Sheet5.png'),
                'width': 33,
                'height': 9
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_1_small_sheet5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Rain-drop-splash_1_Small-Sheet5.png'),
                'width': 24,
                'height': 9
            }
            cls.sprites_cache['apocalypse_puddle_splash_3_normal_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Puddle-Splash_3_Normal-Sheet4.png'),
                'width': 24,
                'height': 6
            }
            cls.sprites_cache['apocalypse_puddle_splash_1_small_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Puddle-Splash_1_Small-Sheet4.png'),
                'width': 20,
                'height': 5
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_2_big2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big2.png'),
                'width': 5,
                'height': 7
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_2_big3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big3.png'),
                'width': 7,
                'height': 9
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_2_big1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big1.png'),
                'width': 3,
                'height': 2
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_2_big4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big4.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_2_big5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big5.png'),
                'width': 7,
                'height': 6
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_1_small5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small5.png'),
                'width': 5,
                'height': 5
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_1_small4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small4.png'),
                'width': 5,
                'height': 8
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_1_small1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small1.png'),
                'width': 3,
                'height': 2
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_1_small3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small3.png'),
                'width': 5,
                'height': 8
            }
            cls.sprites_cache['apocalypse_rain_drop_splash_1_small2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small2.png'),
                'width': 3,
                'height': 7
            }
            cls.sprites_cache['apocalypse_downspout_rainwater1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Downspout_Rainwater/Downspout_Rainwater1.png'),
                'width': 10,
                'height': 9
            }
            cls.sprites_cache['apocalypse_downspout_rainwater3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Downspout_Rainwater/Downspout_Rainwater3.png'),
                'width': 8,
                'height': 9
            }
            cls.sprites_cache['apocalypse_downspout_rainwater2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Downspout_Rainwater/Downspout_Rainwater2.png'),
                'width': 6,
                'height': 8
            }
            cls.sprites_cache['apocalypse_tree_8_birch_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Tree_8_Birch_Yellow.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_tree_5_big_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Tree_5_Big_Yellow.png'),
                'width': 34,
                'height': 52
            }
            cls.sprites_cache['apocalypse_tree_10_small_oak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Tree_10_Small-oak_Yellow.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_tree_7_birch_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Tree_7_Birch_Yellow.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_tree_9_small_oak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Tree_9_Small-oak_Yellow.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_tree_3_normal_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Tree_3_Normal_Yellow.png'),
                'width': 21,
                'height': 30
            }
            cls.sprites_cache['apocalypse_bush_2_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Bush_2_Yellow.png'),
                'width': 28,
                'height': 13
            }
            cls.sprites_cache['apocalypse_bush_1_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Bush_1_Yellow.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_tree_6_big_pine_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Tree_6_Big-pine_Yellow.png'),
                'width': 27,
                'height': 49
            }
            cls.sprites_cache['apocalypse_tree_2_spruce_sparse_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Tree_2_Spruce-Sparse_Yellow.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_tree_1_spruce_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Yellow/Tree_1_Spruce_Yellow.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_grass_4_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass_4_Bleak-Yellow.png'),
                'width': 16,
                'height': 11
            }
            cls.sprites_cache['apocalypse_tree_10_small_oak_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree_10_Small-oak_Bleak-Yellow.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_tree_3_normal_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree_3_Normal_Bleak-Yellow.png'),
                'width': 21,
                'height': 30
            }
            cls.sprites_cache['apocalypse_grass_5_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass_5_Bleak-Yellow.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_tree_9_small_oak_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree_9_Small-oak_Bleak-Yellow.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_grass_4_stepping_on_animation_bleak_yellow_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass_4_Stepping-On-Animation_Bleak-Yellow-Sheet2.png'),
                'width': 32,
                'height': 11
            }
            cls.sprites_cache['apocalypse_tree_2_spruce_sparse_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree_2_Spruce-Sparse_Bleak-Yellow.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_grass_1_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass_1_Bleak-Yellow.png'),
                'width': 7,
                'height': 5
            }
            cls.sprites_cache['apocalypse_bush_2_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Bush_2_Bleak-Yellow.png'),
                'width': 28,
                'height': 13
            }
            cls.sprites_cache['apocalypse_grass_5_stepping_on_animation_bleak_yellow_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass_5_Stepping-On-Animation_Bleak-Yellow-Sheet2.png'),
                'width': 32,
                'height': 14
            }
            cls.sprites_cache['apocalypse_tree_6_big_pine_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree_6_Big-pine_Bleak-Yellow.png'),
                'width': 27,
                'height': 49
            }
            cls.sprites_cache['apocalypse_grass_3_stepping_on_animation_bleak_yellow_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass_3_Stepping-On-Animation_Bleak-Yellow-Sheet2.png'),
                'width': 32,
                'height': 15
            }
            cls.sprites_cache['apocalypse_grass_2_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass_2_Bleak-Yellow.png'),
                'width': 12,
                'height': 10
            }
            cls.sprites_cache['apocalypse_bush_1_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Bush_1_Bleak-Yellow.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_tree_5_big_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree_5_Big_Bleak-Yellow.png'),
                'width': 34,
                'height': 52
            }
            cls.sprites_cache['apocalypse_tree_8_birch_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree_8_Birch_Bleak-Yellow.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_tree_trunk_2_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree-trunk_2_grass_Bleak-Yellow.png'),
                'width': 32,
                'height': 12
            }
            cls.sprites_cache['apocalypse_grass_3_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass_3_Bleak-Yellow.png'),
                'width': 16,
                'height': 15
            }
            cls.sprites_cache['apocalypse_tree_7_birch_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree_7_Birch_Bleak-Yellow.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_tree_1_spruce_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Tree_1_Spruce_Bleak-Yellow.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_rock_grass_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Rocks/Rock-grass_Bleak-Yellow.png'),
                'width': 13,
                'height': 9
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_8'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_8.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_9'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_9.png'),
                'width': 10,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_1.png'),
                'width': 5,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_2.png'),
                'width': 5,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_3.png'),
                'width': 8,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_11'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_11.png'),
                'width': 15,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_7.png'),
                'width': 10,
                'height': 9
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_6'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_6.png'),
                'width': 9,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_10'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_10.png'),
                'width': 11,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_12'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_12.png'),
                'width': 13,
                'height': 10
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_4.png'),
                'width': 8,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_5.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_13'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_13.png'),
                'width': 9,
                'height': 15
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_10_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_10_Lighter.png'),
                'width': 11,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_6_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_6_Lighter.png'),
                'width': 9,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_3_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_3_Lighter.png'),
                'width': 8,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_9_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_9_Lighter.png'),
                'width': 10,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_5_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_5_Lighter.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_13_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_13_Lighter.png'),
                'width': 9,
                'height': 15
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_2_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_2_Lighter.png'),
                'width': 5,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_7_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_7_Lighter.png'),
                'width': 10,
                'height': 9
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_11_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_11_Lighter.png'),
                'width': 15,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_12_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_12_Lighter.png'),
                'width': 13,
                'height': 10
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_4_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_4_Lighter.png'),
                'width': 8,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_1_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_1_Lighter.png'),
                'width': 5,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_bleak_yellow_8_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_8_Lighter.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_tree_9_small_oak_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree_9_Small-oak_Dark-Green.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_bush_2_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Bush_2_Dark-Green.png'),
                'width': 28,
                'height': 13
            }
            cls.sprites_cache['apocalypse_grass_3_stepping_on_animation_dark_green_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass_3_Stepping-On-Animation_Dark-Green-Sheet2.png'),
                'width': 32,
                'height': 15
            }
            cls.sprites_cache['apocalypse_grass_5_stepping_on_animation_dark_green_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass_5_Stepping-On-Animation_Dark-Green-Sheet2.png'),
                'width': 32,
                'height': 14
            }
            cls.sprites_cache['apocalypse_bush_1_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Bush_1_Dark-Green.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_tree_1_spruce_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree_1_Spruce_Dark-Green.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_tree_3_normal_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree_3_Normal_Dark-Green.png'),
                'width': 21,
                'height': 30
            }
            cls.sprites_cache['apocalypse_tree_5_big_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree_5_Big_Dark-Green.png'),
                'width': 34,
                'height': 52
            }
            cls.sprites_cache['apocalypse_tree_trunk_2_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree-trunk_2_grass_Dark-Green.png'),
                'width': 32,
                'height': 12
            }
            cls.sprites_cache['apocalypse_tree_10_small_oak_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree_10_Small-oak_Dark-Green.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_grass_1_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass_1_Dark-Green.png'),
                'width': 7,
                'height': 5
            }
            cls.sprites_cache['apocalypse_tree_6_big_pine_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree_6_Big-pine_Dark-Green.png'),
                'width': 27,
                'height': 49
            }
            cls.sprites_cache['apocalypse_grass_3_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass_3_Dark-Green.png'),
                'width': 16,
                'height': 15
            }
            cls.sprites_cache['apocalypse_tree_7_birch_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree_7_Birch_Dark-Green.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_tree_8_birch_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree_8_Birch_Dark-Green.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_grass_4_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass_4_Dark-Green.png'),
                'width': 16,
                'height': 11
            }
            cls.sprites_cache['apocalypse_grass_5_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass_5_Dark-Green.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_grass_4_stepping_on_animation_dark_green_sheet2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass_4_Stepping-On-Animation_Dark-Green-Sheet2.png'),
                'width': 32,
                'height': 11
            }
            cls.sprites_cache['apocalypse_grass_2_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass_2_Dark-Green.png'),
                'width': 12,
                'height': 10
            }
            cls.sprites_cache['apocalypse_tree_2_spruce_sparse_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Tree_2_Spruce-Sparse_Dark-Green.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_rock_grass_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Rocks/Rock-grass_Dark-Green.png'),
                'width': 13,
                'height': 9
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_3'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_3.png'),
                'width': 8,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_2'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_2.png'),
                'width': 5,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_1'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_1.png'),
                'width': 5,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_13'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_13.png'),
                'width': 9,
                'height': 15
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_5'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_5.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_4'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_4.png'),
                'width': 8,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_12'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_12.png'),
                'width': 13,
                'height': 10
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_10'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_10.png'),
                'width': 11,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_6'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_6.png'),
                'width': 9,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_7'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_7.png'),
                'width': 10,
                'height': 9
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_11'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_11.png'),
                'width': 15,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_9'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_9.png'),
                'width': 10,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_8'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_8.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_13_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_13_Lighter.png'),
                'width': 9,
                'height': 15
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_9_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_9_Lighter.png'),
                'width': 10,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_5_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_5_Lighter.png'),
                'width': 7,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_6_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_6_Lighter.png'),
                'width': 9,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_3_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_3_Lighter.png'),
                'width': 8,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_10_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_10_Lighter.png'),
                'width': 11,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_4_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_4_Lighter.png'),
                'width': 8,
                'height': 7
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_8_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_8_Lighter.png'),
                'width': 10,
                'height': 8
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_1_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_1_Lighter.png'),
                'width': 5,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_12_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_12_Lighter.png'),
                'width': 13,
                'height': 10
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_11_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_11_Lighter.png'),
                'width': 15,
                'height': 5
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_2_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_2_Lighter.png'),
                'width': 5,
                'height': 6
            }
            cls.sprites_cache['apocalypse_moss_on_top_dark_green_7_lighter'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_7_Lighter.png'),
                'width': 10,
                'height': 9
            }
            cls.sprites_cache['apocalypse_tree_2_spruce_sparse_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Tree_2_Spruce-Sparse_Orange.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_tree_1_spruce_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Tree_1_Spruce_Orange.png'),
                'width': 16,
                'height': 29
            }
            cls.sprites_cache['apocalypse_bush_1_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Bush_1_Orange.png'),
                'width': 15,
                'height': 13
            }
            cls.sprites_cache['apocalypse_tree_6_big_pine_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Tree_6_Big-pine_Orange.png'),
                'width': 27,
                'height': 49
            }
            cls.sprites_cache['apocalypse_tree_9_small_oak_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Tree_9_Small-oak_Orange.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_tree_3_normal_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Tree_3_Normal_Orange.png'),
                'width': 21,
                'height': 30
            }
            cls.sprites_cache['apocalypse_bush_2_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Bush_2_Orange.png'),
                'width': 28,
                'height': 13
            }
            cls.sprites_cache['apocalypse_tree_8_birch_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Tree_8_Birch_Orange.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_tree_5_big_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Tree_5_Big_Orange.png'),
                'width': 34,
                'height': 52
            }
            cls.sprites_cache['apocalypse_tree_7_birch_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Tree_7_Birch_Orange.png'),
                'width': 39,
                'height': 45
            }
            cls.sprites_cache['apocalypse_tree_10_small_oak_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Nature/Orange/Tree_10_Small-oak_Orange.png'),
                'width': 24,
                'height': 36
            }
            cls.sprites_cache['apocalypse_container_4_gray_horizontal_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_4_Gray_Horizontal_Overgrown_Green.png'),
                'width': 41,
                'height': 29
            }
            cls.sprites_cache['apocalypse_container_3_gray_horizontal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_3_Gray_Horizontal.png'),
                'width': 41,
                'height': 26
            }
            cls.sprites_cache['apocalypse_container_12_green_horizontal_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_12_Green_Horizontal_Overgrown_Green.png'),
                'width': 41,
                'height': 29
            }
            cls.sprites_cache['apocalypse_container_10_green_vertical_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_10_Green_Vertical_Overgrown_Dark-Green.png'),
                'width': 29,
                'height': 46
            }
            cls.sprites_cache['apocalypse_container_12_green_horizontal_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_12_Green_Horizontal_Overgrown_Dark-Green.png'),
                'width': 41,
                'height': 29
            }
            cls.sprites_cache['apocalypse_container_10_green_vertical_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_10_Green_Vertical_Overgrown_Green.png'),
                'width': 29,
                'height': 46
            }
            cls.sprites_cache['apocalypse_container_2_gray_vertical_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_2_Gray_Vertical_Overgrown_Dark-Green.png'),
                'width': 29,
                'height': 46
            }
            cls.sprites_cache['apocalypse_container_4_gray_horizontal_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_4_Gray_Horizontal_Overgrown_Dark-Green.png'),
                'width': 41,
                'height': 29
            }
            cls.sprites_cache['apocalypse_container_2_gray_vertical_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_2_Gray_Vertical_Overgrown_Green.png'),
                'width': 29,
                'height': 46
            }
            cls.sprites_cache['apocalypse_container_4_gray_horizontal_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_4_Gray_Horizontal_Overgrown_Bleak-Yellow.png'),
                'width': 41,
                'height': 29
            }
            cls.sprites_cache['apocalypse_container_6_red_vertical_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_6_Red_Vertical_Overgrown_Green.png'),
                'width': 29,
                'height': 46
            }
            cls.sprites_cache['apocalypse_container_8_red_horizontal_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_8_Red_Horizontal_Overgrown_Dark-Green.png'),
                'width': 41,
                'height': 29
            }
            cls.sprites_cache['apocalypse_container_9_green_vertical'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_9_Green_Vertical.png'),
                'width': 24,
                'height': 43
            }
            cls.sprites_cache['apocalypse_container_6_red_vertical_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_6_Red_Vertical_Overgrown_Bleak-Yellow.png'),
                'width': 29,
                'height': 46
            }
            cls.sprites_cache['apocalypse_container_8_red_horizontal_overgrown_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_8_Red_Horizontal_Overgrown_Green.png'),
                'width': 41,
                'height': 29
            }
            cls.sprites_cache['apocalypse_container_12_green_horizontal_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_12_Green_Horizontal_Overgrown_Bleak-Yellow.png'),
                'width': 41,
                'height': 29
            }
            cls.sprites_cache['apocalypse_container_7_red_horizontal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_7_Red_Horizontal.png'),
                'width': 41,
                'height': 26
            }
            cls.sprites_cache['apocalypse_container_10_green_vertical_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_10_Green_Vertical_Overgrown_Bleak-Yellow.png'),
                'width': 29,
                'height': 46
            }
            cls.sprites_cache['apocalypse_container_1_gray_vertical'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_1_Gray_Vertical.png'),
                'width': 24,
                'height': 43
            }
            cls.sprites_cache['apocalypse_container_6_red_vertical_overgrown_dark_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_6_Red_Vertical_Overgrown_Dark-Green.png'),
                'width': 29,
                'height': 46
            }
            cls.sprites_cache['apocalypse_container_8_red_horizontal_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_8_Red_Horizontal_Overgrown_Bleak-Yellow.png'),
                'width': 41,
                'height': 29
            }
            cls.sprites_cache['apocalypse_container_2_gray_vertical_overgrown_bleak_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_2_Gray_Vertical_Overgrown_Bleak-Yellow.png'),
                'width': 29,
                'height': 46
            }
            cls.sprites_cache['apocalypse_container_5_red_vertical'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_5_Red_Vertical.png'),
                'width': 24,
                'height': 43
            }
            cls.sprites_cache['apocalypse_container_11_green_horizontal'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Container/Container_11_Green_Horizontal.png'),
                'width': 41,
                'height': 26
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_green_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Green_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_green_blue_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Blue_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_green_red_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Red_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_green_yellow_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Yellow_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_green_light_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Light-Green_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_green_orange_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Orange_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_bleak_yellow_yellow_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Yellow_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_bleak_yellow_light_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Light-Green_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_bleak_yellow_blue_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Blue_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_bleak_yellow_orange_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Orange_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_bleak_yellow_red_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Red_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_bleak_yellow_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Green_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_dark_green_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Green_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_dark_green_orange_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Orange_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_dark_green_blue_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Blue_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_dark_green_red_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Red_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_dark_green_light_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Light-Green_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_8_overgrown_dark_green_yellow_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Yellow_Bus.png'),
                'width': 64,
                'height': 32
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_green_orange_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Orange_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_green_blue_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Blue_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_green_red_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Red_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_green_yellow_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Yellow_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_green_green_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Green_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_green_dark_blue_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Dark-Blue_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_bleak_yellow_green_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Green_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_bleak_yellow_yellow_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Yellow_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_bleak_yellow_blue_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Blue_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_bleak_yellow_red_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Red_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_bleak_yellow_gray_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Gray_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_bleak_yellow_orange_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Orange_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_dark_green_red_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Red_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_dark_green_blue_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Blue_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_dark_green_green_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Green_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_dark_green_orange_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Orange_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_dark_green_yellow_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Yellow_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_7_overgrown_dark_green_gray_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Gray_Truck.png'),
                'width': 59,
                'height': 59
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_green_yellow_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Yellow_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_green_green_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Green_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_green_dark_blue_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Dark-Blue_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_green_blue_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Blue_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_green_orange_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Orange_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_green_red_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Red_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_bleak_yellow_blue_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Blue_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_bleak_yellow_yellow_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Yellow_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_bleak_yellow_gray_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Gray_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_bleak_yellow_red_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Red_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_bleak_yellow_orange_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Orange_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_bleak_yellow_green_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Green_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_dark_green_orange_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Orange_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_dark_green_green_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Green_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_dark_green_red_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Red_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_dark_green_gray_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Gray_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_dark_green_yellow_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Yellow_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_overgrown_dark_green_blue_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Blue_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_green_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Red.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_green_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Orange.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_green_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Green.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_green_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Blue.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_green_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Gray.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_green_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Yellow.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_bleak_yellow_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Yellow.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_bleak_yellow_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Green.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_bleak_yellow_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Orange.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_bleak_yellow_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Blue.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_bleak_yellow_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Gray.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_bleak_yellow_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Red.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_dark_green_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Gray.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_dark_green_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Red.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_dark_green_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Blue.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_dark_green_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Orange.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_dark_green_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Green.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_1_overgrown_dark_green_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Yellow.png'),
                'width': 25,
                'height': 40
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_yellow_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Yellow_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_red_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Red_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_red_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Red_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_gray_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Gray_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_green_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Green_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_yellow_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Yellow_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_green_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Green_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_gray_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Gray_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_orange_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Orange_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_blue_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Blue_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_blue_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Blue_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_green_orange_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Orange_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_gray_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Gray_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_red_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Red_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_orange_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Orange_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_yellow_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Yellow_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_red_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Red_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_gray_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Gray_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_blue_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Blue_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_green_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Green_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_green_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Green_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_blue_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Blue_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_orange_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Orange_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_bleak_yellow_yellow_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Yellow_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_blue_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Blue_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_orange_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Orange_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_green_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Green_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_red_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Red_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_yellow_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Yellow_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_green_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Green_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_yellow_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Yellow_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_blue_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Blue_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_gray_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Gray_Motorcycle_Up.png'),
                'width': 10,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_red_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Red_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_orange_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Orange_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_9_overgrown_dark_green_gray_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Gray_Motorcycle_Side.png'),
                'width': 24,
                'height': 17
            }
            cls.sprites_cache['apocalypse_car_3_overgrown_green_blue_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Green/Car_3_Overgrown_Green_Blue_Van.png'),
                'width': 42,
                'height': 28
            }
            cls.sprites_cache['apocalypse_car_3_overgrown_green_light_green_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Green/Car_3_Overgrown_Green_Light-Green_Van.png'),
                'width': 42,
                'height': 28
            }
            cls.sprites_cache['apocalypse_car_3_overgrown_bleak_yellow_light_green_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Bleak-Yellow/Car_3_Overgrown_Bleak-Yellow_Light-Green_Van.png'),
                'width': 42,
                'height': 28
            }
            cls.sprites_cache['apocalypse_car_3_overgrown_bleak_yellow_blue_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Bleak-Yellow/Car_3_Overgrown_Bleak-Yellow_Blue_Van.png'),
                'width': 42,
                'height': 28
            }
            cls.sprites_cache['apocalypse_car_3_overgrown_dark_green_light_green_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Dark-Green/Car_3_Overgrown_Dark-Green_Light-Green_Van.png'),
                'width': 42,
                'height': 28
            }
            cls.sprites_cache['apocalypse_car_3_overgrown_dark_green_blue_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Dark-Green/Car_3_Overgrown_Dark-Green_Blue_Van.png'),
                'width': 42,
                'height': 28
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_green_red_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Red_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_green_yellow_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Yellow_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_green_gray_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Gray_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_green_orange_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Orange_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_green_blue_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Blue_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_green_green_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Green_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_bleak_yellow_green_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Green_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_bleak_yellow_blue_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Blue_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_bleak_yellow_yellow_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Yellow_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_bleak_yellow_gray_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Gray_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_bleak_yellow_red_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Red_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_bleak_yellow_orange_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Orange_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_dark_green_green_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Green_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_dark_green_gray_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Gray_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_dark_green_orange_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Orange_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_dark_green_yellow_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Yellow_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_dark_green_red_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Red_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_2_overgrown_dark_green_blue_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Blue_Upsidedown.png'),
                'width': 27,
                'height': 39
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_green_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Yellow.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_green_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Green.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_green_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Red.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_green_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Gray.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_green_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Blue.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_green_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Orange.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_bleak_yellow_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Orange.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_bleak_yellow_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Red.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_bleak_yellow_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Blue.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_bleak_yellow_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Gray.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_bleak_yellow_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Yellow.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_bleak_yellow_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Green.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_dark_green_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Red.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_dark_green_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Orange.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_dark_green_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Green.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_dark_green_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Gray.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_dark_green_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Yellow.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_4_overgrown_dark_green_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Blue.png'),
                'width': 42,
                'height': 22
            }
            cls.sprites_cache['apocalypse_car_5_overgrown_green_tractor_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Green/Car_5_Overgrown_Green_Tractor_Side.png'),
                'width': 42,
                'height': 30
            }
            cls.sprites_cache['apocalypse_car_5_overgrown_green_tractor_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Green/Car_5_Overgrown_Green_Tractor_Up.png'),
                'width': 27,
                'height': 35
            }
            cls.sprites_cache['apocalypse_car_5_overgrown_bleak_yellow_tractor_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Bleak-Yellow/Car_5_Overgrown_Bleak-Yellow_Tractor_Side.png'),
                'width': 42,
                'height': 30
            }
            cls.sprites_cache['apocalypse_car_5_overgrown_bleak_yellow_tractor_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Bleak-Yellow/Car_5_Overgrown_Bleak-Yellow_Tractor_Up.png'),
                'width': 27,
                'height': 35
            }
            cls.sprites_cache['apocalypse_car_5_overgrown_dark_green_tractor_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Dark-Green/Car_5_Overgrown_Dark-Green_Tractor_Up.png'),
                'width': 27,
                'height': 35
            }
            cls.sprites_cache['apocalypse_car_5_overgrown_dark_green_tractor_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Dark-Green/Car_5_Overgrown_Dark-Green_Tractor_Side.png'),
                'width': 42,
                'height': 30
            }
            cls.sprites_cache['apocalypse_car_3_rust_light_green_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_3_Rust_Van/Car_3_Rust_Light-Green_Van.png'),
                'width': 43,
                'height': 27
            }
            cls.sprites_cache['apocalypse_car_3_rust_blue_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_3_Rust_Van/Car_3_Rust_Blue_Van.png'),
                'width': 43,
                'height': 27
            }
            cls.sprites_cache['apocalypse_car_8_rust_blue_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Blue_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_rust_yellow_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Yellow_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_rust_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Green_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_rust_light_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Light-Green_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_rust_orange_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Orange_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_rust_red_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Red_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_2_rust_dark_blue_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Dark-Blue_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_rust_yellow_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Yellow_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_rust_red_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Red_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_rust_blue_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Blue_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_rust_green_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Green_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_rust_orange_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Orange_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_4_rust_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Green.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_rust_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Yellow.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_rust_dark_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Dark-Blue.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_rust_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Red.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_rust_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Blue.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_rust_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Orange.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_6_rust_orange_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Orange_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_rust_green_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Green_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_rust_red_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Red_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_rust_dark_blue_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Dark-Blue_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_rust_blue_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Blue_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_rust_yellow_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Yellow_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_5_rust_tractor_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_5_Rust_Tractor/Car_5_Rust_Tractor_Side.png'),
                'width': 41,
                'height': 30
            }
            cls.sprites_cache['apocalypse_car_5_rust_tractor_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_5_Rust_Tractor/Car_5_Rust_Tractor_Up.png'),
                'width': 23,
                'height': 35
            }
            cls.sprites_cache['apocalypse_car_1_rust_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Orange.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_rust_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Blue.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_rust_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Green.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_rust_dark_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Dark-Blue.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_rust_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Red.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_rust_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Yellow.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_7_rust_red_truck_'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Red_Truck_.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_rust_blue_truck_'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Blue_Truck_.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_rust_green_truck_'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Green_Truck_.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_rust_orange_truck_'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Orange_Truck_.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_rust_dark_blue_truck_'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Dark-Blue_Truck_.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_rust_yellow_truck_'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Yellow_Truck_.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_3_light_green_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_3_Van/Car_3_Light-Green_Van.png'),
                'width': 43,
                'height': 27
            }
            cls.sprites_cache['apocalypse_car_3_blue_van'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_3_Van/Car_3_Blue_Van.png'),
                'width': 43,
                'height': 27
            }
            cls.sprites_cache['apocalypse_car_9_yellow_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Yellow_Motorcycle_Side.png'),
                'width': 23,
                'height': 16
            }
            cls.sprites_cache['apocalypse_car_9_red_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Red_Motorcycle_Up.png'),
                'width': 9,
                'height': 21
            }
            cls.sprites_cache['apocalypse_car_9_orange_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Orange_Motorcycle_Up.png'),
                'width': 9,
                'height': 21
            }
            cls.sprites_cache['apocalypse_car_9_blue_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Blue_Motorcycle_Side.png'),
                'width': 23,
                'height': 16
            }
            cls.sprites_cache['apocalypse_car_9_green_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Green_Motorcycle_Up.png'),
                'width': 9,
                'height': 21
            }
            cls.sprites_cache['apocalypse_car_9_gray_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Gray_Motorcycle_Side.png'),
                'width': 23,
                'height': 16
            }
            cls.sprites_cache['apocalypse_car_9_orange_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Orange_Motorcycle_Side.png'),
                'width': 23,
                'height': 16
            }
            cls.sprites_cache['apocalypse_car_9_gray_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Gray_Motorcycle_Up.png'),
                'width': 9,
                'height': 21
            }
            cls.sprites_cache['apocalypse_car_9_red_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Red_Motorcycle_Side.png'),
                'width': 23,
                'height': 16
            }
            cls.sprites_cache['apocalypse_car_9_yellow_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Yellow_Motorcycle_Up.png'),
                'width': 9,
                'height': 21
            }
            cls.sprites_cache['apocalypse_car_9_blue_motorcycle_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Blue_Motorcycle_Up.png'),
                'width': 9,
                'height': 21
            }
            cls.sprites_cache['apocalypse_car_9_green_motorcycle_side'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Green_Motorcycle_Side.png'),
                'width': 23,
                'height': 16
            }
            cls.sprites_cache['apocalypse_car_1_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Gray.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Red.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Blue.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Yellow.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Orange.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_1_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Green.png'),
                'width': 25,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_7_orange_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Orange_Truck.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_red_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Red_Truck.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_gray_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Gray_Truck.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_yellow_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Yellow_Truck.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_blue_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Blue_Truck.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_7_green_truck'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Green_Truck.png'),
                'width': 59,
                'height': 58
            }
            cls.sprites_cache['apocalypse_car_8_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Green_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_red_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Red_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_blue_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Blue_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_light_green_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Light-Green_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_yellow_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Yellow_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_8_orange_bus'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Orange_Bus.png'),
                'width': 61,
                'height': 31
            }
            cls.sprites_cache['apocalypse_car_2_red_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Red_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_blue_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Blue_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_green_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Green_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_yellow_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Yellow_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_gray_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Gray_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_2_orange_upsidedown'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Orange_Upsidedown.png'),
                'width': 27,
                'height': 37
            }
            cls.sprites_cache['apocalypse_car_6_gray_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Gray_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_orange_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Orange_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_green_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Green_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_blue_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Blue_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_yellow_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Yellow_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_6_red_scrap'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Red_Scrap.png'),
                'width': 39,
                'height': 20
            }
            cls.sprites_cache['apocalypse_car_4_green'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Green.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_yellow'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Yellow.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_blue'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Blue.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_orange'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Orange.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_red'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Red.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_car_4_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Gray.png'),
                'width': 38,
                'height': 19
            }
            cls.sprites_cache['apocalypse_window_15_beige'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_15_Beige.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_14_broken_beige'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_14_Broken_Beige.png'),
                'width': 15,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_3_wood'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_3_wood.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_1_broken_wood'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_1_broken_wood.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_8_broken_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_8_broken_gray.png'),
                'width': 15,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_6_boarded_up_wood'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_6_Boarded-up_wood.png'),
                'width': 15,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_5_boarded_up_wood'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_5_Boarded-up_wood.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_7_broken_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_7_broken_gray.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_4_wood'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_4_wood.png'),
                'width': 15,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_9_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_9_gray.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_10_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_10_gray.png'),
                'width': 15,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_21_open_boarded_up'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_21_open_Boarded-up.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_window_12_boarded_up_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_12_Boarded-up_gray.png'),
                'width': 15,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_11_boarded_up_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_11_Boarded-up_gray.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_20_open_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_20_open_gray.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_window_17_boarded_up_beige'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_17_Boarded-up_Beige.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_19_gray'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_19_gray.png'),
                'width': 16,
                'height': 14
            }
            cls.sprites_cache['apocalypse_window_16_beige'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_16_Beige.png'),
                'width': 15,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_18_boarded_up_beige'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_18_Boarded-up_Beige.png'),
                'width': 15,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_13_broken_beige'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_13_Broken_Beige.png'),
                'width': 13,
                'height': 15
            }
            cls.sprites_cache['apocalypse_window_2_broken_wood'] = {
                'sheet': SpriteSheet('apocalypse/Objects/Windows/Window_2_broken_wood.png'),
                'width': 15,
                'height': 15
            }
            cls.sprites_cache['apocalypse_grass_on_top_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Grass_On-Top_TileSet.png'),
                'width': 122,
                'height': 91
            }
            cls.sprites_cache['apocalypse_gutter_and_downspout'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Gutter-And-Downspout.png'),
                'width': 187,
                'height': 112
            }
            cls.sprites_cache['apocalypse_iron_fence_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Iron-Fence_TileSet.png'),
                'width': 38,
                'height': 59
            }
            cls.sprites_cache['apocalypse_background_green_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Background_Green_TileSet.png'),
                'width': 384,
                'height': 272
            }
            cls.sprites_cache['apocalypse_roof_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Roof_TileSet.png'),
                'width': 256,
                'height': 80
            }
            cls.sprites_cache['apocalypse_background_bleak_yellow_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Background_Bleak-Yellow_TileSet.png'),
                'width': 384,
                'height': 272
            }
            cls.sprites_cache['apocalypse_garbage_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Garbage_TileSet.png'),
                'width': 128,
                'height': 64
            }
            cls.sprites_cache['apocalypse_background_dark_green_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Background_Dark-Green_TileSet.png'),
                'width': 384,
                'height': 272
            }
            cls.sprites_cache['apocalypse_brick_wall_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Brick-Wall_TileSet.png'),
                'width': 96,
                'height': 48
            }
            cls.sprites_cache['apocalypse_buildings_dark_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Buildings/Buildings_dark_TileSet.png'),
                'width': 208,
                'height': 208
            }
            cls.sprites_cache['apocalypse_buildings_gray_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Buildings/Buildings_gray_TileSet.png'),
                'width': 208,
                'height': 208
            }
            cls.sprites_cache['apocalypse_buildings_white_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Buildings/Buildings_white_TileSet.png'),
                'width': 208,
                'height': 208
            }
            cls.sprites_cache['apocalypse_buildings_beige_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Buildings/Buildings_beige_TileSet.png'),
                'width': 208,
                'height': 208
            }
            cls.sprites_cache['apocalypse_wire_fence_tileset'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Wire-Fence/Wire-Fence_TileSet.png'),
                'width': 80,
                'height': 48
            }
            cls.sprites_cache['apocalypse_wire_fence_opening_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Wire-Fence/Wire-Fence_Opening_Sheet8.png'),
                'width': 159,
                'height': 22
            }
            cls.sprites_cache['apocalypse_wire_fence_closing_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Wire-Fence/Wire-Fence_Closing_Sheet8.png'),
                'width': 163,
                'height': 22
            }
            cls.sprites_cache['apocalypse_wire_fence_opening_no_lock_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Wire-Fence/Wire-Fence_Opening_No-Lock_Sheet8.png'),
                'width': 142,
                'height': 22
            }
            cls.sprites_cache['apocalypse_wire_fence_gate_lock'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Wire-Fence/Wire-Fence_Gate_Lock.png'),
                'width': 16,
                'height': 16
            }
            cls.sprites_cache['apocalypse_wire_fence_gate'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Wire-Fence/Wire-Fence_Gate.png'),
                'width': 16,
                'height': 16
            }
            cls.sprites_cache['apocalypse_wire_fence_closing_no_lock_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Tiles/Wire-Fence/Wire-Fence_Closing_No-Lock_Sheet7.png'),
                'width': 142,
                'height': 22
            }
            cls.sprites_cache['apocalypse_zombie_small_side_left_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_Idle-Sheet6.png'),
                'width': 66,
                'height': 15
            }
            cls.sprites_cache['apocalypse_zombie_small_down_second_attack_sheet11'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Down_Second-Attack-Sheet11.png'),
                'width': 163,
                'height': 57
            }
            cls.sprites_cache['apocalypse_zombie_small_down_first_attack_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Down_First-Attack-Sheet4.png'),
                'width': 52,
                'height': 16
            }
            cls.sprites_cache['apocalypse_zombie_small_up_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Up_Idle-Sheet6.png'),
                'width': 78,
                'height': 15
            }
            cls.sprites_cache['apocalypse_zombie_small_side_left_first_attack_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_First-Attack-Sheet4.png'),
                'width': 44,
                'height': 14
            }
            cls.sprites_cache['apocalypse_zombie_small_down_walk_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Down_walk-Sheet6.png'),
                'width': 72,
                'height': 16
            }
            cls.sprites_cache['apocalypse_zombie_small_side_walk_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_Walk-Sheet6.png'),
                'width': 78,
                'height': 15
            }
            cls.sprites_cache['apocalypse_zombie_small_side_first_attack_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_First-Attack-Sheet4.png'),
                'width': 43,
                'height': 14
            }
            cls.sprites_cache['apocalypse_zombie_small_side_left_first_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_First-Death-Sheet6.png'),
                'width': 96,
                'height': 14
            }
            cls.sprites_cache['apocalypse_zombie_small_side_left_second_attack_sheet11'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_Second-Attack-Sheet11.png'),
                'width': 682,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_small_up_first_attack_sheet4'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Up_First-Attack-Sheet4.png'),
                'width': 56,
                'height': 15
            }
            cls.sprites_cache['apocalypse_zombie_small_side_second_attack_sheet11'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_Second-Attack-Sheet11.png'),
                'width': 682,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_small_side_left_walk_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_Walk-Sheet6.png'),
                'width': 78,
                'height': 15
            }
            cls.sprites_cache['apocalypse_zombie_small_side_left_second_death_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_Second-Death-Sheet7.png'),
                'width': 112,
                'height': 16
            }
            cls.sprites_cache['apocalypse_zombie_small_up_walk_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Up_Walk-Sheet6.png'),
                'width': 78,
                'height': 16
            }
            cls.sprites_cache['apocalypse_zombie_small_side_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_Idle-Sheet6.png'),
                'width': 66,
                'height': 15
            }
            cls.sprites_cache['apocalypse_zombie_small_down_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Down_Idle-Sheet6.png'),
                'width': 78,
                'height': 16
            }
            cls.sprites_cache['apocalypse_zombie_small_side_first_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_First-Death-Sheet6.png'),
                'width': 96,
                'height': 14
            }
            cls.sprites_cache['apocalypse_zombie_small_up_second_attack_sheet11'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Up_Second-Attack-Sheet11.png'),
                'width': 163,
                'height': 58
            }
            cls.sprites_cache['apocalypse_zombie_small_side_second_death_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_Second-Death-Sheet7.png'),
                'width': 112,
                'height': 16
            }
            cls.sprites_cache['apocalypse_zombie_big_up_second_attack_sheet15'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Up_Second-Attack-Sheet15.png'),
                'width': 393,
                'height': 24
            }
            cls.sprites_cache['apocalypse_zombie_big_side_left_first_attack_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_First-Attack-Sheet8.png'),
                'width': 184,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_big_down_first_attack_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Down_First-Attack-Sheet8.png'),
                'width': 158,
                'height': 25
            }
            cls.sprites_cache['apocalypse_zombie_big_side_left_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_Walk-Sheet8.png'),
                'width': 128,
                'height': 24
            }
            cls.sprites_cache['apocalypse_zombie_big_up_first_attack_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Up_First-Attack-Sheet8.png'),
                'width': 144,
                'height': 24
            }
            cls.sprites_cache['apocalypse_zombie_big_up_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Up_Idle-Sheet6.png'),
                'width': 96,
                'height': 22
            }
            cls.sprites_cache['apocalypse_zombie_big_up_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Up_Walk-Sheet8.png'),
                'width': 127,
                'height': 24
            }
            cls.sprites_cache['apocalypse_zombie_big_side_first_death_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_First-Death-Sheet7.png'),
                'width': 201,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_big_side_left_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_Idle-Sheet6.png'),
                'width': 96,
                'height': 22
            }
            cls.sprites_cache['apocalypse_zombie_big_side_first_attack_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_First-Attack-Sheet8.png'),
                'width': 184,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_big_down_second_attack_sheet15'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Down_Second-Attack-Sheet15.png'),
                'width': 324,
                'height': 30
            }
            cls.sprites_cache['apocalypse_zombie_big_side_left_second_death_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_Second-Death-Sheet8.png'),
                'width': 232,
                'height': 24
            }
            cls.sprites_cache['apocalypse_zombie_big_down_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Down_Walk-Sheet8.png'),
                'width': 128,
                'height': 24
            }
            cls.sprites_cache['apocalypse_zombie_big_side_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_Walk-Sheet8.png'),
                'width': 128,
                'height': 24
            }
            cls.sprites_cache['apocalypse_zombie_big_side_left_first_death_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_First-Death-Sheet7.png'),
                'width': 203,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_big_side_second_death_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_Second-Death-Sheet8.png'),
                'width': 230,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_big_side_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_Idle-Sheet6.png'),
                'width': 96,
                'height': 22
            }
            cls.sprites_cache['apocalypse_zombie_big_down_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Down_Idle-Sheet6.png'),
                'width': 96,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_big_side_second_attack_sheet15'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_Second-Attack-Sheet15.png'),
                'width': 436,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_big_side_left_second_attack_sheet15'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_Second-Attack-Sheet15.png'),
                'width': 450,
                'height': 23
            }
            cls.sprites_cache['apocalypse_shot_1_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Shot/shot_1-Sheet3.png'),
                'width': 21,
                'height': 6
            }
            cls.sprites_cache['apocalypse_shot_2_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Shot/shot_2-Sheet3.png'),
                'width': 18,
                'height': 6
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_left_second_death_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_Second-Death-Sheet7.png'),
                'width': 189,
                'height': 20
            }
            cls.sprites_cache['apocalypse_zombie_axe_up_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Up_Idle-Sheet6.png'),
                'width': 72,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_Walk-Sheet8.png'),
                'width': 168,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_first_attack_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_First-Attack-Sheet7.png'),
                'width': 172,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_down_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Down_Walk-Sheet8.png'),
                'width': 96,
                'height': 20
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_first_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_First-Death-Sheet6.png'),
                'width': 161,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_down_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Down_Idle-Sheet6.png'),
                'width': 78,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_down_first_attack_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Down_First-Attack-Sheet7.png'),
                'width': 103,
                'height': 21
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_Idle-Sheet6.png'),
                'width': 132,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_up_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Up_Walk-Sheet8.png'),
                'width': 96,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_second_attack_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_Second-Attack-Sheet9.png'),
                'width': 236,
                'height': 27
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_left_first_attack_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_First-Attack-Sheet7.png'),
                'width': 175,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_down_second_attack_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Down_Second-Attack-Sheet9.png'),
                'width': 141,
                'height': 23
            }
            cls.sprites_cache['apocalypse_zombie_axe_up_second_attack_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Up_Second-Attack-Sheet9.png'),
                'width': 122,
                'height': 24
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_left_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_Idle-Sheet6.png'),
                'width': 132,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_left_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_Walk-Sheet8.png'),
                'width': 168,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_left_first_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_First-Death-Sheet6.png'),
                'width': 162,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_up_first_attack_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Up_First-Attack-Sheet7.png'),
                'width': 90,
                'height': 25
            }
            cls.sprites_cache['apocalypse_zombie_axe_side_left_second_attack_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_Second-Attack-Sheet9.png'),
                'width': 243,
                'height': 27
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_down_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Down_Walk-Sheet8.png'),
                'width': 88,
                'height': 20
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_Walk-Sheet8.png'),
                'width': 112,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_left_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_Idle-Sheet6.png'),
                'width': 90,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_first_attack_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_First-Attack-Sheet7.png'),
                'width': 123,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_left_first_attack_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_First-Attack-Sheet7.png'),
                'width': 126,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_left_taking_axe_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_Taking-Axe-Sheet3.png'),
                'width': 60,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_Idle-Sheet6.png'),
                'width': 90,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_left_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_Walk-Sheet8.png'),
                'width': 112,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_down_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Down_Idle-Sheet6.png'),
                'width': 66,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_down_first_attack_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Down_First-Attack-Sheet7.png'),
                'width': 83,
                'height': 21
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_second_death_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_Second-Death-Sheet7.png'),
                'width': 151,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_up_walk_sheet8'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Up_Walk-Sheet8.png'),
                'width': 88,
                'height': 20
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_left_first_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_First-Death-Sheet6.png'),
                'width': 132,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_up_first_attack_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Up_First-Attack-Sheet7.png'),
                'width': 83,
                'height': 21
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_first_death_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_First-Death-Sheet6.png'),
                'width': 129,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_left_second_death_sheet7'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_Second-Death-Sheet7.png'),
                'width': 154,
                'height': 19
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_side_taking_axe_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_Taking-Axe-Sheet3.png'),
                'width': 53,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_up_taking_axe_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Up_Taking-Axe-Sheet3.png'),
                'width': 39,
                'height': 21
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_down_taking_axe_sheet3'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Down_Taking-Axe-Sheet3.png'),
                'width': 36,
                'height': 18
            }
            cls.sprites_cache['apocalypse_zombie_axe_no_axe_up_idle_sheet6'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Up_Idle-Sheet6.png'),
                'width': 66,
                'height': 19
            }
            cls.sprites_cache['apocalypse_axe_side_left_thrown_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side-left_Thrown-Sheet9.png'),
                'width': 126,
                'height': 14
            }
            cls.sprites_cache['apocalypse_axe_vertical_thrown_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Vertical_Thrown-Sheet9.png'),
                'width': 27,
                'height': 16
            }
            cls.sprites_cache['apocalypse_axe_side_left_landed'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side-left_Landed.png'),
                'width': 13,
                'height': 9
            }
            cls.sprites_cache['apocalypse_axe_side_landing_sheet5'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side_Landing-Sheet5.png'),
                'width': 87,
                'height': 16
            }
            cls.sprites_cache['apocalypse_axe_down_landed'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Down_Landed.png'),
                'width': 3,
                'height': 10
            }
            cls.sprites_cache['apocalypse_axe_side_landed'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side_Landed.png'),
                'width': 13,
                'height': 9
            }
            cls.sprites_cache['apocalypse_axe_up_landed'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Up_Landed.png'),
                'width': 3,
                'height': 9
            }
            cls.sprites_cache['apocalypse_axe_up_landing_sheet5'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Up_Landing-Sheet5.png'),
                'width': 58,
                'height': 15
            }
            cls.sprites_cache['apocalypse_axe_down_landing_sheet5'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Down_Landing-Sheet5.png'),
                'width': 58,
                'height': 18
            }
            cls.sprites_cache['apocalypse_axe_side_left_landing_sheet5'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side-left_Landing-Sheet5.png'),
                'width': 95,
                'height': 16
            }
            cls.sprites_cache['apocalypse_axe_side_thrown_sheet9'] = {
                'sheet': SpriteSheet('apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side_Thrown-Sheet9.png'),
                'width': 126,
                'height': 14
            }
            cls.sprites_cache['bullet_all_fire_bullet_pixel_16x16_00'] = {
                'sheet': SpriteSheet('bullet/All_Fire_Bullet_Pixel_16x16_00.png'),
                'width': 640,
                'height': 398
            }
            cls.sprites_cache['pixel_village_wood'] = {
                'sheet': SpriteSheet('pixel_village/Weapons/Wood/Wood.png'),
                'width': 159,
                'height': 80
            }
            cls.sprites_cache['pixel_village_bone'] = {
                'sheet': SpriteSheet('pixel_village/Weapons/Bone/Bone.png'),
                'width': 159,
                'height': 80
            }
            cls.sprites_cache['pixel_village_hands'] = {
                'sheet': SpriteSheet('pixel_village/Weapons/Hands/Hands.png'),
                'width': 26,
                'height': 87
            }
            cls.sprites_cache['pixel_village_bricks_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Bricks_01-Sheet.png'),
                'width': 62,
                'height': 89
            }
            cls.sprites_cache['pixel_village_iron_03_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Iron_03-Sheet.png'),
                'width': 96,
                'height': 128
            }
            cls.sprites_cache['pixel_village_stone_02_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Stone_02-Sheet.png'),
                'width': 85,
                'height': 113
            }
            cls.sprites_cache['pixel_village_iron_02_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Iron_02-Sheet.png'),
                'width': 86,
                'height': 123
            }
            cls.sprites_cache['pixel_village_furnace'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Furnace.png'),
                'width': 189,
                'height': 382
            }
            cls.sprites_cache['pixel_village_stone_03_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Stone_03-Sheet.png'),
                'width': 89,
                'height': 126
            }
            cls.sprites_cache['pixel_village_bricks_03_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Bricks_03-Sheet.png'),
                'width': 96,
                'height': 124
            }
            cls.sprites_cache['pixel_village_iron_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Iron_01-Sheet.png'),
                'width': 64,
                'height': 93
            }
            cls.sprites_cache['pixel_village_bricks_02_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Bricks_02-Sheet.png'),
                'width': 84,
                'height': 121
            }
            cls.sprites_cache['pixel_village_stone_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Furnace/Stone_01-Sheet.png'),
                'width': 64,
                'height': 86
            }
            cls.sprites_cache['pixel_village_level_3_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Sawmill/Level_3-Sheet.png'),
                'width': 896,
                'height': 635
            }
            cls.sprites_cache['pixel_village_level_1'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Sawmill/Level_1.png'),
                'width': 31,
                'height': 26
            }
            cls.sprites_cache['pixel_village_level_2_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Sawmill/Level_2-Sheet.png'),
                'width': 640,
                'height': 508
            }
            cls.sprites_cache['pixel_village_base'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Sawmill/Base.png'),
                'width': 256,
                'height': 133
            }
            cls.sprites_cache['pixel_village_bonfire_07_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_07-Sheet.png'),
                'width': 126,
                'height': 14
            }
            cls.sprites_cache['pixel_village_bonfire'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire.png'),
                'width': 63,
                'height': 354
            }
            cls.sprites_cache['pixel_village_bonfire_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_01-Sheet.png'),
                'width': 124,
                'height': 27
            }
            cls.sprites_cache['pixel_village_bonfire_06_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_06-Sheet.png'),
                'width': 112,
                'height': 6
            }
            cls.sprites_cache['pixel_village_fire_02_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Fire_02-Sheet.png'),
                'width': 105,
                'height': 21
            }
            cls.sprites_cache['pixel_village_bonfire_05_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_05-Sheet.png'),
                'width': 125,
                'height': 14
            }
            cls.sprites_cache['pixel_village_bonfire_08_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_08-Sheet.png'),
                'width': 119,
                'height': 11
            }
            cls.sprites_cache['pixel_village_smoke_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Smoke-Sheet.png'),
                'width': 99,
                'height': 30
            }
            cls.sprites_cache['pixel_village_bonfire_03_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_03-Sheet.png'),
                'width': 126,
                'height': 11
            }
            cls.sprites_cache['pixel_village_fire_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Fire_01-Sheet.png'),
                'width': 122,
                'height': 36
            }
            cls.sprites_cache['pixel_village_bonfire_04_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_04-Sheet.png'),
                'width': 125,
                'height': 19
            }
            cls.sprites_cache['pixel_village_bonfire_10_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_10-Sheet.png'),
                'width': 183,
                'height': 31
            }
            cls.sprites_cache['pixel_village_bonfire_09_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_09-Sheet.png'),
                'width': 311,
                'height': 27
            }
            cls.sprites_cache['pixel_village_bonfire_02_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_02-Sheet.png'),
                'width': 126,
                'height': 29
            }
            cls.sprites_cache['pixel_village_workbench'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Workbench/Workbench.png'),
                'width': 192,
                'height': 351
            }
            cls.sprites_cache['pixel_village_anvil_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Anvil/Anvil_01-Sheet.png'),
                'width': 510,
                'height': 381
            }
            cls.sprites_cache['pixel_village_anvil_02_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Anvil/Anvil_02-Sheet.png'),
                'width': 479,
                'height': 466
            }
            cls.sprites_cache['pixel_village_anvil'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Anvil/Anvil.png'),
                'width': 271,
                'height': 146
            }
            cls.sprites_cache['pixel_village_anvil_03_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Anvil/Anvil_03-Sheet.png'),
                'width': 768,
                'height': 545
            }
            cls.sprites_cache['pixel_village_cooking_station'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Cooking Station.png'),
                'width': 287,
                'height': 207
            }
            cls.sprites_cache['pixel_village_estructure'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Estructure.png'),
                'width': 287,
                'height': 204
            }
            cls.sprites_cache['pixel_village_grill_04_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Grill/Grill_04-Sheet.png'),
                'width': 298,
                'height': 50
            }
            cls.sprites_cache['pixel_village_grill_02_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Grill/Grill_02-Sheet.png'),
                'width': 251,
                'height': 53
            }
            cls.sprites_cache['pixel_village_grill_03_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Grill/Grill_03-Sheet.png'),
                'width': 248,
                'height': 45
            }
            cls.sprites_cache['pixel_village_grill_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Grill/Grill_01-Sheet.png'),
                'width': 253,
                'height': 55
            }
            cls.sprites_cache['pixel_village_butchery_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Butchery/Butchery_01-Sheet.png'),
                'width': 31,
                'height': 29
            }
            cls.sprites_cache['pixel_village_butchery_04'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Butchery/Butchery_04.png'),
                'width': 69,
                'height': 64
            }
            cls.sprites_cache['pixel_village_butchery_02'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Butchery/Butchery_02.png'),
                'width': 32,
                'height': 29
            }
            cls.sprites_cache['pixel_village_butchery_03'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Butchery/Butchery_03.png'),
                'width': 48,
                'height': 48
            }
            cls.sprites_cache['pixel_village_cooker_01'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Cooker/Cooker_01.png'),
                'width': 42,
                'height': 50
            }
            cls.sprites_cache['pixel_village_cooker_02'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Cooker/Cooker_02.png'),
                'width': 36,
                'height': 35
            }
            cls.sprites_cache['pixel_village_cooker_03_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Cooker/Cooker_03-Sheet.png'),
                'width': 190,
                'height': 26
            }
            cls.sprites_cache['pixel_village_cooker_04_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Cooking Station/Cooker/Cooker_04-Sheet.png'),
                'width': 318,
                'height': 80
            }
            cls.sprites_cache['pixel_village_alchemy_table_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Alchemy/Alchemy_Table_01-Sheet.png'),
                'width': 192,
                'height': 673
            }
            cls.sprites_cache['pixel_village_alchemy_table_03_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Alchemy/Alchemy_Table_03-Sheet.png'),
                'width': 400,
                'height': 392
            }
            cls.sprites_cache['pixel_village_alchemy_table_02_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Stations/Alchemy/Alchemy_Table_02-Sheet.png'),
                'width': 528,
                'height': 300
            }
            cls.sprites_cache['pixel_village_floors'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Buildings/Floors.png'),
                'width': 48,
                'height': 48
            }
            cls.sprites_cache['pixel_village_walls'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Buildings/Walls.png'),
                'width': 672,
                'height': 782
            }
            cls.sprites_cache['pixel_village_roofs'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Buildings/Roofs.png'),
                'width': 368,
                'height': 285
            }
            cls.sprites_cache['pixel_village_shadows'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Shadows.png'),
                'width': 223,
                'height': 212
            }
            cls.sprites_cache['pixel_village_props'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Structures/Buildings/Props.png'),
                'width': 218,
                'height': 236
            }
            cls.sprites_cache['pixel_village_vegetation'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Vegetation.png'),
                'width': 392,
                'height': 428
            }
            cls.sprites_cache['pixel_village_farm'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Farm.png'),
                'width': 400,
                'height': 240
            }
            cls.sprites_cache['pixel_village_rocks'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Rocks.png'),
                'width': 202,
                'height': 304
            }
            cls.sprites_cache['pixel_village_tools'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Tools.png'),
                'width': 176,
                'height': 271
            }
            cls.sprites_cache['pixel_village_dungeon_props'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Dungeon_Props.png'),
                'width': 143,
                'height': 92
            }
            cls.sprites_cache['pixel_village_meat'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Meat.png'),
                'width': 61,
                'height': 139
            }
            cls.sprites_cache['pixel_village_esoteric'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Esoteric.png'),
                'width': 111,
                'height': 233
            }
            cls.sprites_cache['pixel_village_pan'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Pan.png'),
                'width': 160,
                'height': 174
            }
            cls.sprites_cache['pixel_village_resources'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Resources.png'),
                'width': 110,
                'height': 176
            }
            cls.sprites_cache['pixel_village_furniture'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Furniture.png'),
                'width': 799,
                'height': 736
            }
            cls.sprites_cache['pixel_village_size_04_export'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Trees/Model_03/Size_04-export.png'),
                'width': 267,
                'height': 416
            }
            cls.sprites_cache['pixel_village_size_04_export_export'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Trees/Model_03/Size_04-export-export.png'),
                'width': 267,
                'height': 416
            }
            cls.sprites_cache['pixel_village_size_03_export'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Trees/Model_03/Size_03-export.png'),
                'width': 184,
                'height': 287
            }
            cls.sprites_cache['pixel_village_size_05'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Trees/Model_01/Size_05.png'),
                'width': 436,
                'height': 368
            }
            cls.sprites_cache['pixel_village_size_04'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Trees/Model_01/Size_04.png'),
                'width': 355,
                'height': 254
            }
            cls.sprites_cache['pixel_village_size_03'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Trees/Model_01/Size_03.png'),
                'width': 207,
                'height': 192
            }
            cls.sprites_cache['pixel_village_size_02'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Static/Trees/Model_01/Size_02.png'),
                'width': 246,
                'height': 126
            }
            cls.sprites_cache['pixel_village_pan_03_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Animated/Pan_03-Sheet.png'),
                'width': 373,
                'height': 27
            }
            cls.sprites_cache['pixel_village_pan_05_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Animated/Pan_05-Sheet.png'),
                'width': 246,
                'height': 32
            }
            cls.sprites_cache['pixel_village_pan_02_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Animated/Pan_02-Sheet.png'),
                'width': 62,
                'height': 18
            }
            cls.sprites_cache['pixel_village_pan_04_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Animated/Pan_04-Sheet.png'),
                'width': 116,
                'height': 17
            }
            cls.sprites_cache['pixel_village_pan_01_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Props/Animated/Pan_01-Sheet.png'),
                'width': 114,
                'height': 21
            }
            cls.sprites_cache['pixel_village_dungeon_tiles'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Tilesets/Dungeon_Tiles.png'),
                'width': 368,
                'height': 352
            }
            cls.sprites_cache['pixel_village_wall_variations'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Tilesets/Wall_Variations.png'),
                'width': 256,
                'height': 480
            }
            cls.sprites_cache['pixel_village_floors_tiles'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Tilesets/Floors_Tiles.png'),
                'width': 320,
                'height': 416
            }
            cls.sprites_cache['pixel_village_water_tiles'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Tilesets/Water_tiles.png'),
                'width': 384,
                'height': 240
            }
            cls.sprites_cache['pixel_village_wall_tiles'] = {
                'sheet': SpriteSheet('pixel_village/Environment/Tilesets/Wall_Tiles.png'),
                'width': 288,
                'height': 400
            }
            cls.sprites_cache['pixel_village_idle_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Npc/Rogue/Idle/Idle-Sheet.png'),
                'width': 115,
                'height': 30
            }
            cls.sprites_cache['pixel_village_death_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Npc/Rogue/Death/Death-Sheet.png'),
                'width': 355,
                'height': 30
            }
            cls.sprites_cache['pixel_village_run_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Npc/Rogue/Run/Run-Sheet.png'),
                'width': 339,
                'height': 32
            }
            cls.sprites_cache['pixel_village_watering_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Watering_Base/Watering_Down-Sheet.png'),
                'width': 465,
                'height': 32
            }
            cls.sprites_cache['pixel_village_watering_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Watering_Base/Watering_Up-Sheet.png'),
                'width': 468,
                'height': 31
            }
            cls.sprites_cache['pixel_village_watering_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Watering_Base/Watering_Side-Sheet.png'),
                'width': 475,
                'height': 31
            }
            cls.sprites_cache['pixel_village_crush_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Crush_Base/Crush_Up-Sheet.png'),
                'width': 463,
                'height': 40
            }
            cls.sprites_cache['pixel_village_crush_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Crush_Base/Crush_Down-Sheet.png'),
                'width': 469,
                'height': 58
            }
            cls.sprites_cache['pixel_village_crush_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Crush_Base/Crush_Side-Sheet.png'),
                'width': 482,
                'height': 34
            }
            cls.sprites_cache['pixel_village_walk_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Walk_Base/Walk_Down-Sheet.png'),
                'width': 335,
                'height': 30
            }
            cls.sprites_cache['pixel_village_walk_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Walk_Base/Walk_Side-Sheet.png'),
                'width': 335,
                'height': 30
            }
            cls.sprites_cache['pixel_village_walk_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Walk_Base/Walk_Up-Sheet.png'),
                'width': 335,
                'height': 30
            }
            cls.sprites_cache['pixel_village_death_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Death_Base/Death_Down-Sheet.png'),
                'width': 466,
                'height': 48
            }
            cls.sprites_cache['pixel_village_death_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Death_Base/Death_Up-Sheet.png'),
                'width': 466,
                'height': 32
            }
            cls.sprites_cache['pixel_village_death_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Death_Base/Death_Side-Sheet.png'),
                'width': 481,
                'height': 37
            }
            cls.sprites_cache['pixel_village_hit_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Hit_Base/Hit_Side-Sheet.png'),
                'width': 205,
                'height': 30
            }
            cls.sprites_cache['pixel_village_hit_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Hit_Base/Hit_Down-Sheet.png'),
                'width': 208,
                'height': 31
            }
            cls.sprites_cache['pixel_village_hit_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Hit_Base/Hit_Up-Sheet.png'),
                'width': 208,
                'height': 31
            }
            cls.sprites_cache['pixel_village_carry_idle_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Carry_Idle/Carry_Idle_Side-Sheet.png'),
                'width': 210,
                'height': 30
            }
            cls.sprites_cache['pixel_village_carry_idle_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Carry_Idle/Carry_Idle_Down-Sheet.png'),
                'width': 208,
                'height': 30
            }
            cls.sprites_cache['pixel_village_carry_idle_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Carry_Idle/Carry_Idle_Up-Sheet.png'),
                'width': 210,
                'height': 30
            }
            cls.sprites_cache['pixel_village_idle_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Idle_Base/Idle_Down-Sheet.png'),
                'width': 208,
                'height': 30
            }
            cls.sprites_cache['pixel_village_idle_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Idle_Base/Idle_Up-Sheet.png'),
                'width': 208,
                'height': 30
            }
            cls.sprites_cache['pixel_village_idle_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Idle_Base/Idle_Side-Sheet.png'),
                'width': 207,
                'height': 30
            }
            cls.sprites_cache['pixel_village_pierce_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Pierce_Base/Pierce_Side-Sheet.png'),
                'width': 470,
                'height': 31
            }
            cls.sprites_cache['pixel_village_pierce_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Pierce_Base/Pierce_Down-Sheet.png'),
                'width': 468,
                'height': 45
            }
            cls.sprites_cache['pixel_village_pierce_top_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Pierce_Base/Pierce_Top-Sheet.png'),
                'width': 466,
                'height': 39
            }
            cls.sprites_cache['pixel_village_carry_walk_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Carry_Walk/Carry_Walk_Side-Sheet.png'),
                'width': 338,
                'height': 30
            }
            cls.sprites_cache['pixel_village_carry_walk_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Carry_Walk/Carry_Walk_Up-Sheet.png'),
                'width': 338,
                'height': 30
            }
            cls.sprites_cache['pixel_village_carry_walk_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Carry_Walk/Carry_Walk_Down-Sheet.png'),
                'width': 336,
                'height': 30
            }
            cls.sprites_cache['pixel_village_slice_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Slice_Base/Slice_Side-Sheet.png'),
                'width': 483,
                'height': 47
            }
            cls.sprites_cache['pixel_village_slice_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Slice_Base/Slice_Up-Sheet.png'),
                'width': 470,
                'height': 60
            }
            cls.sprites_cache['pixel_village_slice_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Slice_Base/Slice_Down-Sheet.png'),
                'width': 467,
                'height': 63
            }
            cls.sprites_cache['pixel_village_fishing_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Fishing_Base/Fishing_Down-Sheet.png'),
                'width': 465,
                'height': 64
            }
            cls.sprites_cache['pixel_village_fishing_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Fishing_Base/Fishing_Up-Sheet.png'),
                'width': 460,
                'height': 53
            }
            cls.sprites_cache['pixel_village_fishing_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Fishing_Base/Fishing_Side-Sheet.png'),
                'width': 484,
                'height': 39
            }
            cls.sprites_cache['pixel_village_collect_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Collect_Base/Collect_Side-Sheet.png'),
                'width': 461,
                'height': 30
            }
            cls.sprites_cache['pixel_village_collect_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Collect_Base/Collect_Down-Sheet.png'),
                'width': 464,
                'height': 32
            }
            cls.sprites_cache['pixel_village_collect_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Collect_Base/Collect_Up-Sheet.png'),
                'width': 466,
                'height': 31
            }
            cls.sprites_cache['pixel_village_carry_run_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Carry_Run/Carry_Run_Side-Sheet.png'),
                'width': 338,
                'height': 31
            }
            cls.sprites_cache['pixel_village_carry_run_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Carry_Run/Carry_Run_Up-Sheet.png'),
                'width': 338,
                'height': 30
            }
            cls.sprites_cache['pixel_village_carry_run_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Carry_Run/Carry_Run_Down-Sheet.png'),
                'width': 336,
                'height': 30
            }
            cls.sprites_cache['pixel_village_run_down_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Run_Base/Run_Down-Sheet.png'),
                'width': 335,
                'height': 30
            }
            cls.sprites_cache['pixel_village_run_side_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Run_Base/Run_Side-Sheet.png'),
                'width': 337,
                'height': 31
            }
            cls.sprites_cache['pixel_village_run_up_sheet'] = {
                'sheet': SpriteSheet('pixel_village/Entities/Characters/Body_A/Animations/Run_Base/Run_Up-Sheet.png'),
                'width': 335,
                'height': 30
            }
            cls.sprites_cache['player_survivor_move_handgun_13'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_13.png'),
                'width': 212,
                'height': 156
            }
            cls.sprites_cache['player_survivor_move_handgun_12'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_12.png'),
                'width': 212,
                'height': 156
            }
            cls.sprites_cache['player_survivor_move_handgun_10'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_10.png'),
                'width': 212,
                'height': 157
            }
            cls.sprites_cache['player_survivor_move_handgun_11'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_11.png'),
                'width': 212,
                'height': 156
            }
            cls.sprites_cache['player_survivor_move_handgun_15'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_15.png'),
                'width': 211,
                'height': 156
            }
            cls.sprites_cache['player_survivor_move_handgun_14'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_14.png'),
                'width': 211,
                'height': 155
            }
            cls.sprites_cache['player_survivor_move_handgun_16'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_16.png'),
                'width': 210,
                'height': 155
            }
            cls.sprites_cache['player_survivor_move_handgun_17'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_17.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_handgun_1'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_1.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_handgun_0'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_0.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_handgun_2'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_2.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_handgun_3'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_3.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_handgun_7'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_7.png'),
                'width': 212,
                'height': 156
            }
            cls.sprites_cache['player_survivor_move_handgun_6'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_6.png'),
                'width': 211,
                'height': 155
            }
            cls.sprites_cache['player_survivor_move_handgun_4'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_4.png'),
                'width': 210,
                'height': 155
            }
            cls.sprites_cache['player_survivor_move_handgun_5'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_5.png'),
                'width': 211,
                'height': 156
            }
            cls.sprites_cache['player_survivor_move_handgun_8'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_8.png'),
                'width': 212,
                'height': 156
            }
            cls.sprites_cache['player_survivor_move_handgun_9'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_9.png'),
                'width': 212,
                'height': 156
            }
            cls.sprites_cache['player_survivor_move_handgun_19'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_19.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_handgun_18'] = {
                'sheet': SpriteSheet('player/handgun/move/survivor-move_handgun_18.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_handgun_16'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_16.png'),
                'width': 209,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_handgun_7'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_7.png'),
                'width': 209,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_handgun_6'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_6.png'),
                'width': 209,
                'height': 152
            }
            cls.sprites_cache['player_survivor_idle_handgun_17'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_17.png'),
                'width': 209,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_handgun_15'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_15.png'),
                'width': 209,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_handgun_4'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_4.png'),
                'width': 209,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_handgun_5'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_5.png'),
                'width': 209,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_handgun_14'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_14.png'),
                'width': 209,
                'height': 152
            }
            cls.sprites_cache['player_survivor_idle_handgun_10'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_10.png'),
                'width': 209,
                'height': 152
            }
            cls.sprites_cache['player_survivor_idle_handgun_1'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_1.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_handgun_0'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_0.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_handgun_11'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_11.png'),
                'width': 209,
                'height': 152
            }
            cls.sprites_cache['player_survivor_idle_handgun_13'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_13.png'),
                'width': 209,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_handgun_2'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_2.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_handgun_3'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_3.png'),
                'width': 209,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_handgun_12'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_12.png'),
                'width': 209,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_handgun_19'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_19.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_handgun_8'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_8.png'),
                'width': 209,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_handgun_9'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_9.png'),
                'width': 209,
                'height': 152
            }
            cls.sprites_cache['player_survivor_idle_handgun_18'] = {
                'sheet': SpriteSheet('player/handgun/idle/survivor-idle_handgun_18.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_handgun_3'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_3.png'),
                'width': 212,
                'height': 158
            }
            cls.sprites_cache['player_survivor_reload_handgun_11'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_11.png'),
                'width': 208,
                'height': 161
            }
            cls.sprites_cache['player_survivor_reload_handgun_10'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_10.png'),
                'width': 207,
                'height': 164
            }
            cls.sprites_cache['player_survivor_reload_handgun_2'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_2.png'),
                'width': 210,
                'height': 156
            }
            cls.sprites_cache['player_survivor_reload_handgun_0'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_0.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_handgun_12'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_12.png'),
                'width': 209,
                'height': 157
            }
            cls.sprites_cache['player_survivor_reload_handgun_13'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_13.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_handgun_1'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_1.png'),
                'width': 210,
                'height': 155
            }
            cls.sprites_cache['player_survivor_reload_handgun_5'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_5.png'),
                'width': 214,
                'height': 163
            }
            cls.sprites_cache['player_survivor_reload_handgun_4'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_4.png'),
                'width': 212,
                'height': 160
            }
            cls.sprites_cache['player_survivor_reload_handgun_6'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_6.png'),
                'width': 211,
                'height': 166
            }
            cls.sprites_cache['player_survivor_reload_handgun_14'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_14.png'),
                'width': 209,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_handgun_7'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_7.png'),
                'width': 208,
                'height': 169
            }
            cls.sprites_cache['player_survivor_reload_handgun_9'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_9.png'),
                'width': 207,
                'height': 168
            }
            cls.sprites_cache['player_survivor_reload_handgun_8'] = {
                'sheet': SpriteSheet('player/handgun/reload/survivor-reload_handgun_8.png'),
                'width': 206,
                'height': 172
            }
            cls.sprites_cache['player_survivor_shoot_handgun_1'] = {
                'sheet': SpriteSheet('player/handgun/shoot/survivor-shoot_handgun_1.png'),
                'width': 200,
                'height': 154
            }
            cls.sprites_cache['player_survivor_shoot_handgun_0'] = {
                'sheet': SpriteSheet('player/handgun/shoot/survivor-shoot_handgun_0.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_shoot_handgun_2'] = {
                'sheet': SpriteSheet('player/handgun/shoot/survivor-shoot_handgun_2.png'),
                'width': 205,
                'height': 154
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_6'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_6.png'),
                'width': 181,
                'height': 189
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_7'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_7.png'),
                'width': 242,
                'height': 161
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_5'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_5.png'),
                'width': 161,
                'height': 178
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_4'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_4.png'),
                'width': 155,
                'height': 181
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_0'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_0.png'),
                'width': 210,
                'height': 154
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_1'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_1.png'),
                'width': 204,
                'height': 161
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_3'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_3.png'),
                'width': 169,
                'height': 181
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_2'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_2.png'),
                'width': 188,
                'height': 173
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_9'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_9.png'),
                'width': 185,
                'height': 190
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_8'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_8.png'),
                'width': 211,
                'height': 164
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_12'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_12.png'),
                'width': 214,
                'height': 161
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_13'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_13.png'),
                'width': 223,
                'height': 153
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_11'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_11.png'),
                'width': 194,
                'height': 169
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_10'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_10.png'),
                'width': 191,
                'height': 182
            }
            cls.sprites_cache['player_survivor_meleeattack_handgun_14'] = {
                'sheet': SpriteSheet('player/handgun/meleeattack/survivor-meleeattack_handgun_14.png'),
                'width': 216,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_shotgun_9'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_9.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_shotgun_8'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_8.png'),
                'width': 256,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_shotgun_19'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_19.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_18'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_18.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_13'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_13.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_shotgun_12'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_12.png'),
                'width': 256,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_shotgun_10'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_10.png'),
                'width': 256,
                'height': 155
            }
            cls.sprites_cache['player_survivor_move_shotgun_11'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_11.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_shotgun_15'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_15.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_14'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_14.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_shotgun_16'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_16.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_17'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_17.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_5'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_5.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_4'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_4.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_6'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_6.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_shotgun_7'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_7.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_shotgun_3'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_3.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_2'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_2.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_0'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_shotgun_1'] = {
                'sheet': SpriteSheet('player/shotgun/move/survivor-move_shotgun_1.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_9'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_9.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_8'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_8.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_19'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_19.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_18'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_18.png'),
                'width': 259,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_shotgun_3'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_3.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_16'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_16.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_17'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_17.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_2'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_2.png'),
                'width': 259,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_shotgun_0'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_15'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_15.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_14'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_14.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_1'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_1.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_5'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_5.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_10'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_10.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_11'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_11.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_4'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_4.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_6'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_6.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_13'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_13.png'),
                'width': 258,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_shotgun_12'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_12.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_shotgun_7'] = {
                'sheet': SpriteSheet('player/shotgun/idle/survivor-idle_shotgun_7.png'),
                'width': 258,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_shotgun_18'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_18.png'),
                'width': 259,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_shotgun_19'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_19.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_reload_shotgun_8'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_8.png'),
                'width': 266,
                'height': 159
            }
            cls.sprites_cache['player_survivor_reload_shotgun_9'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_9.png'),
                'width': 265,
                'height': 159
            }
            cls.sprites_cache['player_survivor_reload_shotgun_7'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_7.png'),
                'width': 266,
                'height': 160
            }
            cls.sprites_cache['player_survivor_reload_shotgun_11'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_11.png'),
                'width': 262,
                'height': 159
            }
            cls.sprites_cache['player_survivor_reload_shotgun_10'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_10.png'),
                'width': 264,
                'height': 158
            }
            cls.sprites_cache['player_survivor_reload_shotgun_6'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_6.png'),
                'width': 267,
                'height': 160
            }
            cls.sprites_cache['player_survivor_reload_shotgun_4'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_4.png'),
                'width': 267,
                'height': 160
            }
            cls.sprites_cache['player_survivor_reload_shotgun_12'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_12.png'),
                'width': 259,
                'height': 161
            }
            cls.sprites_cache['player_survivor_reload_shotgun_13'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_13.png'),
                'width': 257,
                'height': 161
            }
            cls.sprites_cache['player_survivor_reload_shotgun_5'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_5.png'),
                'width': 268,
                'height': 161
            }
            cls.sprites_cache['player_survivor_reload_shotgun_1'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_1.png'),
                'width': 260,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_shotgun_17'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_17.png'),
                'width': 259,
                'height': 156
            }
            cls.sprites_cache['player_survivor_reload_shotgun_16'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_16.png'),
                'width': 259,
                'height': 157
            }
            cls.sprites_cache['player_survivor_reload_shotgun_0'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_reload_shotgun_2'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_2.png'),
                'width': 263,
                'height': 156
            }
            cls.sprites_cache['player_survivor_reload_shotgun_14'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_14.png'),
                'width': 258,
                'height': 160
            }
            cls.sprites_cache['player_survivor_reload_shotgun_15'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_15.png'),
                'width': 258,
                'height': 159
            }
            cls.sprites_cache['player_survivor_reload_shotgun_3'] = {
                'sheet': SpriteSheet('player/shotgun/reload/survivor-reload_shotgun_3.png'),
                'width': 265,
                'height': 159
            }
            cls.sprites_cache['player_survivor_shoot_shotgun_2'] = {
                'sheet': SpriteSheet('player/shotgun/shoot/survivor-shoot_shotgun_2.png'),
                'width': 255,
                'height': 153
            }
            cls.sprites_cache['player_survivor_shoot_shotgun_0'] = {
                'sheet': SpriteSheet('player/shotgun/shoot/survivor-shoot_shotgun_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_shoot_shotgun_1'] = {
                'sheet': SpriteSheet('player/shotgun/shoot/survivor-shoot_shotgun_1.png'),
                'width': 253,
                'height': 153
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_8'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_8.png'),
                'width': 282,
                'height': 163
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_9'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_9.png'),
                'width': 221,
                'height': 229
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_12'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_12.png'),
                'width': 210,
                'height': 224
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_13'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_13.png'),
                'width': 256,
                'height': 162
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_11'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_11.png'),
                'width': 179,
                'height': 248
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_10'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_10.png'),
                'width': 159,
                'height': 256
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_14'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_14.png'),
                'width': 267,
                'height': 153
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_2'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_2.png'),
                'width': 241,
                'height': 167
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_3'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_3.png'),
                'width': 224,
                'height': 189
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_1'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_1.png'),
                'width': 254,
                'height': 158
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_0'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_4'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_4.png'),
                'width': 214,
                'height': 200
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_5'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_5.png'),
                'width': 209,
                'height': 203
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_7'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_7.png'),
                'width': 266,
                'height': 174
            }
            cls.sprites_cache['player_survivor_meleeattack_shotgun_6'] = {
                'sheet': SpriteSheet('player/shotgun/meleeattack/survivor-meleeattack_shotgun_6.png'),
                'width': 212,
                'height': 219
            }
            cls.sprites_cache['player_survivor_move_rifle_10'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_10.png'),
                'width': 256,
                'height': 155
            }
            cls.sprites_cache['player_survivor_move_rifle_11'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_11.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_rifle_13'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_13.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_rifle_12'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_12.png'),
                'width': 256,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_rifle_16'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_16.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_17'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_17.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_15'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_15.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_14'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_14.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_rifle_4'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_4.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_5'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_5.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_7'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_7.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_rifle_6'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_6.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_rifle_2'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_2.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_3'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_3.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_1'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_1.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_0'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_8'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_8.png'),
                'width': 256,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_rifle_9'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_9.png'),
                'width': 257,
                'height': 154
            }
            cls.sprites_cache['player_survivor_move_rifle_19'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_19.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_move_rifle_18'] = {
                'sheet': SpriteSheet('player/rifle/move/survivor-move_rifle_18.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_13'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_13.png'),
                'width': 258,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_rifle_0'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_1'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_1.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_12'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_12.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_10'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_10.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_3'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_3.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_2'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_2.png'),
                'width': 259,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_rifle_11'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_11.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_15'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_15.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_6'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_6.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_7'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_7.png'),
                'width': 258,
                'height': 154
            }
            cls.sprites_cache['player_survivor_idle_rifle_14'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_14.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_16'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_16.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_5'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_5.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_4'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_4.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_17'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_17.png'),
                'width': 258,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_9'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_9.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_8'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_8.png'),
                'width': 257,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_19'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_19.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_idle_rifle_18'] = {
                'sheet': SpriteSheet('player/rifle/idle/survivor-idle_rifle_18.png'),
                'width': 259,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_rifle_3'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_3.png'),
                'width': 265,
                'height': 159
            }
            cls.sprites_cache['player_survivor_reload_rifle_2'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_2.png'),
                'width': 263,
                'height': 156
            }
            cls.sprites_cache['player_survivor_reload_rifle_0'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_reload_rifle_1'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_1.png'),
                'width': 260,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_rifle_5'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_5.png'),
                'width': 268,
                'height': 161
            }
            cls.sprites_cache['player_survivor_reload_rifle_4'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_4.png'),
                'width': 266,
                'height': 160
            }
            cls.sprites_cache['player_survivor_reload_rifle_6'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_6.png'),
                'width': 267,
                'height': 160
            }
            cls.sprites_cache['player_survivor_reload_rifle_7'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_7.png'),
                'width': 266,
                'height': 160
            }
            cls.sprites_cache['player_survivor_reload_rifle_10'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_10.png'),
                'width': 264,
                'height': 158
            }
            cls.sprites_cache['player_survivor_reload_rifle_11'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_11.png'),
                'width': 262,
                'height': 159
            }
            cls.sprites_cache['player_survivor_reload_rifle_13'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_13.png'),
                'width': 257,
                'height': 161
            }
            cls.sprites_cache['player_survivor_reload_rifle_12'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_12.png'),
                'width': 259,
                'height': 161
            }
            cls.sprites_cache['player_survivor_reload_rifle_16'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_16.png'),
                'width': 259,
                'height': 157
            }
            cls.sprites_cache['player_survivor_reload_rifle_17'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_17.png'),
                'width': 259,
                'height': 156
            }
            cls.sprites_cache['player_survivor_reload_rifle_15'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_15.png'),
                'width': 258,
                'height': 159
            }
            cls.sprites_cache['player_survivor_reload_rifle_14'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_14.png'),
                'width': 258,
                'height': 160
            }
            cls.sprites_cache['player_survivor_reload_rifle_19'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_19.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_reload_rifle_18'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_18.png'),
                'width': 259,
                'height': 154
            }
            cls.sprites_cache['player_survivor_reload_rifle_9'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_9.png'),
                'width': 265,
                'height': 159
            }
            cls.sprites_cache['player_survivor_reload_rifle_8'] = {
                'sheet': SpriteSheet('player/rifle/reload/survivor-reload_rifle_8.png'),
                'width': 266,
                'height': 159
            }
            cls.sprites_cache['player_survivor_shoot_rifle_1'] = {
                'sheet': SpriteSheet('player/rifle/shoot/survivor-shoot_rifle_1.png'),
                'width': 253,
                'height': 153
            }
            cls.sprites_cache['player_survivor_shoot_rifle_0'] = {
                'sheet': SpriteSheet('player/rifle/shoot/survivor-shoot_rifle_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_shoot_rifle_2'] = {
                'sheet': SpriteSheet('player/rifle/shoot/survivor-shoot_rifle_2.png'),
                'width': 255,
                'height': 153
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_12'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_12.png'),
                'width': 210,
                'height': 224
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_13'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_13.png'),
                'width': 256,
                'height': 162
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_11'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_11.png'),
                'width': 179,
                'height': 248
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_10'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_10.png'),
                'width': 159,
                'height': 256
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_14'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_14.png'),
                'width': 267,
                'height': 153
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_6'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_6.png'),
                'width': 213,
                'height': 219
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_7'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_7.png'),
                'width': 266,
                'height': 174
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_5'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_5.png'),
                'width': 210,
                'height': 203
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_4'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_4.png'),
                'width': 215,
                'height': 200
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_0'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_0.png'),
                'width': 259,
                'height': 153
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_1'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_1.png'),
                'width': 254,
                'height': 158
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_3'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_3.png'),
                'width': 224,
                'height': 189
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_2'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_2.png'),
                'width': 241,
                'height': 166
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_9'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_9.png'),
                'width': 221,
                'height': 229
            }
            cls.sprites_cache['player_survivor_meleeattack_rifle_8'] = {
                'sheet': SpriteSheet('player/rifle/meleeattack/survivor-meleeattack_rifle_8.png'),
                'width': 282,
                'height': 163
            }
            cls.sprites_cache['player_survivor_idle_0'] = {
                'sheet': SpriteSheet('player/feet/idle/survivor-idle_0.png'),
                'width': 98,
                'height': 114
            }
            cls.sprites_cache['player_survivor_walk_1'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_1.png'),
                'width': 140,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_0'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_0.png'),
                'width': 146,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_2'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_2.png'),
                'width': 127,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_3'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_3.png'),
                'width': 111,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_7'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_7.png'),
                'width': 109,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_6'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_6.png'),
                'width': 93,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_4'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_4.png'),
                'width': 94,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_5'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_5.png'),
                'width': 78,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_11'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_11.png'),
                'width': 139,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_10'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_10.png'),
                'width': 145,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_12'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_12.png'),
                'width': 126,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_13'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_13.png'),
                'width': 109,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_17'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_17.png'),
                'width': 111,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_16'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_16.png'),
                'width': 94,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_14'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_14.png'),
                'width': 93,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_15'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_15.png'),
                'width': 78,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_18'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_18.png'),
                'width': 127,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_19'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_19.png'),
                'width': 140,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_8'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_8.png'),
                'width': 126,
                'height': 100
            }
            cls.sprites_cache['player_survivor_walk_9'] = {
                'sheet': SpriteSheet('player/feet/walk/survivor-walk_9.png'),
                'width': 139,
                'height': 100
            }
            cls.sprites_cache['player_survivor_strafe_left_0'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_0.png'),
                'width': 130,
                'height': 144
            }
            cls.sprites_cache['player_survivor_strafe_left_1'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_1.png'),
                'width': 130,
                'height': 140
            }
            cls.sprites_cache['player_survivor_strafe_left_3'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_3.png'),
                'width': 130,
                'height': 124
            }
            cls.sprites_cache['player_survivor_strafe_left_2'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_2.png'),
                'width': 130,
                'height': 133
            }
            cls.sprites_cache['player_survivor_strafe_left_6'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_6.png'),
                'width': 130,
                'height': 94
            }
            cls.sprites_cache['player_survivor_strafe_left_7'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_7.png'),
                'width': 130,
                'height': 88
            }
            cls.sprites_cache['player_survivor_strafe_left_5'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_5.png'),
                'width': 130,
                'height': 103
            }
            cls.sprites_cache['player_survivor_strafe_left_4'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_4.png'),
                'width': 130,
                'height': 114
            }
            cls.sprites_cache['player_survivor_strafe_left_16'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_16.png'),
                'width': 130,
                'height': 114
            }
            cls.sprites_cache['player_survivor_strafe_left_17'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_17.png'),
                'width': 130,
                'height': 124
            }
            cls.sprites_cache['player_survivor_strafe_left_15'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_15.png'),
                'width': 130,
                'height': 103
            }
            cls.sprites_cache['player_survivor_strafe_left_14'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_14.png'),
                'width': 130,
                'height': 94
            }
            cls.sprites_cache['player_survivor_strafe_left_10'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_10.png'),
                'width': 130,
                'height': 78
            }
            cls.sprites_cache['player_survivor_strafe_left_11'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_11.png'),
                'width': 130,
                'height': 80
            }
            cls.sprites_cache['player_survivor_strafe_left_13'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_13.png'),
                'width': 130,
                'height': 88
            }
            cls.sprites_cache['player_survivor_strafe_left_12'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_12.png'),
                'width': 130,
                'height': 84
            }
            cls.sprites_cache['player_survivor_strafe_left_19'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_19.png'),
                'width': 130,
                'height': 140
            }
            cls.sprites_cache['player_survivor_strafe_left_18'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_18.png'),
                'width': 130,
                'height': 133
            }
            cls.sprites_cache['player_survivor_strafe_left_9'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_9.png'),
                'width': 130,
                'height': 80
            }
            cls.sprites_cache['player_survivor_strafe_left_8'] = {
                'sheet': SpriteSheet('player/feet/strafe_left/survivor-strafe_left_8.png'),
                'width': 130,
                'height': 84
            }
            cls.sprites_cache['player_survivor_run_0'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_0.png'),
                'width': 176,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_1'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_1.png'),
                'width': 167,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_19'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_19.png'),
                'width': 167,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_3'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_3.png'),
                'width': 126,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_2'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_2.png'),
                'width': 149,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_18'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_18.png'),
                'width': 149,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_6'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_6.png'),
                'width': 104,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_7'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_7.png'),
                'width': 126,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_5'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_5.png'),
                'width': 84,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_4'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_4.png'),
                'width': 105,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_13'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_13.png'),
                'width': 126,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_9'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_9.png'),
                'width': 168,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_8'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_8.png'),
                'width': 149,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_12'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_12.png'),
                'width': 149,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_10'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_10.png'),
                'width': 176,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_11'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_11.png'),
                'width': 168,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_15'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_15.png'),
                'width': 84,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_14'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_14.png'),
                'width': 104,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_16'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_16.png'),
                'width': 105,
                'height': 100
            }
            cls.sprites_cache['player_survivor_run_17'] = {
                'sheet': SpriteSheet('player/feet/run/survivor-run_17.png'),
                'width': 126,
                'height': 100
            }
            cls.sprites_cache['player_survivor_strafe_right_0'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_0.png'),
                'width': 129,
                'height': 147
            }
            cls.sprites_cache['player_survivor_strafe_right_1'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_1.png'),
                'width': 129,
                'height': 143
            }
            cls.sprites_cache['player_survivor_strafe_right_3'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_3.png'),
                'width': 129,
                'height': 126
            }
            cls.sprites_cache['player_survivor_strafe_right_2'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_2.png'),
                'width': 129,
                'height': 135
            }
            cls.sprites_cache['player_survivor_strafe_right_6'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_6.png'),
                'width': 129,
                'height': 91
            }
            cls.sprites_cache['player_survivor_strafe_right_7'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_7.png'),
                'width': 129,
                'height': 82
            }
            cls.sprites_cache['player_survivor_strafe_right_5'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_5.png'),
                'width': 129,
                'height': 103
            }
            cls.sprites_cache['player_survivor_strafe_right_4'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_4.png'),
                'width': 129,
                'height': 114
            }
            cls.sprites_cache['player_survivor_strafe_right_19'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_19.png'),
                'width': 129,
                'height': 143
            }
            cls.sprites_cache['player_survivor_strafe_right_18'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_18.png'),
                'width': 129,
                'height': 135
            }
            cls.sprites_cache['player_survivor_strafe_right_13'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_13.png'),
                'width': 129,
                'height': 82
            }
            cls.sprites_cache['player_survivor_strafe_right_12'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_12.png'),
                'width': 129,
                'height': 78
            }
            cls.sprites_cache['player_survivor_strafe_right_10'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_10.png'),
                'width': 129,
                'height': 70
            }
            cls.sprites_cache['player_survivor_strafe_right_11'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_11.png'),
                'width': 129,
                'height': 72
            }
            cls.sprites_cache['player_survivor_strafe_right_15'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_15.png'),
                'width': 129,
                'height': 103
            }
            cls.sprites_cache['player_survivor_strafe_right_14'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_14.png'),
                'width': 129,
                'height': 91
            }
            cls.sprites_cache['player_survivor_strafe_right_16'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_16.png'),
                'width': 129,
                'height': 114
            }
            cls.sprites_cache['player_survivor_strafe_right_17'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_17.png'),
                'width': 129,
                'height': 126
            }
            cls.sprites_cache['player_survivor_strafe_right_9'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_9.png'),
                'width': 129,
                'height': 72
            }
            cls.sprites_cache['player_survivor_strafe_right_8'] = {
                'sheet': SpriteSheet('player/feet/strafe_right/survivor-strafe_right_8.png'),
                'width': 129,
                'height': 78
            }
            cls.sprites_cache['player_bullet'] = {
                'sheet': SpriteSheet('player/bullet/bullet.png'),
                'width': 208,
                'height': 546
            }
            cls.sprites_cache['player_survivor_move_flashlight_19'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_19.png'),
                'width': 268,
                'height': 166
            }
            cls.sprites_cache['player_survivor_move_flashlight_6'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_6.png'),
                'width': 268,
                'height': 168
            }
            cls.sprites_cache['player_survivor_move_flashlight_7'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_7.png'),
                'width': 270,
                'height': 169
            }
            cls.sprites_cache['player_survivor_move_flashlight_18'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_18.png'),
                'width': 268,
                'height': 168
            }
            cls.sprites_cache['player_survivor_move_flashlight_5'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_5.png'),
                'width': 268,
                'height': 167
            }
            cls.sprites_cache['player_survivor_move_flashlight_4'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_4.png'),
                'width': 268,
                'height': 167
            }
            cls.sprites_cache['player_survivor_move_flashlight_0'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_0.png'),
                'width': 267,
                'height': 166
            }
            cls.sprites_cache['player_survivor_move_flashlight_1'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_1.png'),
                'width': 268,
                'height': 166
            }
            cls.sprites_cache['player_survivor_move_flashlight_3'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_3.png'),
                'width': 268,
                'height': 167
            }
            cls.sprites_cache['player_survivor_move_flashlight_2'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_2.png'),
                'width': 268,
                'height': 167
            }
            cls.sprites_cache['player_survivor_move_flashlight_10'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_10.png'),
                'width': 272,
                'height': 174
            }
            cls.sprites_cache['player_survivor_move_flashlight_11'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_11.png'),
                'width': 272,
                'height': 173
            }
            cls.sprites_cache['player_survivor_move_flashlight_13'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_13.png'),
                'width': 270,
                'height': 172
            }
            cls.sprites_cache['player_survivor_move_flashlight_12'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_12.png'),
                'width': 271,
                'height': 173
            }
            cls.sprites_cache['player_survivor_move_flashlight_16'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_16.png'),
                'width': 268,
                'height': 168
            }
            cls.sprites_cache['player_survivor_move_flashlight_9'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_9.png'),
                'width': 272,
                'height': 172
            }
            cls.sprites_cache['player_survivor_move_flashlight_8'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_8.png'),
                'width': 271,
                'height': 171
            }
            cls.sprites_cache['player_survivor_move_flashlight_17'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_17.png'),
                'width': 268,
                'height': 168
            }
            cls.sprites_cache['player_survivor_move_flashlight_15'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_15.png'),
                'width': 268,
                'height': 169
            }
            cls.sprites_cache['player_survivor_move_flashlight_14'] = {
                'sheet': SpriteSheet('player/flashlight/move/survivor-move_flashlight_14.png'),
                'width': 268,
                'height': 170
            }
            cls.sprites_cache['player_survivor_idle_flashlight_0'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_0.png'),
                'width': 266,
                'height': 165
            }
            cls.sprites_cache['player_survivor_idle_flashlight_1'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_1.png'),
                'width': 266,
                'height': 165
            }
            cls.sprites_cache['player_survivor_idle_flashlight_3'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_3.png'),
                'width': 266,
                'height': 166
            }
            cls.sprites_cache['player_survivor_idle_flashlight_2'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_2.png'),
                'width': 266,
                'height': 165
            }
            cls.sprites_cache['player_survivor_idle_flashlight_6'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_6.png'),
                'width': 266,
                'height': 167
            }
            cls.sprites_cache['player_survivor_idle_flashlight_7'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_7.png'),
                'width': 265,
                'height': 167
            }
            cls.sprites_cache['player_survivor_idle_flashlight_5'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_5.png'),
                'width': 266,
                'height': 166
            }
            cls.sprites_cache['player_survivor_idle_flashlight_4'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_4.png'),
                'width': 265,
                'height': 166
            }
            cls.sprites_cache['player_survivor_idle_flashlight_18'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_18.png'),
                'width': 266,
                'height': 165
            }
            cls.sprites_cache['player_survivor_idle_flashlight_19'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_19.png'),
                'width': 266,
                'height': 165
            }
            cls.sprites_cache['player_survivor_idle_flashlight_12'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_12.png'),
                'width': 266,
                'height': 167
            }
            cls.sprites_cache['player_survivor_idle_flashlight_13'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_13.png'),
                'width': 265,
                'height': 167
            }
            cls.sprites_cache['player_survivor_idle_flashlight_11'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_11.png'),
                'width': 266,
                'height': 168
            }
            cls.sprites_cache['player_survivor_idle_flashlight_10'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_10.png'),
                'width': 266,
                'height': 168
            }
            cls.sprites_cache['player_survivor_idle_flashlight_14'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_14.png'),
                'width': 266,
                'height': 167
            }
            cls.sprites_cache['player_survivor_idle_flashlight_15'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_15.png'),
                'width': 266,
                'height': 166
            }
            cls.sprites_cache['player_survivor_idle_flashlight_17'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_17.png'),
                'width': 266,
                'height': 166
            }
            cls.sprites_cache['player_survivor_idle_flashlight_16'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_16.png'),
                'width': 265,
                'height': 166
            }
            cls.sprites_cache['player_survivor_idle_flashlight_9'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_9.png'),
                'width': 266,
                'height': 168
            }
            cls.sprites_cache['player_survivor_idle_flashlight_8'] = {
                'sheet': SpriteSheet('player/flashlight/idle/survivor-idle_flashlight_8.png'),
                'width': 266,
                'height': 167
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_9'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_9.png'),
                'width': 226,
                'height': 158
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_8'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_8.png'),
                'width': 241,
                'height': 157
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_5'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_5.png'),
                'width': 280,
                'height': 159
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_4'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_4.png'),
                'width': 278,
                'height': 160
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_6'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_6.png'),
                'width': 249,
                'height': 191
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_14'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_14.png'),
                'width': 265,
                'height': 170
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_7'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_7.png'),
                'width': 247,
                'height': 155
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_3'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_3.png'),
                'width': 274,
                'height': 162
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_11'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_11.png'),
                'width': 216,
                'height': 160
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_10'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_10.png'),
                'width': 211,
                'height': 159
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_2'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_2.png'),
                'width': 271,
                'height': 164
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_0'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_0.png'),
                'width': 266,
                'height': 165
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_12'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_12.png'),
                'width': 227,
                'height': 175
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_13'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_13.png'),
                'width': 254,
                'height': 176
            }
            cls.sprites_cache['player_survivor_meleeattack_flashlight_1'] = {
                'sheet': SpriteSheet('player/flashlight/meleeattack/survivor-meleeattack_flashlight_1.png'),
                'width': 268,
                'height': 164
            }
            cls.sprites_cache['player_survivor_move_knife_18'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_18.png'),
                'width': 218,
                'height': 168
            }
            cls.sprites_cache['player_survivor_move_knife_19'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_19.png'),
                'width': 216,
                'height': 169
            }
            cls.sprites_cache['player_survivor_move_knife_9'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_9.png'),
                'width': 232,
                'height': 174
            }
            cls.sprites_cache['player_survivor_move_knife_8'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_8.png'),
                'width': 230,
                'height': 172
            }
            cls.sprites_cache['player_survivor_move_knife_12'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_12.png'),
                'width': 230,
                'height': 172
            }
            cls.sprites_cache['player_survivor_move_knife_6'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_6.png'),
                'width': 227,
                'height': 170
            }
            cls.sprites_cache['player_survivor_move_knife_7'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_7.png'),
                'width': 229,
                'height': 172
            }
            cls.sprites_cache['player_survivor_move_knife_13'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_13.png'),
                'width': 229,
                'height': 172
            }
            cls.sprites_cache['player_survivor_move_knife_11'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_11.png'),
                'width': 232,
                'height': 174
            }
            cls.sprites_cache['player_survivor_move_knife_5'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_5.png'),
                'width': 224,
                'height': 169
            }
            cls.sprites_cache['player_survivor_move_knife_4'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_4.png'),
                'width': 222,
                'height': 167
            }
            cls.sprites_cache['player_survivor_move_knife_10'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_10.png'),
                'width': 232,
                'height': 174
            }
            cls.sprites_cache['player_survivor_move_knife_14'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_14.png'),
                'width': 227,
                'height': 170
            }
            cls.sprites_cache['player_survivor_move_knife_0'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_0.png'),
                'width': 215,
                'height': 169
            }
            cls.sprites_cache['player_survivor_move_knife_1'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_1.png'),
                'width': 215,
                'height': 169
            }
            cls.sprites_cache['player_survivor_move_knife_15'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_15.png'),
                'width': 225,
                'height': 169
            }
            cls.sprites_cache['player_survivor_move_knife_17'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_17.png'),
                'width': 221,
                'height': 168
            }
            cls.sprites_cache['player_survivor_move_knife_3'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_3.png'),
                'width': 220,
                'height': 168
            }
            cls.sprites_cache['player_survivor_move_knife_2'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_2.png'),
                'width': 217,
                'height': 168
            }
            cls.sprites_cache['player_survivor_move_knife_16'] = {
                'sheet': SpriteSheet('player/knife/move/survivor-move_knife_16.png'),
                'width': 222,
                'height': 167
            }
            cls.sprites_cache['player_survivor_idle_knife_18'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_18.png'),
                'width': 232,
                'height': 170
            }
            cls.sprites_cache['player_survivor_idle_knife_19'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_19.png'),
                'width': 231,
                'height': 169
            }
            cls.sprites_cache['player_survivor_idle_knife_8'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_8.png'),
                'width': 235,
                'height': 172
            }
            cls.sprites_cache['player_survivor_idle_knife_9'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_9.png'),
                'width': 235,
                'height': 174
            }
            cls.sprites_cache['player_survivor_idle_knife_2'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_2.png'),
                'width': 232,
                'height': 170
            }
            cls.sprites_cache['player_survivor_idle_knife_3'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_3.png'),
                'width': 232,
                'height': 170
            }
            cls.sprites_cache['player_survivor_idle_knife_1'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_1.png'),
                'width': 231,
                'height': 169
            }
            cls.sprites_cache['player_survivor_idle_knife_0'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_0.png'),
                'width': 231,
                'height': 169
            }
            cls.sprites_cache['player_survivor_idle_knife_4'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_4.png'),
                'width': 233,
                'height': 171
            }
            cls.sprites_cache['player_survivor_idle_knife_5'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_5.png'),
                'width': 233,
                'height': 172
            }
            cls.sprites_cache['player_survivor_idle_knife_7'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_7.png'),
                'width': 235,
                'height': 172
            }
            cls.sprites_cache['player_survivor_idle_knife_6'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_6.png'),
                'width': 234,
                'height': 172
            }
            cls.sprites_cache['player_survivor_idle_knife_11'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_11.png'),
                'width': 235,
                'height': 174
            }
            cls.sprites_cache['player_survivor_idle_knife_10'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_10.png'),
                'width': 235,
                'height': 174
            }
            cls.sprites_cache['player_survivor_idle_knife_12'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_12.png'),
                'width': 235,
                'height': 172
            }
            cls.sprites_cache['player_survivor_idle_knife_13'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_13.png'),
                'width': 235,
                'height': 172
            }
            cls.sprites_cache['player_survivor_idle_knife_17'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_17.png'),
                'width': 232,
                'height': 170
            }
            cls.sprites_cache['player_survivor_idle_knife_16'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_16.png'),
                'width': 233,
                'height': 171
            }
            cls.sprites_cache['player_survivor_idle_knife_14'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_14.png'),
                'width': 234,
                'height': 172
            }
            cls.sprites_cache['player_survivor_idle_knife_15'] = {
                'sheet': SpriteSheet('player/knife/idle/survivor-idle_knife_15.png'),
                'width': 233,
                'height': 172
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_8'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_8.png'),
                'width': 240,
                'height': 229
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_9'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_9.png'),
                'width': 214,
                'height': 266
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_4'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_4.png'),
                'width': 174,
                'height': 182
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_10'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_10.png'),
                'width': 221,
                'height': 254
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_11'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_11.png'),
                'width': 231,
                'height': 225
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_5'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_5.png'),
                'width': 171,
                'height': 177
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_7'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_7.png'),
                'width': 262,
                'height': 169
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_13'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_13.png'),
                'width': 246,
                'height': 178
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_12'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_12.png'),
                'width': 242,
                'height': 188
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_6'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_6.png'),
                'width': 207,
                'height': 176
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_2'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_2.png'),
                'width': 191,
                'height': 169
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_3'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_3.png'),
                'width': 184,
                'height': 175
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_1'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_1.png'),
                'width': 221,
                'height': 170
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_14'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_14.png'),
                'width': 238,
                'height': 170
            }
            cls.sprites_cache['player_survivor_meleeattack_knife_0'] = {
                'sheet': SpriteSheet('player/knife/meleeattack/survivor-meleeattack_knife_0.png'),
                'width': 231,
                'height': 169
            }
            print(f"✓ {len(cls.sprites_cache)} sprites chargés")
    
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
# 'apocalypse_2_tires_grass_bleak_yellow' - 16x16px - apocalypse/Objects/2-Tires_Grass_Bleak-Yellow.png
# 'apocalypse_2_tires_grass_dark_green' - 16x16px - apocalypse/Objects/2-Tires_Grass_Dark-Green.png
# 'apocalypse_2_tires_grass_green' - 16x16px - apocalypse/Objects/2-Tires_Grass_Green.png
# 'apocalypse_air_vent_1' - 13x9px - apocalypse/Objects/Buildings/Air-vent_1.png
# 'apocalypse_air_vent_2_rusty' - 13x9px - apocalypse/Objects/Buildings/Air-vent_2_rusty.png
# 'apocalypse_air_vent_3' - 9x12px - apocalypse/Objects/Buildings/Air-vent_3.png
# 'apocalypse_air_vent_4_rusty' - 9x12px - apocalypse/Objects/Buildings/Air-vent_4_rusty.png
# 'apocalypse_ammo_crate_blue' - 9x7px - apocalypse/Objects/Pickable/Ammo-crate_Blue.png
# 'apocalypse_ammo_crate_green' - 9x7px - apocalypse/Objects/Pickable/Ammo-crate_Green.png
# 'apocalypse_ammo_crate_red' - 9x7px - apocalypse/Objects/Pickable/Ammo-crate_Red.png
# 'apocalypse_antenna_1' - 14x15px - apocalypse/Objects/Buildings/Antenna_1.png
# 'apocalypse_antenna_2' - 14x14px - apocalypse/Objects/Buildings/Antenna_2.png
# 'apocalypse_awning_blue_1' - 32x16px - apocalypse/Objects/Buildings/Awning_blue_1.png
# 'apocalypse_awning_blue_2' - 48x16px - apocalypse/Objects/Buildings/Awning_blue_2.png
# 'apocalypse_awning_blue_3' - 64x16px - apocalypse/Objects/Buildings/Awning_blue_3.png
# 'apocalypse_awning_blue_4' - 80x16px - apocalypse/Objects/Buildings/Awning_blue_4.png
# 'apocalypse_awning_blue_5' - 96x16px - apocalypse/Objects/Buildings/Awning_blue_5.png
# 'apocalypse_awning_orange_1' - 32x16px - apocalypse/Objects/Buildings/Awning_orange_1.png
# 'apocalypse_awning_orange_2' - 48x16px - apocalypse/Objects/Buildings/Awning_orange_2.png
# 'apocalypse_awning_orange_3' - 64x16px - apocalypse/Objects/Buildings/Awning_orange_3.png
# 'apocalypse_awning_orange_4' - 80x16px - apocalypse/Objects/Buildings/Awning_orange_4.png
# 'apocalypse_awning_orange_5' - 96x16px - apocalypse/Objects/Buildings/Awning_orange_5.png
# 'apocalypse_axe_down_landed' - 3x10px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Down_Landed.png
# 'apocalypse_axe_down_landing_sheet5' - 58x18px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Down_Landing-Sheet5.png
# 'apocalypse_axe_side_landed' - 13x9px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side_Landed.png
# 'apocalypse_axe_side_landing_sheet5' - 87x16px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side_Landing-Sheet5.png
# 'apocalypse_axe_side_left_landed' - 13x9px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side-left_Landed.png
# 'apocalypse_axe_side_left_landing_sheet5' - 95x16px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side-left_Landing-Sheet5.png
# 'apocalypse_axe_side_left_thrown_sheet9' - 126x14px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side-left_Thrown-Sheet9.png
# 'apocalypse_axe_side_thrown_sheet9' - 126x14px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Side_Thrown-Sheet9.png
# 'apocalypse_axe_up_landed' - 3x9px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Up_Landed.png
# 'apocalypse_axe_up_landing_sheet5' - 58x15px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Up_Landing-Sheet5.png
# 'apocalypse_axe_vertical_thrown_sheet9' - 27x16px - apocalypse/Enemies/Zombie_Axe/Axe/Axe_Vertical_Thrown-Sheet9.png
# 'apocalypse_background_bleak_yellow_tileset' - 384x272px - apocalypse/Tiles/Background_Bleak-Yellow_TileSet.png
# 'apocalypse_background_dark_green_tileset' - 384x272px - apocalypse/Tiles/Background_Dark-Green_TileSet.png
# 'apocalypse_background_green_tileset' - 384x272px - apocalypse/Tiles/Background_Green_TileSet.png
# 'apocalypse_balcony_1_left' - 40x32px - apocalypse/Objects/Buildings/Balcony_1_Left.png
# 'apocalypse_balcony_2_right' - 40x32px - apocalypse/Objects/Buildings/Balcony_2_Right.png
# 'apocalypse_balcony_3_left_ladder_hole' - 40x32px - apocalypse/Objects/Buildings/Balcony_3_Left_Ladder-hole.png
# 'apocalypse_balcony_4_right_ladder_hole' - 40x32px - apocalypse/Objects/Buildings/Balcony_4_Right_Ladder-hole.png
# 'apocalypse_bandage' - 5x7px - apocalypse/Objects/Pickable/Bandage.png
# 'apocalypse_barrel_blue_1' - 12x16px - apocalypse/Objects/Barrel_blue_1.png
# 'apocalypse_barrel_blue_2' - 15x10px - apocalypse/Objects/Barrel_blue_2.png
# 'apocalypse_barrel_red_1' - 12x16px - apocalypse/Objects/Barrel_red_1.png
# 'apocalypse_barrel_red_2' - 15x10px - apocalypse/Objects/Barrel_red_2.png
# 'apocalypse_barrel_rust_blue_1' - 12x16px - apocalypse/Objects/Barrel_rust_blue_1.png
# 'apocalypse_barrel_rust_blue_2' - 15x10px - apocalypse/Objects/Barrel_rust_blue_2.png
# 'apocalypse_barrel_rust_red_1' - 12x16px - apocalypse/Objects/Barrel_rust_red_1.png
# 'apocalypse_barrel_rust_red_2' - 15x10px - apocalypse/Objects/Barrel_rust_red_2.png
# 'apocalypse_bat' - 11x12px - apocalypse/Objects/Pickable/Bat.png
# 'apocalypse_bat_down_attack_sheet4' - 78x25px - apocalypse/Character/Bat/Bat_down_attack-Sheet4.png
# 'apocalypse_bat_down_idle_and_run_sheet6' - 102x11px - apocalypse/Character/Bat/Bat_down_idle-and-run-Sheet6.png
# 'apocalypse_bat_side_attack_sheet4' - 105x16px - apocalypse/Character/Bat/Bat_side_attack-Sheet4.png
# 'apocalypse_bat_side_death_sheet6' - 106x13px - apocalypse/Character/Bat/Bat_side_Death-Sheet6.png
# 'apocalypse_bat_side_idle_and_run_sheet6' - 96x13px - apocalypse/Character/Bat/Bat_side_idle-and-run-Sheet6.png
# 'apocalypse_bat_side_left_attack_sheet4' - 112x16px - apocalypse/Character/Bat/Bat_side-left_attack-Sheet4.png
# 'apocalypse_bat_side_left_death_sheet6' - 108x13px - apocalypse/Character/Bat/Bat_side-left_Death-Sheet6.png
# 'apocalypse_bat_side_left_idle_and_run_sheet6' - 96x13px - apocalypse/Character/Bat/Bat_side-left_idle-and-run-Sheet6.png
# 'apocalypse_bat_up_attack_sheet4' - 77x25px - apocalypse/Character/Bat/Bat_up_attack-Sheet4.png
# 'apocalypse_bat_up_idle_and_run_sheet6' - 96x14px - apocalypse/Character/Bat/Bat_up_idle-and-run-Sheet6.png
# 'apocalypse_bench_1_down' - 32x15px - apocalypse/Objects/Bench_1_down.png
# 'apocalypse_bench_2_down_overgrown_bleak_yellow' - 32x15px - apocalypse/Objects/Bench_2_down_Overgrown_Bleak-Yellow.png
# 'apocalypse_bench_2_down_overgrown_dark_green' - 32x15px - apocalypse/Objects/Bench_2_down_Overgrown_Dark-Green.png
# 'apocalypse_bench_2_down_overgrown_green' - 32x15px - apocalypse/Objects/Bench_2_down_Overgrown_Green.png
# 'apocalypse_bench_3_side' - 11x28px - apocalypse/Objects/Bench_3_side.png
# 'apocalypse_bench_4_side_overgrown_bleak_yellow' - 13x28px - apocalypse/Objects/Bench_4_side_Overgrown_Bleak-Yellow.png
# 'apocalypse_bench_4_side_overgrown_dark_green' - 13x28px - apocalypse/Objects/Bench_4_side_Overgrown_Dark-Green.png
# 'apocalypse_bench_4_side_overgrown_green' - 13x28px - apocalypse/Objects/Bench_4_side_Overgrown_Green.png
# 'apocalypse_bench_5_up' - 32x13px - apocalypse/Objects/Bench_5_up.png
# 'apocalypse_bench_6_up_overgrown_bleak_yellow' - 32x14px - apocalypse/Objects/Bench_6_up_Overgrown_Bleak-Yellow.png
# 'apocalypse_bench_6_up_overgrown_dark_green' - 32x14px - apocalypse/Objects/Bench_6_up_Overgrown_Dark-Green.png
# 'apocalypse_bench_6_up_overgrown_green' - 32x14px - apocalypse/Objects/Bench_6_up_Overgrown_Green.png
# 'apocalypse_blank_not_pressed' - 76x21px - apocalypse/UI/Menu/Main Menu/Blank_Not-Pressed.png
# 'apocalypse_blank_pressed' - 76x19px - apocalypse/UI/Menu/Main Menu/Blank_Pressed.png
# 'apocalypse_brick_wall_1_lying' - 13x12px - apocalypse/Objects/Buildings/Brick-wall_1_Lying.png
# 'apocalypse_brick_wall_2_lying' - 11x7px - apocalypse/Objects/Buildings/Brick-wall_2_Lying.png
# 'apocalypse_brick_wall_tileset' - 96x48px - apocalypse/Tiles/Brick-Wall_TileSet.png
# 'apocalypse_buildings_beige_tileset' - 208x208px - apocalypse/Tiles/Buildings/Buildings_beige_TileSet.png
# 'apocalypse_buildings_dark_tileset' - 208x208px - apocalypse/Tiles/Buildings/Buildings_dark_TileSet.png
# 'apocalypse_buildings_gray_tileset' - 208x208px - apocalypse/Tiles/Buildings/Buildings_gray_TileSet.png
# 'apocalypse_buildings_white_tileset' - 208x208px - apocalypse/Tiles/Buildings/Buildings_white_TileSet.png
# 'apocalypse_bullet_box_1_blue' - 6x4px - apocalypse/Objects/Pickable/Bullet-box_1_Blue.png
# 'apocalypse_bullet_box_1_green' - 6x4px - apocalypse/Objects/Pickable/Bullet-box_1_Green.png
# 'apocalypse_bullet_box_1_red' - 6x4px - apocalypse/Objects/Pickable/Bullet-box_1_Red.png
# 'apocalypse_bush_1_bleak_yellow' - 15x13px - apocalypse/Objects/Nature/Bleak-Yellow/Bush_1_Bleak-Yellow.png
# 'apocalypse_bush_1_dark_green' - 15x13px - apocalypse/Objects/Nature/Dark-Green/Bush_1_Dark-Green.png
# 'apocalypse_bush_1_green' - 15x13px - apocalypse/Objects/Nature/Green/Bush_1_Green.png
# 'apocalypse_bush_1_orange' - 15x13px - apocalypse/Objects/Nature/Orange/Bush_1_Orange.png
# 'apocalypse_bush_1_red' - 15x13px - apocalypse/Objects/Nature/Red/Bush_1_Red.png
# 'apocalypse_bush_1_yellow' - 15x13px - apocalypse/Objects/Nature/Yellow/Bush_1_Yellow.png
# 'apocalypse_bush_2_bleak_yellow' - 28x13px - apocalypse/Objects/Nature/Bleak-Yellow/Bush_2_Bleak-Yellow.png
# 'apocalypse_bush_2_dark_green' - 28x13px - apocalypse/Objects/Nature/Dark-Green/Bush_2_Dark-Green.png
# 'apocalypse_bush_2_green' - 28x13px - apocalypse/Objects/Nature/Green/Bush_2_Green.png
# 'apocalypse_bush_2_orange' - 28x13px - apocalypse/Objects/Nature/Orange/Bush_2_Orange.png
# 'apocalypse_bush_2_red' - 28x13px - apocalypse/Objects/Nature/Red/Bush_2_Red.png
# 'apocalypse_bush_2_yellow' - 28x13px - apocalypse/Objects/Nature/Yellow/Bush_2_Yellow.png
# 'apocalypse_button_no_not_pressed' - 9x9px - apocalypse/UI/Menu/Button_No_Not-Pressed.png
# 'apocalypse_button_no_pressed' - 9x8px - apocalypse/UI/Menu/Button_No_Pressed.png
# 'apocalypse_button_no_sheet2' - 18x9px - apocalypse/UI/Menu/Button_No-Sheet2.png
# 'apocalypse_button_yes_not_pressed' - 10x9px - apocalypse/UI/Menu/Button_Yes_Not-Pressed.png
# 'apocalypse_button_yes_pressed' - 10x8px - apocalypse/UI/Menu/Button_Yes_Pressed.png
# 'apocalypse_button_yes_sheet2' - 20x9px - apocalypse/UI/Menu/Button_Yes-Sheet2.png
# 'apocalypse_canned_food' - 7x7px - apocalypse/Objects/Pickable/Canned-food.png
# 'apocalypse_canned_soup' - 5x7px - apocalypse/Objects/Pickable/Canned-soup.png
# 'apocalypse_car_1_blue' - 25x37px - apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Blue.png
# 'apocalypse_car_1_gray' - 25x37px - apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Gray.png
# 'apocalypse_car_1_green' - 25x37px - apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Green.png
# 'apocalypse_car_1_orange' - 25x37px - apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Orange.png
# 'apocalypse_car_1_overgrown_bleak_yellow_blue' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Blue.png
# 'apocalypse_car_1_overgrown_bleak_yellow_gray' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Gray.png
# 'apocalypse_car_1_overgrown_bleak_yellow_green' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Green.png
# 'apocalypse_car_1_overgrown_bleak_yellow_orange' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Orange.png
# 'apocalypse_car_1_overgrown_bleak_yellow_red' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Red.png
# 'apocalypse_car_1_overgrown_bleak_yellow_yellow' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Bleak-Yellow/Car_1_Overgrown_Bleak-Yellow_Yellow.png
# 'apocalypse_car_1_overgrown_dark_green_blue' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Blue.png
# 'apocalypse_car_1_overgrown_dark_green_gray' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Gray.png
# 'apocalypse_car_1_overgrown_dark_green_green' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Green.png
# 'apocalypse_car_1_overgrown_dark_green_orange' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Orange.png
# 'apocalypse_car_1_overgrown_dark_green_red' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Red.png
# 'apocalypse_car_1_overgrown_dark_green_yellow' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Dark-Green/Car_1_Overgrown_Dark-Green_Yellow.png
# 'apocalypse_car_1_overgrown_green_blue' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Blue.png
# 'apocalypse_car_1_overgrown_green_gray' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Gray.png
# 'apocalypse_car_1_overgrown_green_green' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Green.png
# 'apocalypse_car_1_overgrown_green_orange' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Orange.png
# 'apocalypse_car_1_overgrown_green_red' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Red.png
# 'apocalypse_car_1_overgrown_green_yellow' - 25x40px - apocalypse/Objects/Vehicles/Overgrown/Car_1_Overgrown/Green/Car_1_Overgrown_Green_Yellow.png
# 'apocalypse_car_1_red' - 25x37px - apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Red.png
# 'apocalypse_car_1_rust_blue' - 25x37px - apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Blue.png
# 'apocalypse_car_1_rust_dark_blue' - 25x37px - apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Dark-Blue.png
# 'apocalypse_car_1_rust_green' - 25x37px - apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Green.png
# 'apocalypse_car_1_rust_orange' - 25x37px - apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Orange.png
# 'apocalypse_car_1_rust_red' - 25x37px - apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Red.png
# 'apocalypse_car_1_rust_yellow' - 25x37px - apocalypse/Objects/Vehicles/Rust/Car_1_Rust/Car_1_Rust_Yellow.png
# 'apocalypse_car_1_yellow' - 25x37px - apocalypse/Objects/Vehicles/Normal/Car_1/Car_1_Yellow.png
# 'apocalypse_car_2_blue_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Blue_Upsidedown.png
# 'apocalypse_car_2_gray_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Gray_Upsidedown.png
# 'apocalypse_car_2_green_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Green_Upsidedown.png
# 'apocalypse_car_2_orange_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Orange_Upsidedown.png
# 'apocalypse_car_2_overgrown_bleak_yellow_blue_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Blue_Upsidedown.png
# 'apocalypse_car_2_overgrown_bleak_yellow_gray_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Gray_Upsidedown.png
# 'apocalypse_car_2_overgrown_bleak_yellow_green_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Green_Upsidedown.png
# 'apocalypse_car_2_overgrown_bleak_yellow_orange_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Orange_Upsidedown.png
# 'apocalypse_car_2_overgrown_bleak_yellow_red_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Red_Upsidedown.png
# 'apocalypse_car_2_overgrown_bleak_yellow_yellow_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Bleak-Yellow/Car_2_Overgrown_Bleak-Yellow_Yellow_Upsidedown.png
# 'apocalypse_car_2_overgrown_dark_green_blue_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Blue_Upsidedown.png
# 'apocalypse_car_2_overgrown_dark_green_gray_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Gray_Upsidedown.png
# 'apocalypse_car_2_overgrown_dark_green_green_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Green_Upsidedown.png
# 'apocalypse_car_2_overgrown_dark_green_orange_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Orange_Upsidedown.png
# 'apocalypse_car_2_overgrown_dark_green_red_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Red_Upsidedown.png
# 'apocalypse_car_2_overgrown_dark_green_yellow_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Dark-Green/Car_2_Overgrown_Dark-Green_Yellow_Upsidedown.png
# 'apocalypse_car_2_overgrown_green_blue_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Blue_Upsidedown.png
# 'apocalypse_car_2_overgrown_green_gray_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Gray_Upsidedown.png
# 'apocalypse_car_2_overgrown_green_green_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Green_Upsidedown.png
# 'apocalypse_car_2_overgrown_green_orange_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Orange_Upsidedown.png
# 'apocalypse_car_2_overgrown_green_red_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Red_Upsidedown.png
# 'apocalypse_car_2_overgrown_green_yellow_upsidedown' - 27x39px - apocalypse/Objects/Vehicles/Overgrown/Car_2_Overgrown_Upsidedown/Green/Car_2_Overgrown_Green_Yellow_Upsidedown.png
# 'apocalypse_car_2_red_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Red_Upsidedown.png
# 'apocalypse_car_2_rust_blue_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Blue_Upsidedown.png
# 'apocalypse_car_2_rust_dark_blue_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Dark-Blue_Upsidedown.png
# 'apocalypse_car_2_rust_green_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Green_Upsidedown.png
# 'apocalypse_car_2_rust_orange_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Orange_Upsidedown.png
# 'apocalypse_car_2_rust_red_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Red_Upsidedown.png
# 'apocalypse_car_2_rust_yellow_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Rust/Car_2_Rust_Upsidedown/Car_2_Rust_Yellow_Upsidedown.png
# 'apocalypse_car_2_yellow_upsidedown' - 27x37px - apocalypse/Objects/Vehicles/Normal/Car_2_Upsidedown/Car_2_Yellow_Upsidedown.png
# 'apocalypse_car_3_blue_van' - 43x27px - apocalypse/Objects/Vehicles/Normal/Car_3_Van/Car_3_Blue_Van.png
# 'apocalypse_car_3_light_green_van' - 43x27px - apocalypse/Objects/Vehicles/Normal/Car_3_Van/Car_3_Light-Green_Van.png
# 'apocalypse_car_3_overgrown_bleak_yellow_blue_van' - 42x28px - apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Bleak-Yellow/Car_3_Overgrown_Bleak-Yellow_Blue_Van.png
# 'apocalypse_car_3_overgrown_bleak_yellow_light_green_van' - 42x28px - apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Bleak-Yellow/Car_3_Overgrown_Bleak-Yellow_Light-Green_Van.png
# 'apocalypse_car_3_overgrown_dark_green_blue_van' - 42x28px - apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Dark-Green/Car_3_Overgrown_Dark-Green_Blue_Van.png
# 'apocalypse_car_3_overgrown_dark_green_light_green_van' - 42x28px - apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Dark-Green/Car_3_Overgrown_Dark-Green_Light-Green_Van.png
# 'apocalypse_car_3_overgrown_green_blue_van' - 42x28px - apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Green/Car_3_Overgrown_Green_Blue_Van.png
# 'apocalypse_car_3_overgrown_green_light_green_van' - 42x28px - apocalypse/Objects/Vehicles/Overgrown/Car_3_Overgrown_Van/Green/Car_3_Overgrown_Green_Light-Green_Van.png
# 'apocalypse_car_3_rust_blue_van' - 43x27px - apocalypse/Objects/Vehicles/Rust/Car_3_Rust_Van/Car_3_Rust_Blue_Van.png
# 'apocalypse_car_3_rust_light_green_van' - 43x27px - apocalypse/Objects/Vehicles/Rust/Car_3_Rust_Van/Car_3_Rust_Light-Green_Van.png
# 'apocalypse_car_4_blue' - 38x19px - apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Blue.png
# 'apocalypse_car_4_gray' - 38x19px - apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Gray.png
# 'apocalypse_car_4_green' - 38x19px - apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Green.png
# 'apocalypse_car_4_orange' - 38x19px - apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Orange.png
# 'apocalypse_car_4_overgrown_bleak_yellow_blue' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Blue.png
# 'apocalypse_car_4_overgrown_bleak_yellow_gray' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Gray.png
# 'apocalypse_car_4_overgrown_bleak_yellow_green' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Green.png
# 'apocalypse_car_4_overgrown_bleak_yellow_orange' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Orange.png
# 'apocalypse_car_4_overgrown_bleak_yellow_red' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Red.png
# 'apocalypse_car_4_overgrown_bleak_yellow_yellow' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Bleak-Yellow/Car_4_Overgrown_Bleak-Yellow_Yellow.png
# 'apocalypse_car_4_overgrown_dark_green_blue' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Blue.png
# 'apocalypse_car_4_overgrown_dark_green_gray' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Gray.png
# 'apocalypse_car_4_overgrown_dark_green_green' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Green.png
# 'apocalypse_car_4_overgrown_dark_green_orange' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Orange.png
# 'apocalypse_car_4_overgrown_dark_green_red' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Red.png
# 'apocalypse_car_4_overgrown_dark_green_yellow' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Dark-Green/Car_4_Overgrown_Dark-Green_Yellow.png
# 'apocalypse_car_4_overgrown_green_blue' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Blue.png
# 'apocalypse_car_4_overgrown_green_gray' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Gray.png
# 'apocalypse_car_4_overgrown_green_green' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Green.png
# 'apocalypse_car_4_overgrown_green_orange' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Orange.png
# 'apocalypse_car_4_overgrown_green_red' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Red.png
# 'apocalypse_car_4_overgrown_green_yellow' - 42x22px - apocalypse/Objects/Vehicles/Overgrown/Car_4_Overgrown/Green/Car_4_Overgrown_Green_Yellow.png
# 'apocalypse_car_4_red' - 38x19px - apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Red.png
# 'apocalypse_car_4_rust_blue' - 38x19px - apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Blue.png
# 'apocalypse_car_4_rust_dark_blue' - 38x19px - apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Dark-Blue.png
# 'apocalypse_car_4_rust_green' - 38x19px - apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Green.png
# 'apocalypse_car_4_rust_orange' - 38x19px - apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Orange.png
# 'apocalypse_car_4_rust_red' - 38x19px - apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Red.png
# 'apocalypse_car_4_rust_yellow' - 38x19px - apocalypse/Objects/Vehicles/Rust/Car_4_Rust/Car_4_Rust_Yellow.png
# 'apocalypse_car_4_yellow' - 38x19px - apocalypse/Objects/Vehicles/Normal/Car_4/Car_4_Yellow.png
# 'apocalypse_car_5_overgrown_bleak_yellow_tractor_side' - 42x30px - apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Bleak-Yellow/Car_5_Overgrown_Bleak-Yellow_Tractor_Side.png
# 'apocalypse_car_5_overgrown_bleak_yellow_tractor_up' - 27x35px - apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Bleak-Yellow/Car_5_Overgrown_Bleak-Yellow_Tractor_Up.png
# 'apocalypse_car_5_overgrown_dark_green_tractor_side' - 42x30px - apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Dark-Green/Car_5_Overgrown_Dark-Green_Tractor_Side.png
# 'apocalypse_car_5_overgrown_dark_green_tractor_up' - 27x35px - apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Dark-Green/Car_5_Overgrown_Dark-Green_Tractor_Up.png
# 'apocalypse_car_5_overgrown_green_tractor_side' - 42x30px - apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Green/Car_5_Overgrown_Green_Tractor_Side.png
# 'apocalypse_car_5_overgrown_green_tractor_up' - 27x35px - apocalypse/Objects/Vehicles/Overgrown/Car_5_Overgrown_Tractor/Green/Car_5_Overgrown_Green_Tractor_Up.png
# 'apocalypse_car_5_rust_tractor_side' - 41x30px - apocalypse/Objects/Vehicles/Rust/Car_5_Rust_Tractor/Car_5_Rust_Tractor_Side.png
# 'apocalypse_car_5_rust_tractor_up' - 23x35px - apocalypse/Objects/Vehicles/Rust/Car_5_Rust_Tractor/Car_5_Rust_Tractor_Up.png
# 'apocalypse_car_6_blue_scrap' - 39x20px - apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Blue_Scrap.png
# 'apocalypse_car_6_gray_scrap' - 39x20px - apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Gray_Scrap.png
# 'apocalypse_car_6_green_scrap' - 39x20px - apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Green_Scrap.png
# 'apocalypse_car_6_orange_scrap' - 39x20px - apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Orange_Scrap.png
# 'apocalypse_car_6_overgrown_bleak_yellow_blue_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Blue_Scrap.png
# 'apocalypse_car_6_overgrown_bleak_yellow_gray_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Gray_Scrap.png
# 'apocalypse_car_6_overgrown_bleak_yellow_green_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Green_Scrap.png
# 'apocalypse_car_6_overgrown_bleak_yellow_orange_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Orange_Scrap.png
# 'apocalypse_car_6_overgrown_bleak_yellow_red_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Red_Scrap.png
# 'apocalypse_car_6_overgrown_bleak_yellow_yellow_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Bleak-Yellow/Car_6_Overgrown_Bleak-Yellow_Yellow_Scrap.png
# 'apocalypse_car_6_overgrown_dark_green_blue_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Blue_Scrap.png
# 'apocalypse_car_6_overgrown_dark_green_gray_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Gray_Scrap.png
# 'apocalypse_car_6_overgrown_dark_green_green_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Green_Scrap.png
# 'apocalypse_car_6_overgrown_dark_green_orange_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Orange_Scrap.png
# 'apocalypse_car_6_overgrown_dark_green_red_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Red_Scrap.png
# 'apocalypse_car_6_overgrown_dark_green_yellow_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Dark-Green/Car_6_Overgrown_Dark-Green_Yellow_Scrap.png
# 'apocalypse_car_6_overgrown_green_blue_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Blue_Scrap.png
# 'apocalypse_car_6_overgrown_green_dark_blue_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Dark-Blue_Scrap.png
# 'apocalypse_car_6_overgrown_green_green_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Green_Scrap.png
# 'apocalypse_car_6_overgrown_green_orange_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Orange_Scrap.png
# 'apocalypse_car_6_overgrown_green_red_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Red_Scrap.png
# 'apocalypse_car_6_overgrown_green_yellow_scrap' - 39x20px - apocalypse/Objects/Vehicles/Overgrown/Car_6_Overgrown_Scrap/Green/Car_6_Overgrown_Green_Yellow_Scrap.png
# 'apocalypse_car_6_red_scrap' - 39x20px - apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Red_Scrap.png
# 'apocalypse_car_6_rust_blue_scrap' - 39x20px - apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Blue_Scrap.png
# 'apocalypse_car_6_rust_dark_blue_scrap' - 39x20px - apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Dark-Blue_Scrap.png
# 'apocalypse_car_6_rust_green_scrap' - 39x20px - apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Green_Scrap.png
# 'apocalypse_car_6_rust_orange_scrap' - 39x20px - apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Orange_Scrap.png
# 'apocalypse_car_6_rust_red_scrap' - 39x20px - apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Red_Scrap.png
# 'apocalypse_car_6_rust_yellow_scrap' - 39x20px - apocalypse/Objects/Vehicles/Rust/Car_6_Rust_Scrap/Car_6_Rust_Yellow_Scrap.png
# 'apocalypse_car_6_yellow_scrap' - 39x20px - apocalypse/Objects/Vehicles/Normal/Car_6_Scrap/Car_6_Yellow_Scrap.png
# 'apocalypse_car_7_blue_truck' - 59x58px - apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Blue_Truck.png
# 'apocalypse_car_7_gray_truck' - 59x58px - apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Gray_Truck.png
# 'apocalypse_car_7_green_truck' - 59x58px - apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Green_Truck.png
# 'apocalypse_car_7_orange_truck' - 59x58px - apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Orange_Truck.png
# 'apocalypse_car_7_overgrown_bleak_yellow_blue_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Blue_Truck.png
# 'apocalypse_car_7_overgrown_bleak_yellow_gray_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Gray_Truck.png
# 'apocalypse_car_7_overgrown_bleak_yellow_green_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Green_Truck.png
# 'apocalypse_car_7_overgrown_bleak_yellow_orange_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Orange_Truck.png
# 'apocalypse_car_7_overgrown_bleak_yellow_red_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Red_Truck.png
# 'apocalypse_car_7_overgrown_bleak_yellow_yellow_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Bleak-Yellow/Car_7_Overgrown_Bleak-Yellow_Yellow_Truck.png
# 'apocalypse_car_7_overgrown_dark_green_blue_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Blue_Truck.png
# 'apocalypse_car_7_overgrown_dark_green_gray_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Gray_Truck.png
# 'apocalypse_car_7_overgrown_dark_green_green_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Green_Truck.png
# 'apocalypse_car_7_overgrown_dark_green_orange_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Orange_Truck.png
# 'apocalypse_car_7_overgrown_dark_green_red_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Red_Truck.png
# 'apocalypse_car_7_overgrown_dark_green_yellow_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Dark-Green/Car_7_Overgrown_Dark-Green_Yellow_Truck.png
# 'apocalypse_car_7_overgrown_green_blue_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Blue_Truck.png
# 'apocalypse_car_7_overgrown_green_dark_blue_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Dark-Blue_Truck.png
# 'apocalypse_car_7_overgrown_green_green_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Green_Truck.png
# 'apocalypse_car_7_overgrown_green_orange_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Orange_Truck.png
# 'apocalypse_car_7_overgrown_green_red_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Red_Truck.png
# 'apocalypse_car_7_overgrown_green_yellow_truck' - 59x59px - apocalypse/Objects/Vehicles/Overgrown/Car_7_Overgrown_Truck/Green/Car_7_Overgrown_Green_Yellow_Truck.png
# 'apocalypse_car_7_red_truck' - 59x58px - apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Red_Truck.png
# 'apocalypse_car_7_rust_blue_truck_' - 59x58px - apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Blue_Truck_.png
# 'apocalypse_car_7_rust_dark_blue_truck_' - 59x58px - apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Dark-Blue_Truck_.png
# 'apocalypse_car_7_rust_green_truck_' - 59x58px - apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Green_Truck_.png
# 'apocalypse_car_7_rust_orange_truck_' - 59x58px - apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Orange_Truck_.png
# 'apocalypse_car_7_rust_red_truck_' - 59x58px - apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Red_Truck_.png
# 'apocalypse_car_7_rust_yellow_truck_' - 59x58px - apocalypse/Objects/Vehicles/Rust/Car_7_Rust_Truck/Car_7_Rust_Yellow_Truck_.png
# 'apocalypse_car_7_yellow_truck' - 59x58px - apocalypse/Objects/Vehicles/Normal/Car_7_Truck/Car_7_Yellow_Truck.png
# 'apocalypse_car_8_blue_bus' - 61x31px - apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Blue_Bus.png
# 'apocalypse_car_8_green_bus' - 61x31px - apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Green_Bus.png
# 'apocalypse_car_8_light_green_bus' - 61x31px - apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Light-Green_Bus.png
# 'apocalypse_car_8_orange_bus' - 61x31px - apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Orange_Bus.png
# 'apocalypse_car_8_overgrown_bleak_yellow_blue_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Blue_Bus.png
# 'apocalypse_car_8_overgrown_bleak_yellow_green_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Green_Bus.png
# 'apocalypse_car_8_overgrown_bleak_yellow_light_green_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Light-Green_Bus.png
# 'apocalypse_car_8_overgrown_bleak_yellow_orange_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Orange_Bus.png
# 'apocalypse_car_8_overgrown_bleak_yellow_red_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Red_Bus.png
# 'apocalypse_car_8_overgrown_bleak_yellow_yellow_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Bleak-Yellow/Car_8_Overgrown_Bleak-Yellow_Yellow_Bus.png
# 'apocalypse_car_8_overgrown_dark_green_blue_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Blue_Bus.png
# 'apocalypse_car_8_overgrown_dark_green_green_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Green_Bus.png
# 'apocalypse_car_8_overgrown_dark_green_light_green_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Light-Green_Bus.png
# 'apocalypse_car_8_overgrown_dark_green_orange_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Orange_Bus.png
# 'apocalypse_car_8_overgrown_dark_green_red_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Red_Bus.png
# 'apocalypse_car_8_overgrown_dark_green_yellow_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Dark-Green/Car_8_Overgrown_Dark-Green_Yellow_Bus.png
# 'apocalypse_car_8_overgrown_green_blue_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Blue_Bus.png
# 'apocalypse_car_8_overgrown_green_green_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Green_Bus.png
# 'apocalypse_car_8_overgrown_green_light_green_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Light-Green_Bus.png
# 'apocalypse_car_8_overgrown_green_orange_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Orange_Bus.png
# 'apocalypse_car_8_overgrown_green_red_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Red_Bus.png
# 'apocalypse_car_8_overgrown_green_yellow_bus' - 64x32px - apocalypse/Objects/Vehicles/Overgrown/Car_8_Overgrown_Bus/Green/Car_8_Overgrown_Green_Yellow_Bus.png
# 'apocalypse_car_8_red_bus' - 61x31px - apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Red_Bus.png
# 'apocalypse_car_8_rust_blue_bus' - 61x31px - apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Blue_Bus.png
# 'apocalypse_car_8_rust_green_bus' - 61x31px - apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Green_Bus.png
# 'apocalypse_car_8_rust_light_green_bus' - 61x31px - apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Light-Green_Bus.png
# 'apocalypse_car_8_rust_orange_bus' - 61x31px - apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Orange_Bus.png
# 'apocalypse_car_8_rust_red_bus' - 61x31px - apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Red_Bus.png
# 'apocalypse_car_8_rust_yellow_bus' - 61x31px - apocalypse/Objects/Vehicles/Rust/Car_8_Rust_Bus/Car_8_Rust_Yellow_Bus.png
# 'apocalypse_car_8_yellow_bus' - 61x31px - apocalypse/Objects/Vehicles/Normal/Car_8_Bus/Car_8_Yellow_Bus.png
# 'apocalypse_car_9_blue_motorcycle_side' - 23x16px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Blue_Motorcycle_Side.png
# 'apocalypse_car_9_blue_motorcycle_up' - 9x21px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Blue_Motorcycle_Up.png
# 'apocalypse_car_9_gray_motorcycle_side' - 23x16px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Gray_Motorcycle_Side.png
# 'apocalypse_car_9_gray_motorcycle_up' - 9x21px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Gray_Motorcycle_Up.png
# 'apocalypse_car_9_green_motorcycle_side' - 23x16px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Green_Motorcycle_Side.png
# 'apocalypse_car_9_green_motorcycle_up' - 9x21px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Green_Motorcycle_Up.png
# 'apocalypse_car_9_orange_motorcycle_side' - 23x16px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Orange_Motorcycle_Side.png
# 'apocalypse_car_9_orange_motorcycle_up' - 9x21px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Orange_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_bleak_yellow_blue_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Blue_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_bleak_yellow_blue_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Blue_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_bleak_yellow_gray_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Gray_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_bleak_yellow_gray_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Gray_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_bleak_yellow_green_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Green_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_bleak_yellow_green_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Green_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_bleak_yellow_orange_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Orange_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_bleak_yellow_orange_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Orange_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_bleak_yellow_red_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Red_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_bleak_yellow_red_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Red_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_bleak_yellow_yellow_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Yellow_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_bleak_yellow_yellow_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Bleak-Yellow/Car_9_Overgrown_Bleak-Yellow_Yellow_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_dark_green_blue_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Blue_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_dark_green_blue_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Blue_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_dark_green_gray_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Gray_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_dark_green_gray_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Gray_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_dark_green_green_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Green_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_dark_green_green_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Green_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_dark_green_orange_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Orange_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_dark_green_orange_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Orange_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_dark_green_red_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Red_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_dark_green_red_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Red_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_dark_green_yellow_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Yellow_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_dark_green_yellow_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Dark-Green/Car_9_Overgrown_Dark-Green_Yellow_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_green_blue_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Blue_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_green_blue_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Blue_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_green_gray_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Gray_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_green_gray_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Gray_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_green_green_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Green_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_green_green_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Green_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_green_orange_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Orange_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_green_orange_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Orange_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_green_red_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Red_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_green_red_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Red_Motorcycle_Up.png
# 'apocalypse_car_9_overgrown_green_yellow_motorcycle_side' - 24x17px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Yellow_Motorcycle_Side.png
# 'apocalypse_car_9_overgrown_green_yellow_motorcycle_up' - 10x22px - apocalypse/Objects/Vehicles/Overgrown/Car_9_Motorcycle/Green/Car_9_Overgrown_Green_Yellow_Motorcycle_Up.png
# 'apocalypse_car_9_red_motorcycle_side' - 23x16px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Red_Motorcycle_Side.png
# 'apocalypse_car_9_red_motorcycle_up' - 9x21px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Red_Motorcycle_Up.png
# 'apocalypse_car_9_yellow_motorcycle_side' - 23x16px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Yellow_Motorcycle_Side.png
# 'apocalypse_car_9_yellow_motorcycle_up' - 9x21px - apocalypse/Objects/Vehicles/Normal/Car_9_Motorcycle/Car_9_Yellow_Motorcycle_Up.png
# 'apocalypse_cardboard_1' - 11x9px - apocalypse/Objects/Cardboard_1.png
# 'apocalypse_cardboard_2' - 12x10px - apocalypse/Objects/Cardboard_2.png
# 'apocalypse_character_down_idle_no_hands_sheet6' - 66x16px - apocalypse/Character/Main/Idle/Character_down_idle_no-hands-Sheet6.png
# 'apocalypse_character_down_idle_sheet6' - 78x16px - apocalypse/Character/Main/Idle/Character_down_idle-Sheet6.png
# 'apocalypse_character_down_pick_up_nohands_sheet3' - 33x16px - apocalypse/Character/Main/Pick-up/Character_down_Pick-up_NoHands-Sheet3.png
# 'apocalypse_character_down_pick_up_sheet3' - 36x16px - apocalypse/Character/Main/Pick-up/Character_down_Pick-up-Sheet3.png
# 'apocalypse_character_down_punch_no_hands_sheet4' - 44x17px - apocalypse/Character/Main/Punch/Character_down_punch_no-hands-Sheet4.png
# 'apocalypse_character_down_punch_sheet4' - 48x18px - apocalypse/Character/Main/Punch/Character_down_punch-Sheet4.png
# 'apocalypse_character_down_run_no_hands_sheet6' - 66x17px - apocalypse/Character/Main/Run/Character_down_run_no-hands-Sheet6.png
# 'apocalypse_character_down_run_sheet6' - 77x17px - apocalypse/Character/Main/Run/Character_down_run-Sheet6.png
# 'apocalypse_character_side_death1_nohands_sheet6' - 124x16px - apocalypse/Character/Main/Death/Character_side_death1_NoHands-Sheet6.png
# 'apocalypse_character_side_death1_sheet6' - 126x16px - apocalypse/Character/Main/Death/Character_side_death1-Sheet6.png
# 'apocalypse_character_side_death2_nohands_sheet6' - 146x16px - apocalypse/Character/Main/Death/Character_side_death2_NoHands-Sheet6.png
# 'apocalypse_character_side_death2_sheet6' - 147x16px - apocalypse/Character/Main/Death/Character_side_death2-Sheet6.png
# 'apocalypse_character_side_death3_nohands_sheet6' - 145x16px - apocalypse/Character/Main/Death/Character_side_death3_NoHands-Sheet6.png
# 'apocalypse_character_side_death3_sheet6' - 147x16px - apocalypse/Character/Main/Death/Character_side_death3-Sheet6.png
# 'apocalypse_character_side_idle_no_hands_sheet6' - 60x16px - apocalypse/Character/Main/Idle/Character_side_idle_no-hands-Sheet6.png
# 'apocalypse_character_side_idle_sheet6' - 72x16px - apocalypse/Character/Main/Idle/Character_side_idle-Sheet6.png
# 'apocalypse_character_side_left_death1_nohands_sheet6' - 126x16px - apocalypse/Character/Main/Death/Character_side-left_death1_NoHands-Sheet6.png
# 'apocalypse_character_side_left_death1_sheet6' - 126x16px - apocalypse/Character/Main/Death/Character_side-left_death1-Sheet6.png
# 'apocalypse_character_side_left_death2_nohands_sheet7' - 147x16px - apocalypse/Character/Main/Death/Character_side-left_death2_NoHands-Sheet7.png
# 'apocalypse_character_side_left_death2_sheet7' - 147x16px - apocalypse/Character/Main/Death/Character_side-left_death2-Sheet7.png
# 'apocalypse_character_side_left_death3_nohands_sheet7' - 147x16px - apocalypse/Character/Main/Death/Character_side-left_death3_NoHands-Sheet7.png
# 'apocalypse_character_side_left_death3_sheet7' - 147x16px - apocalypse/Character/Main/Death/Character_side-left_death3-Sheet7.png
# 'apocalypse_character_side_left_idle_no_hands_sheet6' - 60x16px - apocalypse/Character/Main/Idle/Character_side-left_idle_no-hands-Sheet6.png
# 'apocalypse_character_side_left_idle_sheet6' - 72x16px - apocalypse/Character/Main/Idle/Character_side-left_idle-Sheet6.png
# 'apocalypse_character_side_left_pick_up_nohands_sheet3' - 30x16px - apocalypse/Character/Main/Pick-up/Character_side-left_Pick-up_NoHands-Sheet3.png
# 'apocalypse_character_side_left_pick_up_sheet3' - 33x16px - apocalypse/Character/Main/Pick-up/Character_side-left_Pick-up-Sheet3.png
# 'apocalypse_character_side_left_punch_no_hands_sheet4' - 52x16px - apocalypse/Character/Main/Punch/Character_side-left_punch_no-hands-Sheet4.png
# 'apocalypse_character_side_left_punch_sheet4' - 80x18px - apocalypse/Character/Main/Punch/Character_side-left_punch-Sheet4.png
# 'apocalypse_character_side_left_run_no_hands_sheet6' - 60x17px - apocalypse/Character/Main/Run/Character_side-left_run_no-hands-Sheet6.png
# 'apocalypse_character_side_left_run_sheet6' - 84x17px - apocalypse/Character/Main/Run/Character_side-left_run-Sheet6.png
# 'apocalypse_character_side_pick_up_nohands_sheet3' - 30x16px - apocalypse/Character/Main/Pick-up/Character_side_Pick-up_NoHands-Sheet3.png
# 'apocalypse_character_side_pick_up_sheet3' - 33x16px - apocalypse/Character/Main/Pick-up/Character_side_Pick-up-Sheet3.png
# 'apocalypse_character_side_punch_no_hands_sheet4' - 50x16px - apocalypse/Character/Main/Punch/Character_side_punch_no-hands-Sheet4.png
# 'apocalypse_character_side_punch_sheet4' - 73x16px - apocalypse/Character/Main/Punch/Character_side_punch-Sheet4.png
# 'apocalypse_character_side_run_no_hands_sheet6' - 60x17px - apocalypse/Character/Main/Run/Character_side_run_no-hands-Sheet6.png
# 'apocalypse_character_side_run_sheet6' - 81x17px - apocalypse/Character/Main/Run/Character_side_run-Sheet6.png
# 'apocalypse_character_up_idle_no_hands_sheet6' - 66x16px - apocalypse/Character/Main/Idle/Character_up_idle_no-hands-Sheet6.png
# 'apocalypse_character_up_idle_sheet6' - 66x16px - apocalypse/Character/Main/Idle/Character_up_idle-Sheet6.png
# 'apocalypse_character_up_pick_up_nohands_sheet3' - 33x15px - apocalypse/Character/Main/Pick-up/Character_up_Pick-up_NoHands-Sheet3.png
# 'apocalypse_character_up_pick_up_sheet3' - 33x15px - apocalypse/Character/Main/Pick-up/Character_up_Pick-up-Sheet3.png
# 'apocalypse_character_up_punch_no_hands_sheet4' - 44x17px - apocalypse/Character/Main/Punch/Character_up_punch_no-hands-Sheet4.png
# 'apocalypse_character_up_punch_sheet4' - 48x17px - apocalypse/Character/Main/Punch/Character_up_punch-Sheet4.png
# 'apocalypse_character_up_run_no_hands_sheet6' - 66x17px - apocalypse/Character/Main/Run/Character_up_run_no-hands-Sheet6.png
# 'apocalypse_character_up_run_sheet6' - 77x17px - apocalypse/Character/Main/Run/Character_up_run-Sheet6.png
# 'apocalypse_checkmark' - 7x5px - apocalypse/UI/Menu/Checkmark.png
# 'apocalypse_checkmark_body' - 7x7px - apocalypse/UI/Menu/Checkmark-Body.png
# 'apocalypse_checkmark_sheet5' - 35x5px - apocalypse/UI/Menu/Checkmark-Sheet5.png
# 'apocalypse_chips_pack_red' - 10x10px - apocalypse/Objects/Chips-pack_Red.png
# 'apocalypse_chips_pack_yellow' - 11x11px - apocalypse/Objects/Chips-pack_Yellow.png
# 'apocalypse_container_10_green_vertical_overgrown_bleak_yellow' - 29x46px - apocalypse/Objects/Container/Container_10_Green_Vertical_Overgrown_Bleak-Yellow.png
# 'apocalypse_container_10_green_vertical_overgrown_dark_green' - 29x46px - apocalypse/Objects/Container/Container_10_Green_Vertical_Overgrown_Dark-Green.png
# 'apocalypse_container_10_green_vertical_overgrown_green' - 29x46px - apocalypse/Objects/Container/Container_10_Green_Vertical_Overgrown_Green.png
# 'apocalypse_container_11_green_horizontal' - 41x26px - apocalypse/Objects/Container/Container_11_Green_Horizontal.png
# 'apocalypse_container_12_green_horizontal_overgrown_bleak_yellow' - 41x29px - apocalypse/Objects/Container/Container_12_Green_Horizontal_Overgrown_Bleak-Yellow.png
# 'apocalypse_container_12_green_horizontal_overgrown_dark_green' - 41x29px - apocalypse/Objects/Container/Container_12_Green_Horizontal_Overgrown_Dark-Green.png
# 'apocalypse_container_12_green_horizontal_overgrown_green' - 41x29px - apocalypse/Objects/Container/Container_12_Green_Horizontal_Overgrown_Green.png
# 'apocalypse_container_1_gray_vertical' - 24x43px - apocalypse/Objects/Container/Container_1_Gray_Vertical.png
# 'apocalypse_container_2_gray_vertical_overgrown_bleak_yellow' - 29x46px - apocalypse/Objects/Container/Container_2_Gray_Vertical_Overgrown_Bleak-Yellow.png
# 'apocalypse_container_2_gray_vertical_overgrown_dark_green' - 29x46px - apocalypse/Objects/Container/Container_2_Gray_Vertical_Overgrown_Dark-Green.png
# 'apocalypse_container_2_gray_vertical_overgrown_green' - 29x46px - apocalypse/Objects/Container/Container_2_Gray_Vertical_Overgrown_Green.png
# 'apocalypse_container_3_gray_horizontal' - 41x26px - apocalypse/Objects/Container/Container_3_Gray_Horizontal.png
# 'apocalypse_container_4_gray_horizontal_overgrown_bleak_yellow' - 41x29px - apocalypse/Objects/Container/Container_4_Gray_Horizontal_Overgrown_Bleak-Yellow.png
# 'apocalypse_container_4_gray_horizontal_overgrown_dark_green' - 41x29px - apocalypse/Objects/Container/Container_4_Gray_Horizontal_Overgrown_Dark-Green.png
# 'apocalypse_container_4_gray_horizontal_overgrown_green' - 41x29px - apocalypse/Objects/Container/Container_4_Gray_Horizontal_Overgrown_Green.png
# 'apocalypse_container_5_red_vertical' - 24x43px - apocalypse/Objects/Container/Container_5_Red_Vertical.png
# 'apocalypse_container_6_red_vertical_overgrown_bleak_yellow' - 29x46px - apocalypse/Objects/Container/Container_6_Red_Vertical_Overgrown_Bleak-Yellow.png
# 'apocalypse_container_6_red_vertical_overgrown_dark_green' - 29x46px - apocalypse/Objects/Container/Container_6_Red_Vertical_Overgrown_Dark-Green.png
# 'apocalypse_container_6_red_vertical_overgrown_green' - 29x46px - apocalypse/Objects/Container/Container_6_Red_Vertical_Overgrown_Green.png
# 'apocalypse_container_7_red_horizontal' - 41x26px - apocalypse/Objects/Container/Container_7_Red_Horizontal.png
# 'apocalypse_container_8_red_horizontal_overgrown_bleak_yellow' - 41x29px - apocalypse/Objects/Container/Container_8_Red_Horizontal_Overgrown_Bleak-Yellow.png
# 'apocalypse_container_8_red_horizontal_overgrown_dark_green' - 41x29px - apocalypse/Objects/Container/Container_8_Red_Horizontal_Overgrown_Dark-Green.png
# 'apocalypse_container_8_red_horizontal_overgrown_green' - 41x29px - apocalypse/Objects/Container/Container_8_Red_Horizontal_Overgrown_Green.png
# 'apocalypse_container_9_green_vertical' - 24x43px - apocalypse/Objects/Container/Container_9_Green_Vertical.png
# 'apocalypse_crafting_1_1' - 47x22px - apocalypse/UI/Crafting/Crafting_1_1.png
# 'apocalypse_crafting_1_2' - 70x22px - apocalypse/UI/Crafting/Crafting_1_2.png
# 'apocalypse_crafting_2_1' - 49x22px - apocalypse/UI/Crafting/Crafting_2_1.png
# 'apocalypse_crafting_2_2' - 72x22px - apocalypse/UI/Crafting/Crafting_2_2.png
# 'apocalypse_crafting_arrow' - 7x11px - apocalypse/UI/Crafting/Crafting_Arrow.png
# 'apocalypse_crafting_cell' - 21x22px - apocalypse/UI/Crafting/Crafting-cell.png
# 'apocalypse_crafting_equal' - 9x8px - apocalypse/UI/Crafting/Crafting_Equal.png
# 'apocalypse_crafting_main_menu' - 85x91px - apocalypse/UI/Crafting/Crafting-main-menu.png
# 'apocalypse_crafting_plus' - 10x11px - apocalypse/UI/Crafting/Crafting_Plus.png
# 'apocalypse_crafting_scrollbox' - 4x28px - apocalypse/UI/Crafting/Crafting_Scrollbox.png
# 'apocalypse_cursor' - 7x8px - apocalypse/UI/Menu/Cursor.png
# 'apocalypse_destroyed_wall_corner' - 14x13px - apocalypse/Objects/Buildings/Destroyed-wall_corner.png
# 'apocalypse_destroyed_wall_not_corner' - 16x14px - apocalypse/Objects/Buildings/Destroyed-wall_not-corner.png
# 'apocalypse_door_1_beige' - 16x25px - apocalypse/Objects/Buildings/Door_1_Beige.png
# 'apocalypse_door_2_ajar_beige' - 16x27px - apocalypse/Objects/Buildings/Door_2_Ajar_Beige.png
# 'apocalypse_door_3_boarded_up_beige' - 16x25px - apocalypse/Objects/Buildings/Door_3_Boarded-up_Beige.png
# 'apocalypse_door_4_metal' - 16x25px - apocalypse/Objects/Buildings/Door_4_Metal.png
# 'apocalypse_door_5_rusty_metal' - 16x25px - apocalypse/Objects/Buildings/Door_5_Rusty_Metal.png
# 'apocalypse_door_6_boarded_up_metal' - 16x25px - apocalypse/Objects/Buildings/Door_6_Boarded-up_Metal.png
# 'apocalypse_downspout_rainwater1' - 10x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Downspout_Rainwater/Downspout_Rainwater1.png
# 'apocalypse_downspout_rainwater2' - 6x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Downspout_Rainwater/Downspout_Rainwater2.png
# 'apocalypse_downspout_rainwater3' - 8x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Downspout_Rainwater/Downspout_Rainwater3.png
# 'apocalypse_downspout_rainwater_sheet3' - 29x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Downspout_Rainwater-Sheet3.png
# 'apocalypse_duct_1_side' - 9x10px - apocalypse/Objects/Buildings/Duct_1_side.png
# 'apocalypse_duct_2_down' - 9x8px - apocalypse/Objects/Buildings/Duct_2_down.png
# 'apocalypse_duct_3_up' - 9x10px - apocalypse/Objects/Buildings/Duct_3_up.png
# 'apocalypse_enterance_bleak_yellow' - 31x27px - apocalypse/Objects/Buildings/Enterance_Bleak-Yellow.png
# 'apocalypse_enterance_dark_green' - 31x27px - apocalypse/Objects/Buildings/Enterance_Dark-Green.png
# 'apocalypse_enterance_green' - 31x27px - apocalypse/Objects/Buildings/Enterance_Green.png
# 'apocalypse_exhaust_pipe' - 5x11px - apocalypse/Objects/Exhaust-pipe.png
# 'apocalypse_fire_down_sheet3' - 20x10px - apocalypse/Character/Guns/Fire/Fire_Down-Sheet3.png
# 'apocalypse_fire_side_left_sheet3' - 30x7px - apocalypse/Character/Guns/Fire/Fire_side-left-Sheet3.png
# 'apocalypse_fire_side_sheet3' - 30x7px - apocalypse/Character/Guns/Fire/Fire_side-Sheet3.png
# 'apocalypse_fire_up_sheet3' - 20x10px - apocalypse/Character/Guns/Fire/Fire_Up-Sheet3.png
# 'apocalypse_flower_1_blue' - 7x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_1_blue.png
# 'apocalypse_flower_1_purple' - 7x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_1_purple.png
# 'apocalypse_flower_1_red' - 7x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_1_red.png
# 'apocalypse_flower_1_yellow' - 7x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_1_yellow.png
# 'apocalypse_flower_2_blue' - 8x11px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_2_blue.png
# 'apocalypse_flower_2_purple' - 8x11px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_2_purple.png
# 'apocalypse_flower_2_red' - 8x11px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_2_red.png
# 'apocalypse_flower_2_yellow' - 8x11px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flower_2_yellow.png
# 'apocalypse_flowers_1_blue' - 14x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_1_blue.png
# 'apocalypse_flowers_1_purple' - 14x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_1_purple.png
# 'apocalypse_flowers_1_red' - 14x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_1_red.png
# 'apocalypse_flowers_1_yellow' - 14x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_1_yellow.png
# 'apocalypse_flowers_2_blue' - 16x14px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_2_blue.png
# 'apocalypse_flowers_2_purple' - 16x14px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_2_purple.png
# 'apocalypse_flowers_2_red' - 16x14px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_2_red.png
# 'apocalypse_flowers_2_yellow' - 16x14px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_2_yellow.png
# 'apocalypse_flowers_3_blue' - 9x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_3_blue.png
# 'apocalypse_flowers_3_purple' - 9x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_3_purple.png
# 'apocalypse_flowers_3_red' - 9x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_3_red.png
# 'apocalypse_flowers_3_yellow' - 9x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Flowers_3_yellow.png
# 'apocalypse_garbage_bin_1' - 29x23px - apocalypse/Objects/Garbage-Bin_1.png
# 'apocalypse_garbage_bin_2' - 27x20px - apocalypse/Objects/Garbage-Bin_2.png
# 'apocalypse_garbage_bin_3' - 20x28px - apocalypse/Objects/Garbage-Bin_3.png
# 'apocalypse_garbage_bin_4' - 16x27px - apocalypse/Objects/Garbage-Bin_4.png
# 'apocalypse_garbage_tileset' - 128x64px - apocalypse/Tiles/Garbage_TileSet.png
# 'apocalypse_grass_1_bleak_yellow' - 7x5px - apocalypse/Objects/Nature/Bleak-Yellow/Grass_1_Bleak-Yellow.png
# 'apocalypse_grass_1_dark_green' - 7x5px - apocalypse/Objects/Nature/Dark-Green/Grass_1_Dark-Green.png
# 'apocalypse_grass_1_green' - 7x5px - apocalypse/Objects/Nature/Green/Grass_1_Green.png
# 'apocalypse_grass_2_bleak_yellow' - 12x10px - apocalypse/Objects/Nature/Bleak-Yellow/Grass_2_Bleak-Yellow.png
# 'apocalypse_grass_2_dark_green' - 12x10px - apocalypse/Objects/Nature/Dark-Green/Grass_2_Dark-Green.png
# 'apocalypse_grass_2_green' - 12x10px - apocalypse/Objects/Nature/Green/Grass_2_Green.png
# 'apocalypse_grass_3_bleak_yellow' - 16x15px - apocalypse/Objects/Nature/Bleak-Yellow/Grass_3_Bleak-Yellow.png
# 'apocalypse_grass_3_dark_green' - 16x15px - apocalypse/Objects/Nature/Dark-Green/Grass_3_Dark-Green.png
# 'apocalypse_grass_3_green' - 16x15px - apocalypse/Objects/Nature/Green/Grass_3_Green.png
# 'apocalypse_grass_3_stepping_on_animation_bleak_yellow_sheet2' - 32x15px - apocalypse/Objects/Nature/Bleak-Yellow/Grass_3_Stepping-On-Animation_Bleak-Yellow-Sheet2.png
# 'apocalypse_grass_3_stepping_on_animation_dark_green_sheet2' - 32x15px - apocalypse/Objects/Nature/Dark-Green/Grass_3_Stepping-On-Animation_Dark-Green-Sheet2.png
# 'apocalypse_grass_3_stepping_on_animation_green_sheet2' - 32x15px - apocalypse/Objects/Nature/Green/Grass_3_Stepping-On-Animation_Green-Sheet2.png
# 'apocalypse_grass_4_bleak_yellow' - 16x11px - apocalypse/Objects/Nature/Bleak-Yellow/Grass_4_Bleak-Yellow.png
# 'apocalypse_grass_4_dark_green' - 16x11px - apocalypse/Objects/Nature/Dark-Green/Grass_4_Dark-Green.png
# 'apocalypse_grass_4_green' - 16x11px - apocalypse/Objects/Nature/Green/Grass_4_Green.png
# 'apocalypse_grass_4_stepping_on_animation_bleak_yellow_sheet2' - 32x11px - apocalypse/Objects/Nature/Bleak-Yellow/Grass_4_Stepping-On-Animation_Bleak-Yellow-Sheet2.png
# 'apocalypse_grass_4_stepping_on_animation_dark_green_sheet2' - 32x11px - apocalypse/Objects/Nature/Dark-Green/Grass_4_Stepping-On-Animation_Dark-Green-Sheet2.png
# 'apocalypse_grass_4_stepping_on_animation_green_sheet2' - 32x11px - apocalypse/Objects/Nature/Green/Grass_4_Stepping-On-Animation_Green-Sheet2.png
# 'apocalypse_grass_5_bleak_yellow' - 16x14px - apocalypse/Objects/Nature/Bleak-Yellow/Grass_5_Bleak-Yellow.png
# 'apocalypse_grass_5_dark_green' - 16x14px - apocalypse/Objects/Nature/Dark-Green/Grass_5_Dark-Green.png
# 'apocalypse_grass_5_green' - 16x14px - apocalypse/Objects/Nature/Green/Grass_5_Green.png
# 'apocalypse_grass_5_stepping_on_animation_bleak_yellow_sheet2' - 32x14px - apocalypse/Objects/Nature/Bleak-Yellow/Grass_5_Stepping-On-Animation_Bleak-Yellow-Sheet2.png
# 'apocalypse_grass_5_stepping_on_animation_dark_green_sheet2' - 32x14px - apocalypse/Objects/Nature/Dark-Green/Grass_5_Stepping-On-Animation_Dark-Green-Sheet2.png
# 'apocalypse_grass_5_stepping_on_animation_green_sheet2' - 32x14px - apocalypse/Objects/Nature/Green/Grass_5_Stepping-On-Animation_Green-Sheet2.png
# 'apocalypse_grass_on_top_tileset' - 122x91px - apocalypse/Tiles/Grass_On-Top_TileSet.png
# 'apocalypse_gray_brick' - 8x10px - apocalypse/Objects/Gray-brick.png
# 'apocalypse_gray_brick_debris' - 17x15px - apocalypse/Objects/Gray-brick_Debris.png
# 'apocalypse_gun' - 16x8px - apocalypse/Objects/Pickable/Gun.png
# 'apocalypse_gun_bullet' - 7x25px - apocalypse/UI/Bullet Indicators/Gun-Bullet.png
# 'apocalypse_gun_bullet_bullet' - 2x1px - apocalypse/Character/Guns/Bullets/Gun-bullet_Bullet.png
# 'apocalypse_gun_bullet_casing' - 2x1px - apocalypse/Character/Guns/Bullets/Gun-bullet_Casing.png
# 'apocalypse_gun_bullet_empty' - 7x25px - apocalypse/UI/Bullet Indicators/Gun-Bullet_Empty.png
# 'apocalypse_gun_bullet_small' - 5x16px - apocalypse/UI/Bullet Indicators/Small/Gun-Bullet_Small.png
# 'apocalypse_gun_bullet_small_empty' - 5x16px - apocalypse/UI/Bullet Indicators/Small/Gun-Bullet_Small_Empty.png
# 'apocalypse_gun_bullet_whole' - 4x1px - apocalypse/Character/Guns/Bullets/Gun-bullet_Whole.png
# 'apocalypse_gun_down_idle_and_run_sheet6' - 30x16px - apocalypse/Character/Guns/Gun/Gun_down_idle-and-run-Sheet6.png
# 'apocalypse_gun_down_reload_sheet8' - 120x15px - apocalypse/Character/Guns/Gun/Gun_down_reload-Sheet8.png
# 'apocalypse_gun_down_shoot_sheet3' - 15x17px - apocalypse/Character/Guns/Gun/Gun_down_shoot-Sheet3.png
# 'apocalypse_gun_side_death_sheet6' - 107x10px - apocalypse/Character/Guns/Gun/Gun_side_Death-Sheet6.png
# 'apocalypse_gun_side_idle_and_run_sheet6' - 96x10px - apocalypse/Character/Guns/Gun/Gun_side_idle-and-run-Sheet6.png
# 'apocalypse_gun_side_left_death_sheet6' - 108x10px - apocalypse/Character/Guns/Gun/Gun_side-left_Death-Sheet6.png
# 'apocalypse_gun_side_left_idle_and_run_sheet6' - 96x10px - apocalypse/Character/Guns/Gun/Gun_side-left_idle-and-run-Sheet6.png
# 'apocalypse_gun_side_left_reload_sheet8' - 160x11px - apocalypse/Character/Guns/Gun/Gun_side-left_Reload-Sheet8.png
# 'apocalypse_gun_side_left_shoot_sheet3' - 54x10px - apocalypse/Character/Guns/Gun/Gun_side-left_shoot-Sheet3.png
# 'apocalypse_gun_side_reload_sheet8' - 155x11px - apocalypse/Character/Guns/Gun/Gun_side_reload-Sheet8.png
# 'apocalypse_gun_side_shoot_sheet3' - 54x10px - apocalypse/Character/Guns/Gun/Gun_side_shoot-Sheet3.png
# 'apocalypse_gun_up_idle_and_run_sheet6' - 30x16px - apocalypse/Character/Guns/Gun/Gun_up_idle-and-run-Sheet6.png
# 'apocalypse_gun_up_reload_sheet8' - 163x19px - apocalypse/Character/Guns/Gun/Gun_up_reload-Sheet8.png
# 'apocalypse_gun_up_shoot_sheet3' - 15x17px - apocalypse/Character/Guns/Gun/Gun_up_shoot-Sheet3.png
# 'apocalypse_gutter_and_downspout' - 187x112px - apocalypse/Tiles/Gutter-And-Downspout.png
# 'apocalypse_hands_down_idle_sheet6' - 78x16px - apocalypse/Character/Main/Idle/Hands_down_idle-Sheet6.png
# 'apocalypse_hands_down_pick_up_sheet3' - 36x16px - apocalypse/Character/Main/Pick-up/Hands_down_Pick-up-Sheet3.png
# 'apocalypse_hands_down_punch_sheet4' - 48x10px - apocalypse/Character/Main/Punch/Hands_Down_punch-Sheet4.png
# 'apocalypse_hands_down_run_sheet6' - 78x17px - apocalypse/Character/Main/Run/Hands_down_run-Sheet6.png
# 'apocalypse_hands_side_death_sheet6' - 126x16px - apocalypse/Character/Main/Death/Hands_side_death-Sheet6.png
# 'apocalypse_hands_side_idle_sheet6' - 72x16px - apocalypse/Character/Main/Idle/Hands_Side_idle-Sheet6.png
# 'apocalypse_hands_side_left_death_sheet6' - 126x16px - apocalypse/Character/Main/Death/Hands_side-left_death-Sheet6.png
# 'apocalypse_hands_side_left_idle_sheet6' - 72x16px - apocalypse/Character/Main/Idle/Hands_Side-left_idle-Sheet6.png
# 'apocalypse_hands_side_left_punch_sheet4' - 72x10px - apocalypse/Character/Main/Punch/Hands_side-left_punch-Sheet4.png
# 'apocalypse_hands_side_left_run_sheet6' - 84x17px - apocalypse/Character/Main/Run/Hands_side-left_run-Sheet6.png
# 'apocalypse_hands_side_pick_up_sheet3' - 33x16px - apocalypse/Character/Main/Pick-up/Hands_side_Pick-up-Sheet3.png
# 'apocalypse_hands_side_punch_sheet4' - 72x10px - apocalypse/Character/Main/Punch/Hands_side_punch-Sheet4.png
# 'apocalypse_hands_side_run_sheet6' - 84x17px - apocalypse/Character/Main/Run/Hands_Side_run-Sheet6.png
# 'apocalypse_hands_up_idle_sheet6' - 66x16px - apocalypse/Character/Main/Idle/Hands_Up_idle-Sheet6.png
# 'apocalypse_hands_up_pick_up_sheet3' - 33x15px - apocalypse/Character/Main/Pick-up/Hands_Up_Pick-up-Sheet3.png
# 'apocalypse_hands_up_punch_sheet4' - 48x17px - apocalypse/Character/Main/Punch/Hands_Up_punch-Sheet4.png
# 'apocalypse_hands_up_run_sheet6' - 77x6px - apocalypse/Character/Main/Run/Hands_Up_run-Sheet6.png
# 'apocalypse_hatch_1_closed' - 13x10px - apocalypse/Objects/Buildings/Hatch_1_Closed.png
# 'apocalypse_hatch_1_open' - 13x18px - apocalypse/Objects/Buildings/Hatch_1_Open.png
# 'apocalypse_heart_empty' - 13x12px - apocalypse/UI/HP/Heart_Empty.png
# 'apocalypse_heart_full' - 13x12px - apocalypse/UI/HP/Heart_Full.png
# 'apocalypse_heart_half' - 13x12px - apocalypse/UI/HP/Heart_Half.png
# 'apocalypse_heart_small_empty' - 11x10px - apocalypse/UI/HP/Small/Heart_Small_Empty.png
# 'apocalypse_heart_small_full' - 11x10px - apocalypse/UI/HP/Small/Heart_Small_Full.png
# 'apocalypse_heart_small_half' - 11x10px - apocalypse/UI/HP/Small/Heart_Small_Half.png
# 'apocalypse_helmet_side_death_sheet6' - 126x18px - apocalypse/Character/Helmet/Helmet_side_Death-Sheet6.png
# 'apocalypse_helmet_side_idle_and_run_sheet6' - 60x8px - apocalypse/Character/Helmet/Helmet_side_Idle-and-Run-Sheet6.png
# 'apocalypse_helmet_side_idle_and_run_sprite' - 10x7px - apocalypse/Character/Helmet/Helmet_side_Idle-and-Run_Sprite.png
# 'apocalypse_helmet_side_left_death_sheet6' - 126x18px - apocalypse/Character/Helmet/Helmet_side-left_Death-Sheet6.png
# 'apocalypse_helmet_side_left_idle_and_run_sheet6' - 60x8px - apocalypse/Character/Helmet/Helmet_side-left_Idle-and-Run-Sheet6.png
# 'apocalypse_helmet_side_left_idle_and_run_sprite' - 10x7px - apocalypse/Character/Helmet/Helmet_side-left_Idle-and-Run_Sprite.png
# 'apocalypse_helmet_side_left_pick_up_sheet3' - 30x8px - apocalypse/Character/Helmet/Helmet_side-left_Pick-up-Sheet3.png
# 'apocalypse_helmet_side_left_punch_sheet4' - 52x8px - apocalypse/Character/Helmet/Helmet_side-left_Punch-Sheet4.png
# 'apocalypse_helmet_side_pick_up_sheet3' - 30x8px - apocalypse/Character/Helmet/Helmet_side_Pick-up-Sheet3.png
# 'apocalypse_helmet_side_punch_sheet4' - 50x8px - apocalypse/Character/Helmet/Helmet_side_Punch-Sheet4.png
# 'apocalypse_helmet_up_and_down_idle_and_run_sheet6' - 60x9px - apocalypse/Character/Helmet/Helmet_Up-and-Down_Idle-and-Run-Sheet6.png
# 'apocalypse_helmet_up_and_down_idle_and_run_sprite' - 10x8px - apocalypse/Character/Helmet/Helmet_Up-and-Down_Idle-and-Run-Sprite.png
# 'apocalypse_helmet_up_and_down_pick_up_sheet3' - 30x9px - apocalypse/Character/Helmet/Helmet_Up-and-Down_Pick-up-Sheet3.png
# 'apocalypse_helmet_up_and_down_punch_sheet4' - 40x10px - apocalypse/Character/Helmet/Helmet_Up-and-Down_Punch-Sheet4.png
# 'apocalypse_hp' - 43x4px - apocalypse/UI/HP/HP.png
# 'apocalypse_hp_bar' - 55x12px - apocalypse/UI/HP/HP-Bar.png
# 'apocalypse_hp_bar_small' - 53x10px - apocalypse/UI/HP/Small/HP-Bar_Small.png
# 'apocalypse_hp_small' - 43x2px - apocalypse/UI/HP/Small/HP_Small.png
# 'apocalypse_hunger' - 37x2px - apocalypse/UI/Hunger/Hunger.png
# 'apocalypse_hunger_bar' - 50x13px - apocalypse/UI/Hunger/Hunger-Bar.png
# 'apocalypse_hunger_bar_small' - 48x11px - apocalypse/UI/Hunger/Small/Hunger-Bar_Small.png
# 'apocalypse_hunger_empty' - 13x13px - apocalypse/UI/Hunger/Hunger_Empty.png
# 'apocalypse_hunger_full' - 13x13px - apocalypse/UI/Hunger/Hunger_Full.png
# 'apocalypse_hunger_half' - 13x13px - apocalypse/UI/Hunger/Hunger_Half.png
# 'apocalypse_hunger_small_empty' - 11x11px - apocalypse/UI/Hunger/Small/Hunger_Small_Empty.png
# 'apocalypse_hunger_small_full' - 11x11px - apocalypse/UI/Hunger/Small/Hunger_Small_Full.png
# 'apocalypse_hunger_small_half' - 11x11px - apocalypse/UI/Hunger/Small/Hunger_Small_Half.png
# 'apocalypse_hvac' - 16x12px - apocalypse/Objects/Buildings/HVAC.png
# 'apocalypse_hvac_overgrown_bleak_yellow' - 16x15px - apocalypse/Objects/Buildings/HVAC_Overgrown_Bleak-Yellow.png
# 'apocalypse_hvac_overgrown_dark_green' - 16x15px - apocalypse/Objects/Buildings/HVAC_Overgrown_Dark-Green.png
# 'apocalypse_hvac_overgrown_green' - 16x15px - apocalypse/Objects/Buildings/HVAC_Overgrown_Green.png
# 'apocalypse_hydrant_1_red' - 10x15px - apocalypse/Objects/Hydrant_1_red.png
# 'apocalypse_hydrant_1_yellow' - 10x15px - apocalypse/Objects/Hydrant_1_yellow.png
# 'apocalypse_icon_bandage' - 12x12px - apocalypse/UI/Inventory/Objects/Icon_Bandage.png
# 'apocalypse_icon_bat' - 14x14px - apocalypse/UI/Inventory/Objects/Icon_Bat.png
# 'apocalypse_icon_bullet_box_blue' - 14x12px - apocalypse/UI/Inventory/Objects/Icon_Bullet-box_Blue.png
# 'apocalypse_icon_bullet_box_green' - 14x12px - apocalypse/UI/Inventory/Objects/Icon_Bullet-box_Green.png
# 'apocalypse_icon_bullet_box_red' - 14x12px - apocalypse/UI/Inventory/Objects/Icon_Bullet-box_Red.png
# 'apocalypse_icon_bullet_crate_blue' - 15x12px - apocalypse/UI/Inventory/Objects/Icon_Bullet-crate_Blue.png
# 'apocalypse_icon_bullet_crate_green' - 15x12px - apocalypse/UI/Inventory/Objects/Icon_Bullet-crate_Green.png
# 'apocalypse_icon_bullet_crate_red' - 15x12px - apocalypse/UI/Inventory/Objects/Icon_Bullet-crate_Red.png
# 'apocalypse_icon_canned_food' - 12x12px - apocalypse/UI/Inventory/Objects/Icon_Canned-food.png
# 'apocalypse_icon_canned_soup' - 9x14px - apocalypse/UI/Inventory/Objects/Icon_Canned-soup.png
# 'apocalypse_icon_first_aid_kit_red' - 15x12px - apocalypse/UI/Inventory/Objects/Icon_First-Aid-Kit_Red.png
# 'apocalypse_icon_first_aid_kit_white' - 15x12px - apocalypse/UI/Inventory/Objects/Icon_First-Aid-Kit_White.png
# 'apocalypse_icon_gun' - 15x10px - apocalypse/UI/Inventory/Objects/Icon_Gun.png
# 'apocalypse_icon_pistol' - 11x9px - apocalypse/UI/Inventory/Objects/Icon_Pistol.png
# 'apocalypse_icon_reinforced_wooden_wall' - 13x12px - apocalypse/UI/Inventory/Objects/Icon_Reinforced-wooden-wall.png
# 'apocalypse_icon_reinforced_wooden_wall_gate' - 14x13px - apocalypse/UI/Inventory/Objects/Icon_Reinforced-wooden-wall_Gate.png
# 'apocalypse_icon_rock' - 11x8px - apocalypse/UI/Inventory/Objects/Icon_Rock.png
# 'apocalypse_icon_shotgun' - 15x11px - apocalypse/UI/Inventory/Objects/Icon_Shotgun.png
# 'apocalypse_icon_wooden_wall' - 13x12px - apocalypse/UI/Inventory/Objects/Icon_Wooden-wall.png
# 'apocalypse_icon_wooden_wall_gate' - 14x13px - apocalypse/UI/Inventory/Objects/Icon_Wooden-wall_Gate.png
# 'apocalypse_inventory_1' - 143x91px - apocalypse/UI/Inventory/Inventory_1.png
# 'apocalypse_inventory_1_scrollbar' - 146x91px - apocalypse/UI/Inventory/Inventory_1_Scrollbar.png
# 'apocalypse_inventory_2' - 143x91px - apocalypse/UI/Inventory/Inventory_2.png
# 'apocalypse_inventory_cell' - 19x20px - apocalypse/UI/Inventory/Inventory-Cell.png
# 'apocalypse_inventory_chosen' - 19x19px - apocalypse/UI/Inventory/Inventory-Chosen.png
# 'apocalypse_inventory_close_not_pressed' - 7x7px - apocalypse/UI/Crafting/Inventory_Close_Not-Pressed.png
# 'apocalypse_inventory_close_pressed' - 7x6px - apocalypse/UI/Crafting/Inventory_Close_Pressed.png
# 'apocalypse_inventory_close_sheet2' - 14x7px - apocalypse/UI/Crafting/Inventory_Close-Sheet2.png
# 'apocalypse_inventory_scrollbox_1' - 4x28px - apocalypse/UI/Inventory/Inventory_Scrollbox_1.png
# 'apocalypse_iron_beam' - 15x5px - apocalypse/Objects/Iron-beam.png
# 'apocalypse_iron_fence_tileset' - 38x59px - apocalypse/Tiles/Iron-Fence_TileSet.png
# 'apocalypse_ladder_balcony_metal_1' - 21x14px - apocalypse/Objects/Buildings/Ladder_Balcony_Metal_1.png
# 'apocalypse_ladder_balcony_metal_1_rusty' - 21x14px - apocalypse/Objects/Buildings/Ladder_Balcony_Metal_1_Rusty.png
# 'apocalypse_layered_posters_1_for_ground_and_walls' - 15x14px - apocalypse/Objects/Buildings/layered-posters_1_For-ground-and-walls.png
# 'apocalypse_layered_posters_2_for_ground_and_walls' - 14x12px - apocalypse/Objects/Buildings/layered-posters_2_For-ground-and-walls.png
# 'apocalypse_load_not_pressed' - 76x21px - apocalypse/UI/Menu/Main Menu/Load_Not-Pressed.png
# 'apocalypse_load_pressed' - 76x19px - apocalypse/UI/Menu/Main Menu/Load_Pressed.png
# 'apocalypse_manhole' - 16x16px - apocalypse/Objects/Manhole.png
# 'apocalypse_metal_plates' - 23x18px - apocalypse/Objects/Metal-Plates.png
# 'apocalypse_moss_on_top_bleak_yellow_1' - 5x5px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_1.png
# 'apocalypse_moss_on_top_bleak_yellow_10' - 11x7px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_10.png
# 'apocalypse_moss_on_top_bleak_yellow_10_lighter' - 11x7px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_10_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_11' - 15x5px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_11.png
# 'apocalypse_moss_on_top_bleak_yellow_11_lighter' - 15x5px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_11_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_12' - 13x10px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_12.png
# 'apocalypse_moss_on_top_bleak_yellow_12_lighter' - 13x10px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_12_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_13' - 9x15px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_13.png
# 'apocalypse_moss_on_top_bleak_yellow_13_lighter' - 9x15px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_13_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_1_lighter' - 5x5px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_1_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_2' - 5x6px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_2.png
# 'apocalypse_moss_on_top_bleak_yellow_2_lighter' - 5x6px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_2_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_3' - 8x6px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_3.png
# 'apocalypse_moss_on_top_bleak_yellow_3_lighter' - 8x6px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_3_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_4' - 8x7px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_4.png
# 'apocalypse_moss_on_top_bleak_yellow_4_lighter' - 8x7px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_4_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_5' - 7x8px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_5.png
# 'apocalypse_moss_on_top_bleak_yellow_5_lighter' - 7x8px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_5_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_6' - 9x6px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_6.png
# 'apocalypse_moss_on_top_bleak_yellow_6_lighter' - 9x6px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_6_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_7' - 10x9px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_7.png
# 'apocalypse_moss_on_top_bleak_yellow_7_lighter' - 10x9px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_7_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_8' - 10x8px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_8.png
# 'apocalypse_moss_on_top_bleak_yellow_8_lighter' - 10x8px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_8_Lighter.png
# 'apocalypse_moss_on_top_bleak_yellow_9' - 10x7px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Moss-On-Top_Bleak-Yellow_9.png
# 'apocalypse_moss_on_top_bleak_yellow_9_lighter' - 10x7px - apocalypse/Objects/Nature/Bleak-Yellow/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Bleak-Yellow_9_Lighter.png
# 'apocalypse_moss_on_top_dark_green_1' - 5x5px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_1.png
# 'apocalypse_moss_on_top_dark_green_10' - 11x7px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_10.png
# 'apocalypse_moss_on_top_dark_green_10_lighter' - 11x7px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_10_Lighter.png
# 'apocalypse_moss_on_top_dark_green_11' - 15x5px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_11.png
# 'apocalypse_moss_on_top_dark_green_11_lighter' - 15x5px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_11_Lighter.png
# 'apocalypse_moss_on_top_dark_green_12' - 13x10px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_12.png
# 'apocalypse_moss_on_top_dark_green_12_lighter' - 13x10px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_12_Lighter.png
# 'apocalypse_moss_on_top_dark_green_13' - 9x15px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_13.png
# 'apocalypse_moss_on_top_dark_green_13_lighter' - 9x15px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_13_Lighter.png
# 'apocalypse_moss_on_top_dark_green_1_lighter' - 5x5px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_1_Lighter.png
# 'apocalypse_moss_on_top_dark_green_2' - 5x6px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_2.png
# 'apocalypse_moss_on_top_dark_green_2_lighter' - 5x6px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_2_Lighter.png
# 'apocalypse_moss_on_top_dark_green_3' - 8x6px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_3.png
# 'apocalypse_moss_on_top_dark_green_3_lighter' - 8x6px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_3_Lighter.png
# 'apocalypse_moss_on_top_dark_green_4' - 8x7px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_4.png
# 'apocalypse_moss_on_top_dark_green_4_lighter' - 8x7px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_4_Lighter.png
# 'apocalypse_moss_on_top_dark_green_5' - 7x8px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_5.png
# 'apocalypse_moss_on_top_dark_green_5_lighter' - 7x8px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_5_Lighter.png
# 'apocalypse_moss_on_top_dark_green_6' - 9x6px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_6.png
# 'apocalypse_moss_on_top_dark_green_6_lighter' - 9x6px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_6_Lighter.png
# 'apocalypse_moss_on_top_dark_green_7' - 10x9px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_7.png
# 'apocalypse_moss_on_top_dark_green_7_lighter' - 10x9px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_7_Lighter.png
# 'apocalypse_moss_on_top_dark_green_8' - 10x8px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_8.png
# 'apocalypse_moss_on_top_dark_green_8_lighter' - 10x8px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_8_Lighter.png
# 'apocalypse_moss_on_top_dark_green_9' - 10x7px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Moss-On-Top_Dark-Green_9.png
# 'apocalypse_moss_on_top_dark_green_9_lighter' - 10x7px - apocalypse/Objects/Nature/Dark-Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Dark-Green_9_Lighter.png
# 'apocalypse_moss_on_top_green_1' - 5x5px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_1.png
# 'apocalypse_moss_on_top_green_10' - 11x7px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_10.png
# 'apocalypse_moss_on_top_green_10_lighter' - 11x7px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_10_Lighter.png
# 'apocalypse_moss_on_top_green_11' - 15x5px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_11.png
# 'apocalypse_moss_on_top_green_11_lighter' - 15x5px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_11_Lighter.png
# 'apocalypse_moss_on_top_green_12' - 13x10px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_12.png
# 'apocalypse_moss_on_top_green_12_lighter' - 13x10px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_12_Lighter.png
# 'apocalypse_moss_on_top_green_13' - 9x15px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_13.png
# 'apocalypse_moss_on_top_green_13_lighter' - 9x15px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_13_Lighter.png
# 'apocalypse_moss_on_top_green_1_lighter' - 5x5px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_1_Lighter.png
# 'apocalypse_moss_on_top_green_2' - 5x6px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_2.png
# 'apocalypse_moss_on_top_green_2_lighter' - 5x6px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_2_Lighter.png
# 'apocalypse_moss_on_top_green_3' - 8x6px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_3.png
# 'apocalypse_moss_on_top_green_3_lighter' - 8x6px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_3_Lighter.png
# 'apocalypse_moss_on_top_green_4' - 8x7px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_4.png
# 'apocalypse_moss_on_top_green_4_lighter' - 8x7px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_4_Lighter.png
# 'apocalypse_moss_on_top_green_5' - 7x8px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_5.png
# 'apocalypse_moss_on_top_green_5_lighter' - 7x8px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_5_Lighter.png
# 'apocalypse_moss_on_top_green_6' - 9x6px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_6.png
# 'apocalypse_moss_on_top_green_6_lighter' - 9x6px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_6_Lighter.png
# 'apocalypse_moss_on_top_green_7' - 10x9px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_7.png
# 'apocalypse_moss_on_top_green_7_lighter' - 10x9px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_7_Lighter.png
# 'apocalypse_moss_on_top_green_8' - 10x8px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_8.png
# 'apocalypse_moss_on_top_green_8_lighter' - 10x8px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_8_Lighter.png
# 'apocalypse_moss_on_top_green_9' - 10x7px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Moss-On-Top_Green_9.png
# 'apocalypse_moss_on_top_green_9_lighter' - 10x7px - apocalypse/Objects/Nature/Green/Grass-On-Top-Of-Things/Lighter-Outline/Moss-On-Top_Green_9_Lighter.png
# 'apocalypse_mushroom' - 9x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Mushroom.png
# 'apocalypse_mushrooms_1_yellow' - 10x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Mushrooms_1_Yellow.png
# 'apocalypse_mushrooms_2_red' - 10x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Mushrooms_2_Red.png
# 'apocalypse_pallet_1' - 13x14px - apocalypse/Objects/Pallet_1.png
# 'apocalypse_pallet_2' - 14x10px - apocalypse/Objects/Pallet_2.png
# 'apocalypse_pistol' - 8x7px - apocalypse/Objects/Pickable/Pistol.png
# 'apocalypse_pistol_bullet' - 7x13px - apocalypse/UI/Bullet Indicators/Pistol-Bullet.png
# 'apocalypse_pistol_bullet_bullet' - 1x1px - apocalypse/Character/Guns/Bullets/Pistol-bullet_Bullet.png
# 'apocalypse_pistol_bullet_casting' - 1x1px - apocalypse/Character/Guns/Bullets/Pistol-bullet_Casting.png
# 'apocalypse_pistol_bullet_empty' - 7x13px - apocalypse/UI/Bullet Indicators/Pistol-Bullet_Empty.png
# 'apocalypse_pistol_bullet_small' - 6x10px - apocalypse/UI/Bullet Indicators/Small/Pistol-Bullet_Small.png
# 'apocalypse_pistol_bullet_small_empty' - 6x10px - apocalypse/UI/Bullet Indicators/Small/Pistol-Bullet_Small_Empty.png
# 'apocalypse_pistol_bullet_whole' - 2x1px - apocalypse/Character/Guns/Bullets/Pistol-bullet_Whole.png
# 'apocalypse_pistol_down_idle_and_run_sheet6' - 30x11px - apocalypse/Character/Guns/Pistol/Pistol_down_idle-and-run-Sheet6.png
# 'apocalypse_pistol_down_reload_sheet11' - 194x12px - apocalypse/Character/Guns/Pistol/Pistol_down_Reload-Sheet11.png
# 'apocalypse_pistol_down_shoot_sheet3' - 15x11px - apocalypse/Character/Guns/Pistol/Pistol_down_shoot-Sheet3.png
# 'apocalypse_pistol_side_death_sheet6' - 78x9px - apocalypse/Character/Guns/Pistol/Pistol_side_Death-Sheet6.png
# 'apocalypse_pistol_side_idle_and_run_sheet6' - 48x9px - apocalypse/Character/Guns/Pistol/Pistol_side_idle-and-run-Sheet6.png
# 'apocalypse_pistol_side_left_death_sheet6' - 78x9px - apocalypse/Character/Guns/Pistol/Pistol_side-left_Death-Sheet6.png
# 'apocalypse_pistol_side_left_idle_and_run_sheet6' - 48x9px - apocalypse/Character/Guns/Pistol/Pistol_side-left_idle-and-run-Sheet6.png
# 'apocalypse_pistol_side_left_reload_sheet11' - 132x13px - apocalypse/Character/Guns/Pistol/Pistol_side-left_Reload-Sheet11.png
# 'apocalypse_pistol_side_left_shoot_sheet3' - 30x8px - apocalypse/Character/Guns/Pistol/Pistol_side-left_shoot-Sheet3.png
# 'apocalypse_pistol_side_reload_sheet11' - 132x13px - apocalypse/Character/Guns/Pistol/Pistol_side_Reload-Sheet11.png
# 'apocalypse_pistol_side_shoot_sheet3' - 30x8px - apocalypse/Character/Guns/Pistol/Pistol_side_shoot-Sheet3.png
# 'apocalypse_pistol_up_idle_and_run_sheet6' - 30x11px - apocalypse/Character/Guns/Pistol/Pistol_up_idle-and-run-Sheet6.png
# 'apocalypse_pistol_up_reload_sheet11' - 196x19px - apocalypse/Character/Guns/Pistol/Pistol_up_Reload-Sheet11.png
# 'apocalypse_pistol_up_shoot_sheet3' - 15x11px - apocalypse/Character/Guns/Pistol/Pistol_up_shoot-Sheet3.png
# 'apocalypse_play_not_pressed' - 76x21px - apocalypse/UI/Menu/Main Menu/Play_Not-Pressed.png
# 'apocalypse_play_pressed' - 76x19px - apocalypse/UI/Menu/Main Menu/Play_Pressed.png
# 'apocalypse_puddle_on_dry_ground_1' - 22x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_1.png
# 'apocalypse_puddle_on_dry_ground_2' - 28x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_2.png
# 'apocalypse_puddle_on_dry_ground_3' - 12x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_3.png
# 'apocalypse_puddle_on_dry_ground_4' - 18x10px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_4.png
# 'apocalypse_puddle_on_dry_ground_5' - 17x7px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_5.png
# 'apocalypse_puddle_on_dry_ground_6' - 11x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_6.png
# 'apocalypse_puddle_on_dry_ground_7' - 10x4px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Dry-Ground_7.png
# 'apocalypse_puddle_on_grass_1' - 22x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_1.png
# 'apocalypse_puddle_on_grass_1_grass_bleak_yellow' - 25x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_1_Grass_Bleak-Yellow.png
# 'apocalypse_puddle_on_grass_1_grass_dark_green' - 25x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_1_Grass_Dark-Green.png
# 'apocalypse_puddle_on_grass_1_grass_green' - 25x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_1_Grass_Green.png
# 'apocalypse_puddle_on_grass_2' - 28x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_2.png
# 'apocalypse_puddle_on_grass_2_grass_bleak_yellow' - 30x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_2_Grass_Bleak-Yellow.png
# 'apocalypse_puddle_on_grass_2_grass_dark_green' - 30x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_2_Grass_Dark-Green.png
# 'apocalypse_puddle_on_grass_2_grass_green' - 30x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_2_Grass_Green.png
# 'apocalypse_puddle_on_grass_3' - 12x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_3.png
# 'apocalypse_puddle_on_grass_3_grass_bleak_yellow' - 14x15px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_3_Grass_Bleak-Yellow.png
# 'apocalypse_puddle_on_grass_3_grass_dark_green' - 14x15px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_3_Grass_Dark-Green.png
# 'apocalypse_puddle_on_grass_3_grass_green' - 14x15px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_3_Grass_Green.png
# 'apocalypse_puddle_on_grass_4' - 18x10px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_4.png
# 'apocalypse_puddle_on_grass_4_grass_bleak_yellow' - 19x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_4_Grass_Bleak-Yellow.png
# 'apocalypse_puddle_on_grass_4_grass_dark_green' - 19x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_4_Grass_Dark-Green.png
# 'apocalypse_puddle_on_grass_4_grass_green' - 18x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_4_Grass_Green.png
# 'apocalypse_puddle_on_grass_5' - 17x7px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_5.png
# 'apocalypse_puddle_on_grass_5_grass_bleak_yellow' - 20x10px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_5_Grass_Bleak-Yellow.png
# 'apocalypse_puddle_on_grass_5_grass_dark_green' - 20x10px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_5_Grass_Dark-Green.png
# 'apocalypse_puddle_on_grass_5_grass_green' - 20x10px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_5_Grass_Green.png
# 'apocalypse_puddle_on_grass_6' - 11x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_6.png
# 'apocalypse_puddle_on_grass_6_grass_bleak_yellow' - 15x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_6_Grass_Bleak-Yellow.png
# 'apocalypse_puddle_on_grass_6_grass_dark_green' - 15x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_6_Grass_Dark-Green.png
# 'apocalypse_puddle_on_grass_6_grass_green' - 15x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_6_Grass_Green.png
# 'apocalypse_puddle_on_grass_7' - 10x4px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_7.png
# 'apocalypse_puddle_on_grass_7_grass_bleak_yellow' - 14x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_7_Grass_Bleak-Yellow.png
# 'apocalypse_puddle_on_grass_7_grass_dark_green' - 14x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_7_Grass_Dark-Green.png
# 'apocalypse_puddle_on_grass_7_grass_green' - 14x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Grass_7_Grass_Green.png
# 'apocalypse_puddle_on_mud_1' - 22x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_1.png
# 'apocalypse_puddle_on_mud_2' - 28x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_2.png
# 'apocalypse_puddle_on_mud_3' - 12x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_3.png
# 'apocalypse_puddle_on_mud_4' - 18x10px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_4.png
# 'apocalypse_puddle_on_mud_5' - 17x7px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_5.png
# 'apocalypse_puddle_on_mud_6' - 11x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_6.png
# 'apocalypse_puddle_on_mud_7' - 10x4px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Puddle_On-Mud_7.png
# 'apocalypse_puddle_splash_1_small_sheet4' - 20x5px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Puddle-Splash_1_Small-Sheet4.png
# 'apocalypse_puddle_splash_2_squished_sheet4' - 24x5px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Puddle-Splash_2_Squished-Sheet4.png
# 'apocalypse_puddle_splash_3_normal_sheet4' - 24x6px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Puddle-Splash_3_Normal-Sheet4.png
# 'apocalypse_quick_access_inventory' - 124x19px - apocalypse/UI/Inventory/Quick-Access-Inventory.png
# 'apocalypse_quit_not_pressed' - 76x21px - apocalypse/UI/Menu/Main Menu/Quit_Not-Pressed.png
# 'apocalypse_quit_pressed' - 76x19px - apocalypse/UI/Menu/Main Menu/Quit_Pressed.png
# 'apocalypse_rain_drop_1_blue' - 1x3px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rain-Drop_1_Blue.png
# 'apocalypse_rain_drop_1_white' - 1x3px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rain-Drop_1_White.png
# 'apocalypse_rain_drop_2_long_blue' - 1x7px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rain-Drop_2_Long_Blue.png
# 'apocalypse_rain_drop_2_long_white' - 1x7px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rain-Drop_2_Long_White.png
# 'apocalypse_rain_drop_splash_1_small1' - 3x2px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small1.png
# 'apocalypse_rain_drop_splash_1_small2' - 3x7px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small2.png
# 'apocalypse_rain_drop_splash_1_small3' - 5x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small3.png
# 'apocalypse_rain_drop_splash_1_small4' - 5x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small4.png
# 'apocalypse_rain_drop_splash_1_small5' - 5x5px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_1/Rain-drop-splash_1_Small5.png
# 'apocalypse_rain_drop_splash_1_small_sheet5' - 24x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Rain-drop-splash_1_Small-Sheet5.png
# 'apocalypse_rain_drop_splash_2_big1' - 3x2px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big1.png
# 'apocalypse_rain_drop_splash_2_big2' - 5x7px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big2.png
# 'apocalypse_rain_drop_splash_2_big3' - 7x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big3.png
# 'apocalypse_rain_drop_splash_2_big4' - 7x8px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big4.png
# 'apocalypse_rain_drop_splash_2_big5' - 7x6px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/PNG Frames/Rain-drop-splash_2/Rain-drop-splash_2_Big5.png
# 'apocalypse_rain_drop_splash_2_big_sheet5' - 33x9px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Puddles-And-Water-Anim/Animations/Rain-drop-splash_2_Big-Sheet5.png
# 'apocalypse_refrigerator' - 16x28px - apocalypse/Objects/Refrigerator.png
# 'apocalypse_reinforced_wooden_wall_gate_horizontal' - 16x15px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Gate_Horizontal.png
# 'apocalypse_reinforced_wooden_wall_gate_vertical' - 3x23px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Gate_Vertical.png
# 'apocalypse_reinforced_wooden_wall_gates_closingh_openingv_sheet7' - 112x25px - apocalypse/Objects/Buildable/Reinforced/Animation/Reinforced-wooden-wall_Gates-closingH_openingV-Sheet7.png
# 'apocalypse_reinforced_wooden_wall_gates_openingh_closingv_sheet7' - 99x25px - apocalypse/Objects/Buildable/Reinforced/Animation/Reinforced-wooden-wall_Gates-openingH_closingV-Sheet7.png
# 'apocalypse_reinforced_wooden_wall_horizontal' - 16x14px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Horizontal.png
# 'apocalypse_reinforced_wooden_wall_left_side_right&down_connect' - 12x16px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Left-side_Right&Down-connect.png
# 'apocalypse_reinforced_wooden_wall_left_side_right&up_connect' - 12x16px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Left-side_Right&Up-connect.png
# 'apocalypse_reinforced_wooden_wall_middle_right&left&down_connect' - 16x16px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Middle_Right&Left&Down-connect.png
# 'apocalypse_reinforced_wooden_wall_right_side_left&down_connect' - 12x16px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Right-side_Left&Down-connect.png
# 'apocalypse_reinforced_wooden_wall_right_side_left&up_connect' - 12x16px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Right-side_Left&Up-connect.png
# 'apocalypse_reinforced_wooden_wall_vertical' - 8x16px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Vertical.png
# 'apocalypse_reinforced_wooden_wall_vertical_for_gate' - 7x10px - apocalypse/Objects/Buildable/Reinforced/Reinforced_wooden-wall_Vertical_For-gate.png
# 'apocalypse_rock_1' - 8x4px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_1.png
# 'apocalypse_rock_2' - 7x4px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_2.png
# 'apocalypse_rock_3' - 6x4px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_3.png
# 'apocalypse_rock_4' - 5x4px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_4.png
# 'apocalypse_rock_5' - 4x2px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_5.png
# 'apocalypse_rock_6' - 10x7px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_6.png
# 'apocalypse_rock_7' - 14x13px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Rocks/Rock_7.png
# 'apocalypse_rock_grass' - 13x9px - apocalypse/Objects/Nature/Green/Rocks/Rock-grass.png
# 'apocalypse_rock_grass_bleak_yellow' - 13x9px - apocalypse/Objects/Nature/Bleak-Yellow/Rocks/Rock-grass_Bleak-Yellow.png
# 'apocalypse_rock_grass_dark_green' - 13x9px - apocalypse/Objects/Nature/Dark-Green/Rocks/Rock-grass_Dark-Green.png
# 'apocalypse_roof_hole_1_gray' - 13x15px - apocalypse/Objects/Buildings/Roof-hole_1_Gray.png
# 'apocalypse_roof_hole_2_red' - 13x15px - apocalypse/Objects/Buildings/Roof-hole_2_Red.png
# 'apocalypse_roof_tileset' - 256x80px - apocalypse/Tiles/Roof_TileSet.png
# 'apocalypse_save_not_pressed' - 76x21px - apocalypse/UI/Menu/Main Menu/Save_Not-Pressed.png
# 'apocalypse_save_pressed' - 76x19px - apocalypse/UI/Menu/Main Menu/Save_Pressed.png
# 'apocalypse_scrollbar' - 54x7px - apocalypse/UI/Menu/Scrollbar.png
# 'apocalypse_scrollbar_scrollbox' - 4x9px - apocalypse/UI/Menu/Scrollbar_Scrollbox.png
# 'apocalypse_scrollbar_scrollbox_1' - 4x9px - apocalypse/UI/Menu/Scrollbar_Scrollbox_1.png
# 'apocalypse_settings_not_pressed' - 76x21px - apocalypse/UI/Menu/Main Menu/Settings_Not-Pressed.png
# 'apocalypse_settings_pressed' - 76x19px - apocalypse/UI/Menu/Main Menu/Settings_Pressed.png
# 'apocalypse_shopping_cart' - 12x16px - apocalypse/Objects/Shopping-cart.png
# 'apocalypse_shot_1_sheet3' - 21x6px - apocalypse/Enemies/Shot/shot_1-Sheet3.png
# 'apocalypse_shot_2_sheet3' - 18x6px - apocalypse/Enemies/Shot/shot_2-Sheet3.png
# 'apocalypse_shotgun' - 15x6px - apocalypse/Objects/Pickable/Shotgun.png
# 'apocalypse_shotgun_bullet' - 3x1px - apocalypse/Character/Guns/Bullets/Shotgun-bullet.png
# 'apocalypse_shotgun_bullet_empty' - 9x14px - apocalypse/UI/Bullet Indicators/Shotgun-Bullet_Empty.png
# 'apocalypse_shotgun_bullet_small' - 8x10px - apocalypse/UI/Bullet Indicators/Small/Shotgun-Bullet_Small.png
# 'apocalypse_shotgun_bullet_small_empty' - 8x10px - apocalypse/UI/Bullet Indicators/Small/Shotgun-Bullet_Small_Empty.png
# 'apocalypse_shotgun_down_1reload_sheet9' - 102x17px - apocalypse/Character/Guns/Shotgun/Shotgun_down_1reload-Sheet9.png
# 'apocalypse_shotgun_down_2reload_sheet12' - 138x17px - apocalypse/Character/Guns/Shotgun/Shotgun_down_2reload-Sheet12.png
# 'apocalypse_shotgun_down_3reload_sheet15' - 174x17px - apocalypse/Character/Guns/Shotgun/Shotgun_down_3reload-Sheet15.png
# 'apocalypse_shotgun_down_4reload_sheet18' - 210x17px - apocalypse/Character/Guns/Shotgun/Shotgun_down_4reload-Sheet18.png
# 'apocalypse_shotgun_down_idle_and_run_sheet6' - 36x14px - apocalypse/Character/Guns/Shotgun/Shotgun_down_idle-and-run-Sheet6.png
# 'apocalypse_shotgun_down_racking_sheet2' - 12x14px - apocalypse/Character/Guns/Shotgun/Shotgun_down_racking-Sheet2.png
# 'apocalypse_shotgun_down_reload_first_part_sheet4' - 42x16px - apocalypse/Character/Guns/Shotgun/Shotgun_down_reload_first-part-Sheet4.png
# 'apocalypse_shotgun_down_reload_second_part_sheet3' - 26x14px - apocalypse/Character/Guns/Shotgun/Shotgun_down_reload_second-part-Sheet3.png
# 'apocalypse_shotgun_down_reload_third_part_sheet2' - 14x12px - apocalypse/Character/Guns/Shotgun/Shotgun_down_reload_third-part-Sheet2.png
# 'apocalypse_shotgun_down_shoot_sheet3' - 18x15px - apocalypse/Character/Guns/Shotgun/Shotgun_down_shoot-Sheet3.png
# 'apocalypse_shotgun_side_1reload_sheet9' - 135x17px - apocalypse/Character/Guns/Shotgun/Shotgun_side_1reload-Sheet9.png
# 'apocalypse_shotgun_side_2reload_sheet12' - 180x17px - apocalypse/Character/Guns/Shotgun/Shotgun_side_2reload-Sheet12.png
# 'apocalypse_shotgun_side_3reload_sheet15' - 225x17px - apocalypse/Character/Guns/Shotgun/Shotgun_side_3reload-Sheet15.png
# 'apocalypse_shotgun_side_4reload_sheet18' - 270x17px - apocalypse/Character/Guns/Shotgun/Shotgun_side_4reload-Sheet18.png
# 'apocalypse_shotgun_side_death_sheet6' - 95x9px - apocalypse/Character/Guns/Shotgun/Shotgun_side_Death-Sheet6.png
# 'apocalypse_shotgun_side_idle_and_run_sheet6' - 90x8px - apocalypse/Character/Guns/Shotgun/Shotgun_side_idle-and-run-Sheet6.png
# 'apocalypse_shotgun_side_left_1reload_sheet9' - 135x17px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_1reload-Sheet9.png
# 'apocalypse_shotgun_side_left_2reload_sheet12' - 180x17px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_2reload-Sheet12.png
# 'apocalypse_shotgun_side_left_3reload_sheet15' - 225x17px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_3reload-Sheet15.png
# 'apocalypse_shotgun_side_left_4reload_sheet18' - 270x17px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_4reload-Sheet18.png
# 'apocalypse_shotgun_side_left_death_sheet6' - 96x9px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_Death-Sheet6.png
# 'apocalypse_shotgun_side_left_idle_and_run_sheet6' - 90x8px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_idle-and-run-Sheet6.png
# 'apocalypse_shotgun_side_left_racking_sheet2' - 32x7px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_racking-Sheet2.png
# 'apocalypse_shotgun_side_left_reload_first_part_sheet4' - 60x15px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_reload_first-part-Sheet4.png
# 'apocalypse_shotgun_side_left_reload_second_part_sheet3' - 33x16px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_reload_second-part-Sheet3.png
# 'apocalypse_shotgun_side_left_reload_third_part_sheet2' - 30x12px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_reload_third-part-Sheet2.png
# 'apocalypse_shotgun_side_left_shoot_sheet3' - 54x8px - apocalypse/Character/Guns/Shotgun/Shotgun_side-left_shoot-Sheet3.png
# 'apocalypse_shotgun_side_racking_sheet2' - 32x7px - apocalypse/Character/Guns/Shotgun/Shotgun_side_racking-Sheet2.png
# 'apocalypse_shotgun_side_reload_first_part_sheet4' - 60x15px - apocalypse/Character/Guns/Shotgun/Shotgun_side_reload_first-part-Sheet4.png
# 'apocalypse_shotgun_side_reload_second_part_sheet3' - 33x16px - apocalypse/Character/Guns/Shotgun/Shotgun_side_reload_second-part-Sheet3.png
# 'apocalypse_shotgun_side_reload_third_part_sheet2' - 30x12px - apocalypse/Character/Guns/Shotgun/Shotgun_side_reload_third-part-Sheet2.png
# 'apocalypse_shotgun_side_shoot_sheet3' - 54x8px - apocalypse/Character/Guns/Shotgun/Shotgun_side_shoot-Sheet3.png
# 'apocalypse_shotgun_up_1reload_sheet9' - 135x16px - apocalypse/Character/Guns/Shotgun/Shotgun_up_1reload-Sheet9.png
# 'apocalypse_shotgun_up_2reload_sheet12' - 180x16px - apocalypse/Character/Guns/Shotgun/Shotgun_up_2reload-Sheet12.png
# 'apocalypse_shotgun_up_3reload_sheet15' - 225x16px - apocalypse/Character/Guns/Shotgun/Shotgun_up_3reload-Sheet15.png
# 'apocalypse_shotgun_up_4reload_sheet18' - 270x16px - apocalypse/Character/Guns/Shotgun/Shotgun_up_4reload-Sheet18.png
# 'apocalypse_shotgun_up_idle_and_run_sheet6' - 36x16px - apocalypse/Character/Guns/Shotgun/Shotgun_up_idle-and-run-Sheet6.png
# 'apocalypse_shotgun_up_racking_sheet2' - 12x16px - apocalypse/Character/Guns/Shotgun/Shotgun_up_racking-Sheet2.png
# 'apocalypse_shotgun_up_reload_first_part_sheet4' - 56x16px - apocalypse/Character/Guns/Shotgun/Shotgun_up_reload_first-part-Sheet4.png
# 'apocalypse_shotgun_up_reload_second_part_sheet3' - 33x13px - apocalypse/Character/Guns/Shotgun/Shotgun_up_reload_second-part-Sheet3.png
# 'apocalypse_shotgun_up_reload_third_part_sheet2' - 12x14px - apocalypse/Character/Guns/Shotgun/Shotgun_up_reload_third-part-Sheet2.png
# 'apocalypse_shotgun_up_shoot_sheet3' - 18x17px - apocalypse/Character/Guns/Shotgun/Shotgun_up_shoot-Sheet3.png
# 'apocalypse_stick' - 10x6px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Stick.png
# 'apocalypse_stick_leaves' - 12x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Stick_leaves.png
# 'apocalypse_stop_sign_down_1' - 16x25px - apocalypse/Objects/Stop-sign_Down_1.png
# 'apocalypse_stop_sign_down_2_overgrown_bleak_yellow' - 14x25px - apocalypse/Objects/Stop-sign_Down_2_Overgrown_Bleak-Yellow.png
# 'apocalypse_stop_sign_down_2_overgrown_dark_green' - 14x25px - apocalypse/Objects/Stop-sign_Down_2_Overgrown_Dark-Green.png
# 'apocalypse_stop_sign_down_2_overgrown_green' - 14x25px - apocalypse/Objects/Stop-sign_Down_2_Overgrown_Green.png
# 'apocalypse_stop_sign_side_3' - 7x25px - apocalypse/Objects/Stop-sign_Side_3.png
# 'apocalypse_stop_sign_side_4_overgrown_bleak_yellow' - 9x25px - apocalypse/Objects/Stop-sign_Side_4_Overgrown_Bleak-Yellow.png
# 'apocalypse_stop_sign_side_4_overgrown_dark_green' - 9x25px - apocalypse/Objects/Stop-sign_Side_4_Overgrown_Dark-Green.png
# 'apocalypse_stop_sign_side_4_overgrown_green' - 9x25px - apocalypse/Objects/Stop-sign_Side_4_Overgrown_Green.png
# 'apocalypse_stop_sign_up_5' - 15x24px - apocalypse/Objects/Stop-sign_Up_5.png
# 'apocalypse_stop_sign_up_6_overgrown_bleak_yellow' - 15x24px - apocalypse/Objects/Stop-sign_Up_6_Overgrown_Bleak-Yellow.png
# 'apocalypse_stop_sign_up_6_overgrown_dark_green' - 15x24px - apocalypse/Objects/Stop-sign_Up_6_Overgrown_Dark-Green.png
# 'apocalypse_stop_sign_up_6_overgrown_green' - 15x24px - apocalypse/Objects/Stop-sign_Up_6_Overgrown_Green.png
# 'apocalypse_street_light_1_side' - 23x38px - apocalypse/Objects/Street-Light_1_Side.png
# 'apocalypse_street_light_2_up' - 6x49px - apocalypse/Objects/Street-Light_2_Up.png
# 'apocalypse_street_light_3_down' - 6x37px - apocalypse/Objects/Street-Light_3_Down.png
# 'apocalypse_street_light_4_side_overgrown_bleak_yellow' - 26x40px - apocalypse/Objects/Street-Light_4_Side_Overgrown_Bleak-Yellow.png
# 'apocalypse_street_light_4_side_overgrown_dark_green' - 26x40px - apocalypse/Objects/Street-Light_4_Side_Overgrown_Dark-Green.png
# 'apocalypse_street_light_4_side_overgrown_green' - 26x40px - apocalypse/Objects/Street-Light_4_Side_Overgrown_Green.png
# 'apocalypse_street_light_5_up_overgrown_bleak_yellow' - 11x50px - apocalypse/Objects/Street-Light_5_Up_Overgrown_Bleak-Yellow.png
# 'apocalypse_street_light_5_up_overgrown_dark_green' - 11x50px - apocalypse/Objects/Street-Light_5_Up_Overgrown_Dark-Green.png
# 'apocalypse_street_light_5_up_overgrown_green' - 11x50px - apocalypse/Objects/Street-Light_5_Up_Overgrown_Green.png
# 'apocalypse_street_light_6_down_overgrown_bleak_yellow' - 10x37px - apocalypse/Objects/Street-Light_6_Down_Overgrown_Bleak-Yellow.png
# 'apocalypse_street_light_6_down_overgrown_dark_green' - 10x37px - apocalypse/Objects/Street-Light_6_Down_Overgrown_Dark-Green.png
# 'apocalypse_street_light_6_down_overgrown_green' - 10x37px - apocalypse/Objects/Street-Light_6_Down_Overgrown_Green.png
# 'apocalypse_stump_1' - 15x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Stump_1.png
# 'apocalypse_stump_2_mushrooms' - 15x12px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Stump_2_Mushrooms.png
# 'apocalypse_tire_1' - 15x13px - apocalypse/Objects/Tire_1.png
# 'apocalypse_tire_2_grass_bleak_yellow' - 15x13px - apocalypse/Objects/Tire_2_Grass_Bleak-Yellow.png
# 'apocalypse_tire_2_grass_dark_green' - 15x13px - apocalypse/Objects/Tire_2_Grass_Dark-Green.png
# 'apocalypse_tire_2_grass_green' - 15x13px - apocalypse/Objects/Tire_2_Grass_Green.png
# 'apocalypse_traffic_cone' - 9x11px - apocalypse/Objects/Traffic-cone.png
# 'apocalypse_trash_bag_1' - 11x11px - apocalypse/Objects/Trash-bag_1.png
# 'apocalypse_trash_bag_2' - 10x12px - apocalypse/Objects/Trash-bag_2.png
# 'apocalypse_trash_can_1' - 13x13px - apocalypse/Objects/Trash-can_1.png
# 'apocalypse_trash_can_2' - 13x12px - apocalypse/Objects/Trash-can_2.png
# 'apocalypse_tree_10_small_oak_bleak_yellow' - 24x36px - apocalypse/Objects/Nature/Bleak-Yellow/Tree_10_Small-oak_Bleak-Yellow.png
# 'apocalypse_tree_10_small_oak_dark_green' - 24x36px - apocalypse/Objects/Nature/Dark-Green/Tree_10_Small-oak_Dark-Green.png
# 'apocalypse_tree_10_small_oak_green' - 24x36px - apocalypse/Objects/Nature/Green/Tree_10_Small-oak_Green.png
# 'apocalypse_tree_10_small_oak_orange' - 24x36px - apocalypse/Objects/Nature/Orange/Tree_10_Small-oak_Orange.png
# 'apocalypse_tree_10_small_oak_red' - 24x36px - apocalypse/Objects/Nature/Red/Tree_10_Small-oak_Red.png
# 'apocalypse_tree_10_small_oak_yellow' - 24x36px - apocalypse/Objects/Nature/Yellow/Tree_10_Small-oak_Yellow.png
# 'apocalypse_tree_1_spruce_bleak_yellow' - 16x29px - apocalypse/Objects/Nature/Bleak-Yellow/Tree_1_Spruce_Bleak-Yellow.png
# 'apocalypse_tree_1_spruce_dark_green' - 16x29px - apocalypse/Objects/Nature/Dark-Green/Tree_1_Spruce_Dark-Green.png
# 'apocalypse_tree_1_spruce_green' - 16x29px - apocalypse/Objects/Nature/Green/Tree_1_Spruce_Green.png
# 'apocalypse_tree_1_spruce_orange' - 16x29px - apocalypse/Objects/Nature/Orange/Tree_1_Spruce_Orange.png
# 'apocalypse_tree_1_spruce_red' - 16x29px - apocalypse/Objects/Nature/Red/Tree_1_Spruce_Red.png
# 'apocalypse_tree_1_spruce_yellow' - 16x29px - apocalypse/Objects/Nature/Yellow/Tree_1_Spruce_Yellow.png
# 'apocalypse_tree_2_spruce_sparse_bleak_yellow' - 16x29px - apocalypse/Objects/Nature/Bleak-Yellow/Tree_2_Spruce-Sparse_Bleak-Yellow.png
# 'apocalypse_tree_2_spruce_sparse_dark_green' - 16x29px - apocalypse/Objects/Nature/Dark-Green/Tree_2_Spruce-Sparse_Dark-Green.png
# 'apocalypse_tree_2_spruce_sparse_green' - 16x29px - apocalypse/Objects/Nature/Green/Tree_2_Spruce-Sparse_Green.png
# 'apocalypse_tree_2_spruce_sparse_orange' - 16x29px - apocalypse/Objects/Nature/Orange/Tree_2_Spruce-Sparse_Orange.png
# 'apocalypse_tree_2_spruce_sparse_red' - 16x29px - apocalypse/Objects/Nature/Red/Tree_2_Spruce-Sparse_Red.png
# 'apocalypse_tree_2_spruce_sparse_yellow' - 16x29px - apocalypse/Objects/Nature/Yellow/Tree_2_Spruce-Sparse_Yellow.png
# 'apocalypse_tree_3_normal_bleak_yellow' - 21x30px - apocalypse/Objects/Nature/Bleak-Yellow/Tree_3_Normal_Bleak-Yellow.png
# 'apocalypse_tree_3_normal_dark_green' - 21x30px - apocalypse/Objects/Nature/Dark-Green/Tree_3_Normal_Dark-Green.png
# 'apocalypse_tree_3_normal_green' - 21x30px - apocalypse/Objects/Nature/Green/Tree_3_Normal_Green.png
# 'apocalypse_tree_3_normal_orange' - 21x30px - apocalypse/Objects/Nature/Orange/Tree_3_Normal_Orange.png
# 'apocalypse_tree_3_normal_red' - 21x30px - apocalypse/Objects/Nature/Red/Tree_3_Normal_Red.png
# 'apocalypse_tree_3_normal_yellow' - 21x30px - apocalypse/Objects/Nature/Yellow/Tree_3_Normal_Yellow.png
# 'apocalypse_tree_4_dry_green' - 23x32px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Tree_4_Dry_Green.png
# 'apocalypse_tree_5_big_bleak_yellow' - 34x52px - apocalypse/Objects/Nature/Bleak-Yellow/Tree_5_Big_Bleak-Yellow.png
# 'apocalypse_tree_5_big_dark_green' - 34x52px - apocalypse/Objects/Nature/Dark-Green/Tree_5_Big_Dark-Green.png
# 'apocalypse_tree_5_big_green' - 34x52px - apocalypse/Objects/Nature/Green/Tree_5_Big_Green.png
# 'apocalypse_tree_5_big_orange' - 34x52px - apocalypse/Objects/Nature/Orange/Tree_5_Big_Orange.png
# 'apocalypse_tree_5_big_red' - 34x52px - apocalypse/Objects/Nature/Red/Tree_5_Big_Red.png
# 'apocalypse_tree_5_big_yellow' - 34x52px - apocalypse/Objects/Nature/Yellow/Tree_5_Big_Yellow.png
# 'apocalypse_tree_6_big_pine_bleak_yellow' - 27x49px - apocalypse/Objects/Nature/Bleak-Yellow/Tree_6_Big-pine_Bleak-Yellow.png
# 'apocalypse_tree_6_big_pine_dark_green' - 27x49px - apocalypse/Objects/Nature/Dark-Green/Tree_6_Big-pine_Dark-Green.png
# 'apocalypse_tree_6_big_pine_orange' - 27x49px - apocalypse/Objects/Nature/Orange/Tree_6_Big-pine_Orange.png
# 'apocalypse_tree_6_big_pine_red' - 27x49px - apocalypse/Objects/Nature/Red/Tree_6_Big-pine_Red.png
# 'apocalypse_tree_6_big_pine_yellow' - 27x49px - apocalypse/Objects/Nature/Yellow/Tree_6_Big-pine_Yellow.png
# 'apocalypse_tree_6_pine_big_green' - 27x49px - apocalypse/Objects/Nature/Green/Tree_6_Pine_Big_Green.png
# 'apocalypse_tree_7_birch_bleak_yellow' - 39x45px - apocalypse/Objects/Nature/Bleak-Yellow/Tree_7_Birch_Bleak-Yellow.png
# 'apocalypse_tree_7_birch_dark_green' - 39x45px - apocalypse/Objects/Nature/Dark-Green/Tree_7_Birch_Dark-Green.png
# 'apocalypse_tree_7_birch_green' - 39x45px - apocalypse/Objects/Nature/Green/Tree_7_Birch_Green.png
# 'apocalypse_tree_7_birch_orange' - 39x45px - apocalypse/Objects/Nature/Orange/Tree_7_Birch_Orange.png
# 'apocalypse_tree_7_birch_red' - 39x45px - apocalypse/Objects/Nature/Red/Tree_7_Birch_Red.png
# 'apocalypse_tree_7_birch_yellow' - 39x45px - apocalypse/Objects/Nature/Yellow/Tree_7_Birch_Yellow.png
# 'apocalypse_tree_8_birch_bleak_yellow' - 24x36px - apocalypse/Objects/Nature/Bleak-Yellow/Tree_8_Birch_Bleak-Yellow.png
# 'apocalypse_tree_8_birch_dark_green' - 24x36px - apocalypse/Objects/Nature/Dark-Green/Tree_8_Birch_Dark-Green.png
# 'apocalypse_tree_8_birch_green' - 24x36px - apocalypse/Objects/Nature/Green/Tree_8_Birch_Green.png
# 'apocalypse_tree_8_birch_orange' - 24x36px - apocalypse/Objects/Nature/Orange/Tree_8_Birch_Orange.png
# 'apocalypse_tree_8_birch_red' - 24x36px - apocalypse/Objects/Nature/Red/Tree_8_Birch_Red.png
# 'apocalypse_tree_8_birch_yellow' - 24x36px - apocalypse/Objects/Nature/Yellow/Tree_8_Birch_Yellow.png
# 'apocalypse_tree_9_small_oak_bleak_yellow' - 39x45px - apocalypse/Objects/Nature/Bleak-Yellow/Tree_9_Small-oak_Bleak-Yellow.png
# 'apocalypse_tree_9_small_oak_dark_green' - 39x45px - apocalypse/Objects/Nature/Dark-Green/Tree_9_Small-oak_Dark-Green.png
# 'apocalypse_tree_9_small_oak_green' - 39x45px - apocalypse/Objects/Nature/Green/Tree_9_Small-oak_Green.png
# 'apocalypse_tree_9_small_oak_orange' - 39x45px - apocalypse/Objects/Nature/Orange/Tree_9_Small-oak_Orange.png
# 'apocalypse_tree_9_small_oak_red' - 39x45px - apocalypse/Objects/Nature/Red/Tree_9_Small-oak_Red.png
# 'apocalypse_tree_9_small_oak_yellow' - 39x45px - apocalypse/Objects/Nature/Yellow/Tree_9_Small-oak_Yellow.png
# 'apocalypse_tree_trunk_1_green' - 30x11px - apocalypse/Objects/Nature/Flowers_Mashrooms_Other-nature-stuff/Tree-trunk_1_Green.png
# 'apocalypse_tree_trunk_2_grass_bleak_yellow' - 32x12px - apocalypse/Objects/Nature/Bleak-Yellow/Tree-trunk_2_grass_Bleak-Yellow.png
# 'apocalypse_tree_trunk_2_grass_dark_green' - 32x12px - apocalypse/Objects/Nature/Dark-Green/Tree-trunk_2_grass_Dark-Green.png
# 'apocalypse_tree_trunk_2_grass_green' - 32x12px - apocalypse/Objects/Nature/Green/Tree-trunk_2_grass_Green.png
# 'apocalypse_vending_machine_blue' - 14x23px - apocalypse/Objects/Vending-machine_Blue.png
# 'apocalypse_vending_machine_blue_overgrown_bleak_yellow' - 19x26px - apocalypse/Objects/Vending-machine_Blue_Overgrown_Bleak-Yellow.png
# 'apocalypse_vending_machine_blue_overgrown_dark_green' - 19x26px - apocalypse/Objects/Vending-machine_Blue_Overgrown_Dark-Green.png
# 'apocalypse_vending_machine_blue_overgrown_green' - 19x26px - apocalypse/Objects/Vending-machine_Blue_Overgrown_Green.png
# 'apocalypse_vending_machine_red' - 14x23px - apocalypse/Objects/Vending-machine_Red.png
# 'apocalypse_vending_machine_red_overgrown_bleak_yellow' - 19x26px - apocalypse/Objects/Vending-machine_Red_Overgrown_Bleak-Yellow.png
# 'apocalypse_vending_machine_red_overgrown_dark_green' - 19x26px - apocalypse/Objects/Vending-machine_Red_Overgrown_Dark-Green.png
# 'apocalypse_vending_machine_red_overgrown_green' - 19x26px - apocalypse/Objects/Vending-machine_Red_Overgrown_Green.png
# 'apocalypse_washing_machine' - 14x15px - apocalypse/Objects/Washing-machine.png
# 'apocalypse_window_10_gray' - 15x15px - apocalypse/Objects/Windows/Window_10_gray.png
# 'apocalypse_window_11_boarded_up_gray' - 13x15px - apocalypse/Objects/Windows/Window_11_Boarded-up_gray.png
# 'apocalypse_window_12_boarded_up_gray' - 15x15px - apocalypse/Objects/Windows/Window_12_Boarded-up_gray.png
# 'apocalypse_window_13_broken_beige' - 13x15px - apocalypse/Objects/Windows/Window_13_Broken_Beige.png
# 'apocalypse_window_14_broken_beige' - 15x15px - apocalypse/Objects/Windows/Window_14_Broken_Beige.png
# 'apocalypse_window_15_beige' - 13x15px - apocalypse/Objects/Windows/Window_15_Beige.png
# 'apocalypse_window_16_beige' - 15x15px - apocalypse/Objects/Windows/Window_16_Beige.png
# 'apocalypse_window_17_boarded_up_beige' - 13x15px - apocalypse/Objects/Windows/Window_17_Boarded-up_Beige.png
# 'apocalypse_window_18_boarded_up_beige' - 15x15px - apocalypse/Objects/Windows/Window_18_Boarded-up_Beige.png
# 'apocalypse_window_19_gray' - 16x14px - apocalypse/Objects/Windows/Window_19_gray.png
# 'apocalypse_window_1_broken_wood' - 13x15px - apocalypse/Objects/Windows/Window_1_broken_wood.png
# 'apocalypse_window_20_open_gray' - 16x14px - apocalypse/Objects/Windows/Window_20_open_gray.png
# 'apocalypse_window_21_open_boarded_up' - 16x14px - apocalypse/Objects/Windows/Window_21_open_Boarded-up.png
# 'apocalypse_window_2_broken_wood' - 15x15px - apocalypse/Objects/Windows/Window_2_broken_wood.png
# 'apocalypse_window_3_wood' - 13x15px - apocalypse/Objects/Windows/Window_3_wood.png
# 'apocalypse_window_4_wood' - 15x15px - apocalypse/Objects/Windows/Window_4_wood.png
# 'apocalypse_window_5_boarded_up_wood' - 13x15px - apocalypse/Objects/Windows/Window_5_Boarded-up_wood.png
# 'apocalypse_window_6_boarded_up_wood' - 15x15px - apocalypse/Objects/Windows/Window_6_Boarded-up_wood.png
# 'apocalypse_window_7_broken_gray' - 13x15px - apocalypse/Objects/Windows/Window_7_broken_gray.png
# 'apocalypse_window_8_broken_gray' - 15x15px - apocalypse/Objects/Windows/Window_8_broken_gray.png
# 'apocalypse_window_9_gray' - 13x15px - apocalypse/Objects/Windows/Window_9_gray.png
# 'apocalypse_wire_fence_closing_no_lock_sheet7' - 142x22px - apocalypse/Tiles/Wire-Fence/Wire-Fence_Closing_No-Lock_Sheet7.png
# 'apocalypse_wire_fence_closing_sheet8' - 163x22px - apocalypse/Tiles/Wire-Fence/Wire-Fence_Closing_Sheet8.png
# 'apocalypse_wire_fence_gate' - 16x16px - apocalypse/Tiles/Wire-Fence/Wire-Fence_Gate.png
# 'apocalypse_wire_fence_gate_lock' - 16x16px - apocalypse/Tiles/Wire-Fence/Wire-Fence_Gate_Lock.png
# 'apocalypse_wire_fence_opening_no_lock_sheet8' - 142x22px - apocalypse/Tiles/Wire-Fence/Wire-Fence_Opening_No-Lock_Sheet8.png
# 'apocalypse_wire_fence_opening_sheet8' - 159x22px - apocalypse/Tiles/Wire-Fence/Wire-Fence_Opening_Sheet8.png
# 'apocalypse_wire_fence_tileset' - 80x48px - apocalypse/Tiles/Wire-Fence/Wire-Fence_TileSet.png
# 'apocalypse_wooden_wall_gate_horizontal' - 16x15px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Gate_Horizontal.png
# 'apocalypse_wooden_wall_gate_vertical' - 3x23px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Gate_Vertical.png
# 'apocalypse_wooden_wall_gates_closingh_openingv_sheet7' - 112x25px - apocalypse/Objects/Buildable/Wooden/Animations/Wooden-wall_Gates-closingH_openingV-Sheet7.png
# 'apocalypse_wooden_wall_gates_openingh_closingv_sheet7' - 99x25px - apocalypse/Objects/Buildable/Wooden/Animations/Wooden-wall_Gates-openingH_closingV-Sheet7.png
# 'apocalypse_wooden_wall_horizontal' - 16x14px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Horizontal.png
# 'apocalypse_wooden_wall_left_side_right&down_connect' - 12x16px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Left-side_Right&Down-connect.png
# 'apocalypse_wooden_wall_left_side_right&up_connect' - 12x16px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Left-side_Right&Up-connect.png
# 'apocalypse_wooden_wall_middle_right&left&down_connect' - 16x16px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Middle_Right&Left&Down-connect.png
# 'apocalypse_wooden_wall_right_side_left&down_connect' - 12x16px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Right-side_Left&Down-connect.png
# 'apocalypse_wooden_wall_right_side_left&up_connect' - 12x16px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Right-side_Left&Up-connect.png
# 'apocalypse_wooden_wall_vertical' - 8x16px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Vertical.png
# 'apocalypse_wooden_wall_vertical_for_gate' - 7x10px - apocalypse/Objects/Buildable/Wooden/Wooden-wall_Vertical_For-gate.png
# 'apocalypse_zombie_axe_down_first_attack_sheet7' - 103x21px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Down_First-Attack-Sheet7.png
# 'apocalypse_zombie_axe_down_idle_sheet6' - 78x18px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Down_Idle-Sheet6.png
# 'apocalypse_zombie_axe_down_second_attack_sheet9' - 141x23px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Down_Second-Attack-Sheet9.png
# 'apocalypse_zombie_axe_down_walk_sheet8' - 96x20px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Down_Walk-Sheet8.png
# 'apocalypse_zombie_axe_no_axe_down_first_attack_sheet7' - 83x21px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Down_First-Attack-Sheet7.png
# 'apocalypse_zombie_axe_no_axe_down_idle_sheet6' - 66x18px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Down_Idle-Sheet6.png
# 'apocalypse_zombie_axe_no_axe_down_taking_axe_sheet3' - 36x18px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Down_Taking-Axe-Sheet3.png
# 'apocalypse_zombie_axe_no_axe_down_walk_sheet8' - 88x20px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Down_Walk-Sheet8.png
# 'apocalypse_zombie_axe_no_axe_side_first_attack_sheet7' - 123x19px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_First-Attack-Sheet7.png
# 'apocalypse_zombie_axe_no_axe_side_first_death_sheet6' - 129x18px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_First-Death-Sheet6.png
# 'apocalypse_zombie_axe_no_axe_side_idle_sheet6' - 90x18px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_Idle-Sheet6.png
# 'apocalypse_zombie_axe_no_axe_side_left_first_attack_sheet7' - 126x19px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_First-Attack-Sheet7.png
# 'apocalypse_zombie_axe_no_axe_side_left_first_death_sheet6' - 132x18px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_First-Death-Sheet6.png
# 'apocalypse_zombie_axe_no_axe_side_left_idle_sheet6' - 90x18px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_Idle-Sheet6.png
# 'apocalypse_zombie_axe_no_axe_side_left_second_death_sheet7' - 154x19px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_Second-Death-Sheet7.png
# 'apocalypse_zombie_axe_no_axe_side_left_taking_axe_sheet3' - 60x18px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_Taking-Axe-Sheet3.png
# 'apocalypse_zombie_axe_no_axe_side_left_walk_sheet8' - 112x19px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side-left_Walk-Sheet8.png
# 'apocalypse_zombie_axe_no_axe_side_second_death_sheet7' - 151x19px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_Second-Death-Sheet7.png
# 'apocalypse_zombie_axe_no_axe_side_taking_axe_sheet3' - 53x18px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_Taking-Axe-Sheet3.png
# 'apocalypse_zombie_axe_no_axe_side_walk_sheet8' - 112x19px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Side_Walk-Sheet8.png
# 'apocalypse_zombie_axe_no_axe_up_first_attack_sheet7' - 83x21px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Up_First-Attack-Sheet7.png
# 'apocalypse_zombie_axe_no_axe_up_idle_sheet6' - 66x19px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Up_Idle-Sheet6.png
# 'apocalypse_zombie_axe_no_axe_up_taking_axe_sheet3' - 39x21px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Up_Taking-Axe-Sheet3.png
# 'apocalypse_zombie_axe_no_axe_up_walk_sheet8' - 88x20px - apocalypse/Enemies/Zombie_Axe/No-Axe/Zombie_Axe_No-axe_Up_Walk-Sheet8.png
# 'apocalypse_zombie_axe_side_first_attack_sheet7' - 172x19px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_First-Attack-Sheet7.png
# 'apocalypse_zombie_axe_side_first_death_sheet6' - 161x18px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_First-Death-Sheet6.png
# 'apocalypse_zombie_axe_side_idle_sheet6' - 132x18px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_Idle-Sheet6.png
# 'apocalypse_zombie_axe_side_left_first_attack_sheet7' - 175x19px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_First-Attack-Sheet7.png
# 'apocalypse_zombie_axe_side_left_first_death_sheet6' - 162x18px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_First-Death-Sheet6.png
# 'apocalypse_zombie_axe_side_left_idle_sheet6' - 132x18px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_Idle-Sheet6.png
# 'apocalypse_zombie_axe_side_left_second_attack_sheet9' - 243x27px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_Second-Attack-Sheet9.png
# 'apocalypse_zombie_axe_side_left_second_death_sheet7' - 189x20px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_Second-Death-Sheet7.png
# 'apocalypse_zombie_axe_side_left_walk_sheet8' - 168x19px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side-left_Walk-Sheet8.png
# 'apocalypse_zombie_axe_side_second_attack_sheet9' - 236x27px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_Second-Attack-Sheet9.png
# 'apocalypse_zombie_axe_side_walk_sheet8' - 168x19px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Side_Walk-Sheet8.png
# 'apocalypse_zombie_axe_up_first_attack_sheet7' - 90x25px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Up_First-Attack-Sheet7.png
# 'apocalypse_zombie_axe_up_idle_sheet6' - 72x23px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Up_Idle-Sheet6.png
# 'apocalypse_zombie_axe_up_second_attack_sheet9' - 122x24px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Up_Second-Attack-Sheet9.png
# 'apocalypse_zombie_axe_up_walk_sheet8' - 96x23px - apocalypse/Enemies/Zombie_Axe/Zombie_Axe_Up_Walk-Sheet8.png
# 'apocalypse_zombie_big_down_first_attack_sheet8' - 158x25px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Down_First-Attack-Sheet8.png
# 'apocalypse_zombie_big_down_idle_sheet6' - 96x23px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Down_Idle-Sheet6.png
# 'apocalypse_zombie_big_down_second_attack_sheet15' - 324x30px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Down_Second-Attack-Sheet15.png
# 'apocalypse_zombie_big_down_walk_sheet8' - 128x24px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Down_Walk-Sheet8.png
# 'apocalypse_zombie_big_side_first_attack_sheet8' - 184x23px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_First-Attack-Sheet8.png
# 'apocalypse_zombie_big_side_first_death_sheet7' - 201x23px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_First-Death-Sheet7.png
# 'apocalypse_zombie_big_side_idle_sheet6' - 96x22px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_Idle-Sheet6.png
# 'apocalypse_zombie_big_side_left_first_attack_sheet8' - 184x23px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_First-Attack-Sheet8.png
# 'apocalypse_zombie_big_side_left_first_death_sheet7' - 203x23px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_First-Death-Sheet7.png
# 'apocalypse_zombie_big_side_left_idle_sheet6' - 96x22px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_Idle-Sheet6.png
# 'apocalypse_zombie_big_side_left_second_attack_sheet15' - 450x23px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_Second-Attack-Sheet15.png
# 'apocalypse_zombie_big_side_left_second_death_sheet8' - 232x24px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_Second-Death-Sheet8.png
# 'apocalypse_zombie_big_side_left_walk_sheet8' - 128x24px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side-left_Walk-Sheet8.png
# 'apocalypse_zombie_big_side_second_attack_sheet15' - 436x23px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_Second-Attack-Sheet15.png
# 'apocalypse_zombie_big_side_second_death_sheet8' - 230x23px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_Second-Death-Sheet8.png
# 'apocalypse_zombie_big_side_walk_sheet8' - 128x24px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Side_Walk-Sheet8.png
# 'apocalypse_zombie_big_up_first_attack_sheet8' - 144x24px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Up_First-Attack-Sheet8.png
# 'apocalypse_zombie_big_up_idle_sheet6' - 96x22px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Up_Idle-Sheet6.png
# 'apocalypse_zombie_big_up_second_attack_sheet15' - 393x24px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Up_Second-Attack-Sheet15.png
# 'apocalypse_zombie_big_up_walk_sheet8' - 127x24px - apocalypse/Enemies/Zombie_Big/Zombie_Big_Up_Walk-Sheet8.png
# 'apocalypse_zombie_small_down_first_attack_sheet4' - 52x16px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Down_First-Attack-Sheet4.png
# 'apocalypse_zombie_small_down_idle_sheet6' - 78x16px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Down_Idle-Sheet6.png
# 'apocalypse_zombie_small_down_second_attack_sheet11' - 163x57px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Down_Second-Attack-Sheet11.png
# 'apocalypse_zombie_small_down_walk_sheet6' - 72x16px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Down_walk-Sheet6.png
# 'apocalypse_zombie_small_side_first_attack_sheet4' - 43x14px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_First-Attack-Sheet4.png
# 'apocalypse_zombie_small_side_first_death_sheet6' - 96x14px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_First-Death-Sheet6.png
# 'apocalypse_zombie_small_side_idle_sheet6' - 66x15px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_Idle-Sheet6.png
# 'apocalypse_zombie_small_side_left_first_attack_sheet4' - 44x14px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_First-Attack-Sheet4.png
# 'apocalypse_zombie_small_side_left_first_death_sheet6' - 96x14px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_First-Death-Sheet6.png
# 'apocalypse_zombie_small_side_left_idle_sheet6' - 66x15px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_Idle-Sheet6.png
# 'apocalypse_zombie_small_side_left_second_attack_sheet11' - 682x18px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_Second-Attack-Sheet11.png
# 'apocalypse_zombie_small_side_left_second_death_sheet7' - 112x16px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_Second-Death-Sheet7.png
# 'apocalypse_zombie_small_side_left_walk_sheet6' - 78x15px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side-left_Walk-Sheet6.png
# 'apocalypse_zombie_small_side_second_attack_sheet11' - 682x18px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_Second-Attack-Sheet11.png
# 'apocalypse_zombie_small_side_second_death_sheet7' - 112x16px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_Second-Death-Sheet7.png
# 'apocalypse_zombie_small_side_walk_sheet6' - 78x15px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Side_Walk-Sheet6.png
# 'apocalypse_zombie_small_up_first_attack_sheet4' - 56x15px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Up_First-Attack-Sheet4.png
# 'apocalypse_zombie_small_up_idle_sheet6' - 78x15px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Up_Idle-Sheet6.png
# 'apocalypse_zombie_small_up_second_attack_sheet11' - 163x58px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Up_Second-Attack-Sheet11.png
# 'apocalypse_zombie_small_up_walk_sheet6' - 78x16px - apocalypse/Enemies/Zombie_Small/Zombie_Small_Up_Walk-Sheet6.png
# 'bullet_all_fire_bullet_pixel_16x16_00' - 640x398px - bullet/All_Fire_Bullet_Pixel_16x16_00.png
# 'pixel_village_alchemy_table_01_sheet' - 192x673px - pixel_village/Environment/Structures/Stations/Alchemy/Alchemy_Table_01-Sheet.png
# 'pixel_village_alchemy_table_02_sheet' - 528x300px - pixel_village/Environment/Structures/Stations/Alchemy/Alchemy_Table_02-Sheet.png
# 'pixel_village_alchemy_table_03_sheet' - 400x392px - pixel_village/Environment/Structures/Stations/Alchemy/Alchemy_Table_03-Sheet.png
# 'pixel_village_anvil' - 271x146px - pixel_village/Environment/Structures/Stations/Anvil/Anvil.png
# 'pixel_village_anvil_01_sheet' - 510x381px - pixel_village/Environment/Structures/Stations/Anvil/Anvil_01-Sheet.png
# 'pixel_village_anvil_02_sheet' - 479x466px - pixel_village/Environment/Structures/Stations/Anvil/Anvil_02-Sheet.png
# 'pixel_village_anvil_03_sheet' - 768x545px - pixel_village/Environment/Structures/Stations/Anvil/Anvil_03-Sheet.png
# 'pixel_village_base' - 256x133px - pixel_village/Environment/Structures/Stations/Sawmill/Base.png
# 'pixel_village_bone' - 159x80px - pixel_village/Weapons/Bone/Bone.png
# 'pixel_village_bonfire' - 63x354px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire.png
# 'pixel_village_bonfire_01_sheet' - 124x27px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_01-Sheet.png
# 'pixel_village_bonfire_02_sheet' - 126x29px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_02-Sheet.png
# 'pixel_village_bonfire_03_sheet' - 126x11px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_03-Sheet.png
# 'pixel_village_bonfire_04_sheet' - 125x19px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_04-Sheet.png
# 'pixel_village_bonfire_05_sheet' - 125x14px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_05-Sheet.png
# 'pixel_village_bonfire_06_sheet' - 112x6px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_06-Sheet.png
# 'pixel_village_bonfire_07_sheet' - 126x14px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_07-Sheet.png
# 'pixel_village_bonfire_08_sheet' - 119x11px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_08-Sheet.png
# 'pixel_village_bonfire_09_sheet' - 311x27px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_09-Sheet.png
# 'pixel_village_bonfire_10_sheet' - 183x31px - pixel_village/Environment/Structures/Stations/Bonfire/Bonfire_10-Sheet.png
# 'pixel_village_bricks_01_sheet' - 62x89px - pixel_village/Environment/Structures/Stations/Furnace/Bricks_01-Sheet.png
# 'pixel_village_bricks_02_sheet' - 84x121px - pixel_village/Environment/Structures/Stations/Furnace/Bricks_02-Sheet.png
# 'pixel_village_bricks_03_sheet' - 96x124px - pixel_village/Environment/Structures/Stations/Furnace/Bricks_03-Sheet.png
# 'pixel_village_butchery_01_sheet' - 31x29px - pixel_village/Environment/Structures/Stations/Cooking Station/Butchery/Butchery_01-Sheet.png
# 'pixel_village_butchery_02' - 32x29px - pixel_village/Environment/Structures/Stations/Cooking Station/Butchery/Butchery_02.png
# 'pixel_village_butchery_03' - 48x48px - pixel_village/Environment/Structures/Stations/Cooking Station/Butchery/Butchery_03.png
# 'pixel_village_butchery_04' - 69x64px - pixel_village/Environment/Structures/Stations/Cooking Station/Butchery/Butchery_04.png
# 'pixel_village_carry_idle_down_sheet' - 208x30px - pixel_village/Entities/Characters/Body_A/Animations/Carry_Idle/Carry_Idle_Down-Sheet.png
# 'pixel_village_carry_idle_side_sheet' - 210x30px - pixel_village/Entities/Characters/Body_A/Animations/Carry_Idle/Carry_Idle_Side-Sheet.png
# 'pixel_village_carry_idle_up_sheet' - 210x30px - pixel_village/Entities/Characters/Body_A/Animations/Carry_Idle/Carry_Idle_Up-Sheet.png
# 'pixel_village_carry_run_down_sheet' - 336x30px - pixel_village/Entities/Characters/Body_A/Animations/Carry_Run/Carry_Run_Down-Sheet.png
# 'pixel_village_carry_run_side_sheet' - 338x31px - pixel_village/Entities/Characters/Body_A/Animations/Carry_Run/Carry_Run_Side-Sheet.png
# 'pixel_village_carry_run_up_sheet' - 338x30px - pixel_village/Entities/Characters/Body_A/Animations/Carry_Run/Carry_Run_Up-Sheet.png
# 'pixel_village_carry_walk_down_sheet' - 336x30px - pixel_village/Entities/Characters/Body_A/Animations/Carry_Walk/Carry_Walk_Down-Sheet.png
# 'pixel_village_carry_walk_side_sheet' - 338x30px - pixel_village/Entities/Characters/Body_A/Animations/Carry_Walk/Carry_Walk_Side-Sheet.png
# 'pixel_village_carry_walk_up_sheet' - 338x30px - pixel_village/Entities/Characters/Body_A/Animations/Carry_Walk/Carry_Walk_Up-Sheet.png
# 'pixel_village_collect_down_sheet' - 464x32px - pixel_village/Entities/Characters/Body_A/Animations/Collect_Base/Collect_Down-Sheet.png
# 'pixel_village_collect_side_sheet' - 461x30px - pixel_village/Entities/Characters/Body_A/Animations/Collect_Base/Collect_Side-Sheet.png
# 'pixel_village_collect_up_sheet' - 466x31px - pixel_village/Entities/Characters/Body_A/Animations/Collect_Base/Collect_Up-Sheet.png
# 'pixel_village_cooker_01' - 42x50px - pixel_village/Environment/Structures/Stations/Cooking Station/Cooker/Cooker_01.png
# 'pixel_village_cooker_02' - 36x35px - pixel_village/Environment/Structures/Stations/Cooking Station/Cooker/Cooker_02.png
# 'pixel_village_cooker_03_sheet' - 190x26px - pixel_village/Environment/Structures/Stations/Cooking Station/Cooker/Cooker_03-Sheet.png
# 'pixel_village_cooker_04_sheet' - 318x80px - pixel_village/Environment/Structures/Stations/Cooking Station/Cooker/Cooker_04-Sheet.png
# 'pixel_village_cooking_station' - 287x207px - pixel_village/Environment/Structures/Stations/Cooking Station/Cooking Station.png
# 'pixel_village_crush_down_sheet' - 469x58px - pixel_village/Entities/Characters/Body_A/Animations/Crush_Base/Crush_Down-Sheet.png
# 'pixel_village_crush_side_sheet' - 482x34px - pixel_village/Entities/Characters/Body_A/Animations/Crush_Base/Crush_Side-Sheet.png
# 'pixel_village_crush_up_sheet' - 463x40px - pixel_village/Entities/Characters/Body_A/Animations/Crush_Base/Crush_Up-Sheet.png
# 'pixel_village_death_down_sheet' - 466x48px - pixel_village/Entities/Characters/Body_A/Animations/Death_Base/Death_Down-Sheet.png
# 'pixel_village_death_sheet' - 355x30px - pixel_village/Entities/Npc/Rogue/Death/Death-Sheet.png
# 'pixel_village_death_side_sheet' - 481x37px - pixel_village/Entities/Characters/Body_A/Animations/Death_Base/Death_Side-Sheet.png
# 'pixel_village_death_up_sheet' - 466x32px - pixel_village/Entities/Characters/Body_A/Animations/Death_Base/Death_Up-Sheet.png
# 'pixel_village_dungeon_props' - 143x92px - pixel_village/Environment/Props/Static/Dungeon_Props.png
# 'pixel_village_dungeon_tiles' - 368x352px - pixel_village/Environment/Tilesets/Dungeon_Tiles.png
# 'pixel_village_esoteric' - 111x233px - pixel_village/Environment/Props/Static/Esoteric.png
# 'pixel_village_estructure' - 287x204px - pixel_village/Environment/Structures/Stations/Cooking Station/Estructure.png
# 'pixel_village_farm' - 400x240px - pixel_village/Environment/Props/Static/Farm.png
# 'pixel_village_fire_01_sheet' - 122x36px - pixel_village/Environment/Structures/Stations/Bonfire/Fire_01-Sheet.png
# 'pixel_village_fire_02_sheet' - 105x21px - pixel_village/Environment/Structures/Stations/Bonfire/Fire_02-Sheet.png
# 'pixel_village_fishing_down_sheet' - 465x64px - pixel_village/Entities/Characters/Body_A/Animations/Fishing_Base/Fishing_Down-Sheet.png
# 'pixel_village_fishing_side_sheet' - 484x39px - pixel_village/Entities/Characters/Body_A/Animations/Fishing_Base/Fishing_Side-Sheet.png
# 'pixel_village_fishing_up_sheet' - 460x53px - pixel_village/Entities/Characters/Body_A/Animations/Fishing_Base/Fishing_Up-Sheet.png
# 'pixel_village_floors' - 48x48px - pixel_village/Environment/Structures/Buildings/Floors.png
# 'pixel_village_floors_tiles' - 320x416px - pixel_village/Environment/Tilesets/Floors_Tiles.png
# 'pixel_village_furnace' - 189x382px - pixel_village/Environment/Structures/Stations/Furnace/Furnace.png
# 'pixel_village_furniture' - 799x736px - pixel_village/Environment/Props/Static/Furniture.png
# 'pixel_village_grill_01_sheet' - 253x55px - pixel_village/Environment/Structures/Stations/Cooking Station/Grill/Grill_01-Sheet.png
# 'pixel_village_grill_02_sheet' - 251x53px - pixel_village/Environment/Structures/Stations/Cooking Station/Grill/Grill_02-Sheet.png
# 'pixel_village_grill_03_sheet' - 248x45px - pixel_village/Environment/Structures/Stations/Cooking Station/Grill/Grill_03-Sheet.png
# 'pixel_village_grill_04_sheet' - 298x50px - pixel_village/Environment/Structures/Stations/Cooking Station/Grill/Grill_04-Sheet.png
# 'pixel_village_hands' - 26x87px - pixel_village/Weapons/Hands/Hands.png
# 'pixel_village_hit_down_sheet' - 208x31px - pixel_village/Entities/Characters/Body_A/Animations/Hit_Base/Hit_Down-Sheet.png
# 'pixel_village_hit_side_sheet' - 205x30px - pixel_village/Entities/Characters/Body_A/Animations/Hit_Base/Hit_Side-Sheet.png
# 'pixel_village_hit_up_sheet' - 208x31px - pixel_village/Entities/Characters/Body_A/Animations/Hit_Base/Hit_Up-Sheet.png
# 'pixel_village_idle_down_sheet' - 208x30px - pixel_village/Entities/Characters/Body_A/Animations/Idle_Base/Idle_Down-Sheet.png
# 'pixel_village_idle_sheet' - 115x30px - pixel_village/Entities/Npc/Rogue/Idle/Idle-Sheet.png
# 'pixel_village_idle_side_sheet' - 207x30px - pixel_village/Entities/Characters/Body_A/Animations/Idle_Base/Idle_Side-Sheet.png
# 'pixel_village_idle_up_sheet' - 208x30px - pixel_village/Entities/Characters/Body_A/Animations/Idle_Base/Idle_Up-Sheet.png
# 'pixel_village_iron_01_sheet' - 64x93px - pixel_village/Environment/Structures/Stations/Furnace/Iron_01-Sheet.png
# 'pixel_village_iron_02_sheet' - 86x123px - pixel_village/Environment/Structures/Stations/Furnace/Iron_02-Sheet.png
# 'pixel_village_iron_03_sheet' - 96x128px - pixel_village/Environment/Structures/Stations/Furnace/Iron_03-Sheet.png
# 'pixel_village_level_1' - 31x26px - pixel_village/Environment/Structures/Stations/Sawmill/Level_1.png
# 'pixel_village_level_2_sheet' - 640x508px - pixel_village/Environment/Structures/Stations/Sawmill/Level_2-Sheet.png
# 'pixel_village_level_3_sheet' - 896x635px - pixel_village/Environment/Structures/Stations/Sawmill/Level_3-Sheet.png
# 'pixel_village_meat' - 61x139px - pixel_village/Environment/Props/Static/Meat.png
# 'pixel_village_pan' - 160x174px - pixel_village/Environment/Props/Static/Pan.png
# 'pixel_village_pan_01_sheet' - 114x21px - pixel_village/Environment/Props/Animated/Pan_01-Sheet.png
# 'pixel_village_pan_02_sheet' - 62x18px - pixel_village/Environment/Props/Animated/Pan_02-Sheet.png
# 'pixel_village_pan_03_sheet' - 373x27px - pixel_village/Environment/Props/Animated/Pan_03-Sheet.png
# 'pixel_village_pan_04_sheet' - 116x17px - pixel_village/Environment/Props/Animated/Pan_04-Sheet.png
# 'pixel_village_pan_05_sheet' - 246x32px - pixel_village/Environment/Props/Animated/Pan_05-Sheet.png
# 'pixel_village_pierce_down_sheet' - 468x45px - pixel_village/Entities/Characters/Body_A/Animations/Pierce_Base/Pierce_Down-Sheet.png
# 'pixel_village_pierce_side_sheet' - 470x31px - pixel_village/Entities/Characters/Body_A/Animations/Pierce_Base/Pierce_Side-Sheet.png
# 'pixel_village_pierce_top_sheet' - 466x39px - pixel_village/Entities/Characters/Body_A/Animations/Pierce_Base/Pierce_Top-Sheet.png
# 'pixel_village_props' - 218x236px - pixel_village/Environment/Structures/Buildings/Props.png
# 'pixel_village_resources' - 110x176px - pixel_village/Environment/Props/Static/Resources.png
# 'pixel_village_rocks' - 202x304px - pixel_village/Environment/Props/Static/Rocks.png
# 'pixel_village_roofs' - 368x285px - pixel_village/Environment/Structures/Buildings/Roofs.png
# 'pixel_village_run_down_sheet' - 335x30px - pixel_village/Entities/Characters/Body_A/Animations/Run_Base/Run_Down-Sheet.png
# 'pixel_village_run_sheet' - 339x32px - pixel_village/Entities/Npc/Rogue/Run/Run-Sheet.png
# 'pixel_village_run_side_sheet' - 337x31px - pixel_village/Entities/Characters/Body_A/Animations/Run_Base/Run_Side-Sheet.png
# 'pixel_village_run_up_sheet' - 335x30px - pixel_village/Entities/Characters/Body_A/Animations/Run_Base/Run_Up-Sheet.png
# 'pixel_village_shadows' - 223x212px - pixel_village/Environment/Props/Static/Shadows.png
# 'pixel_village_size_02' - 246x126px - pixel_village/Environment/Props/Static/Trees/Model_01/Size_02.png
# 'pixel_village_size_03' - 207x192px - pixel_village/Environment/Props/Static/Trees/Model_01/Size_03.png
# 'pixel_village_size_03_export' - 184x287px - pixel_village/Environment/Props/Static/Trees/Model_03/Size_03-export.png
# 'pixel_village_size_04' - 355x254px - pixel_village/Environment/Props/Static/Trees/Model_01/Size_04.png
# 'pixel_village_size_04_export' - 267x416px - pixel_village/Environment/Props/Static/Trees/Model_03/Size_04-export.png
# 'pixel_village_size_04_export_export' - 267x416px - pixel_village/Environment/Props/Static/Trees/Model_03/Size_04-export-export.png
# 'pixel_village_size_05' - 436x368px - pixel_village/Environment/Props/Static/Trees/Model_01/Size_05.png
# 'pixel_village_slice_down_sheet' - 467x63px - pixel_village/Entities/Characters/Body_A/Animations/Slice_Base/Slice_Down-Sheet.png
# 'pixel_village_slice_side_sheet' - 483x47px - pixel_village/Entities/Characters/Body_A/Animations/Slice_Base/Slice_Side-Sheet.png
# 'pixel_village_slice_up_sheet' - 470x60px - pixel_village/Entities/Characters/Body_A/Animations/Slice_Base/Slice_Up-Sheet.png
# 'pixel_village_smoke_sheet' - 99x30px - pixel_village/Environment/Structures/Stations/Bonfire/Smoke-Sheet.png
# 'pixel_village_stone_01_sheet' - 64x86px - pixel_village/Environment/Structures/Stations/Furnace/Stone_01-Sheet.png
# 'pixel_village_stone_02_sheet' - 85x113px - pixel_village/Environment/Structures/Stations/Furnace/Stone_02-Sheet.png
# 'pixel_village_stone_03_sheet' - 89x126px - pixel_village/Environment/Structures/Stations/Furnace/Stone_03-Sheet.png
# 'pixel_village_tools' - 176x271px - pixel_village/Environment/Props/Static/Tools.png
# 'pixel_village_vegetation' - 392x428px - pixel_village/Environment/Props/Static/Vegetation.png
# 'pixel_village_walk_down_sheet' - 335x30px - pixel_village/Entities/Characters/Body_A/Animations/Walk_Base/Walk_Down-Sheet.png
# 'pixel_village_walk_side_sheet' - 335x30px - pixel_village/Entities/Characters/Body_A/Animations/Walk_Base/Walk_Side-Sheet.png
# 'pixel_village_walk_up_sheet' - 335x30px - pixel_village/Entities/Characters/Body_A/Animations/Walk_Base/Walk_Up-Sheet.png
# 'pixel_village_wall_tiles' - 288x400px - pixel_village/Environment/Tilesets/Wall_Tiles.png
# 'pixel_village_wall_variations' - 256x480px - pixel_village/Environment/Tilesets/Wall_Variations.png
# 'pixel_village_walls' - 672x782px - pixel_village/Environment/Structures/Buildings/Walls.png
# 'pixel_village_water_tiles' - 384x240px - pixel_village/Environment/Tilesets/Water_tiles.png
# 'pixel_village_watering_down_sheet' - 465x32px - pixel_village/Entities/Characters/Body_A/Animations/Watering_Base/Watering_Down-Sheet.png
# 'pixel_village_watering_side_sheet' - 475x31px - pixel_village/Entities/Characters/Body_A/Animations/Watering_Base/Watering_Side-Sheet.png
# 'pixel_village_watering_up_sheet' - 468x31px - pixel_village/Entities/Characters/Body_A/Animations/Watering_Base/Watering_Up-Sheet.png
# 'pixel_village_wood' - 159x80px - pixel_village/Weapons/Wood/Wood.png
# 'pixel_village_workbench' - 192x351px - pixel_village/Environment/Structures/Stations/Workbench/Workbench.png
# 'player_bullet' - 208x546px - player/bullet/bullet.png
# 'player_survivor_idle_0' - 98x114px - player/feet/idle/survivor-idle_0.png
# 'player_survivor_idle_flashlight_0' - 266x165px - player/flashlight/idle/survivor-idle_flashlight_0.png
# 'player_survivor_idle_flashlight_1' - 266x165px - player/flashlight/idle/survivor-idle_flashlight_1.png
# 'player_survivor_idle_flashlight_10' - 266x168px - player/flashlight/idle/survivor-idle_flashlight_10.png
# 'player_survivor_idle_flashlight_11' - 266x168px - player/flashlight/idle/survivor-idle_flashlight_11.png
# 'player_survivor_idle_flashlight_12' - 266x167px - player/flashlight/idle/survivor-idle_flashlight_12.png
# 'player_survivor_idle_flashlight_13' - 265x167px - player/flashlight/idle/survivor-idle_flashlight_13.png
# 'player_survivor_idle_flashlight_14' - 266x167px - player/flashlight/idle/survivor-idle_flashlight_14.png
# 'player_survivor_idle_flashlight_15' - 266x166px - player/flashlight/idle/survivor-idle_flashlight_15.png
# 'player_survivor_idle_flashlight_16' - 265x166px - player/flashlight/idle/survivor-idle_flashlight_16.png
# 'player_survivor_idle_flashlight_17' - 266x166px - player/flashlight/idle/survivor-idle_flashlight_17.png
# 'player_survivor_idle_flashlight_18' - 266x165px - player/flashlight/idle/survivor-idle_flashlight_18.png
# 'player_survivor_idle_flashlight_19' - 266x165px - player/flashlight/idle/survivor-idle_flashlight_19.png
# 'player_survivor_idle_flashlight_2' - 266x165px - player/flashlight/idle/survivor-idle_flashlight_2.png
# 'player_survivor_idle_flashlight_3' - 266x166px - player/flashlight/idle/survivor-idle_flashlight_3.png
# 'player_survivor_idle_flashlight_4' - 265x166px - player/flashlight/idle/survivor-idle_flashlight_4.png
# 'player_survivor_idle_flashlight_5' - 266x166px - player/flashlight/idle/survivor-idle_flashlight_5.png
# 'player_survivor_idle_flashlight_6' - 266x167px - player/flashlight/idle/survivor-idle_flashlight_6.png
# 'player_survivor_idle_flashlight_7' - 265x167px - player/flashlight/idle/survivor-idle_flashlight_7.png
# 'player_survivor_idle_flashlight_8' - 266x167px - player/flashlight/idle/survivor-idle_flashlight_8.png
# 'player_survivor_idle_flashlight_9' - 266x168px - player/flashlight/idle/survivor-idle_flashlight_9.png
# 'player_survivor_idle_handgun_0' - 210x154px - player/handgun/idle/survivor-idle_handgun_0.png
# 'player_survivor_idle_handgun_1' - 210x154px - player/handgun/idle/survivor-idle_handgun_1.png
# 'player_survivor_idle_handgun_10' - 209x152px - player/handgun/idle/survivor-idle_handgun_10.png
# 'player_survivor_idle_handgun_11' - 209x152px - player/handgun/idle/survivor-idle_handgun_11.png
# 'player_survivor_idle_handgun_12' - 209x153px - player/handgun/idle/survivor-idle_handgun_12.png
# 'player_survivor_idle_handgun_13' - 209x153px - player/handgun/idle/survivor-idle_handgun_13.png
# 'player_survivor_idle_handgun_14' - 209x152px - player/handgun/idle/survivor-idle_handgun_14.png
# 'player_survivor_idle_handgun_15' - 209x153px - player/handgun/idle/survivor-idle_handgun_15.png
# 'player_survivor_idle_handgun_16' - 209x153px - player/handgun/idle/survivor-idle_handgun_16.png
# 'player_survivor_idle_handgun_17' - 209x154px - player/handgun/idle/survivor-idle_handgun_17.png
# 'player_survivor_idle_handgun_18' - 210x154px - player/handgun/idle/survivor-idle_handgun_18.png
# 'player_survivor_idle_handgun_19' - 210x154px - player/handgun/idle/survivor-idle_handgun_19.png
# 'player_survivor_idle_handgun_2' - 210x154px - player/handgun/idle/survivor-idle_handgun_2.png
# 'player_survivor_idle_handgun_3' - 209x154px - player/handgun/idle/survivor-idle_handgun_3.png
# 'player_survivor_idle_handgun_4' - 209x153px - player/handgun/idle/survivor-idle_handgun_4.png
# 'player_survivor_idle_handgun_5' - 209x153px - player/handgun/idle/survivor-idle_handgun_5.png
# 'player_survivor_idle_handgun_6' - 209x152px - player/handgun/idle/survivor-idle_handgun_6.png
# 'player_survivor_idle_handgun_7' - 209x153px - player/handgun/idle/survivor-idle_handgun_7.png
# 'player_survivor_idle_handgun_8' - 209x153px - player/handgun/idle/survivor-idle_handgun_8.png
# 'player_survivor_idle_handgun_9' - 209x152px - player/handgun/idle/survivor-idle_handgun_9.png
# 'player_survivor_idle_knife_0' - 231x169px - player/knife/idle/survivor-idle_knife_0.png
# 'player_survivor_idle_knife_1' - 231x169px - player/knife/idle/survivor-idle_knife_1.png
# 'player_survivor_idle_knife_10' - 235x174px - player/knife/idle/survivor-idle_knife_10.png
# 'player_survivor_idle_knife_11' - 235x174px - player/knife/idle/survivor-idle_knife_11.png
# 'player_survivor_idle_knife_12' - 235x172px - player/knife/idle/survivor-idle_knife_12.png
# 'player_survivor_idle_knife_13' - 235x172px - player/knife/idle/survivor-idle_knife_13.png
# 'player_survivor_idle_knife_14' - 234x172px - player/knife/idle/survivor-idle_knife_14.png
# 'player_survivor_idle_knife_15' - 233x172px - player/knife/idle/survivor-idle_knife_15.png
# 'player_survivor_idle_knife_16' - 233x171px - player/knife/idle/survivor-idle_knife_16.png
# 'player_survivor_idle_knife_17' - 232x170px - player/knife/idle/survivor-idle_knife_17.png
# 'player_survivor_idle_knife_18' - 232x170px - player/knife/idle/survivor-idle_knife_18.png
# 'player_survivor_idle_knife_19' - 231x169px - player/knife/idle/survivor-idle_knife_19.png
# 'player_survivor_idle_knife_2' - 232x170px - player/knife/idle/survivor-idle_knife_2.png
# 'player_survivor_idle_knife_3' - 232x170px - player/knife/idle/survivor-idle_knife_3.png
# 'player_survivor_idle_knife_4' - 233x171px - player/knife/idle/survivor-idle_knife_4.png
# 'player_survivor_idle_knife_5' - 233x172px - player/knife/idle/survivor-idle_knife_5.png
# 'player_survivor_idle_knife_6' - 234x172px - player/knife/idle/survivor-idle_knife_6.png
# 'player_survivor_idle_knife_7' - 235x172px - player/knife/idle/survivor-idle_knife_7.png
# 'player_survivor_idle_knife_8' - 235x172px - player/knife/idle/survivor-idle_knife_8.png
# 'player_survivor_idle_knife_9' - 235x174px - player/knife/idle/survivor-idle_knife_9.png
# 'player_survivor_idle_rifle_0' - 259x153px - player/rifle/idle/survivor-idle_rifle_0.png
# 'player_survivor_idle_rifle_1' - 259x153px - player/rifle/idle/survivor-idle_rifle_1.png
# 'player_survivor_idle_rifle_10' - 257x153px - player/rifle/idle/survivor-idle_rifle_10.png
# 'player_survivor_idle_rifle_11' - 257x153px - player/rifle/idle/survivor-idle_rifle_11.png
# 'player_survivor_idle_rifle_12' - 257x153px - player/rifle/idle/survivor-idle_rifle_12.png
# 'player_survivor_idle_rifle_13' - 258x154px - player/rifle/idle/survivor-idle_rifle_13.png
# 'player_survivor_idle_rifle_14' - 257x153px - player/rifle/idle/survivor-idle_rifle_14.png
# 'player_survivor_idle_rifle_15' - 258x153px - player/rifle/idle/survivor-idle_rifle_15.png
# 'player_survivor_idle_rifle_16' - 259x153px - player/rifle/idle/survivor-idle_rifle_16.png
# 'player_survivor_idle_rifle_17' - 258x153px - player/rifle/idle/survivor-idle_rifle_17.png
# 'player_survivor_idle_rifle_18' - 259x154px - player/rifle/idle/survivor-idle_rifle_18.png
# 'player_survivor_idle_rifle_19' - 259x153px - player/rifle/idle/survivor-idle_rifle_19.png
# 'player_survivor_idle_rifle_2' - 259x154px - player/rifle/idle/survivor-idle_rifle_2.png
# 'player_survivor_idle_rifle_3' - 258x153px - player/rifle/idle/survivor-idle_rifle_3.png
# 'player_survivor_idle_rifle_4' - 259x153px - player/rifle/idle/survivor-idle_rifle_4.png
# 'player_survivor_idle_rifle_5' - 258x153px - player/rifle/idle/survivor-idle_rifle_5.png
# 'player_survivor_idle_rifle_6' - 257x153px - player/rifle/idle/survivor-idle_rifle_6.png
# 'player_survivor_idle_rifle_7' - 258x154px - player/rifle/idle/survivor-idle_rifle_7.png
# 'player_survivor_idle_rifle_8' - 257x153px - player/rifle/idle/survivor-idle_rifle_8.png
# 'player_survivor_idle_rifle_9' - 257x153px - player/rifle/idle/survivor-idle_rifle_9.png
# 'player_survivor_idle_shotgun_0' - 259x153px - player/shotgun/idle/survivor-idle_shotgun_0.png
# 'player_survivor_idle_shotgun_1' - 259x153px - player/shotgun/idle/survivor-idle_shotgun_1.png
# 'player_survivor_idle_shotgun_10' - 257x153px - player/shotgun/idle/survivor-idle_shotgun_10.png
# 'player_survivor_idle_shotgun_11' - 257x153px - player/shotgun/idle/survivor-idle_shotgun_11.png
# 'player_survivor_idle_shotgun_12' - 257x153px - player/shotgun/idle/survivor-idle_shotgun_12.png
# 'player_survivor_idle_shotgun_13' - 258x154px - player/shotgun/idle/survivor-idle_shotgun_13.png
# 'player_survivor_idle_shotgun_14' - 257x153px - player/shotgun/idle/survivor-idle_shotgun_14.png
# 'player_survivor_idle_shotgun_15' - 258x153px - player/shotgun/idle/survivor-idle_shotgun_15.png
# 'player_survivor_idle_shotgun_16' - 259x153px - player/shotgun/idle/survivor-idle_shotgun_16.png
# 'player_survivor_idle_shotgun_17' - 258x153px - player/shotgun/idle/survivor-idle_shotgun_17.png
# 'player_survivor_idle_shotgun_18' - 259x154px - player/shotgun/idle/survivor-idle_shotgun_18.png
# 'player_survivor_idle_shotgun_19' - 259x153px - player/shotgun/idle/survivor-idle_shotgun_19.png
# 'player_survivor_idle_shotgun_2' - 259x154px - player/shotgun/idle/survivor-idle_shotgun_2.png
# 'player_survivor_idle_shotgun_3' - 258x153px - player/shotgun/idle/survivor-idle_shotgun_3.png
# 'player_survivor_idle_shotgun_4' - 259x153px - player/shotgun/idle/survivor-idle_shotgun_4.png
# 'player_survivor_idle_shotgun_5' - 258x153px - player/shotgun/idle/survivor-idle_shotgun_5.png
# 'player_survivor_idle_shotgun_6' - 257x153px - player/shotgun/idle/survivor-idle_shotgun_6.png
# 'player_survivor_idle_shotgun_7' - 258x154px - player/shotgun/idle/survivor-idle_shotgun_7.png
# 'player_survivor_idle_shotgun_8' - 257x153px - player/shotgun/idle/survivor-idle_shotgun_8.png
# 'player_survivor_idle_shotgun_9' - 257x153px - player/shotgun/idle/survivor-idle_shotgun_9.png
# 'player_survivor_meleeattack_flashlight_0' - 266x165px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_0.png
# 'player_survivor_meleeattack_flashlight_1' - 268x164px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_1.png
# 'player_survivor_meleeattack_flashlight_10' - 211x159px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_10.png
# 'player_survivor_meleeattack_flashlight_11' - 216x160px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_11.png
# 'player_survivor_meleeattack_flashlight_12' - 227x175px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_12.png
# 'player_survivor_meleeattack_flashlight_13' - 254x176px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_13.png
# 'player_survivor_meleeattack_flashlight_14' - 265x170px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_14.png
# 'player_survivor_meleeattack_flashlight_2' - 271x164px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_2.png
# 'player_survivor_meleeattack_flashlight_3' - 274x162px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_3.png
# 'player_survivor_meleeattack_flashlight_4' - 278x160px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_4.png
# 'player_survivor_meleeattack_flashlight_5' - 280x159px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_5.png
# 'player_survivor_meleeattack_flashlight_6' - 249x191px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_6.png
# 'player_survivor_meleeattack_flashlight_7' - 247x155px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_7.png
# 'player_survivor_meleeattack_flashlight_8' - 241x157px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_8.png
# 'player_survivor_meleeattack_flashlight_9' - 226x158px - player/flashlight/meleeattack/survivor-meleeattack_flashlight_9.png
# 'player_survivor_meleeattack_handgun_0' - 210x154px - player/handgun/meleeattack/survivor-meleeattack_handgun_0.png
# 'player_survivor_meleeattack_handgun_1' - 204x161px - player/handgun/meleeattack/survivor-meleeattack_handgun_1.png
# 'player_survivor_meleeattack_handgun_10' - 191x182px - player/handgun/meleeattack/survivor-meleeattack_handgun_10.png
# 'player_survivor_meleeattack_handgun_11' - 194x169px - player/handgun/meleeattack/survivor-meleeattack_handgun_11.png
# 'player_survivor_meleeattack_handgun_12' - 214x161px - player/handgun/meleeattack/survivor-meleeattack_handgun_12.png
# 'player_survivor_meleeattack_handgun_13' - 223x153px - player/handgun/meleeattack/survivor-meleeattack_handgun_13.png
# 'player_survivor_meleeattack_handgun_14' - 216x154px - player/handgun/meleeattack/survivor-meleeattack_handgun_14.png
# 'player_survivor_meleeattack_handgun_2' - 188x173px - player/handgun/meleeattack/survivor-meleeattack_handgun_2.png
# 'player_survivor_meleeattack_handgun_3' - 169x181px - player/handgun/meleeattack/survivor-meleeattack_handgun_3.png
# 'player_survivor_meleeattack_handgun_4' - 155x181px - player/handgun/meleeattack/survivor-meleeattack_handgun_4.png
# 'player_survivor_meleeattack_handgun_5' - 161x178px - player/handgun/meleeattack/survivor-meleeattack_handgun_5.png
# 'player_survivor_meleeattack_handgun_6' - 181x189px - player/handgun/meleeattack/survivor-meleeattack_handgun_6.png
# 'player_survivor_meleeattack_handgun_7' - 242x161px - player/handgun/meleeattack/survivor-meleeattack_handgun_7.png
# 'player_survivor_meleeattack_handgun_8' - 211x164px - player/handgun/meleeattack/survivor-meleeattack_handgun_8.png
# 'player_survivor_meleeattack_handgun_9' - 185x190px - player/handgun/meleeattack/survivor-meleeattack_handgun_9.png
# 'player_survivor_meleeattack_knife_0' - 231x169px - player/knife/meleeattack/survivor-meleeattack_knife_0.png
# 'player_survivor_meleeattack_knife_1' - 221x170px - player/knife/meleeattack/survivor-meleeattack_knife_1.png
# 'player_survivor_meleeattack_knife_10' - 221x254px - player/knife/meleeattack/survivor-meleeattack_knife_10.png
# 'player_survivor_meleeattack_knife_11' - 231x225px - player/knife/meleeattack/survivor-meleeattack_knife_11.png
# 'player_survivor_meleeattack_knife_12' - 242x188px - player/knife/meleeattack/survivor-meleeattack_knife_12.png
# 'player_survivor_meleeattack_knife_13' - 246x178px - player/knife/meleeattack/survivor-meleeattack_knife_13.png
# 'player_survivor_meleeattack_knife_14' - 238x170px - player/knife/meleeattack/survivor-meleeattack_knife_14.png
# 'player_survivor_meleeattack_knife_2' - 191x169px - player/knife/meleeattack/survivor-meleeattack_knife_2.png
# 'player_survivor_meleeattack_knife_3' - 184x175px - player/knife/meleeattack/survivor-meleeattack_knife_3.png
# 'player_survivor_meleeattack_knife_4' - 174x182px - player/knife/meleeattack/survivor-meleeattack_knife_4.png
# 'player_survivor_meleeattack_knife_5' - 171x177px - player/knife/meleeattack/survivor-meleeattack_knife_5.png
# 'player_survivor_meleeattack_knife_6' - 207x176px - player/knife/meleeattack/survivor-meleeattack_knife_6.png
# 'player_survivor_meleeattack_knife_7' - 262x169px - player/knife/meleeattack/survivor-meleeattack_knife_7.png
# 'player_survivor_meleeattack_knife_8' - 240x229px - player/knife/meleeattack/survivor-meleeattack_knife_8.png
# 'player_survivor_meleeattack_knife_9' - 214x266px - player/knife/meleeattack/survivor-meleeattack_knife_9.png
# 'player_survivor_meleeattack_rifle_0' - 259x153px - player/rifle/meleeattack/survivor-meleeattack_rifle_0.png
# 'player_survivor_meleeattack_rifle_1' - 254x158px - player/rifle/meleeattack/survivor-meleeattack_rifle_1.png
# 'player_survivor_meleeattack_rifle_10' - 159x256px - player/rifle/meleeattack/survivor-meleeattack_rifle_10.png
# 'player_survivor_meleeattack_rifle_11' - 179x248px - player/rifle/meleeattack/survivor-meleeattack_rifle_11.png
# 'player_survivor_meleeattack_rifle_12' - 210x224px - player/rifle/meleeattack/survivor-meleeattack_rifle_12.png
# 'player_survivor_meleeattack_rifle_13' - 256x162px - player/rifle/meleeattack/survivor-meleeattack_rifle_13.png
# 'player_survivor_meleeattack_rifle_14' - 267x153px - player/rifle/meleeattack/survivor-meleeattack_rifle_14.png
# 'player_survivor_meleeattack_rifle_2' - 241x166px - player/rifle/meleeattack/survivor-meleeattack_rifle_2.png
# 'player_survivor_meleeattack_rifle_3' - 224x189px - player/rifle/meleeattack/survivor-meleeattack_rifle_3.png
# 'player_survivor_meleeattack_rifle_4' - 215x200px - player/rifle/meleeattack/survivor-meleeattack_rifle_4.png
# 'player_survivor_meleeattack_rifle_5' - 210x203px - player/rifle/meleeattack/survivor-meleeattack_rifle_5.png
# 'player_survivor_meleeattack_rifle_6' - 213x219px - player/rifle/meleeattack/survivor-meleeattack_rifle_6.png
# 'player_survivor_meleeattack_rifle_7' - 266x174px - player/rifle/meleeattack/survivor-meleeattack_rifle_7.png
# 'player_survivor_meleeattack_rifle_8' - 282x163px - player/rifle/meleeattack/survivor-meleeattack_rifle_8.png
# 'player_survivor_meleeattack_rifle_9' - 221x229px - player/rifle/meleeattack/survivor-meleeattack_rifle_9.png
# 'player_survivor_meleeattack_shotgun_0' - 259x153px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_0.png
# 'player_survivor_meleeattack_shotgun_1' - 254x158px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_1.png
# 'player_survivor_meleeattack_shotgun_10' - 159x256px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_10.png
# 'player_survivor_meleeattack_shotgun_11' - 179x248px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_11.png
# 'player_survivor_meleeattack_shotgun_12' - 210x224px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_12.png
# 'player_survivor_meleeattack_shotgun_13' - 256x162px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_13.png
# 'player_survivor_meleeattack_shotgun_14' - 267x153px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_14.png
# 'player_survivor_meleeattack_shotgun_2' - 241x167px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_2.png
# 'player_survivor_meleeattack_shotgun_3' - 224x189px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_3.png
# 'player_survivor_meleeattack_shotgun_4' - 214x200px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_4.png
# 'player_survivor_meleeattack_shotgun_5' - 209x203px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_5.png
# 'player_survivor_meleeattack_shotgun_6' - 212x219px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_6.png
# 'player_survivor_meleeattack_shotgun_7' - 266x174px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_7.png
# 'player_survivor_meleeattack_shotgun_8' - 282x163px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_8.png
# 'player_survivor_meleeattack_shotgun_9' - 221x229px - player/shotgun/meleeattack/survivor-meleeattack_shotgun_9.png
# 'player_survivor_move_flashlight_0' - 267x166px - player/flashlight/move/survivor-move_flashlight_0.png
# 'player_survivor_move_flashlight_1' - 268x166px - player/flashlight/move/survivor-move_flashlight_1.png
# 'player_survivor_move_flashlight_10' - 272x174px - player/flashlight/move/survivor-move_flashlight_10.png
# 'player_survivor_move_flashlight_11' - 272x173px - player/flashlight/move/survivor-move_flashlight_11.png
# 'player_survivor_move_flashlight_12' - 271x173px - player/flashlight/move/survivor-move_flashlight_12.png
# 'player_survivor_move_flashlight_13' - 270x172px - player/flashlight/move/survivor-move_flashlight_13.png
# 'player_survivor_move_flashlight_14' - 268x170px - player/flashlight/move/survivor-move_flashlight_14.png
# 'player_survivor_move_flashlight_15' - 268x169px - player/flashlight/move/survivor-move_flashlight_15.png
# 'player_survivor_move_flashlight_16' - 268x168px - player/flashlight/move/survivor-move_flashlight_16.png
# 'player_survivor_move_flashlight_17' - 268x168px - player/flashlight/move/survivor-move_flashlight_17.png
# 'player_survivor_move_flashlight_18' - 268x168px - player/flashlight/move/survivor-move_flashlight_18.png
# 'player_survivor_move_flashlight_19' - 268x166px - player/flashlight/move/survivor-move_flashlight_19.png
# 'player_survivor_move_flashlight_2' - 268x167px - player/flashlight/move/survivor-move_flashlight_2.png
# 'player_survivor_move_flashlight_3' - 268x167px - player/flashlight/move/survivor-move_flashlight_3.png
# 'player_survivor_move_flashlight_4' - 268x167px - player/flashlight/move/survivor-move_flashlight_4.png
# 'player_survivor_move_flashlight_5' - 268x167px - player/flashlight/move/survivor-move_flashlight_5.png
# 'player_survivor_move_flashlight_6' - 268x168px - player/flashlight/move/survivor-move_flashlight_6.png
# 'player_survivor_move_flashlight_7' - 270x169px - player/flashlight/move/survivor-move_flashlight_7.png
# 'player_survivor_move_flashlight_8' - 271x171px - player/flashlight/move/survivor-move_flashlight_8.png
# 'player_survivor_move_flashlight_9' - 272x172px - player/flashlight/move/survivor-move_flashlight_9.png
# 'player_survivor_move_handgun_0' - 210x154px - player/handgun/move/survivor-move_handgun_0.png
# 'player_survivor_move_handgun_1' - 210x154px - player/handgun/move/survivor-move_handgun_1.png
# 'player_survivor_move_handgun_10' - 212x157px - player/handgun/move/survivor-move_handgun_10.png
# 'player_survivor_move_handgun_11' - 212x156px - player/handgun/move/survivor-move_handgun_11.png
# 'player_survivor_move_handgun_12' - 212x156px - player/handgun/move/survivor-move_handgun_12.png
# 'player_survivor_move_handgun_13' - 212x156px - player/handgun/move/survivor-move_handgun_13.png
# 'player_survivor_move_handgun_14' - 211x155px - player/handgun/move/survivor-move_handgun_14.png
# 'player_survivor_move_handgun_15' - 211x156px - player/handgun/move/survivor-move_handgun_15.png
# 'player_survivor_move_handgun_16' - 210x155px - player/handgun/move/survivor-move_handgun_16.png
# 'player_survivor_move_handgun_17' - 210x154px - player/handgun/move/survivor-move_handgun_17.png
# 'player_survivor_move_handgun_18' - 210x154px - player/handgun/move/survivor-move_handgun_18.png
# 'player_survivor_move_handgun_19' - 210x154px - player/handgun/move/survivor-move_handgun_19.png
# 'player_survivor_move_handgun_2' - 210x154px - player/handgun/move/survivor-move_handgun_2.png
# 'player_survivor_move_handgun_3' - 210x154px - player/handgun/move/survivor-move_handgun_3.png
# 'player_survivor_move_handgun_4' - 210x155px - player/handgun/move/survivor-move_handgun_4.png
# 'player_survivor_move_handgun_5' - 211x156px - player/handgun/move/survivor-move_handgun_5.png
# 'player_survivor_move_handgun_6' - 211x155px - player/handgun/move/survivor-move_handgun_6.png
# 'player_survivor_move_handgun_7' - 212x156px - player/handgun/move/survivor-move_handgun_7.png
# 'player_survivor_move_handgun_8' - 212x156px - player/handgun/move/survivor-move_handgun_8.png
# 'player_survivor_move_handgun_9' - 212x156px - player/handgun/move/survivor-move_handgun_9.png
# 'player_survivor_move_knife_0' - 215x169px - player/knife/move/survivor-move_knife_0.png
# 'player_survivor_move_knife_1' - 215x169px - player/knife/move/survivor-move_knife_1.png
# 'player_survivor_move_knife_10' - 232x174px - player/knife/move/survivor-move_knife_10.png
# 'player_survivor_move_knife_11' - 232x174px - player/knife/move/survivor-move_knife_11.png
# 'player_survivor_move_knife_12' - 230x172px - player/knife/move/survivor-move_knife_12.png
# 'player_survivor_move_knife_13' - 229x172px - player/knife/move/survivor-move_knife_13.png
# 'player_survivor_move_knife_14' - 227x170px - player/knife/move/survivor-move_knife_14.png
# 'player_survivor_move_knife_15' - 225x169px - player/knife/move/survivor-move_knife_15.png
# 'player_survivor_move_knife_16' - 222x167px - player/knife/move/survivor-move_knife_16.png
# 'player_survivor_move_knife_17' - 221x168px - player/knife/move/survivor-move_knife_17.png
# 'player_survivor_move_knife_18' - 218x168px - player/knife/move/survivor-move_knife_18.png
# 'player_survivor_move_knife_19' - 216x169px - player/knife/move/survivor-move_knife_19.png
# 'player_survivor_move_knife_2' - 217x168px - player/knife/move/survivor-move_knife_2.png
# 'player_survivor_move_knife_3' - 220x168px - player/knife/move/survivor-move_knife_3.png
# 'player_survivor_move_knife_4' - 222x167px - player/knife/move/survivor-move_knife_4.png
# 'player_survivor_move_knife_5' - 224x169px - player/knife/move/survivor-move_knife_5.png
# 'player_survivor_move_knife_6' - 227x170px - player/knife/move/survivor-move_knife_6.png
# 'player_survivor_move_knife_7' - 229x172px - player/knife/move/survivor-move_knife_7.png
# 'player_survivor_move_knife_8' - 230x172px - player/knife/move/survivor-move_knife_8.png
# 'player_survivor_move_knife_9' - 232x174px - player/knife/move/survivor-move_knife_9.png
# 'player_survivor_move_rifle_0' - 259x153px - player/rifle/move/survivor-move_rifle_0.png
# 'player_survivor_move_rifle_1' - 259x153px - player/rifle/move/survivor-move_rifle_1.png
# 'player_survivor_move_rifle_10' - 256x155px - player/rifle/move/survivor-move_rifle_10.png
# 'player_survivor_move_rifle_11' - 257x154px - player/rifle/move/survivor-move_rifle_11.png
# 'player_survivor_move_rifle_12' - 256x154px - player/rifle/move/survivor-move_rifle_12.png
# 'player_survivor_move_rifle_13' - 257x154px - player/rifle/move/survivor-move_rifle_13.png
# 'player_survivor_move_rifle_14' - 257x154px - player/rifle/move/survivor-move_rifle_14.png
# 'player_survivor_move_rifle_15' - 258x153px - player/rifle/move/survivor-move_rifle_15.png
# 'player_survivor_move_rifle_16' - 258x153px - player/rifle/move/survivor-move_rifle_16.png
# 'player_survivor_move_rifle_17' - 258x153px - player/rifle/move/survivor-move_rifle_17.png
# 'player_survivor_move_rifle_18' - 258x153px - player/rifle/move/survivor-move_rifle_18.png
# 'player_survivor_move_rifle_19' - 259x153px - player/rifle/move/survivor-move_rifle_19.png
# 'player_survivor_move_rifle_2' - 258x153px - player/rifle/move/survivor-move_rifle_2.png
# 'player_survivor_move_rifle_3' - 258x153px - player/rifle/move/survivor-move_rifle_3.png
# 'player_survivor_move_rifle_4' - 258x153px - player/rifle/move/survivor-move_rifle_4.png
# 'player_survivor_move_rifle_5' - 258x153px - player/rifle/move/survivor-move_rifle_5.png
# 'player_survivor_move_rifle_6' - 257x154px - player/rifle/move/survivor-move_rifle_6.png
# 'player_survivor_move_rifle_7' - 257x154px - player/rifle/move/survivor-move_rifle_7.png
# 'player_survivor_move_rifle_8' - 256x154px - player/rifle/move/survivor-move_rifle_8.png
# 'player_survivor_move_rifle_9' - 257x154px - player/rifle/move/survivor-move_rifle_9.png
# 'player_survivor_move_shotgun_0' - 259x153px - player/shotgun/move/survivor-move_shotgun_0.png
# 'player_survivor_move_shotgun_1' - 259x153px - player/shotgun/move/survivor-move_shotgun_1.png
# 'player_survivor_move_shotgun_10' - 256x155px - player/shotgun/move/survivor-move_shotgun_10.png
# 'player_survivor_move_shotgun_11' - 257x154px - player/shotgun/move/survivor-move_shotgun_11.png
# 'player_survivor_move_shotgun_12' - 256x154px - player/shotgun/move/survivor-move_shotgun_12.png
# 'player_survivor_move_shotgun_13' - 257x154px - player/shotgun/move/survivor-move_shotgun_13.png
# 'player_survivor_move_shotgun_14' - 257x154px - player/shotgun/move/survivor-move_shotgun_14.png
# 'player_survivor_move_shotgun_15' - 258x153px - player/shotgun/move/survivor-move_shotgun_15.png
# 'player_survivor_move_shotgun_16' - 258x153px - player/shotgun/move/survivor-move_shotgun_16.png
# 'player_survivor_move_shotgun_17' - 258x153px - player/shotgun/move/survivor-move_shotgun_17.png
# 'player_survivor_move_shotgun_18' - 258x153px - player/shotgun/move/survivor-move_shotgun_18.png
# 'player_survivor_move_shotgun_19' - 259x153px - player/shotgun/move/survivor-move_shotgun_19.png
# 'player_survivor_move_shotgun_2' - 258x153px - player/shotgun/move/survivor-move_shotgun_2.png
# 'player_survivor_move_shotgun_3' - 258x153px - player/shotgun/move/survivor-move_shotgun_3.png
# 'player_survivor_move_shotgun_4' - 258x153px - player/shotgun/move/survivor-move_shotgun_4.png
# 'player_survivor_move_shotgun_5' - 258x153px - player/shotgun/move/survivor-move_shotgun_5.png
# 'player_survivor_move_shotgun_6' - 257x154px - player/shotgun/move/survivor-move_shotgun_6.png
# 'player_survivor_move_shotgun_7' - 257x154px - player/shotgun/move/survivor-move_shotgun_7.png
# 'player_survivor_move_shotgun_8' - 256x154px - player/shotgun/move/survivor-move_shotgun_8.png
# 'player_survivor_move_shotgun_9' - 257x154px - player/shotgun/move/survivor-move_shotgun_9.png
# 'player_survivor_reload_handgun_0' - 210x154px - player/handgun/reload/survivor-reload_handgun_0.png
# 'player_survivor_reload_handgun_1' - 210x155px - player/handgun/reload/survivor-reload_handgun_1.png
# 'player_survivor_reload_handgun_10' - 207x164px - player/handgun/reload/survivor-reload_handgun_10.png
# 'player_survivor_reload_handgun_11' - 208x161px - player/handgun/reload/survivor-reload_handgun_11.png
# 'player_survivor_reload_handgun_12' - 209x157px - player/handgun/reload/survivor-reload_handgun_12.png
# 'player_survivor_reload_handgun_13' - 210x154px - player/handgun/reload/survivor-reload_handgun_13.png
# 'player_survivor_reload_handgun_14' - 209x154px - player/handgun/reload/survivor-reload_handgun_14.png
# 'player_survivor_reload_handgun_2' - 210x156px - player/handgun/reload/survivor-reload_handgun_2.png
# 'player_survivor_reload_handgun_3' - 212x158px - player/handgun/reload/survivor-reload_handgun_3.png
# 'player_survivor_reload_handgun_4' - 212x160px - player/handgun/reload/survivor-reload_handgun_4.png
# 'player_survivor_reload_handgun_5' - 214x163px - player/handgun/reload/survivor-reload_handgun_5.png
# 'player_survivor_reload_handgun_6' - 211x166px - player/handgun/reload/survivor-reload_handgun_6.png
# 'player_survivor_reload_handgun_7' - 208x169px - player/handgun/reload/survivor-reload_handgun_7.png
# 'player_survivor_reload_handgun_8' - 206x172px - player/handgun/reload/survivor-reload_handgun_8.png
# 'player_survivor_reload_handgun_9' - 207x168px - player/handgun/reload/survivor-reload_handgun_9.png
# 'player_survivor_reload_rifle_0' - 259x153px - player/rifle/reload/survivor-reload_rifle_0.png
# 'player_survivor_reload_rifle_1' - 260x154px - player/rifle/reload/survivor-reload_rifle_1.png
# 'player_survivor_reload_rifle_10' - 264x158px - player/rifle/reload/survivor-reload_rifle_10.png
# 'player_survivor_reload_rifle_11' - 262x159px - player/rifle/reload/survivor-reload_rifle_11.png
# 'player_survivor_reload_rifle_12' - 259x161px - player/rifle/reload/survivor-reload_rifle_12.png
# 'player_survivor_reload_rifle_13' - 257x161px - player/rifle/reload/survivor-reload_rifle_13.png
# 'player_survivor_reload_rifle_14' - 258x160px - player/rifle/reload/survivor-reload_rifle_14.png
# 'player_survivor_reload_rifle_15' - 258x159px - player/rifle/reload/survivor-reload_rifle_15.png
# 'player_survivor_reload_rifle_16' - 259x157px - player/rifle/reload/survivor-reload_rifle_16.png
# 'player_survivor_reload_rifle_17' - 259x156px - player/rifle/reload/survivor-reload_rifle_17.png
# 'player_survivor_reload_rifle_18' - 259x154px - player/rifle/reload/survivor-reload_rifle_18.png
# 'player_survivor_reload_rifle_19' - 259x153px - player/rifle/reload/survivor-reload_rifle_19.png
# 'player_survivor_reload_rifle_2' - 263x156px - player/rifle/reload/survivor-reload_rifle_2.png
# 'player_survivor_reload_rifle_3' - 265x159px - player/rifle/reload/survivor-reload_rifle_3.png
# 'player_survivor_reload_rifle_4' - 266x160px - player/rifle/reload/survivor-reload_rifle_4.png
# 'player_survivor_reload_rifle_5' - 268x161px - player/rifle/reload/survivor-reload_rifle_5.png
# 'player_survivor_reload_rifle_6' - 267x160px - player/rifle/reload/survivor-reload_rifle_6.png
# 'player_survivor_reload_rifle_7' - 266x160px - player/rifle/reload/survivor-reload_rifle_7.png
# 'player_survivor_reload_rifle_8' - 266x159px - player/rifle/reload/survivor-reload_rifle_8.png
# 'player_survivor_reload_rifle_9' - 265x159px - player/rifle/reload/survivor-reload_rifle_9.png
# 'player_survivor_reload_shotgun_0' - 259x153px - player/shotgun/reload/survivor-reload_shotgun_0.png
# 'player_survivor_reload_shotgun_1' - 260x154px - player/shotgun/reload/survivor-reload_shotgun_1.png
# 'player_survivor_reload_shotgun_10' - 264x158px - player/shotgun/reload/survivor-reload_shotgun_10.png
# 'player_survivor_reload_shotgun_11' - 262x159px - player/shotgun/reload/survivor-reload_shotgun_11.png
# 'player_survivor_reload_shotgun_12' - 259x161px - player/shotgun/reload/survivor-reload_shotgun_12.png
# 'player_survivor_reload_shotgun_13' - 257x161px - player/shotgun/reload/survivor-reload_shotgun_13.png
# 'player_survivor_reload_shotgun_14' - 258x160px - player/shotgun/reload/survivor-reload_shotgun_14.png
# 'player_survivor_reload_shotgun_15' - 258x159px - player/shotgun/reload/survivor-reload_shotgun_15.png
# 'player_survivor_reload_shotgun_16' - 259x157px - player/shotgun/reload/survivor-reload_shotgun_16.png
# 'player_survivor_reload_shotgun_17' - 259x156px - player/shotgun/reload/survivor-reload_shotgun_17.png
# 'player_survivor_reload_shotgun_18' - 259x154px - player/shotgun/reload/survivor-reload_shotgun_18.png
# 'player_survivor_reload_shotgun_19' - 259x153px - player/shotgun/reload/survivor-reload_shotgun_19.png
# 'player_survivor_reload_shotgun_2' - 263x156px - player/shotgun/reload/survivor-reload_shotgun_2.png
# 'player_survivor_reload_shotgun_3' - 265x159px - player/shotgun/reload/survivor-reload_shotgun_3.png
# 'player_survivor_reload_shotgun_4' - 267x160px - player/shotgun/reload/survivor-reload_shotgun_4.png
# 'player_survivor_reload_shotgun_5' - 268x161px - player/shotgun/reload/survivor-reload_shotgun_5.png
# 'player_survivor_reload_shotgun_6' - 267x160px - player/shotgun/reload/survivor-reload_shotgun_6.png
# 'player_survivor_reload_shotgun_7' - 266x160px - player/shotgun/reload/survivor-reload_shotgun_7.png
# 'player_survivor_reload_shotgun_8' - 266x159px - player/shotgun/reload/survivor-reload_shotgun_8.png
# 'player_survivor_reload_shotgun_9' - 265x159px - player/shotgun/reload/survivor-reload_shotgun_9.png
# 'player_survivor_run_0' - 176x100px - player/feet/run/survivor-run_0.png
# 'player_survivor_run_1' - 167x100px - player/feet/run/survivor-run_1.png
# 'player_survivor_run_10' - 176x100px - player/feet/run/survivor-run_10.png
# 'player_survivor_run_11' - 168x100px - player/feet/run/survivor-run_11.png
# 'player_survivor_run_12' - 149x100px - player/feet/run/survivor-run_12.png
# 'player_survivor_run_13' - 126x100px - player/feet/run/survivor-run_13.png
# 'player_survivor_run_14' - 104x100px - player/feet/run/survivor-run_14.png
# 'player_survivor_run_15' - 84x100px - player/feet/run/survivor-run_15.png
# 'player_survivor_run_16' - 105x100px - player/feet/run/survivor-run_16.png
# 'player_survivor_run_17' - 126x100px - player/feet/run/survivor-run_17.png
# 'player_survivor_run_18' - 149x100px - player/feet/run/survivor-run_18.png
# 'player_survivor_run_19' - 167x100px - player/feet/run/survivor-run_19.png
# 'player_survivor_run_2' - 149x100px - player/feet/run/survivor-run_2.png
# 'player_survivor_run_3' - 126x100px - player/feet/run/survivor-run_3.png
# 'player_survivor_run_4' - 105x100px - player/feet/run/survivor-run_4.png
# 'player_survivor_run_5' - 84x100px - player/feet/run/survivor-run_5.png
# 'player_survivor_run_6' - 104x100px - player/feet/run/survivor-run_6.png
# 'player_survivor_run_7' - 126x100px - player/feet/run/survivor-run_7.png
# 'player_survivor_run_8' - 149x100px - player/feet/run/survivor-run_8.png
# 'player_survivor_run_9' - 168x100px - player/feet/run/survivor-run_9.png
# 'player_survivor_shoot_handgun_0' - 210x154px - player/handgun/shoot/survivor-shoot_handgun_0.png
# 'player_survivor_shoot_handgun_1' - 200x154px - player/handgun/shoot/survivor-shoot_handgun_1.png
# 'player_survivor_shoot_handgun_2' - 205x154px - player/handgun/shoot/survivor-shoot_handgun_2.png
# 'player_survivor_shoot_rifle_0' - 259x153px - player/rifle/shoot/survivor-shoot_rifle_0.png
# 'player_survivor_shoot_rifle_1' - 253x153px - player/rifle/shoot/survivor-shoot_rifle_1.png
# 'player_survivor_shoot_rifle_2' - 255x153px - player/rifle/shoot/survivor-shoot_rifle_2.png
# 'player_survivor_shoot_shotgun_0' - 259x153px - player/shotgun/shoot/survivor-shoot_shotgun_0.png
# 'player_survivor_shoot_shotgun_1' - 253x153px - player/shotgun/shoot/survivor-shoot_shotgun_1.png
# 'player_survivor_shoot_shotgun_2' - 255x153px - player/shotgun/shoot/survivor-shoot_shotgun_2.png
# 'player_survivor_strafe_left_0' - 130x144px - player/feet/strafe_left/survivor-strafe_left_0.png
# 'player_survivor_strafe_left_1' - 130x140px - player/feet/strafe_left/survivor-strafe_left_1.png
# 'player_survivor_strafe_left_10' - 130x78px - player/feet/strafe_left/survivor-strafe_left_10.png
# 'player_survivor_strafe_left_11' - 130x80px - player/feet/strafe_left/survivor-strafe_left_11.png
# 'player_survivor_strafe_left_12' - 130x84px - player/feet/strafe_left/survivor-strafe_left_12.png
# 'player_survivor_strafe_left_13' - 130x88px - player/feet/strafe_left/survivor-strafe_left_13.png
# 'player_survivor_strafe_left_14' - 130x94px - player/feet/strafe_left/survivor-strafe_left_14.png
# 'player_survivor_strafe_left_15' - 130x103px - player/feet/strafe_left/survivor-strafe_left_15.png
# 'player_survivor_strafe_left_16' - 130x114px - player/feet/strafe_left/survivor-strafe_left_16.png
# 'player_survivor_strafe_left_17' - 130x124px - player/feet/strafe_left/survivor-strafe_left_17.png
# 'player_survivor_strafe_left_18' - 130x133px - player/feet/strafe_left/survivor-strafe_left_18.png
# 'player_survivor_strafe_left_19' - 130x140px - player/feet/strafe_left/survivor-strafe_left_19.png
# 'player_survivor_strafe_left_2' - 130x133px - player/feet/strafe_left/survivor-strafe_left_2.png
# 'player_survivor_strafe_left_3' - 130x124px - player/feet/strafe_left/survivor-strafe_left_3.png
# 'player_survivor_strafe_left_4' - 130x114px - player/feet/strafe_left/survivor-strafe_left_4.png
# 'player_survivor_strafe_left_5' - 130x103px - player/feet/strafe_left/survivor-strafe_left_5.png
# 'player_survivor_strafe_left_6' - 130x94px - player/feet/strafe_left/survivor-strafe_left_6.png
# 'player_survivor_strafe_left_7' - 130x88px - player/feet/strafe_left/survivor-strafe_left_7.png
# 'player_survivor_strafe_left_8' - 130x84px - player/feet/strafe_left/survivor-strafe_left_8.png
# 'player_survivor_strafe_left_9' - 130x80px - player/feet/strafe_left/survivor-strafe_left_9.png
# 'player_survivor_strafe_right_0' - 129x147px - player/feet/strafe_right/survivor-strafe_right_0.png
# 'player_survivor_strafe_right_1' - 129x143px - player/feet/strafe_right/survivor-strafe_right_1.png
# 'player_survivor_strafe_right_10' - 129x70px - player/feet/strafe_right/survivor-strafe_right_10.png
# 'player_survivor_strafe_right_11' - 129x72px - player/feet/strafe_right/survivor-strafe_right_11.png
# 'player_survivor_strafe_right_12' - 129x78px - player/feet/strafe_right/survivor-strafe_right_12.png
# 'player_survivor_strafe_right_13' - 129x82px - player/feet/strafe_right/survivor-strafe_right_13.png
# 'player_survivor_strafe_right_14' - 129x91px - player/feet/strafe_right/survivor-strafe_right_14.png
# 'player_survivor_strafe_right_15' - 129x103px - player/feet/strafe_right/survivor-strafe_right_15.png
# 'player_survivor_strafe_right_16' - 129x114px - player/feet/strafe_right/survivor-strafe_right_16.png
# 'player_survivor_strafe_right_17' - 129x126px - player/feet/strafe_right/survivor-strafe_right_17.png
# 'player_survivor_strafe_right_18' - 129x135px - player/feet/strafe_right/survivor-strafe_right_18.png
# 'player_survivor_strafe_right_19' - 129x143px - player/feet/strafe_right/survivor-strafe_right_19.png
# 'player_survivor_strafe_right_2' - 129x135px - player/feet/strafe_right/survivor-strafe_right_2.png
# 'player_survivor_strafe_right_3' - 129x126px - player/feet/strafe_right/survivor-strafe_right_3.png
# 'player_survivor_strafe_right_4' - 129x114px - player/feet/strafe_right/survivor-strafe_right_4.png
# 'player_survivor_strafe_right_5' - 129x103px - player/feet/strafe_right/survivor-strafe_right_5.png
# 'player_survivor_strafe_right_6' - 129x91px - player/feet/strafe_right/survivor-strafe_right_6.png
# 'player_survivor_strafe_right_7' - 129x82px - player/feet/strafe_right/survivor-strafe_right_7.png
# 'player_survivor_strafe_right_8' - 129x78px - player/feet/strafe_right/survivor-strafe_right_8.png
# 'player_survivor_strafe_right_9' - 129x72px - player/feet/strafe_right/survivor-strafe_right_9.png
# 'player_survivor_walk_0' - 146x100px - player/feet/walk/survivor-walk_0.png
# 'player_survivor_walk_1' - 140x100px - player/feet/walk/survivor-walk_1.png
# 'player_survivor_walk_10' - 145x100px - player/feet/walk/survivor-walk_10.png
# 'player_survivor_walk_11' - 139x100px - player/feet/walk/survivor-walk_11.png
# 'player_survivor_walk_12' - 126x100px - player/feet/walk/survivor-walk_12.png
# 'player_survivor_walk_13' - 109x100px - player/feet/walk/survivor-walk_13.png
# 'player_survivor_walk_14' - 93x100px - player/feet/walk/survivor-walk_14.png
# 'player_survivor_walk_15' - 78x100px - player/feet/walk/survivor-walk_15.png
# 'player_survivor_walk_16' - 94x100px - player/feet/walk/survivor-walk_16.png
# 'player_survivor_walk_17' - 111x100px - player/feet/walk/survivor-walk_17.png
# 'player_survivor_walk_18' - 127x100px - player/feet/walk/survivor-walk_18.png
# 'player_survivor_walk_19' - 140x100px - player/feet/walk/survivor-walk_19.png
# 'player_survivor_walk_2' - 127x100px - player/feet/walk/survivor-walk_2.png
# 'player_survivor_walk_3' - 111x100px - player/feet/walk/survivor-walk_3.png
# 'player_survivor_walk_4' - 94x100px - player/feet/walk/survivor-walk_4.png
# 'player_survivor_walk_5' - 78x100px - player/feet/walk/survivor-walk_5.png
# 'player_survivor_walk_6' - 93x100px - player/feet/walk/survivor-walk_6.png
# 'player_survivor_walk_7' - 109x100px - player/feet/walk/survivor-walk_7.png
# 'player_survivor_walk_8' - 126x100px - player/feet/walk/survivor-walk_8.png
# 'player_survivor_walk_9' - 139x100px - player/feet/walk/survivor-walk_9.png
