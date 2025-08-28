from dataclasses import dataclass

@dataclass
class ShipData:
    acceleration: float = 0.2
    deceleration: float = -0.005
    max_velocity: int = 10
    turn_angle: int = 6
    bullet_velocity: float = 13.0
    max_bullets: int = 4
    bullet_ttl: int = 35
    hyper_space_ttl: int = 100