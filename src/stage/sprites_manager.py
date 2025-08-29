from typing import List

from .rederer import Renderable

class SpriteManager:
    def __init__(self):
        self.sprite_list: List[Renderable] = []

    def add_sprite(self, sprite: Renderable) -> None:
        self.sprite_list.append(sprite)

    def remove_sprite(self, sprite: Renderable) -> None:
        if sprite in self.sprite_list:
            self.sprite_list.remove(sprite)

    def get_sprites(self) -> List[Renderable]:
        return self.sprite_list
