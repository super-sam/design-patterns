class Address:
    def __init__(self, pincode: int, addr_line: str, city: str, state: str, country: str) -> None:
        self.__pincode: int = pincode
        self.__address_line: str = addr_line
        self.__city: str = city
        self.__state: str = state
        self.__country: str = country


class Person:
    def __init__(self, name: str, address: Address, phone: str, email: str) -> None:
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email
        
