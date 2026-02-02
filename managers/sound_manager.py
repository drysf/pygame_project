"""Gestionnaire de sons synthétiques."""
import pygame
import random
import math
import array


class SoundManager:
    """Gère la création et la lecture des sons du jeu."""
    
    def __init__(self):
        """Initialise le gestionnaire de sons."""
        self.sounds = {}
        self.create_sounds()
    
    def create_sounds(self):
        """Crée tous les sons synthétiques du jeu."""
        try:
            # Son de tir
            shoot_sound = pygame.mixer.Sound(buffer=self._generate_shoot_sound())
            shoot_sound.set_volume(0.3)
            self.sounds['shoot'] = shoot_sound
            
            # Son de saut
            jump_sound = pygame.mixer.Sound(buffer=self._generate_jump_sound())
            jump_sound.set_volume(0.4)
            self.sounds['jump'] = jump_sound
            
            # Son de pas/course
            step_sound = pygame.mixer.Sound(buffer=self._generate_step_sound())
            step_sound.set_volume(0.2)
            self.sounds['step'] = step_sound
            
            # Son de dégâts
            hit_sound = pygame.mixer.Sound(buffer=self._generate_hit_sound())
            hit_sound.set_volume(0.5)
            self.sounds['hit'] = hit_sound
            
            # Son de powerup
            powerup_sound = pygame.mixer.Sound(buffer=self._generate_powerup_sound())
            powerup_sound.set_volume(0.5)
            self.sounds['powerup'] = powerup_sound
            
            # Son de mort ennemi
            enemy_death = pygame.mixer.Sound(buffer=self._generate_enemy_death_sound())
            enemy_death.set_volume(0.4)
            self.sounds['enemy_death'] = enemy_death
            
        except Exception as e:
            print(f"Erreur lors de la création des sons: {e}")
    
    def _generate_shoot_sound(self):
        """Génère un son de tir."""
        sample_rate = 22050
        duration = 0.1
        samples = int(sample_rate * duration)
        buf = array.array('h')
        
        for i in range(samples):
            t = i / sample_rate
            freq = 800 - (t * 5000)
            value = int(32767 * 0.5 * math.sin(2 * math.pi * freq * t) * (1 - t/duration))
            buf.append(value)
        
        return buf.tobytes()
    
    def _generate_jump_sound(self):
        """Génère un son de saut."""
        sample_rate = 22050
        duration = 0.15
        samples = int(sample_rate * duration)
        buf = array.array('h')
        
        for i in range(samples):
            t = i / sample_rate
            freq = 200 + (t * 600)
            value = int(32767 * 0.4 * math.sin(2 * math.pi * freq * t) * (1 - t/duration))
            buf.append(value)
        
        return buf.tobytes()
    
    def _generate_step_sound(self):
        """Génère un son de pas."""
        sample_rate = 22050
        duration = 0.08
        samples = int(sample_rate * duration)
        buf = array.array('h')
        
        for i in range(samples):
            t = i / sample_rate
            noise = random.randint(-8000, 8000)
            value = int(noise * (1 - t/duration))
            buf.append(max(-32767, min(32767, value)))
        
        return buf.tobytes()
    
    def _generate_hit_sound(self):
        """Génère un son de dégâts."""
        sample_rate = 22050
        duration = 0.2
        samples = int(sample_rate * duration)
        buf = array.array('h')
        
        for i in range(samples):
            t = i / sample_rate
            freq = 150
            noise = random.randint(-5000, 5000)
            value = int((32767 * 0.3 * math.sin(2 * math.pi * freq * t) + noise) * (1 - t/duration))
            buf.append(max(-32767, min(32767, value)))
        
        return buf.tobytes()
    
    def _generate_powerup_sound(self):
        """Génère un son de powerup."""
        sample_rate = 22050
        duration = 0.3
        samples = int(sample_rate * duration)
        buf = array.array('h')
        
        for i in range(samples):
            t = i / sample_rate
            freq = 400 + (t * 400)
            value = int(32767 * 0.4 * math.sin(2 * math.pi * freq * t))
            buf.append(value)
        
        return buf.tobytes()
    
    def _generate_enemy_death_sound(self):
        """Génère un son de mort d'ennemi."""
        sample_rate = 22050
        duration = 0.25
        samples = int(sample_rate * duration)
        buf = array.array('h')
        
        for i in range(samples):
            t = i / sample_rate
            freq = 400 - (t * 300)
            value = int(32767 * 0.4 * math.sin(2 * math.pi * freq * t) * (1 - t/duration))
            buf.append(value)
        
        return buf.tobytes()
    
    def play(self, sound_name):
        """
        Joue un son.
        
        Args:
            sound_name: Nom du son à jouer
        """
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
