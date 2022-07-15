from abc import ABC, abstractmethod
import unittest


class Shape(ABC):
    def __str__(self):
        return  ""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def resize(self, factor):
        self.side *= factor

    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def __getattr__(self, item):
        for key in self.__dict__.keys():
            if hasattr(self.__dict__[key], item):
                return getattr(self.__dict__['shape'], item)
        raise KeyError

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __delattr__(self, item):
        delattr(self.__dict__["shape"], item)

    def __str__(self):
        return f'{self.shape} has the color {self.color}'


class Evaluate(unittest.TestCase):
    def test_circle(self):
        circle = ColoredShape(Circle(5), 'red')
        self.assertEqual('A circle of radius 5 has the color red', str(circle))

        circle.resize(10)
        self.assertEqual('A circle of radius 50 has the color red', str(circle))

        circle.color = 'blue'
        self.assertEqual('A circle of radius 50 has the color blue', str(circle))

    def test_size(self):
        square = ColoredShape(Square(5), 'green')
        self.assertEqual('A square with side 5 has the color green', str(square))

        square.resize(2)
        self.assertEqual('A square with side 10 has the color green', str(square))


if __name__ == "__main__":
    unittest.main()