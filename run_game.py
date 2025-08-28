from src import Game, Stage

import pygame


if not pygame.font:
    print("Warning, fonts disabled")
if not pygame.mixer:
    print("Warning, sound disabled")

def main():
    stage = Stage("Atari Asteroids")
    game = Game(stage)
    game.run()

if __name__ == "__main__":
    main()
