from .interfaces import IBulletFactory
from .bullet import Bullet

class BulletFactory(IBulletFactory):
    def create_bullet(self, position, heading, shooter, ttl, velocity, stage):
        return Bullet(position, heading, shooter, ttl, velocity, stage)
