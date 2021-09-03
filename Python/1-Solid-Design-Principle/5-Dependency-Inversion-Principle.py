from enum import Enum
from abc import abstractmethod
# High level class/modules shouldn't depend on low level modules
# They should depend on abstractions


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBILING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                print(f'{name} has a child called {r[2].name}')

# Problem is High level Research depends on how data is stored in Relationship
# If we change relation from list to dict, hight level Research will break
class Research:
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    def __init__(self, relationships):
        relationships.find_all_children_of('John')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relations = Relationships()
relations.add_parent_and_child(parent, child1)
relations.add_parent_and_child(parent, child2)

Research(relations)
