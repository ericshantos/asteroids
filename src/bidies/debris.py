import random

from ..util import Point, Vector2d
from ..stage import Stage


class Debris(Point):    
    def __init__(self, position: Vector2d, stage: Stage, ttl: int = 80):
        heading = Vector2d(random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5))
        super().__init__(position, heading, stage)
        self.ttl = ttl

    def _clamp(self, value: int, min_value: int = 0, max_value: int = 255) -> int:
        return max(min_value, min(value, max_value))

    def move(self) -> None:    
        super().move()
        r, g, b = self.color
        r = self._clamp(r - 5)
        g = self._clamp(g - 5)
        b = self._clamp(b - 5)
        self.color = (r, g, b)

        if r == 0 and g == 0 and b == 0:
            self.stage.remove_sprite(self)
