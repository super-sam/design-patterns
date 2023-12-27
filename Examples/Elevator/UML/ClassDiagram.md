# Class Diagram

## Button
```mermaid
classDiagram
class Button{
    <<Abstract>>
    - status: bool
    + pressedDown(): bool
    + isPressed(): bool
}

class ElevatorButton{
    - destinationFloorNumber : int
}

class HallButton{
    - buttonSign: Direction
    - sourceFloorNumber: int
}

Button <|-- ElevatorButton : Extends
Button <|-- HallButton : Extends
```

## Elevator & Hall Panel
```mermaid
---
title: R6, R7
---
classDiagram
class ElevatorPanel{
    - floorButtons: List~ElevatorButton~
    - openButton: ElevatorButton
    - closeButton: ElevetorButton
}

class HallPanel{
    - up: HallButton
    - down: HallButton
}
```

## Display
```mermaid
classDiagram
class Display{
    - floor: int
    - capacity: int
    - direction: Direction
    + showElevatorDisplay()
    + showHallDisplay()
} 
```

## Door
```mermaid
classDiagram
class Door{
    - state: DoorState
    + isOpen(): bool
}
```

## Elevetor Car
```mermaid
classDiagram
class ElevatorCar{
    - id: int
    - door: Door
    - state: ElevatorState
    - display: Display
    - panel: ElevatorPanel
    - currentFloor: int
    + openDoor() : bool
    + closeDoor(): bool
    + move(): bool
    + stop(): bool
}
```

## Floor & Building
```mermaid
---
title: R10
---
classDiagram
class Floor{
    - displays: List~Display~
    - panels: List~HallPanel~
    + isBottomMost(): bool
    + isTopMost(): bool
}

class Building{
    - floors: List~Floor~
    - elevators: List~ElevatorCar~
}
```

## Elevator System
```mermaid
classDiagram
class ElevatorSystem{
    - building: Building
    + monitoring()
    + selectBestElevatorCar()
}
```

## Enumerations
```mermaid
classDiagram
class ElevatorState{
    <<enumeration>>
    IDLE
    UP
    DOWN
}
class Direction{
    <<enumetation>>
    UP
    DOWN
}
class DoorState{
    <<enumetation>>
    OPEN
    CLOSE
}
```

## Relationship

### Aggregation
```mermaid
classDiagram
direction LR
Building --o ElevatorSystem
```

### Composition
```mermaid
classDiagram
ElevatorButton --* ElevatorPanel
ElevatorPanel --* ElevatorCar
Display --* Floor
Display --* ElevatorCar
HallButton --* HallPanel
HallPanel --* Floor
Floor --* Building
ElevatorCar --* Building
ElevatorCar *-- Door
```

### Inheritance
```mermaid
classDiagram
direction TB
Button <|-- HallButton: extends
Button <|-- ElevatorButton: extends

```

## Design Patterns
- **Strategy Pattern**: The system could have multiple dispatch requrest depending on the particular layout of the building and its senarios