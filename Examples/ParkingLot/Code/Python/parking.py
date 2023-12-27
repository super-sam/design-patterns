from abc import ABC, abstractmethod


class ParkingSpot(ABC):
    def __init__(self, id, is_free, vehicle) -> None:
        self.__id = id
        self.__is_free = is_free
        self.__vehicle = vehicle

    def get_is_free(self):
        pass

    @abstractmethod
    def assign_vehicle(self, vehicle):
        pass
    
    def remove_vehicle(self):
        pass

class Handicapped(ParkingSpot):
    def __init__(self, id, is_free, vehicle) -> None:
        super().__init__(id, is_free, vehicle)
    
    # vehicle here refers to an instance of the Vehicle class
    def assign_vehicle(self, vehicle):
        pass

class Large(ParkingSpot):
    def __init__(self, id, is_free, vehicle) -> None:
        super().__init__(id, is_free, vehicle)
    
    # vehicle here refers to an instance of the Vehicle class
    def assign_vehicle(self, vehicle):
        pass

class Motercycle(ParkingSpot):
    def __init__(self, id, is_free, vehicle) -> None:
        super().__init__(id, is_free, vehicle)
    
    # vehicle here refers to an instance of the Vehicle class
    def assign_vehicle(self, vehicle):
        pass

class Compact(ParkingSpot):
    def __init__(self, id, is_free, vehicle) -> None:
        super().__init__(id, is_free, vehicle)
    
    # vehicle here refers to an instance of the Vehicle class
    def assign_vehicle(self, vehicle):
        pass
