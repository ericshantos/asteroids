from .interfaces import IBulletFactory
from .bullet import Bullet

from typing import Tuple

from ..stage import Stage

class BulletFactory(IBulletFactory):
    def create_bullet(self, position: Tuple[float, float], heading: float, shooter: str, ttl: float, velocity: float, stage: Stage) -> Bullet:
        return Bullet(position, heading, shooter, ttl, velocity, stage)
