from abc import ABC, abstractmethod

class IStage(ABC):
    @abstractmethod
    def add_sprite(self, sprite):
        pass

class IBulletFactory(ABC):
    @abstractmethod
    def create_bullet(self, position, heading, shooter, ttl, velocity, stage):
        pass