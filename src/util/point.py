from .vector_sprite import VectorSprite

class Point(VectorSprite):
    def __init__(self, position, heading, stage):
        self.point_list = [(0, 0), (1, 1), (1, 0), (0, 1)]

        super().__init__(position, heading, self.point_list)

        self.stage = stage
        self.ttl = 30

    def move(self):
        self.ttl -= 1
        if (self.ttl <= 0):
            self.stage.remove_sprite(self)

        super().move()
