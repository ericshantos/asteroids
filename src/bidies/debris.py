import random

from ..util import Point, Vector2d

def clamp(value, min_value=0, max_value=255):
    return max(min_value, min(value, max_value))

class Debris(Point):    
    def __init__(self, position, stage, ttl=80):
        heading = Vector2d(random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5))
        super().__init__(position, heading, stage)
        self.ttl = ttl

    def move(self):    
        super().move()
        r, g, b = self.color
        r = clamp(r - 5)
        g = clamp(g - 5)
        b = clamp(b - 5)
        self.color = (r, g, b)

        if r == 0 and g == 0 and b == 0:
            self.stage.remove_sprite(self)
