"""Système de boutique d'armes"""
import pygame
from menu import Button


class ShopItem:
    """Article de la boutique"""
    
    def __init__(self, name, weapon_key, description, price, damage, fire_rate, special=""):
        self.name = name
        self.weapon_key = weapon_key
        self.description = description
        self.price = price
        self.damage = damage
        self.fire_rate = fire_rate
        self.special = special
        self.owned = False


class Shop:
    """Boutique d'armes"""
    
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        self.title_font = pygame.font.Font(None, 60)
        self.font = pygame.font.Font(None, 28)
        self.small_font = pygame.font.Font(None, 22)
        
        # Articles disponibles - Armes américaines
        self.items = [
            ShopItem("M9 Beretta", "handgun", "Standard US Army sidearm", 0, 20, 4, "FREE"),
            ShopItem("KA-BAR Knife", "knife", "USMC combat knife", 0, 50, 2, "FREE"),
            ShopItem("M4 Carbine", "rifle", "Full-auto assault rifle", 300, 15, 10, "Auto"),
            ShopItem("M870 Shotgun", "shotgun", "Massive close-range damage", 500, 12, 1.2, "8 pellets"),
            ShopItem("MP5 SMG", "smg", "High rate of fire", 750, 10, 15, "Fast"),
            ShopItem("M24 Sniper", "sniper", "One shot, one kill", 1000, 80, 0.8, "Precision"),
            ShopItem("M203 Grenade", "grenade", "Explosive area damage", 1500, 100, 0.5, "Explosive"),
            ShopItem("M134 Minigun", "minigun", "Devastating firepower", 2500, 8, 25, "Suppression"),
        ]
        
        # Les 2 premières armes sont gratuites et déjà possédées
        self.items[0].owned = True
        self.items[1].owned = True
        
        # Boutons
        self.item_buttons = []
        self._create_item_buttons()
        
        self.back_button = Button(20, self.screen_height - 70, 150, 50, "BACK",
                                  color=(60, 60, 60), hover_color=(90, 90, 90))
        
        self.player_data = None
        self.message = ""
        self.message_timer = 0
        self.message_color = (255, 255, 255)
        
        # Scroll
        self.scroll_y = 0
        self.max_scroll = 0
    
    def set_player_data(self, player_data):
        """Définit les données du joueur"""
        self.player_data = player_data
        
        # Mettre à jour les armes possédées
        for item in self.items:
            if item.weapon_key in player_data.owned_weapons:
                item.owned = True
    
    def _create_item_buttons(self):
        """Crée les boutons pour les articles"""
        self.item_buttons = []
        start_y = 130
        item_height = 100
        
        for i, item in enumerate(self.items):
            y = start_y + i * (item_height + 15)
            
            if item.owned:
                color = (50, 100, 50)
                hover_color = (70, 120, 70)
            else:
                color = (70, 100, 140)
                hover_color = (90, 130, 170)
            
            button = Button(50, y, self.screen_width - 100, item_height, "",
                           color=color, hover_color=hover_color)
            self.item_buttons.append((button, item))
        
        # Calculer le scroll maximum
        total_height = len(self.items) * (item_height + 15) + start_y + 100
        self.max_scroll = max(0, total_height - self.screen_height)
    
    def update(self, dt):
        """Met à jour le shop"""
        mouse_pos = pygame.mouse.get_pos()
        
        # Appliquer le scroll aux positions de souris pour les boutons
        adjusted_mouse = (mouse_pos[0], mouse_pos[1] + self.scroll_y)
        
        for button, item in self.item_buttons:
            # Ajuster la position du bouton pour le scroll
            original_y = button.rect.y
            button.rect.y -= self.scroll_y
            button.update(mouse_pos)
            button.rect.y = original_y
        
        self.back_button.update(mouse_pos)
        
        # Timer du message
        if self.message_timer > 0:
            self.message_timer -= dt
            if self.message_timer <= 0:
                self.message = ""
        
        # Mettre à jour les couleurs des boutons
        for button, item in self.item_buttons:
            if item.owned:
                button.color = (50, 100, 50)
                button.hover_color = (70, 120, 70)
            else:
                button.color = (70, 100, 140)
                button.hover_color = (90, 130, 170)
    
    def handle_event(self, event):
        """Gère les événements"""
        # Scroll avec la molette
        if event.type == pygame.MOUSEWHEEL:
            self.scroll_y -= event.y * 30
            self.scroll_y = max(0, min(self.scroll_y, self.max_scroll))
        
        if self.back_button.is_clicked(event):
            return "back"
        
        for button, item in self.item_buttons:
            # Ajuster pour le scroll
            original_y = button.rect.y
            button.rect.y -= self.scroll_y
            clicked = button.is_clicked(event)
            button.rect.y = original_y
            
            if clicked:
                return self._buy_item(item)
        
        return None
    
    def _buy_item(self, item):
        """Tente d'acheter un article"""
        if item.owned:
            self.message = f"{item.name} - Already owned!"
            self.message_color = (255, 200, 100)
            self.message_timer = 2.0
            return None
        
        if not self.player_data:
            return None
        
        if self.player_data.gold >= item.price:
            self.player_data.gold -= item.price
            self.player_data.owned_weapons.add(item.weapon_key)
            item.owned = True
            
            self.message = f"{item.name} purchased!"
            self.message_color = (100, 255, 100)
            self.message_timer = 2.0
            return "purchased"
        else:
            needed = item.price - self.player_data.gold
            self.message = f"Not enough funds! Need ${needed} more"
            self.message_color = (255, 100, 100)
            self.message_timer = 2.0
            return None
    
    def draw(self):
        """Dessine la boutique"""
        # Fond avec dégradé militaire
        for y in range(self.screen_height):
            ratio = y / self.screen_height
            r = int(25 + ratio * 15)
            g = int(35 + ratio * 20)
            b = int(25 + ratio * 15)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (self.screen_width, y))
        
        # Bande supérieure avec motif drapeau
        pygame.draw.rect(self.screen, (0, 40, 104), (0, 0, self.screen_width, 90))
        
        # Étoiles décoratives
        for i in range(8):
            x = 50 + i * 120
            self._draw_star(x, 45, 12, (255, 255, 255))
        
        # Titre
        title = self.title_font.render("Armurerie du bataillon", True, (255, 215, 0))
        title_rect = title.get_rect(center=(self.screen_width // 2, 45))
        self.screen.blit(title, title_rect)
        
        # Sous-titre
        subtitle = self.small_font.render("Aux armes, soldat !", True, (200, 200, 200))
        subtitle_rect = subtitle.get_rect(center=(self.screen_width // 2, 75))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Afficher l'or
        if self.player_data:
            gold_bg = pygame.Rect(self.screen_width - 180, 100, 165, 45)
            pygame.draw.rect(self.screen, (20, 40, 20), gold_bg, border_radius=8)
            pygame.draw.rect(self.screen, (255, 215, 0), gold_bg, 2, border_radius=8)
            
            gold_text = self.font.render(f"$ {self.player_data.gold:,}", True, (255, 215, 0))
            gold_rect = gold_text.get_rect(center=gold_bg.center)
            self.screen.blit(gold_text, gold_rect)
        
        # Zone de scroll pour les items
        clip_rect = pygame.Rect(0, 100, self.screen_width, self.screen_height - 180)
        self.screen.set_clip(clip_rect)
        
        # Dessiner les articles
        for button, item in self.item_buttons:
            # Appliquer le scroll
            draw_y = button.rect.y - self.scroll_y
            
            # Ne dessiner que si visible
            if draw_y + button.rect.height > 100 and draw_y < self.screen_height - 80:
                # Dessiner le bouton avec offset
                temp_rect = button.rect.copy()
                button.rect.y = draw_y
                button.draw(self.screen)
                button.rect = temp_rect
                
                # Contenu de l'article
                self._draw_item(item, 50, draw_y, self.screen_width - 100, button.rect.height)
        
        self.screen.set_clip(None)
        
        # Indicateur de scroll
        if self.max_scroll > 0:
            scroll_ratio = self.scroll_y / self.max_scroll
            indicator_height = 50
            indicator_y = 100 + scroll_ratio * (self.screen_height - 280 - indicator_height)
            pygame.draw.rect(self.screen, (100, 100, 100), 
                           (self.screen_width - 15, indicator_y, 10, indicator_height), 
                           border_radius=5)
        
        # Message de feedback
        if self.message:
            msg_surface = self.font.render(self.message, True, self.message_color)
            msg_rect = msg_surface.get_rect(center=(self.screen_width // 2, self.screen_height - 110))
            
            # Fond du message
            bg_rect = msg_rect.inflate(30, 15)
            pygame.draw.rect(self.screen, (0, 0, 0), bg_rect, border_radius=8)
            pygame.draw.rect(self.screen, self.message_color, bg_rect, 2, border_radius=8)
            self.screen.blit(msg_surface, msg_rect)
        
        # Bouton retour
        self.back_button.draw(self.screen)
    
    def _draw_star(self, x, y, size, color):
        """Dessine une étoile à 5 branches"""
        import math
        points = []
        for i in range(5):
            angle = math.radians(-90 + i * 72)
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append((px, py))
            angle = math.radians(-90 + i * 72 + 36)
            px = x + size * 0.4 * math.cos(angle)
            py = y + size * 0.4 * math.sin(angle)
            points.append((px, py))
        if len(points) >= 3:
            pygame.draw.polygon(self.screen, color, points)
    
    def _draw_item(self, item, x, y, width, height):
        """Dessine un article"""
        # Icône d'arme
        icon_rect = pygame.Rect(x + 15, y + 15, 70, 70)
        if item.owned:
            icon_color = (34, 85, 34)
            border_color = (100, 200, 100)
        else:
            icon_color = (60, 60, 80)
            border_color = (100, 100, 150)
        
        pygame.draw.rect(self.screen, icon_color, icon_rect, border_radius=10)
        pygame.draw.rect(self.screen, border_color, icon_rect, 2, border_radius=10)
        
        # Symbole de l'arme
        icon_text = self.font.render(item.name[0], True, (255, 255, 255))
        icon_text_rect = icon_text.get_rect(center=icon_rect.center)
        self.screen.blit(icon_text, icon_text_rect)
        
        # Nom de l'arme
        name_color = (100, 255, 100) if item.owned else (255, 255, 255)
        name_text = self.font.render(item.name, True, name_color)
        self.screen.blit(name_text, (x + 100, y + 15))
        
        # Description
        desc_text = self.small_font.render(item.description, True, (180, 180, 180))
        self.screen.blit(desc_text, (x + 100, y + 42))
        
        # Stats
        stats_text = self.small_font.render(
            f"DMG: {item.damage}  |  ROF: {item.fire_rate}/s  |  {item.special}", 
            True, (150, 200, 255)
        )
        self.screen.blit(stats_text, (x + 100, y + 65))
        
        # Prix ou statut
        if item.owned:
            status_text = self.font.render("OWNED", True, (100, 255, 100))
        else:
            status_text = self.font.render(f"$ {item.price:,}", True, (255, 215, 0))
        
        status_rect = status_text.get_rect(right=x + width - 20, centery=y + height // 2)
        self.screen.blit(status_text, status_rect)
