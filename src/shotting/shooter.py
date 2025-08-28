from ..util import Vector2d, VectorSprite

from .bullet_manager import BulletManager
from .bullet_factory import BulletFactory


class Shooter(VectorSprite):
    def __init__(self, position, heading, pointlist, stage, max_bullet = 3):
        super().__init__(position, heading, pointlist)
        self.stage = stage
        self.bullet_manager = BulletManager(stage, max_bullet)
        self.bullet_factory = BulletFactory()
        self.bullets = self.bullet_manager.bullets

    def fire_bullet(self, heading, ttl, velocity):
        position = Vector2d(self.position.x, self.position.y)
        return self.bullet_manager.fire_bullet(
            position, heading, self, ttl, velocity, self.bullet_factory
        )

    def bullet_collision(self, target):
        return self.bullet_manager.bullet_collision(target)
    