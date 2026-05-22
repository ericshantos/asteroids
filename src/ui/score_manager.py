from ..entities import Player

class ScoreManager:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.score: int = 0
        self.score_for_extra_life: int = 0

    def add_points(self, points: int) -> None:
        if self.player.lives <= 0 and not self.player.is_alive:
            return

        self.score += points
        self.score_for_extra_life += points

        if self.score_for_extra_life >= 10000:
            self.player.lives += 1
            self.score_for_extra_life -= 10000

    def get_formatted_score(self) -> str:
        if self.score == 0:
            return "00"
        return str(self.score)

    def reset(self) -> None:
        self.score = 0
        self.score_for_extra_life = 0
        