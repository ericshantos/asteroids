from .interfaces import IBulletFactory

class BulletManager:
    def __init__(self, stage, max_bullets: int):
        self.stage = stage
        self.max_bullets = max_bullets
        self.bullets = []

    def fire_bullet(self, position, heading, shooter, ttl, velocity, factory: IBulletFactory):
        if len(self.bullets) >= self.max_bullets:
            return False
        new_bullet = factory.create_bullet(position, heading, shooter, ttl, velocity, self.stage)
        self.bullets.append(new_bullet)
        self.stage.add_sprite(new_bullet)
        return True

    def bullet_collision(self, target):
        collision_detected = False
        for bullet in self.bullets:
            if bullet.ttl > 0 and target.collides_with(bullet):
                collision_detected = True
                bullet.ttl = 0
        return collision_detected
