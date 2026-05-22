import pygame
import random
import math
from typing import Tuple, List
from .bullet import Bullet


class Saucer:
    def __init__(self, screen_width: int, screen_height: int, size_type: str = "large") -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.size_type = size_type  
        
        self.scale = 2.0 if size_type == "large" else 1.0
        self.color: Tuple[int, int, int] = (255, 255, 255)
        
        self.raw_points: List[Tuple[float, float]] = [
            (-9, 0), (-3, -3), (-2, -6), (2, -6), 
            (3, -3), (9, 0), (3, 4), (-3, 4), (-9, 0),
            (9, 0), (3, -3), (-3, -3), (-9, 0)
        ]
        self.shape_points = [(x * self.scale, y * self.scale) for x, y in self.raw_points]
        
        self.direction = random.choice([-1, 1])
        self.x = -20.0 if self.direction == 1 else float(screen_width + 20)
        self.y = float(random.randint(120, screen_height - 120))
        
        self.speed_x = 2.5 * self.direction
        self.speed_y = 0.0
        
        self.last_dir_change = pygame.time.get_ticks()
        self.dir_change_interval = 1000  
        self.is_alive = True

        self.bullets: List[Bullet] = []
        self.last_shot_time = pygame.time.get_ticks()
        self.shoot_interval = 1200 if size_type == "small" else 2000

        self.particles: List[dict] = []
        self.is_exploding = False

    def trigger_explosion(self) -> None:
        self.is_alive = False
        self.is_exploding = True
        
        for _ in range(random.randint(15, 25)):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1.0, 4.0)
            self.particles.append({
                "x": self.x,
                "y": self.y,
                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed,
                "lifetime": random.randint(30, 50),
                "alpha": 255
            })

    def move(self, player_x: float = None, player_y: float = None) -> None:
        if not self.is_alive and not self.is_exploding and len(self.bullets) == 0:
            return
            
        if self.is_alive:
            self.x += self.speed_x
            now = pygame.time.get_ticks()
            
            if now - self.last_dir_change > self.dir_change_interval:
                self.speed_y = random.choice([-1.5, 0, 1.5])
                self.last_dir_change = now
                
            self.y += self.speed_y
            
            if self.y < 60:
                self.y = 60
                self.speed_y = 1.5
            elif self.y > self.screen_height - 60:
                self.y = self.screen_height - 60
                self.speed_y = -1.5

            if (self.direction == 1 and self.x > self.screen_width + 30) or \
               (self.direction == -1 and self.x < -30):
                self.is_alive = False

            self._shoot_logic(now, player_x, player_y)

        if self.is_exploding:
            for p in self.particles[:]:
                p["x"] += p["vx"]
                p["y"] += p["vy"]
                p["lifetime"] -= 1
                p["alpha"] = max(0, int((p["lifetime"] / 50) * 255))
                
                if p["lifetime"] <= 0:
                    self.particles.remove(p)
            
            if len(self.particles) == 0:
                self.is_exploding = False

        for bullet in self.bullets[:]:
            bullet.update(self.screen_width, self.screen_height)
            if bullet.lifetime >= bullet.max_lifetime:
                self.bullets.remove(bullet)

    def _shoot_logic(self, current_time: int, player_x: float, player_y: float) -> None:
        if current_time - self.last_shot_time > self.shoot_interval:
                if player_x is not None and player_y is not None:
                    if self.size_type == "large":
                        angle = random.uniform(0, 360)
                    else:
                        dx = player_x - self.x
                        dy = self.y - player_y
                        
                        angle = math.degrees(math.atan2(dx, dy))
                        
                        angle += random.uniform(-15, 15)

                    new_bullet = Bullet(self.x, self.y, angle)
                    new_bullet.speed = 7.0
                    
                    rad = math.radians(angle)
                    new_bullet.velocity_x = math.sin(rad) * new_bullet.speed
                    new_bullet.velocity_y = math.cos(rad) * new_bullet.speed
                    
                    self.bullets.append(new_bullet)
                    self.last_shot_time = current_time

    def draw(self, surface: pygame.Surface) -> None:
        for bullet in self.bullets:
            bullet.draw(surface)

        if self.is_exploding:
            for p in self.particles:
                p_surface = pygame.Surface((4, 4), pygame.SRCALPHA)
                pygame.draw.circle(p_surface, (255, 255, 255, p["alpha"]), (2, 2), 2)
                surface.blit(p_surface, (int(p["x"]), int(p["y"])))

        if not self.is_alive:
            return
            
        transformed_points = [(px + self.x, py + self.y) for px, py in self.shape_points]
        pygame.draw.aalines(surface, self.color, True, transformed_points)

    def get_rect(self) -> pygame.Rect:
        width = 18 * self.scale
        height = 10 * self.scale
        return pygame.Rect(int(self.x - width / 2), int(self.y - height / 2), int(width), int(height))