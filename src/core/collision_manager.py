from typing import List
from ..entities import Player, Asteroid
from ..entities import BulletManager
from ..ui import ScoreManager
import pygame


class CollisionManager:
    def __init__(self, player: Player, asteroids: List[Asteroid], bullet_manager: BulletManager, score_manager: ScoreManager, game=None) -> None:
        self.player = player
        self.asteroids = asteroids
        self.bullet_manager = bullet_manager
        self.score_manager = score_manager
        self.game = game  

    def check_all_collisions(self) -> None:
        self._cleanup_dead_asteroids()
        self._check_player_asteroid_collisions()
        self._check_bullet_asteroid_collisions()
        
        self._check_bullet_saucer_collisions()
        self._check_saucer_bullets_against_player()

    def _cleanup_dead_asteroids(self) -> None:
        for asteroid in self.asteroids[:]:
            if not asteroid.is_alive and all(p["alpha"] <= 0 for p in asteroid.particles):
                self.asteroids.remove(asteroid)

    def _split_asteroid(self, parent: Asteroid) -> None:
        if parent.size == 3:
            for _ in range(3):
                self.asteroids.append(Asteroid(size=2, x=parent.x, y=parent.y))
        elif parent.size == 2:
            for _ in range(2):
                self.asteroids.append(Asteroid(size=1, x=parent.x, y=parent.y))

    def _check_player_asteroid_collisions(self) -> None:
        if not self.player.is_alive:
            return

        for asteroid in self.asteroids:
            if not asteroid.is_alive:
                continue

            distance = ((self.player.x - asteroid.x) ** 2 + (self.player.y - asteroid.y) ** 2) ** 0.5
            if distance < (self.player.radius + asteroid.radius):
                
                if self.game and hasattr(self.game, 'sound_manager'):
                    self.game.sound_manager.play_explosion()
                
                self.player.trigger_explosion()
                asteroid.trigger_explosion() 
                self._split_asteroid(asteroid) 
                break

    def _check_bullet_asteroid_collisions(self) -> None:
        bullets_to_remove = []

        for bullet in self.bullet_manager.bullets:
            for asteroid in self.asteroids:
                if not asteroid.is_alive:
                    continue

                distance = ((bullet.x - asteroid.x) ** 2 + (bullet.y - asteroid.y) ** 2) ** 0.5
                if distance < asteroid.radius:
                    bullets_to_remove.append(bullet)

                    if self.game and hasattr(self.game, 'sound_manager'):
                        self.game.sound_manager.play_explosion()

                    asteroid.trigger_explosion()
                    
                    score_table = {3: 20, 2: 50, 1: 100}
                    points = score_table.get(asteroid.size, 0)
                    self.score_manager.add_points(points)
                    
                    if self.score_manager.score_for_extra_life >= 10000  and self.game:
                        pass

                    self._split_asteroid(asteroid)
                    break

        for bullet in bullets_to_remove:
            if bullet in self.bullet_manager.bullets:
                self.bullet_manager.bullets.remove(bullet)

    def _check_bullet_saucer_collisions(self) -> None:
            if self.game is None or self.game.saucer is None or not self.game.saucer.is_alive or self.game.saucer.is_exploding:
                return

            saucer = self.game.saucer
            saucer_rect = saucer.get_rect()
            bullets_to_remove = []

            for bullet in self.bullet_manager.bullets:
                if saucer_rect.collidepoint(bullet.x, bullet.y):
                    bullets_to_remove.append(bullet)
                    
                    if hasattr(self.game, 'sound_manager'):
                        self.game.sound_manager.play_explosion()

                    saucer.trigger_explosion() 
                    
                    points = 1000 if saucer.size_type == "small" else 200
                    self.score_manager.add_points(points)
                    break

            for bullet in bullets_to_remove:
                if bullet in self.bullet_manager.bullets:
                    self.bullet_manager.bullets.remove(bullet)

    def _check_saucer_bullets_against_player(self) -> None:
        if self.game is None or self.game.saucer is None or not self.player.is_alive:
            return

        saucer = self.game.saucer
        
        for bullet in saucer.bullets[:]:
            distance = ((bullet.x - self.player.x) ** 2 + (bullet.y - self.player.y) ** 2) ** 0.5
            
            if distance < self.player.radius:

                if hasattr(self.game, 'sound_manager'):
                    self.game.sound_manager.play_explosion()
                    
                saucer.bullets.remove(bullet)
                self.player.trigger_explosion()
                break