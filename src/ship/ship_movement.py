import math

from ..sound_manager import player

class ShipMovement:
    def __init__(self, ship):
        self.ship = ship

    def rotate_left(self):
        self.ship.angle += self.ship.data.turn_angle
        self.ship.thrust_jet.angle += self.ship.data.turn_angle

    def rotate_right(self):
        self.ship.angle -= self.ship.data.turn_angle
        self.ship.thrust_jet.angle -= self.ship.data.turn_angle

    def increase_thrust(self):
        player.play_sound_continuous("thrust")
        if math.hypot(self.ship.heading.x, self.ship.heading.y) > self.ship.data.max_velocity:
            return

        dx = self.ship.data.acceleration * math.sin(math.radians(self.ship.angle)) * -1
        dy = self.ship.data.acceleration * math.cos(math.radians(self.ship.angle)) * -1
        self.change_velocity(dx, dy)

    def decrease_thrust(self):
        player.stop_sound("thrust")
        if (self.ship.heading.x == 0 and self.ship.heading.y == 0):
            return

        dx = self.ship.heading.x * self.ship.data.deceleration
        dy = self.ship.heading.y * self.ship.data.deceleration
        self.change_velocity(dx, dy)

    def change_velocity(self, dx, dy):
        self.ship.heading.x += dx
        self.ship.heading.y += dy
        self.ship.thrust_jet.heading.x += dx
        self.ship.thrust_jet.heading.y += dy
