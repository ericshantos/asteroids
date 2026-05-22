from enum import Enum
from pathlib import Path
from ..constants import res_dir


import pygame


class Font(Enum):
    F15 = ("Hyperspace.otf", 15)
    F20 = ("Hyperspace.otf", 20)
    F32 = ("Hyperspace.otf", 32)
    F45 = ("Hyperspace.otf", 45)
    F64 = ("Hyperspace.otf", 64)

    def get_font(self):
        font_name, font_size = self.value
        return pygame.font.Font(res_dir / font_name, font_size)
        