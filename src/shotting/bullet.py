from ..util import Point

from typing import Tuple

class Bullet(Point):
    def __init__(self, position: Tuple[float, float], heading: float, shooter: str, ttl: float, velocity: float, stage: str):
        super().__init__(position, heading, stage)
        self.shooter = shooter
        self.ttl = ttl
        self.velocity = velocity

    def move(self) -> None:
        super().move()
        if self.ttl <= 0:
            self.shooter.bullets.remove(self)
