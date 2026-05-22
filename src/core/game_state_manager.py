class GameStateManager:
    def __init__(self) -> None:
        self._state: str = "START"

    @property
    def current_state(self) -> str:
        return self._state

    def set_state(self, new_state: str) -> None:
        valid_states = {"START", "PLAYING", "PAUSE", "GAME_OVER"}
        if new_state in valid_states:
            self._state = new_state

    def toggle_pause(self) -> None:
        """Alterna especificamente entre pausa e jogabilidade ativa."""
        if self._state == "PLAYING":
            self._state = "PAUSE"
        elif self._state == "PAUSE":
            self._state = "PLAYING"