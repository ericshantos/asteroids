from ...ship import Ship, ship_data
from ...stage import Stage

from typing import Optional

class ShipManager:
    def __init__(self, stage: Stage):
        self.stage = stage
        self.ship: Optional[Ship] = None
        self.lives: int = 0
        self.lives_list: list[Ship] = []
        self.start_lives: int = 5

    def create_new_ship(self) -> None:
        if self.ship:
            [self.stage.remove_sprite(debris) for debris in self.ship.ship_debris_list]
        self.ship = Ship(self.stage, data=ship_data)
        self.stage.add_sprite(self.ship.thrust_jet)
        self.stage.add_sprite(self.ship)

    def create_lives_list(self) -> None:
        self.lives = 0
        self.lives_list = []
        for i in range(1, self.start_lives):
            self.add_life(i)

    def add_life(self, life_number: int) -> None:
        self.lives += 1
        ship = Ship(self.stage, data=ship_data)
        ship.position.x = self.stage.width - (life_number * ship.bounding_rect.width) - 10
        ship.position.y = ship.bounding_rect.height
        self.stage.add_sprite(ship)
        self.lives_list.append(ship)

    def remove_life(self) -> None:
        self.lives -= 1
        if self.lives_list:
            ship = self.lives_list.pop()
            self.stage.remove_sprite(ship)
