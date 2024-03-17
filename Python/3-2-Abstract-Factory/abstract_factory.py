from __future__ import annotations
from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def has_legs(self) -> str:
        pass
    
    @abstractmethod
    def sit_on(self) -> str:
        pass

class ModernChair(Chair):
    def has_legs(self) -> str:
        return "Modern chair has 4 legs"
    
    def sit_on(self) -> str:
        return "Sitting on modern chair"

class VictorianChair(Chair):
    def has_legs(self) -> str:
        return "Victorian chair has 4 legs"
    
    def sit_on(self) -> str:
        return "Sitting on victorian chair"

class ArtDecoChair(Chair):
    def has_legs(self) -> str:
        return "Art deco chair has 4 legs"
    
    def sit_on(self) -> str:
        return "Sitting on art deco chair"

class Sofa(ABC):
    @abstractmethod
    def has_legs(self) -> str:
        pass
    
    @abstractmethod
    def sit_on(self) -> str:
        pass

class ModernSofa(Sofa):
    def has_legs(self) -> str:
        return "Modern sofa has 4 legs"
    
    def sit_on(self) -> str:
        return "Sitting on modern sofa"

class VictorianSofa(Sofa):
    def has_legs(self) -> str:
        return "Victorian sofa has 4 legs"
    
    def sit_on(self) -> str:
        return "Sitting on victorian sofa"

class ArtDecoSofa(Sofa):
    def has_legs(self) -> str:
        return "Art deco sofa has 4 legs"
    
    def sit_on(self) -> str:
        return "Sitting on art deco sofa"

class CoffeeTable(ABC):
    @abstractmethod
    def has_legs(self) -> str:
        pass
    
    @abstractmethod
    def put_on(self) -> str:
        pass

class ModernCoffeeTable(CoffeeTable):
    def has_legs(self) -> str:
        return "Modern coffee table has 4 legs"
    
    def put_on(self) -> str:
        return "Putting on modern coffee table"

class VictorianCoffeeTable(CoffeeTable):
    def has_legs(self) -> str:
        return "Victorian coffee table has 4 legs"
    
    def put_on(self) -> str:
        return "Putting on victorian coffee table"

class ArtDecoCoffeeTable(CoffeeTable):
    def has_legs(self) -> str:
        return "Art deco coffee table has 4 legs"
    
    def put_on(self) -> str:
        return "Putting on art deco coffee table"

class AbstractFactoryFurniture(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass


class ConcreteFactoryModernFurniture(AbstractFactoryFurniture):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_sofa(self) -> Sofa:
        return ModernSofa()
    
    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()
    

class ConcreteFactoryVictorianFurniture(AbstractFactoryFurniture):
    def create_chair(self) -> Chair:
        return VictorianChair()
    
    def create_sofa(self) -> Sofa:
        return VictorianSofa()
    
    def create_coffee_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()

class ConcreteFactoryArtDecoFurniture(AbstractFactoryFurniture):
    def create_chair(self) -> Chair:
        return ArtDecoChair()
    
    def create_sofa(self) -> Sofa:
        return ArtDecoSofa()
    
    def create_coffee_table(self) -> CoffeeTable:
        return ArtDecoCoffeeTable()

def client_code(factory: AbstractFactoryFurniture):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    coffee_table = factory.create_coffee_table()

    print(f"{chair.has_legs()}")
    print(f"{chair.sit_on()}")
    print(f"{sofa.has_legs()}")
    print(f"{sofa.sit_on()}")
    print(f"{coffee_table.has_legs()}")
    print(f"{coffee_table.put_on()}")

class FactoryFurniture():
    @staticmethod
    def create_modern_furniture() -> AbstractFactoryFurniture:
        return ConcreteFactoryModernFurniture()

    @staticmethod
    def create_victorian_furniture() -> AbstractFactoryFurniture:
        return ConcreteFactoryVictorianFurniture()
    
    @staticmethod
    def create_art_deco_furniture() -> AbstractFactoryFurniture:
        return ConcreteFactoryArtDecoFurniture()

if __name__ == "__main__":
    client_code(FactoryFurniture.create_modern_furniture())
    client_code(FactoryFurniture.create_victorian_furniture())
    client_code(FactoryFurniture.create_art_deco_furniture())
    