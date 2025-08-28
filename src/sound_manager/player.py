from .sounds import Sounds

class Player(Sounds):
    def __init__(self, ext: str = ".WAV"):
        super().__init__(ext)
        self.init_sounds_manager()

    def play_sound(self, name: str) -> None:
        self.get_sound(name).play()

    def play_sound_continuous(self, name: str) -> None:
        self.get_sound(name).play(-1)

    def stop_sound(self, name: str) -> None:
        self.get_sound(name).stop()

