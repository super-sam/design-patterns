class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        old_can_vote = self.can_vote

        self._age = value
        self.property_changed('age', value)
        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)

    @property
    def can_vote(self):
        return self.age >= 18


class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        person.property_changed.append(
            self.person_changed
        )

    def person_changed(self, name, value):
        if name == "age":
            if value < 16:
                print("Sorry, you still cannot drive")
            else:
                print("Ok, you can drive now")
                self.person.property_changed.remove(
                    self.person_changed
                )


if __name__ == "__main__":
    def person_changed(name, value):
        if name == 'can_vote':
            print(f"Voting ability change to {value}")

    p = Person()
    p.property_changed.append(person_changed)
    ta = TrafficAuthority(p)
    for age in range(14, 21):
        print(f"Setting age to {age}")
        p.age = age
