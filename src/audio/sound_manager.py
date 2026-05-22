import pygame
from pathlib import Path
from ..constants import res_dir
import random


class SoundManager:
    
    def __init__(self):
        pygame.mixer.init()
        
        self.sounds = {}
        
        self._load_sounds()
    
    def _load_sounds(self):
        sound_files = {
            'explode1': 'EXPLODE1.WAV',
            'explode2': 'EXPLODE2.WAV',
            'explode3': 'EXPLODE3.WAV',
            'fire': 'FIRE.WAV',
            'life': 'LIFE.WAV',
            'saucer_small': 'SSAUCER.WAV',
            'saucer_large': 'LSAUCER.WAV',
            'thrust': 'THRUST.WAV'
        }
        
        for sound_name, filename in sound_files.items():
            try:
                sound_path = res_dir / filename
                if sound_path.exists():
                    self.sounds[sound_name] = pygame.mixer.Sound(str(sound_path))
                else:
                    print(f"Warning: Sound file not found: {sound_path}")
                    self.sounds[sound_name] = None
            except Exception as e:
                print(f"Error loading sound {filename}: {e}")
                self.sounds[sound_name] = None
    
    def play_explosion(self):
        explosion_sound = random.choice(['explode1', 'explode2', 'explode3'])
        self._play_sound(explosion_sound)
    
    def play_shoot(self):
        self._play_sound('fire')
    
    def play_extra_life(self):
        self._play_sound('life')
    
    def play_saucer_appear(self, size_type: str):
        if size_type == "small":
            self._play_sound('saucer_small')
        else:
            self._play_sound('saucer_large')
    
    def play_thrust(self):
        self._play_sound('thrust')
    
    def _play_sound(self, sound_name):
        sound = self.sounds.get(sound_name)
        if sound is not None:
            sound.play()
