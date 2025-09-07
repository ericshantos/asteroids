import random, math

from ..sound_manager import player
from ..shotting import Shooter
from ..util import Vector2d
from .datas import SaucerData 


class Saucer(Shooter):
    def __init__(self, stage, saucer_type, ship, data=None, max_bullets=1):
        if data is None:
            data = SaucerData()

        self.saucer_type = saucer_type
        self.ship = ship
        self.scoreValue = data.scores[saucer_type]
        self.data = data

        position = Vector2d(0.0, random.randrange(0, stage.height))
        heading = Vector2d(data.velocities[saucer_type], 0.0)

        player.stop_sound("ssaucer")
        player.stop_sound("lsaucer")
        player.play_sound_continuous(
            "lsaucer" if saucer_type == data.large_saucer_type else "ssaucer"
        )

        self.laps = 0
        self.lastx = 0
        
        # Scale the shape
        new_point_list = [self.scale(point, data.scales[saucer_type]) for point in data.point_list]
        super().__init__(position, heading, new_point_list, stage, max_bullets)

        self.rotate_and_transform()

    # Set the bullet velocity and create the bullet
    def launch_bullet(self):
        if self.ship is not None:            
            dx = self.ship.position.x - self.position.x
            dy = self.ship.position.y - self.position.y
            mag = math.sqrt(dx*dx + dy*dy)
            heading = Vector2d(self.data.bullet_velocity * (dx/mag), self.data.bullet_velocity * (dy/mag))
            shot_fired = self.fire_bullet(heading, self.data.bullet_ttl[self.saucer_type], self.data.bullet_velocity)
            
            if shot_fired: player.play_sound("sfire")

    def move(self):        
        super().move()  
        
        if (self.position.x > self.stage.width * 0.33) and (self.position.x < self.stage.width * 0.66):
            self.heading.y = self.heading.x
        else:
            self.heading.y = 0
        
        self.launch_bullet()
        
        # have we lapped?        
        if self.lastx > self.position.x:
            self.lastx = 0
            self.laps += 1
        else:
            self.lastx = self.position.x
                    