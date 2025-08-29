from abc import ABC, abstractmethod
from typing import List

class Moverable(ABC):
    @abstractmethod
    def move_sprites(self, sprites: List) -> None:
        raise NotImplementedError

class SpriteMover(Moverable):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def move_sprites(self, sprites: List) -> None:
        for sprite in sprites:
            sprite.move()
            if sprite.position.x < 0:
                sprite.position.x = self.width
            if sprite.position.x > self.width:
                sprite.position.x = 0
            if sprite.position.y < 0:
                sprite.position.y = self.height
            if sprite.position.y > self.height:
                sprite.position.y = 0
                