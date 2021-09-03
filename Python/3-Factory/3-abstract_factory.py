from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This test is nice but I\'d prefer it with milk")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


def make_drink(type: str) -> HotDrinkFactory:
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialize = False

    def __init__(self):
        if not self.initialize:
            self.initialize = True
            for drink in self.AvailableDrink:
                name = drink.name[0] + drink.name[1:].lower()
                factory_name = f'{name}Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks: ')
        for factory in self.factories:
            print(factory[0])

        choice = input(f'Please pick drink (0-{len(self.factories) - 1}): ')
        idx = int(choice)
        s = input(f'Specify amount: ')
        amount = int(s)

        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    entry = input('What drink do you like?')
    drink = make_drink(entry)
    drink.consume()

    hdm = HotDrinkMachine()
    new_drink = hdm.make_drink()
    new_drink.consume()