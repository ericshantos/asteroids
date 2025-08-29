from .interfaces import IBulletFactory
from .bullet import Bullet
from ..stage import Stage
from ..stage.rederer import Renderable

from typing import List, Tuple

class BulletManager:
    def __init__(self, stage: Stage, max_bullets: int):
        self.stage = stage
        self.max_bullets = max_bullets
        self.bullets: List[Bullet] = []

    def fire_bullet(self, position: Tuple[float, float], heading: float, shooter: str, ttl: float, velocity: float, factory: IBulletFactory) -> bool:
        if len(self.bullets) >= self.max_bullets:
            return False
        new_bullet = factory.create_bullet(position, heading, shooter, ttl, velocity, self.stage)
        self.bullets.append(new_bullet)
        self.stage.add_sprite(new_bullet)
        return True

    def bullet_collision(self, target: Renderable) -> bool:
        collision_detected = False
        for bullet in self.bullets:
            if bullet.ttl > 0 and target.collides_with(bullet):
                collision_detected = True
                bullet.ttl = 0
        return collision_detected
