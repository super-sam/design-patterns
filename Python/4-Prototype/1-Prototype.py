from dataclasses import dataclass
from typing import Text
import copy


@dataclass
class Address:
    street_address: Text
    city: str
    country: str

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

@dataclass
class Person:
    name: str
    address: Address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


supratim = Person('Supratim', Address('123 patrapada', 'Bhubaneswar', 'India'))
print(supratim)
sapna = supratim
sapna.name = "Sapna"
print("Info".center(50, '-'))
print(supratim)
print(sapna)

print("Deep Copy".center(50, '-'))
supratim = copy.deepcopy(sapna)
supratim.name = 'Supratim'
supratim.address.street_address = '333 Suryanagar'

print(supratim)
print(sapna)