from abc import ABC, abstractmethod


class Moverable(ABC):
    @abstractmethod
    def move_sprites(self):
        raise NotImplementedError

class SpriteMover(Moverable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def move_sprites(self, sprites):
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
                