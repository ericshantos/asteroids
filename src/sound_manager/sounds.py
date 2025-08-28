import pygame

from ..constants import res_dir

class Sounds:
    def __init__(self, ext: str):
        self.sounds: dict = {}
        self.ext = ext

    def init_sounds_manager(self) -> None:
        pygame.mixer.init()
        for file in res_dir.iterdir():
            if file.suffix.lower() == self.ext.lower():
                self.sounds[file.stem.lower()] = pygame.mixer.Sound(res_dir / file.name)

    def get_sound(self, name: str) -> pygame.mixer.Sound:
        return self.sounds.get(name)
    