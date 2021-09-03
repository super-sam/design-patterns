# Not Recommended
class CEO:
    __shared_state = {
        'name': 'Supratim',
        'age': 30
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old'

class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} is managing INR {self.money_managed}'


if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 29
    print(ceo1 == ceo2)
    print(ceo1)
    print(ceo2)

    cfo1 = CFO()
    cfo1.name = 'Supratim'
    cfo1.money_managed = 10
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Sapna'
    cfo2.money_managed = 100

    print(cfo1 == cfo2)
    print(cfo1)
    print(cfo2)