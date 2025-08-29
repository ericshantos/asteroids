import random

from ...bidies import Saucer, saucer_data
from ...sound_manager import player

from typing import Optional
from ...stage import Stage
from ...ship import Ship


class SaucerManager:
    def __init__(self, stage: Stage):
        self.stage = stage
        self.saucer: Optional[Saucer] = None

    def update(self, seconds_count, ship: Ship) -> None:
        if self.saucer and self.saucer.laps >= 2:
            self.kill_saucer()

        if seconds_count % 2000 == 0 and self.saucer is None:
            rand_val = random.randrange(0, 10)
            saucer_type = saucer_data.small_saucer_type if rand_val <= 3 else saucer_data.large_saucer_type
            self.saucer = Saucer(self.stage, saucer_type, ship, data=saucer_data)
            self.stage.add_sprite(self.saucer)

    def kill_saucer(self) -> None:
        player.stop_sound("lsaucer")
        player.stop_sound("ssaucer")
        player.play_sound("explode2")
        self.stage.remove_sprite(self.saucer)
        self.saucer = None
