# Solid Design Principle
|||
|--|--|
|S| [Single Responsibility Principle (SRP)](#single-responsibility-principle)|
|O| [Open Close Principle (OCP)](#open-close-principle) |
|L| [Liskov Substitution Principle (LSP)](#liskov-substitution-principle)|
|I| [Interface Segregation Principle (ISP)](#interface-segrigation-principle)|
|D| [Dependency Inversion Principle (DIP)](#dependency-inversion-principle)|

## Single Responsibility Principle
A class should have onle one reason to change
### Problem
```mermaid
---
title: Book Invoice Printer
---
classDiagram
direction LR
class Book{
    name: str
    author: str
    year: int
    price: float
    isbn: long
    Book()
}

class Invoice{
    books: list~Book~
    quantity: int
    discount: float
    tax: float
    total: float
    Invoice()
    calculateTotal()
    printInvoice()
    saveToDatabase()
}
Invoice <-- Book
```
We have added Print & Storage functionality

### Solution
```mermaid
classDiagram
direction LR
class Book
class Invoice{
    books: list~Book~
    quantity: int
    discount: float
    tax: float
    total: float
    Invoice()
    calculateTotal()
}
class InvoicePrinter{
    invoice: Invoice
    print(): void
}
class InvoiceStorage{
    invoice: Invoice
    saveToDatabase(): void
}
Book --> Invoice
Invoice --o InvoicePrinter
Invoice --o InvoiceStorage
```


## Open Close Principle
A software artifact should be open for extension but close for modification

## Liskov Substitution Principle
Object of a subclass should behave the same way as of the superclass. Applies to abstraction concept like inheritance & polymorphism.

### Problem
```mermaid
classDiagram
direction LR
class Vehicle{
    - name: string
    - speed: int
    - startEngine(): void
}
class Car
class Bicycle
Vehicle <|-- Car: extends
Vehicle <|-- Bicycle: extends
```

### Solution
```mermaid
classDiagram
direction LR
class Vehicle{
    name: str
    speed: ind
}
class Motorized{
    startEngine(): void
}
class Manual{
    startMoving(): void
}
class Car
class Bicycle

Vehicle <|-- Motorized : extends
Vehicle <|-- Manual: extends
Motorized <|-- Car: extends
Manual <|-- Bicycle: extends
```

## Interface Segrigation Principle
Doesn't recommend having methods thatan interface would not use and require.

Precise code design thst follows the correct abstraction guidelines.

### Problem
```mermaid
classDiagram
direction BT
class Shape{
    <<interface>>
    area()*: float
    volume()*: float
}
class Square{
    area(): float
    volume(): float
}
class Cube{
    area(): float
    volume(): float
}
class Rectangle{
    area(): float
    volume(): float
}
Square ..|> Shape
Cube ..|> Shape
Rectangle ..|> Shape
```

### Solution
```mermaid
classDiagram
direction BT
class Shape{
    <<interface>>
    area()*: float
}
class Shape3D{
    <<interface>>
    volume()*: float
}
class Square{
    area(): float
}
class Cube{
    area(): float
    volume(): float
}
class Rectangle{
    area(): float
}
Square ..|> Shape
Rectangle ..|> Shape
Shape3D ..|> Shape
Cube ..|> Shape3D
```


## Dependency Inversion Principle
High level models should not depend on low level modules but rather should both depends on abstractions

### Problem
```mermaid
classDiagram
class Headmaster{
    teachers: List~Teacher~
    assistants: List~Assistant~
    helpers: List~Helpers~
    addTeacher(Teacher): void
    addAssistant(Assistant): void
    addHelper(Helper):void 
}
class Teacher
class Helper
class Assistant
Teacher --> Headmaster
Assistant --> Headmaster
Helper --> Headmaster

```
If additional faculty comes under headmaster, it will be difficult to add without changing the Headmaster.

### Solution
```mermaid
classDiagram
class Headmaster
    Headmaster: addFaculty(Faculty)- void
class Faculty
Faculty <-- Headmaster
Teacher --|> Faculty: extends
Helper --|> Faculty: extends
Assistant --|> Faculty: extends
Secretary ..|> Faculty: extends
```
