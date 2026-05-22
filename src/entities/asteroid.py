import math
import random
import pygame
from typing import List, Tuple


class Asteroid:
    def __init__(self, screen_width: int = 1000, screen_height: int = 700, size: int = 3, x: float = None, y: float = None) -> None:
        self.size: int = size
        
        if self.size == 3:
            self.radius = 70
        elif self.size == 2:
            self.radius = 25
        else:
            self.radius = 8

        self.is_alive: bool = True
        self.particles: List[dict] = []

        if x is None or y is None:
            self.x, self.y = self._generate_edge_position(screen_width, screen_height)
            self.speed_x, self.speed_y = self._generate_inward_velocity(screen_width, screen_height)
        else:
            self.x = x
            self.y = y
            angle = random.uniform(0, math.pi * 2)
            
            speed_multiplier = {3: 1.5, 2: 2.8, 1: 4.2}[self.size]
            self.speed_x = math.cos(angle) * speed_multiplier
            self.speed_y = math.sin(angle) * speed_multiplier

        base_points = [
            (0.0, -1.0), (0.5, -0.8), (1.0, -0.3), (0.8, 0.2), (1.0, 0.6),
            (0.4, 1.0), (-0.2, 0.8), (-0.6, 1.0), (-1.0, 0.4), (-0.8, -0.3),
            (-1.0, -0.7), (-0.4, -0.8)
        ]

        self.points = []
        for px, py in base_points:
            jitter_x = random.uniform(-0.12, 0.12)
            jitter_y = random.uniform(-0.12, 0.12)
            self.points.append(((px + jitter_x) * self.radius, (py + jitter_y) * self.radius))

        self.saucer = None
        self.last_saucer_spawn = pygame.time.get_ticks()
        self.saucer_spawn_interval = 15000

    def _generate_edge_position(self, width: int, height: int) -> Tuple[float, float]:
        edge = random.choice(["LEFT", "RIGHT", "TOP", "BOTTOM"])
        if edge == "LEFT": return -self.radius, random.uniform(0, height)
        elif edge == "RIGHT": return width + self.radius, random.uniform(0, height)
        elif edge == "TOP": return random.uniform(0, width), -self.radius
        else: return random.uniform(0, width), height + self.radius

    def _generate_inward_velocity(self, width: int, height: int) -> Tuple[float, float]:
        target_x = random.uniform(width * 0.2, width * 0.8)
        target_y = random.uniform(height * 0.2, height * 0.8)
        dx, dy = target_x - self.x, target_y - self.y
        distance = (dx**2 + dy**2) ** 0.5
        
        base_speed = random.uniform(1.0, 1.8)
        return (dx / distance) * base_speed, (dy / distance) * base_speed

    def trigger_explosion(self) -> None:
        self.is_alive = False
        for _ in range(random.randint(8, 15)):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(1.0, 3.5)
            self.particles.append({
                "x": self.x, "y": self.y,
                "vel_x": math.cos(angle) * speed,
                "vel_y": math.sin(angle) * speed,
                "alpha": 255
            })

    def update(self) -> None:
        if not self.is_alive:
            for p in self.particles:
                p["x"] += p["vel_x"]
                p["y"] += p["vel_y"]
                p["alpha"] = max(0, p["alpha"] - 6)
            return

        self.x += self.speed_x
        self.y += self.speed_y
        self.wrap_around(1000, 700)

    def wrap_around(self, width: int, height: int) -> None:
        if self.x < -self.radius: self.x = width + self.radius
        elif self.x > width + self.radius: self.x = -self.radius
        if self.y < -self.radius: self.y = height + self.radius
        elif self.y > height + self.radius: self.y = -self.radius

    def draw(self, screen: pygame.Surface) -> None:
        if not self.is_alive:
            for p in self.particles:
                if p["alpha"] > 0:
                    color = (p["alpha"], p["alpha"], p["alpha"])
                    pygame.draw.circle(screen, color, (int(p["x"]), int(p["y"])), 1)
            return

        transformed_points = [(self.x + px, self.y + py) for px, py in self.points]
        pygame.draw.polygon(screen, (255, 255, 255), transformed_points, 2)
