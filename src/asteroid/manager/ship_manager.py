from ...ship import Ship, ship_data

class ShipManager:
    def __init__(self, stage):
        self.stage = stage
        self.ship = None
        self.lives = 0
        self.livesList = []
        self.startLives = 5

    def create_new_ship(self):
        if self.ship:
            [self.stage.remove_sprite(debris) for debris in self.ship.ship_debris_list]
        self.ship = Ship(self.stage, data=ship_data)
        self.stage.add_sprite(self.ship.thrust_jet)
        self.stage.add_sprite(self.ship)

    def create_lives_list(self):
        self.lives = 0
        self.livesList = []
        for i in range(1, self.startLives):
            self.add_life(i)

    def add_life(self, lifeNumber):
        self.lives += 1
        ship = Ship(self.stage, data=ship_data)
        ship.position.x = self.stage.width - (lifeNumber * ship.bounding_rect.width) - 10
        ship.position.y = ship.bounding_rect.height
        self.stage.add_sprite(ship)
        self.livesList.append(ship)

    def remove_life(self):
        self.lives -= 1
        if self.livesList:
            ship = self.livesList.pop()
            self.stage.remove_sprite(ship)
