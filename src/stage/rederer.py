from abc import ABC, abstractmethod
import pygame

class Renderable(ABC):
    @abstractmethod
    def draw_sprites(self):
        raise NotImplementedError

class Renderer:
    def __init__(self, screen, showBoundingBoxes=False):
        self.screen = screen
        self.showBoundingBoxes = showBoundingBoxes

    def draw_sprites(self, sprites):
        for sprite in sprites:
            safe_color = tuple([max(0, min(255, c)) for c in sprite.color])

            sprite.boundingRect = pygame.draw.aalines(
                self.screen, safe_color, True, sprite.draw())
            
            if self.showBoundingBoxes:
                pygame.draw.rect(self.screen, (255, 255, 255), sprite.boundingRect, 1)
