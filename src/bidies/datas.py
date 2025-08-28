from dataclasses import dataclass, field

@dataclass
class RockData:
    large_rock_type: int = 0
    medium_rock_type: int = 1
    small_rock_type: int = 2
    velocities: tuple[float, ...] = (1.5, 3.0, 4.5)
    scale: tuple[float, ...] = (2.5, 1.5, 0.6)
    rock_shape: int = 1

@dataclass
class SaucerData:
    large_saucer_type: int = 0
    small_saucer_type: int = 1
    velocities: tuple[float, ...] = (1.5, 2.5)    
    scales: tuple[float, ...] = (1.5, 1.0)
    scores: tuple[int, ...] = (500, 1000)
    point_list: list[tuple[int, int]] = field(default_factory=lambda: [(-9,0), (-3,-3), (-2,-6), (-2,-6), (2,-6), (3,-3), (9,0), (-9,0), (-3,4), (3,4), (9,0)])
    max_bullets: int = 1
    bullet_ttl: list[int] = field(default_factory=lambda: [60, 90])
    bullet_velocity: int = 5