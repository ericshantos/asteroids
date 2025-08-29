from ..util import VectorSprite, Vector2d
from ..stage import Stage

from typing import List, Tuple


class ThrustJet(VectorSprite):
    def __init__(self, stage: Stage, ship):
        position = Vector2d(stage.width/2, stage.height/2)
        heading = Vector2d(0, 0)
        self.accelerating: bool = False
        self.ship = ship
        super().__init__(position, heading, [(-3, 7), (0, 13), (3, 7)])

    def draw(self) -> List[Tuple[int, int]]:
        if self.accelerating and self.ship.in_hyper_space == False:
            self.color = (255, 255, 255)
        else:
            self.color = (0, 0, 0)

        super().draw()
        return self.transformed_point_list
