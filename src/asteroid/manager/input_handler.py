import sys
import pygame

class InputHandler:
    def __init__(self, game):
        self.game = game

    def process(self, events):
        self.game.frameAdvance = False
        ship = self.game.ship_manager.ship
        state = self.game.state_manager.state

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)

                if state == "playing":
                    if event.key in (pygame.K_SPACE, pygame.K_b):
                        ship.fire_bullet()
                    elif event.key == pygame.K_h:
                        ship.enter_hyper_space()

                # Permitir Enter no attract_mode ou gameover
                if state in ('attract_mode', 'gameover'):
                    if event.key == pygame.K_RETURN:
                        self.game.initialiseGame()

                if event.key == pygame.K_p:
                    self.game.paused = not self.game.paused
                if event.key == pygame.K_j:
                    self.game.showingFPS = not self.game.showingFPS
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_o:
                    self.game.frameAdvance = True
