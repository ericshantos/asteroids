from ...bidies import Rock, rock_data
from ...util import Vector2d

import random

class RockManager:
    def __init__(self, stage):
        self.stage = stage
        self.rocks = []
        self.numRocks = 3

    def create_rocks(self, num):
        for _ in range(num):
            position = Vector2d(random.randrange(-10, 10), random.randrange(-10, 10))
            rock = Rock(position, rock_data.large_rock_type, data=rock_data)
            self.stage.add_sprite(rock)
            self.rocks.append(rock)

    def clear_rocks(self):
        for r in self.rocks:
            self.stage.remove_sprite(r)
        self.rocks = []

    def level_up(self):
        self.numRocks += 1
        self.create_rocks(self.numRocks)
