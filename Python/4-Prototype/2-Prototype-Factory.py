from dataclasses import dataclass
from typing import Text
import copy


@dataclass
class Address:
    street_address: Text
    suite: int
    city: str

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'



@dataclass
class Employee:
    name: str
    address: Address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee: Employee = Employee('', Address('123 east drive', 0, 'Bhubaneswar'))
    aux_office_employee: Employee = Employee('', Address('123b east drive', 0, 'Bhubaneswar'))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, suite)

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee, name, suite)


supratim = EmployeeFactory.new_main_office_employee('Supratim', 101)
sapna = EmployeeFactory.new_aux_office_employee('Sapna', 503)

print(supratim)
print(sapna)