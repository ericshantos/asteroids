import math

from ..shotting import Shooter
from ..util import Vector2d, VectorSprite

from typing import List, Optional, Tuple

from .ship_movement import ShipMovement
from .ship_explosion import ShipExplosion
from .ship_hyper_space import ShipHyperSpace

from .data import ShipData
from .thrust_jet import ThrustJet

from ..sound_manager import player

class Ship(Shooter):
    def __init__(self, stage, data: Optional[ShipData] = None):
        self.in_hyper_space = False
        self.ship_debris_list: List[VectorSprite] = []
        self.visible = True
        self.data = data or ShipData()

        heading = Vector2d(0, 0)
        self.thrust_jet = ThrustJet(stage, self)
        position = Vector2d(stage.width/2, stage.height/2)
        point_list = [(0, -10), (6, 10), (3, 7), (-3, 7), (-6, 10)]

        super().__init__(position, heading, point_list, stage)
        
        self.movement = ShipMovement(self)
        self.explosion = ShipExplosion(self)
        self.hyper_space = ShipHyperSpace(self)

    def draw(self):
        if self.visible:
            if not self.in_hyper_space:
                VectorSprite.draw(self)
            else:
                self.hyper_space.update()
        return self.transformed_point_list

    def rotate_left(self):
        self.movement.rotate_left()

    def rotate_right(self):
        self.movement.rotate_right()

    def increase_thrust(self):
        self.movement.increase_thrust()

    def decrease_thrust(self):
        self.movement.decrease_thrust()

    def move(self):
        VectorSprite.move(self)
        self.movement.decrease_thrust()

    def explode(self):
        self.explosion.explode()

    def add_ship_debris(self, point_list: List[Tuple[int, int]]):
        self.explosion.add_ship_debris(point_list)

    def fire_bullet(self):
        if not self.in_hyper_space:
            vx = self.data.bullet_velocity * math.sin(math.radians(self.angle)) * -1
            vy = self.data.bullet_velocity * math.cos(math.radians(self.angle)) * -1
            heading = Vector2d(vx, vy)

            super().fire_bullet(
                heading, 
                self.data.bullet_ttl,
                self.data.bullet_velocity
            )

            player.play_sound("fire")

    def enter_hyper_space(self):
        self.hyper_space.enter()
