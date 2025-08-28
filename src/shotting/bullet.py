from ..util import Point

class Bullet(Point):
    def __init__(self, position, heading, shooter, ttl, velocity, stage):
        super().__init__(position, heading, stage)
        self.shooter = shooter
        self.ttl = ttl
        self.velocity = velocity

    def move(self):
        super().move()
        if self.ttl <= 0:
            self.shooter.bullets.remove(self)
