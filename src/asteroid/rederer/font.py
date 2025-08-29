from enum import Enum
import pygame

from ...constants import res_dir

from typing import Tuple

class Font(Enum):
    F15: Tuple[str, int] = ("Hyperspace.otf", 15)
    F20: Tuple[str, int] = ("Hyperspace.otf", 20)
    F30: Tuple[str, int] = ("Hyperspace.otf", 30)
    F45: Tuple[str, int] = ("Hyperspace.otf", 45)

    def get_font(self) -> pygame.font.Font:
        font_name, font_size = self.value
        return pygame.font.Font(res_dir / font_name, font_size)
