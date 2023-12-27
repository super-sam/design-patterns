from abc import ABC

class Address:
    def __init__(self, street, city, state, pincode, country) -> None:
        self.__street = street
        self.__city = city
        self.__state = state
        self.__pincode = pincode
        self.__country = country

class Person(ABC):
    def __init__(self, name: str, address: Address, email: str, phone: str) -> None:
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
    