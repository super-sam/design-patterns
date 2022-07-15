from dataclasses import dataclass


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name: str = name
        self.address: str = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f"{name} needs a doctor at {address}")


def call_family(name, *args):
    print(f"Calling {name}'s family")


if __name__ == "__main__":
    person = Person("Supratim", "Tankapani Road")
    person.falls_ill.append(call_doctor)
    person.falls_ill.append(call_family)

    person.catch_a_cold()
