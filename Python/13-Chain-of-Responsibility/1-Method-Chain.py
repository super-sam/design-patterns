from typing import Callable
from dataclasses import dataclass, field

@dataclass
class Creature:
    name: str
    attack: str
    defence: str

    def __str__(self):
        return f"{self.name} ({self.attack} / {self.defence})"

@dataclass
class CreatureModifier:
    creature: Creature
    next_modifier: Callable = field(default=None)

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Double {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()


class DoubleDefenceModifier(CreatureModifier):
    def handle(self):
        print(f"Double {self.creature.name}'s defence")
        self.creature.defence *= 2
        super().handle()


if __name__ == "__main__":
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)
    root.add_modifier(DoubleAttackModifier(goblin))
    root.handle()
    print(goblin)
    root.add_modifier(DoubleDefenceModifier(goblin))
    root.handle()
    print(goblin)