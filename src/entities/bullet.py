import math
import pygame
from typing import List


class Bullet:
    def __init__(self, x: float, y: float, angle: float) -> None:
        self.x: float = x
        self.y: float = y

        self.speed: float = 10
        self.radius: int = 3

        radians = math.radians(angle)
        self.velocity_x: float = math.sin(radians) * self.speed
        self.velocity_y: float = math.cos(radians) * self.speed
        
        self.lifetime: int = 0
        self.max_lifetime: int = 60

    def update(self, width: int = 1000, height: int = 700) -> None:
        self.x += self.velocity_x
        self.y -= self.velocity_y
        
        self.lifetime += 1

        self.wrap_around(width, height)

    def wrap_around(self, width: int, height: int) -> None:
        if self.x < -self.radius:
            self.x = width + self.radius
        elif self.x > width + self.radius:
            self.x = -self.radius

        if self.y < -self.radius:
            self.y = height + self.radius
        elif self.y > height + self.radius:
            self.y = -self.radius

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.x), int(self.y)),
            self.radius
        )


class BulletManager:
    def __init__(self) -> None:
        self.bullets: List[Bullet] = []

    def shoot(self, x: float, y: float, angle: float) -> None:
        self.bullets.append(Bullet(x, y, angle))

    def update(self) -> None:
        for bullet in self.bullets:
            bullet.update(1000, 700)
            
        self.clean_expired_bullets()

    def clean_expired_bullets(self) -> None:
        self.bullets = [
            bullet for bullet in self.bullets
            if bullet.lifetime < bullet.max_lifetime
        ]

    def draw(self, screen: pygame.Surface) -> None:
        for bullet in self.bullets:
            bullet.draw(screen)
            