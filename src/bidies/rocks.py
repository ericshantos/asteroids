import random

from .datas import RockData

from ..util import VectorSprite, Vector2d


class Rock(VectorSprite):
    
    # Create the rock polygon to the given scale
    def __init__(self, position, rock_type, data = None):
        if data is None:
            data = RockData()
        scale = data.scale[rock_type]
        velocity = data.velocities[rock_type]
        heading = Vector2d(random.uniform(-velocity, velocity), random.uniform(-velocity, velocity))
        
        # Ensure that the rocks don't just sit there or move along regular lines
        if heading.x == 0: heading.x = 0.1
        if heading.y == 0: heading.y = 0.1
                        
        self.data = data
        self.rock_type = rock_type
        new_point_list = [self.scale(point, scale) for point in self.create_point_list()]
        
        super().__init__(position, heading, new_point_list)


    # Create different rock type pointlists
    def create_point_list(self):
        
        if (self.data.rock_shape == 1):
            point_list = [(-4,-12), (6,-12), (13, -4), (13, 5), (6, 13), (0,13), (0,4),\
                     (-8,13), (-15, 4), (-7,1), (-15,-3)]
 
        elif (self.data.rock_shape == 2):
            point_list = [(-6,-12), (1,-5), (8, -12), (15, -5), (12,0), (15,6), (5,13),\
                         (-7,13), (-14,7), (-14,-5)]
            
        elif (self.data.rock_shape == 3):
            point_list = [(-7,-12), (1,-9), (8,-12), (15,-5), (8,-3), (15,4), (8,12),\
                         (-3,10), (-6,12), (-14,7), (-10,0), (-14,-5)]            

        elif (self.data.rock_shape == 4):
            point_list = [(-7,-11), (3,-11), (13,-5), (13,-2), (2,2), (13,8), (6,14),\
                         (2,10), (-7,14), (-15,5), (-15,-5), (-5,-5), (-7,-11)]

        self.data.rock_shape += 1
        if (self.data.rock_shape == 5):
            self.data.rock_shape = 1

        return point_list
    
    # Spin the rock when it moves
    def move(self):
        super().move()                        
        
        # Original Asteroid didn't have spinning rocks but they look nicer
        self.angle += 1
