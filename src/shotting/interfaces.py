from abc import ABC, abstractmethod

from typing import Tuple
from ..stage.rederer import Renderable
from .bullet import Bullet

class IStage(ABC):
    @abstractmethod
    def add_sprite(self, sprite: Renderable) -> None:
        pass

class IBulletFactory(ABC):
    @abstractmethod
    def create_bullet(self, position: Tuple[float, float], heading: float, shooter: str, ttl: float, velocity: float, stage: str) -> Bullet:
        pass