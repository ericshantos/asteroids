import random

from ..util import Vector2d, VectorSprite


class ShipExplosion:
    def __init__(self, ship):
        self.ship = ship
        self.shape = [
            [(0, -10), (6, 10)],
            [(6, 10), (3, 7)],
            [(3, 7), (-3, 7)],
            [(-3, 7), (-6, 10)],
            [(-6, 10), (0, -10)]
        ]

    def explode(self):
        for s in self.shape:
            self.ship.add_ship_debris(s)

    # Create a piece of ship debris
    def add_ship_debris(self, point_list):
        heading = Vector2d(0, 0)
        position = Vector2d(self.ship.position.x, self.ship.position.y)
        debris = VectorSprite(position, heading, point_list, self.ship.angle)

        self.ship.stage.add_sprite_with_bounding(debris)

        # Calc a velocity moving away from the ship's center
        center_x = debris.boundingRect.centerx
        center_y = debris.boundingRect.centery

        # Alter the random values below to change the rate of expansion
        debris.heading.x = (
            (center_x - position.x) + 0.1
        ) / random.uniform(20, 40)
        debris.heading.y = (
            (center_y - self.ship.position.y) + 0.1
        ) / random.uniform(20, 40)
        self.ship.ship_debris_list.append(debris)
        