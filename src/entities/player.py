import math
import random
import pygame
from typing import List, Tuple


class Player:
    def __init__(self, x: float, y: float) -> None:
        self.start_x: float = x
        self.start_y: float = y
        
        self.x: float = x
        self.y: float = y

        self.angle: float = 0
        self.velocity_x: float = 0
        self.velocity_y: float = 0

        self.rotation_speed: float = 4
        self.acceleration: float = 0.15
        self.friction: float = 0.99
        self.radius: int = 8

        self.is_accelerating: bool = False

        self.is_alive: bool = True
        self.lives: int = 3
        self.fragments: List[dict] = []
        
        self.respawn_timer: int = 0
        self.respawn_delay: int = 90

    def update(self, width: int = 1000, height: int = 700) -> None:
        if not self.is_alive:
            self._update_explosion()
            
            if self.lives > 0:
                self.respawn_timer += 1
                if self.respawn_timer >= self.respawn_delay:
                    self.respawn()
            return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.rotation_speed

        if keys[pygame.K_UP]:
            self.is_accelerating = True
            radians = math.radians(self.angle)
            self.velocity_x += math.sin(radians) * self.acceleration
            self.velocity_y += math.cos(radians) * self.acceleration
        else:
            self.is_accelerating = False

        self.x += self.velocity_x
        self.y -= self.velocity_y

        self.velocity_x *= self.friction
        self.velocity_y *= self.friction

        self.wrap_around(width, height)

    def trigger_explosion(self) -> None:
        self.is_alive = False
        self.lives -= 1
        self.respawn_timer = 0
        self.is_accelerating = False
        
        ship_lines = [
            ((0, -12), (7, 10)),
            ((7, 10), (0, 5)),
            ((0, 5), (-7, 10)),
            ((-7, 10), (0, -12))
        ]

        radians = math.radians(self.angle)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)

        for p1, p2 in ship_lines:
            x1 = self.x + (p1[0] * cos_a + p1[1] * sin_a)
            y1 = self.y - (p1[0] * -sin_a + p1[1] * cos_a)
            x2 = self.x + (p2[0] * cos_a + p2[1] * sin_a)
            y2 = self.y - (p2[0] * -sin_a + p2[1] * cos_a)

            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            dx = center_x - self.x
            dy = center_y - self.y
            dist = (dx**2 + dy**2) ** 0.5 + 0.1

            self.fragments.append({
                "x1": x1, "y1": y1,
                "x2": x2, "y2": y2,
                "vel_x": (dx / dist) * random.uniform(0.3, 0.8) + (self.velocity_x * 0.2),
                "vel_y": (dy / dist) * random.uniform(0.3, 0.8) + (self.velocity_y * 0.2),
                "alpha": 255
            })

    def respawn(self) -> None:
        self.x = self.start_x
        self.y = self.start_y
        self.angle = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.fragments.clear()
        self.is_alive = True

    def _update_explosion(self) -> None:
        for frag in self.fragments:
            frag["x1"] += frag["vel_x"]
            frag["y1"] += frag["vel_y"]
            frag["x2"] += frag["vel_x"]
            frag["y2"] += frag["vel_y"]
            frag["alpha"] = max(0, frag["alpha"] - 4)

    def wrap_around(self, width: int, height: int) -> None:
        if self.x < -self.radius: self.x = width + self.radius
        elif self.x > width + self.radius: self.x = -self.radius
        if self.y < -self.radius: self.y = height + self.radius
        elif self.y > height + self.radius: self.y = -self.radius

    def draw(self, screen: pygame.Surface) -> None:
        if not self.is_alive:
            for frag in self.fragments:
                if frag["alpha"] > 0:
                    color = (frag["alpha"], frag["alpha"], frag["alpha"])
                    pygame.draw.line(screen, color, (frag["x1"], frag["y1"]), (frag["x2"], frag["y2"]), 2)
            
            if self.lives <= 0:
                pass
            return

        radians = math.radians(self.angle)

        tip_x = self.x + math.sin(radians) * 12
        tip_y = self.y - math.cos(radians) * 12
        right_x = self.x + math.sin(radians - 2.5) * 10
        right_y = self.y - math.cos(radians - 2.5) * 10
        inner_x = self.x - math.sin(radians) * 4
        inner_y = self.y + math.cos(radians) * 4
        left_x = self.x + math.sin(radians + 2.5) * 10
        left_y = self.y - math.cos(radians + 2.5) * 10

        pygame.draw.polygon(
            screen,
            (255, 255, 255),
            [(tip_x, tip_y), (right_x, right_y), (inner_x, inner_y), (left_x, left_y)],
            2
        )

        if self.is_accelerating:
            if random.choice([True, False]):
                fire_tip_x = self.x - math.sin(radians) * 10
                fire_tip_y = self.y + math.cos(radians) * 10
                fire_left_x = self.x + math.sin(radians + 2.8) * 6
                fire_left_y = self.y - math.cos(radians + 2.8) * 6
                fire_right_x = self.x + math.sin(radians - 2.8) * 6
                fire_right_y = self.y - math.cos(radians - 2.8) * 6

                pygame.draw.polygon(
                    screen,
                    (255, 255, 255),
                    [(inner_x, inner_y), (fire_left_x, fire_left_y), (fire_tip_x, fire_tip_y), (fire_right_x, fire_right_y)],
                    2
                )
                