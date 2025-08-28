from .rederer import HUDRenderer
from .manager import (
    GameStateManager, 
    ShipManager, 
    RockManager, 
    SaucerManager, 
    CollisionSystem, 
    InputHandler
)

import pygame

from ..sound_manager import player

class Game:
    def __init__(self, stage):
        self.stage = stage

        self.state_manager = GameStateManager()
        self.ship_manager = ShipManager(stage)
        self.rock_manager = RockManager(stage)
        self.saucer_manager = SaucerManager(stage)
        self.hud = HUDRenderer(stage)
        self.collision_system = CollisionSystem(stage, self.ship_manager, self.rock_manager, self.saucer_manager)
        self.input_handler = InputHandler(self)

        self.paused = False
        self.showingFPS = False
        self.frameAdvance = False
        self.fps = 0
        self.secondsCount = 1
        self.score = 0
        self.nextLife = 10000

        self.rock_manager.create_rocks(3)

    def initialiseGame(self):
        self.state_manager.set_state("playing")
        self.rock_manager.clear_rocks()
        if self.saucer_manager.saucer:
            self.saucer_manager.kill_saucer()

        self.ship_manager.startLives = 5
        self.ship_manager.create_new_ship()
        self.ship_manager.create_lives_list()
        self.score = 0
        self.rock_manager.numRocks = 3
        self.rock_manager.create_rocks(self.rock_manager.numRocks)
        self.secondsCount = 1
        self.nextLife = 10000

    def run(self):
        clock = pygame.time.Clock()
        frameCount = 0
        timePassed = 0

        while True:
            self.input_handler.process(pygame.event.get())

            if self.paused and not self.frameAdvance:
                self.hud.display_text("Paused")
                pygame.display.update()
                continue

            timePassed += clock.tick(60)
            frameCount += 1
            if frameCount % 10 == 0:
                self.fps = round(frameCount / (timePassed / 1000.0))
                frameCount, timePassed = 0, 0

            self.secondsCount += 1

            if self.state_manager.state == "playing":
                self.update_playing()
            elif self.state_manager.state == "exploding":
                self.handle_explosion()
            else:
                self.hud.display_text("Press Start to Play")

            self.stage.screen.fill((10, 10, 10))
            self.stage.move_sprites()
            self.stage.draw_sprites()
            self.saucer_manager.update(self.secondsCount, self.ship_manager.ship)
            self.hud.render(self.fps, self.showingFPS, self.state_manager.state, self.score)

            pygame.display.flip()

    def update_playing(self):
        if self.ship_manager.lives == 0:
            self.state_manager.set_state("gameover")
            return

        self.score, ship_hit = self.collision_system.update(self.score)

        if ship_hit:
            self.state_manager.set_state("exploding")

        if len(self.rock_manager.rocks) == 0:
            self.rock_manager.level_up()

        if self.score > 0 and self.score > self.nextLife:
            player.play_sound("extralife")
            self.nextLife += 10000
            self.ship_manager.add_life(self.ship_manager.lives)

        self.process_keys()


    def process_keys(self):
        key = pygame.key.get_pressed()
        ship = self.ship_manager.ship

        if key[pygame.K_LEFT] or key[pygame.K_z]:
            ship.rotate_left()
        elif key[pygame.K_RIGHT] or key[pygame.K_x]:
            ship.rotate_right()

        if key[pygame.K_UP] or key[pygame.K_n]:
            ship.increase_thrust()
            ship.thrust_jet.accelerating = True
        else:
            ship.thrust_jet.accelerating = False

    def handle_explosion(self):
        self.state_manager.explodingCount += 1
        if self.state_manager.explodingCount > 180:
            self.state_manager.set_state("playing")
            self.state_manager.explodingCount = 0

            for debris in self.ship_manager.ship.ship_debris_list:
                self.stage.remove_sprite(debris)
            self.ship_manager.ship.ship_debris_list.clear()

            if self.ship_manager.lives > 0:
                self.ship_manager.create_new_ship()
            else:
                self.ship_manager.ship.visible = False
