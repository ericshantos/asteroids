from .font import Font

class HUDRenderer:
    def __init__(self, stage):
        self.stage = stage

    def render(self, fps, showingFPS, state, score):
        if state == "attract_mode":
            self.display_attract_mode()
        elif state == "gameover":
            self.display_game_over()

        self.display_score(score)

        if showingFPS:
            self.display_fps(fps)


    def display_text(self, text, x=None, y=None, font=Font.F30, color=(200,200,200)):

        text_surface = font.get_font().render(text, True, color)

        rect = text_surface.get_rect()
        rect.centerx = x if x is not None else self.stage.width / 2
        rect.y = y if y is not None else self.stage.height / 2
        self.stage.screen.blit(text_surface, rect)

    def display_attract_mode(self):
        self.display_text("Asteroids", y=self.stage.height/2 - 100, font=Font.F45, color=(180,180,180))
        self.display_text("Press Start to Play", y=self.stage.height/2 - 20, color=(200,200,200))
        self.display_text("(C) 1979 Atari INC.", y=self.stage.height - 35, font=Font.F20, color=(255,255,255))

    def display_score(self, score):
        self.display_text(f"{score:02d}", x=50, y=45, color=(200,200,200))

    def display_fps(self, fps):
        self.display_text(f"{fps} FPS", x=50, y=15, font=Font.F15, color=(255,255,255))

    def display_game_over(self):
        self.display_text("GAME OVER", y=self.stage.height/2 - 50, font=Font.F45, color=(255,50,50))
        self.display_text("Press Start to Play Again", y=self.stage.height/2 + 20, color=(200,200,200))
