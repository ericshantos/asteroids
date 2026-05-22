import pygame
import sys
import random
from typing import Tuple

from .entities import Player, Asteroid, BulletManager, Saucer
from .core import CollisionManager, GameStateManager
from .ui import ScoreManager, HUD
from .audio import SoundManager


class Game:
    WIDTH: int = 1000
    HEIGHT: int = 700
    FPS: int = 60
    BACKGROUND_COLOR: Tuple[int, int, int] = (0, 0, 0)

    def __init__(self) -> None:
        pygame.init()
        
        self.screen: pygame.Surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Asteroids")
        self.clock: pygame.time.Clock = pygame.time.Clock()
        
        self.sound_manager = SoundManager()

        self.running: bool = True
        self.state_manager = GameStateManager()
        
        self.player = Player(self.WIDTH // 2, self.HEIGHT // 2)
        self.bullet_manager = BulletManager()
        self.score_manager = ScoreManager(player=self.player)
        self.hud = HUD(screen=self.screen, player=self.player, score_manager=self.score_manager)
        
        self.saucer = None
        self.last_saucer_spawn = pygame.time.get_ticks()
        self.saucer_spawn_interval = 15000
        
        self.asteroids = [Asteroid(size=3) for _ in range(4)]
        
        self.collision_manager = CollisionManager(
            player=self.player, 
            asteroids=self.asteroids, 
            bullet_manager=self.bullet_manager,
            score_manager=self.score_manager,
            game=self
        )

        self.score_manager.game = self

    def _reset_game_entities(self) -> None:
        self.player = Player(self.WIDTH // 2, self.HEIGHT // 2)
        self.bullet_manager = BulletManager()
        self.score_manager = ScoreManager(player=self.player)
        
        self.saucer = None
        self.last_saucer_spawn = pygame.time.get_ticks()
        self.asteroids = [Asteroid(size=3) for _ in range(5)]
        
        self.collision_manager = CollisionManager(
            player=self.player, 
            asteroids=self.asteroids, 
            bullet_manager=self.bullet_manager,
            score_manager=self.score_manager,
            game=self
        )
        
        self.hud = HUD(
            screen=self.screen, 
            player=self.player, 
            score_manager=self.score_manager
        )

        self.score_manager.game = self

    def handle_events(self) -> None:
        current_state = self.state_manager.current_state

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.KEYDOWN:
                if current_state == "START":
                    if event.key == pygame.K_SPACE:
                        self._reset_game_entities()
                        self.state_manager.set_state("PLAYING")
                
                elif current_state == "PLAYING":
                    if event.key == pygame.K_SPACE and self.player.is_alive:
                        self.bullet_manager.shoot(
                            x=self.player.x, 
                            y=self.player.y, 
                            angle=self.player.angle
                        )
                        self.sound_manager.play_shoot()
                    elif event.key == pygame.K_p:
                        self.state_manager.toggle_pause()
                
                elif current_state == "PAUSE":
                    if event.key == pygame.K_p:
                        self.state_manager.toggle_pause()
                
                elif current_state == "GAME_OVER":
                    if event.key == pygame.K_SPACE:
                        self._reset_game_entities()
                        self.state_manager.set_state("PLAYING")

    def update(self) -> None:
            current_state = self.state_manager.current_state

            if current_state == "START":
                for asteroid in self.asteroids:
                    asteroid.update()

            elif current_state == "PLAYING":
                if self.player.is_accelerating and self.player.is_alive:
                    self.sound_manager.play_thrust()

                self.player.update()
                
                for asteroid in self.asteroids:
                    asteroid.update()
                    
                now = pygame.time.get_ticks()
                if self.saucer is None:
                    if now - self.last_saucer_spawn > self.saucer_spawn_interval:
                        saucer_size = "small" if random.random() < 0.3 else "large"
                        self.saucer = Saucer(self.WIDTH, self.HEIGHT, size_type=saucer_size)
                        self.sound_manager.play_saucer_appear(saucer_size)
                        self.last_saucer_spawn = now
                else:
                    self.saucer.move(player_x=self.player.x, player_y=self.player.y)
                    
                    if not self.saucer.is_alive and not self.saucer.is_exploding and len(self.saucer.bullets) == 0:
                        self.saucer = None
                        self.last_saucer_spawn = now

                self.bullet_manager.update()
                self.collision_manager.check_all_collisions()

                if self.player.lives <= 0 and not self.player.is_alive:
                    self.state_manager.set_state("GAME_OVER")

    def draw(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)
        
        current_state = self.state_manager.current_state

        if current_state == "START":
            for asteroid in self.asteroids:
                asteroid.draw(self.screen)
        else:
            self.player.draw(self.screen)
            
            for asteroid in self.asteroids:
                asteroid.draw(self.screen)
                
            if self.saucer is not None:
                self.saucer.draw(self.screen)
                
            self.bullet_manager.draw(self.screen)
        
        self.hud.draw(self.state_manager)

        pygame.display.flip()

    def run(self) -> None:
        while self.running:
            self.clock.tick(self.FPS)
            self.handle_events()
            self.update()
            self.draw()
            
        pygame.quit()
        sys.exit()
        