'''
LSP (Liskov Substitution Principal)
Derived or child classes must be substitutable for their base or parent class

This ensure that any class that is child should be usable in place of its parent without
any unexpected behaviour.

'''
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def get_minimum_salary(self):
        pass

class EmployeeBonus(ABC):
    @abstractmethod
    def calculate_bonus(self, salary):
         pass


class PermanantEmployee(Employee, EmployeeBonus):
    def __init__(self, id, name):
        super().__init__(id, name)

    def calculate_bonus(self, salary):
        return 0.1 * salary

    def get_minimum_salary(self):
        return 15000


class TemporaryEmployee(Employee, EmployeeBonus):
    def __init__(self, id, name):
        super().__init__(id, name)

    def calculate_bonus(self, salary):
        return 0.05 * salary

    def get_minimum_salary(self):
        return 10000


class ContractEmployee(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)

    def get_minimum_salary(self):
        return 5000


if __name__ == '__main__':
    emp_john = PermanantEmployee(1, 'John')
    emp_jason = TemporaryEmployee(2, 'Jason')
    emp_jacob = ContractEmployee(2, 'Jacob')

    print(emp_john.calculate_bonus(100))
    print(emp_jason.calculate_bonus(100))
    print(dir(emp_jacob))