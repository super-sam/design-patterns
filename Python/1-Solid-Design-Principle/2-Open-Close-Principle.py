from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


'''
Adding new filters when the requirement comes violets Open Close Principle (OCP)
This, added new filters(funtions) when requirements comes cause

"State space explosion"
 
'''
# OCP = Open for extension, Closed for modification
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


# Specification Pattern

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return self.color == item.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return self.size == item.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class NewProductFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green Products (old): ')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    print('Large items:')
    for p in pf.filter_by_size(products, Size.LARGE):
        print(f' - {p.name} is large')

    print('Large blue items:')
    for p in pf.filter_by_size_and_color(products, Size.LARGE, Color.BLUE):
        print(f' - {p.name} is large and blue')

    print('Green Products (new): ')
    npf = NewProductFilter()
    green_spec = ColorSpecification(Color.GREEN)
    for p in npf.filter(products, green_spec):
        print(f' - {p.name} is green')

    print('Large items:')
    large_spec = SizeSpecification(Size.LARGE)
    for p in npf.filter(products, large_spec):
        print(f' - {p.name} is large')

    print('Large blue items:')
    # large_blue_spec = AndSpecification(large_spec, ColorSpecification(Color.BLUE))
    large_blue_spec = large_spec & ColorSpecification(Color.BLUE)
    # large_blue_spec = large_spec & ColorSpecification(Color.BLUE)
    for p in npf.filter(products, large_blue_spec):
        print(f' - {p.name} is large and blue')
