from enum import Enum
from math import *
from dataclasses import dataclass


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

@dataclass
class Point:
    """Cartesian Point
    Attributes:
        x: X coordinate
        y: Y coordinate
    """
    x: float
    y: float

    def __str__(self):
        return f'Point: x is {self.x}, y is {self.y}'

    @staticmethod
    def new_cartesian_point(x: float, y: float):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * (sin(theta)))


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p)
    print(p2)