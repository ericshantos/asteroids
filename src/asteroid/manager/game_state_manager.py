from typing import Callable


class GameStateManager:
    def __init__(self):
        self.state: str = "attract_mode"
        self.exploding_count: int = 0

    def set_state(self, new_state: str) -> None:
        self.state = new_state

    def update_exploding(self, ttl: int, on_explode_done: Callable) -> None:
        self.exploding_count += 1
        if self.exploding_count > ttl:
            self.set_state("playing")
            self.exploding_count = 0
            on_explode_done()
