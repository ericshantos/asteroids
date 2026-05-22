import pygame
from ..entities import Player
from ..core.game_state_manager import GameStateManager
from .score_manager import ScoreManager
from .font import Font


class HUD:
    def __init__(self, screen: pygame.Surface, player: Player, score_manager: ScoreManager) -> None:
        self.screen = screen
        self.player = player
        self.score_manager = score_manager
        
        self.color = (255, 255, 255)
        
        self.lives_start_x = 30
        self.lives_start_y = 35
        self.lives_spacing = 25

        self.title_font = Font.F45.get_font()
        self.instruct_font = Font.F20.get_font()

    def draw(self, state_manager: GameStateManager) -> None:
        current_state = state_manager.current_state

        if current_state != "START":
            self._draw_score()
            self._draw_lives()

        if current_state == "START":
            self._draw_start_screen()
        elif current_state == "PAUSE":
            self._draw_pause_screen()
        elif current_state == "GAME_OVER":
            self._draw_game_over_screen()

    def _draw_score(self) -> None:
        score_string = self.score_manager.get_formatted_score()
        score_surface = Font.F32.get_font().render(score_string, True, self.color)
        
        screen_width = self.screen.get_width()
        score_x = screen_width - score_surface.get_width() - 40
        score_y = 25  
        self.screen.blit(score_surface, (score_x, score_y))

    def _draw_lives(self) -> None:
        for i in range(self.player.lives):
            life_x = self.lives_start_x + (i * self.lives_spacing)
            life_y = self.lives_start_y
            
            pygame.draw.polygon(
                self.screen,
                self.color,
                [(life_x, life_y - 8), (life_x + 5, life_y + 6), (life_x, life_y + 2), (life_x - 5, life_y + 6)],
                1
            )
  
    def _draw_start_screen(self) -> None:
        title_surf = self.title_font.render("ASTEROIDS", True, self.color)
        instruct_surf = self.instruct_font.render("PRESS START TO PLAY", True, self.color)
        copyright_surf = Font.F15.get_font().render("(C) 1979 ATARI INC.", True, self.color)
        
        cx = self.screen.get_width() // 2
        cy = self.screen.get_height() // 2
        bottom_y = self.screen.get_height() - 50
        
        self.screen.blit(title_surf, (cx - title_surf.get_width() // 2, cy - 40))
        self.screen.blit(instruct_surf, (cx - instruct_surf.get_width() // 2, cy + 30))
        self.screen.blit(copyright_surf, (cx - copyright_surf.get_width() // 2, bottom_y))

    def _draw_pause_screen(self) -> None:
        pause_surf = self.title_font.render("PAUSE", True, self.color)
        instruct_surf = self.instruct_font.render("PRESSIONE P PARA RETORNAR", True, self.color)
        
        cx, cy = self.screen.get_width() // 2, self.screen.get_height() // 2
        
        self.screen.blit(pause_surf, (cx - pause_surf.get_width() // 2, cy - 30))
        self.screen.blit(instruct_surf, (cx - instruct_surf.get_width() // 2, cy + 50))

    def _draw_game_over_screen(self) -> None:
        go_surf = self.title_font.render("GAME OVER", True, (255, 0, 0))
        instruct_surf = self.instruct_font.render("PRESSIONE ESPACO PARA REINICIAR", True, self.color)
        
        cx, cy = self.screen.get_width() // 2, self.screen.get_height() // 2
        
        self.screen.blit(go_surf, (cx - go_surf.get_width() // 2, cy - 30))
        self.screen.blit(instruct_surf, (cx - instruct_surf.get_width() // 2, cy + 50))
