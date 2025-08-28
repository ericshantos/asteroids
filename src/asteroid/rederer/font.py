from enum import Enum
import pygame

from ...constants import res_dir

class Font(Enum):
    F15 = ("Hyperspace.otf", 15)
    F20 = ("Hyperspace.otf", 20)
    F30 = ("Hyperspace.otf", 30)
    F45 = ("Hyperspace.otf", 45)

    def get_font(self):
        font_name, font_size = self.value
        return pygame.font.Font(res_dir / font_name, font_size)
