#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Copyright (C) 2008  Nick Redshaw
#    Copyright (C) 2018  Francisco Sanchez Arroyo
#

import pygame, math

import math
import pygame

from .geometry import calculate_intersect_point

class VectorSprite:

    def __init__(self, position, heading, point_list, angle=0, color=(255, 255, 255)):
        self.position = position
        self.heading = heading
        self.angle = angle
        self.v_angle = 0
        self.point_list = point_list
        self.color = color
        self.ttl = 25

        self.bounding_rect = pygame.Rect(0, 0, 0, 0)
        self.transformed_point_list = []

    def move(self):
        self._update_position()
        self.rotate_and_transform()

    def _update_position(self):
        self.position.x += self.heading.x
        self.position.y += self.heading.y
        self.angle += self.v_angle

    def rotate_and_transform(self):
        self.transformed_point_list = [
            self._translate_point(self._rotate_point(p))
            for p in self.point_list
        ]

        self.update_bounding_rect()


    def _rotate_point(self, point):
        cos_val = math.cos(math.radians(self.angle))
        sin_val = math.sin(math.radians(self.angle))
        x = point[0] * cos_val + point[1] * sin_val
        y = point[1] * cos_val - point[0] * sin_val
        return [int(x), int(y)]

    def _translate_point(self, point):
        return [point[0] + self.position.x, point[1] + self.position.y]

    def scale(self, point, scale):
        x = int(point[0] * scale)
        y = int(point[1] * scale)
        return [x, y]

    def draw(self):
        self.rotate_and_transform()
        return self.transformed_point_list

    def collides_with(self, target):
        return self.bounding_rect.colliderect(target.bounding_rect)

    def check_polygon_collision(self, target):
        for i in range(len(self.transformed_point_list)):
            for j in range(len(target.transformed_point_list)):
                p1 = self.transformed_point_list[i-1]
                p2 = self.transformed_point_list[i]
                p3 = target.transformed_point_list[j-1]
                p4 = target.transformed_point_list[j]
                p = calculate_intersect_point(p1, p2, p3, p4)
                if p is not None:
                    return p
        return None

    def update_bounding_rect(self):
        if not self.transformed_point_list:
            return
        xs = [p[0] for p in self.transformed_point_list]
        ys = [p[1] for p in self.transformed_point_list]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        self.bounding_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
