from typing import List, Tuple
from .vector_sprite import VectorSprite

from ..stage import Stage


class Point(VectorSprite):
    def __init__(self, position: Tuple[int, int], heading: Tuple[int, int], stage: Stage):
        self.point_list: List[Tuple[int, int]] = [(0, 0), (1, 1), (1, 0), (0, 1)]

        super().__init__(position, heading, self.point_list)

        self.stage = stage
        self.ttl: int = 30

    def move(self) -> None:
        self.ttl -= 1
        if (self.ttl <= 0):
            self.stage.remove_sprite(self)

        super().move()
