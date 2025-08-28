import random

from ..util import Vector2d


class ShipHyperSpace:
    
    def __init__(self, ship):
        self.ship = ship
    
    def enter(self):
        if not self.ship.in_hyper_space:
            self.ship.in_hyper_space = True
            self.ship.hyper_space_ttl = 100
            self.ship.color = (0, 0, 0)
            self.ship.thrust_jet.color = (0, 0, 0)
    
    def update(self):
        if self.ship.in_hyper_space:
            self.ship.hyper_space_ttl -= 1
            if self.ship.hyper_space_ttl == 0:
                self.exit()
    
    def exit(self):
        self.ship.in_hyper_space = False
        self.ship.color = (255, 255, 255)
        self.ship.thrust_jet.color = (255, 255, 255)
        self.ship.position.x = random.randrange(0, self.ship.stage.width)
        self.ship.position.y = random.randrange(0, self.ship.stage.height)
        position = Vector2d(self.ship.position.x, self.ship.position.y)
        self.ship.thrust_jet.position = position
