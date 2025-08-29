from ...util import Vector2d
from ...bidies import Rock, Debris, rock_data
from ...sound_manager import player

from ...stage import Stage
from .ship_manager import ShipManager
from .rock_manager import RockManager
from .saucer_manager import SaucerManager

from typing import Tuple


class CollisionSystem:
    def __init__(self, stage: Stage, ship_manager: ShipManager, rock_manager: RockManager, saucer_manager: SaucerManager):
        self.stage = stage
        self.ship_manager = ship_manager
        self.rock_manager = rock_manager
        self.saucer_manager = saucer_manager

    def update(self, score: int) -> Tuple[int, bool]:
        ship = self.ship_manager.ship
        saucer = self.saucer_manager.saucer
        new_score = score
        ship_hit, saucer_hit = False, False

        # Rocks
        for rock in list(self.rock_manager.rocks):
            rock_hit = False

            if not ship.in_hyper_space and rock.collides_with(ship):
                if rock.check_polygon_collision(ship):
                    ship_hit = True
                    rock_hit = True

            if saucer and rock.collides_with(saucer):
                saucer_hit = True
                rock_hit = True

            if saucer and saucer.bullet_collision(rock):
                rock_hit = True

            if ship.bullet_collision(rock):
                rock_hit = True

            if rock_hit:
                self.rock_manager.rocks.remove(rock)
                self.stage.remove_sprite(rock)

                if rock.rock_type == rock_data.large_rock_type:
                    player.play_sound("explode1")
                    new_type = rock_data.medium_rock_type
                    new_score += 50
                elif rock.rock_type == rock_data.medium_rock_type:
                    player.play_sound("explode2")
                    new_type = rock_data.small_rock_type
                    new_score += 100
                else:
                    player.play_sound("explode3")
                    new_type = None
                    new_score += 200

                if new_type:
                    for _ in range(2):
                        position = Vector2d(rock.position.x, rock.position.y)
                        newRock = Rock(position, new_type, data=rock_data)
                        self.stage.add_sprite(newRock)
                        self.rock_manager.rocks.append(newRock)

                self.create_debris(rock)

        # Saucer collisions
        if saucer:
            if not ship.in_hyper_space and saucer.bullet_collision(ship):
                ship_hit = True
            if saucer.collides_with(ship):
                ship_hit = True
                saucer_hit = True

            if saucer_hit:
                self.create_debris(saucer)
                self.saucer_manager.kill_saucer()

        # Notifica se a nave foi atingida
        if ship_hit:
            self.kill_ship()

        return new_score, ship_hit

    def create_debris(self, sprite) -> None:
        for _ in range(25):
            debris = Debris(Vector2d(sprite.position.x, sprite.position.y), self.stage)
            self.stage.add_sprite(debris)

    def kill_ship(self) -> None:
        player.stop_sound("thrust")
        player.play_sound("explode2")
        self.ship_manager.remove_life()
        ship = self.ship_manager.ship
        self.stage.remove_sprite(ship)
        self.stage.remove_sprite(ship.thrust_jet)
        ship.explode()
