class GameStateManager:
    def __init__(self):
        self.state = "attract_mode"
        self.explodingCount = 0

    def set_state(self, new_state):
        self.state = new_state

    def update_exploding(self, ttl, on_explode_done):
        self.explodingCount += 1
        if self.explodingCount > ttl:
            self.set_state("playing")
            self.explodingCount = 0
            on_explode_done()
