from .rederer import Renderer, Renderable
from .sprite_mover import SpriteMover, Moverable
from .sprites_manager import SpriteManager

import pygame


class Stage:
    def __init__(self, 
        caption, 
        dimensions=None, 
        renderer=None, 
        sprite_mover=None, 
        sprite_manager=None
    ):
        pygame.init()

        if dimensions is None:
            dimensions = pygame.display.list_modes()[0]

        pygame.display.set_mode(dimensions, pygame.FULLSCREEN)
        pygame.mouse.set_visible(False)
        pygame.display.set_caption(caption)

        self.width, self.height = dimensions
        self.screen: pygame.display = pygame.display.get_surface()

        self.renderer: Renderable = renderer or Renderer(self.screen)
        self.sprite_mover: Moverable = sprite_mover or SpriteMover(self.width, self.height)
        self.sprite_manager: SpriteManager = sprite_manager or SpriteManager()

    def add_sprite(self, sprite):
        self.sprite_manager.add_sprite(sprite)

    def remove_sprite(self, sprite):
        self.sprite_manager.remove_sprite(sprite)

    def draw_sprites(self):
        self.renderer.draw_sprites(self.sprite_manager.get_sprites())

    def move_sprites(self):
        self.sprite_mover.move_sprites(self.sprite_manager.get_sprites())


    def add_sprite_with_bounding(self, sprite):
        self.add_sprite(sprite)
        sprite.boundingRect = pygame.draw.aalines(
            self.screen, sprite.color, True, sprite.draw()
        )
