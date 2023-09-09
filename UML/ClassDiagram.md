# Class Diagram
## Class Notation
### Class

```mermaid
classDiagram
class Movie{
    + title: string
    - year: int
    # genre: string
    + setter(): void
    + setTitle(): void
    + getYear(): int
}   
```
### Access Modifier
| Public | Protected | Private |Package/Internal |
|--|--|--|--|
| - | # | +| ~ | 

### Enumeration
```mermaid
classDiagram
class EnumName{
    <<enumeration>>
    attributeType: Dtype
}
```
### Interface
```mermaid
classDiagram
class InterfaceName{
    <<interface>>
    fn(): rtype
}
```

### Abstract
```mermaid
classDiagram
class AbstractName{
    <<abstract>>
    attr: atype
    fn(): rtype
}
```

## Relations
```mermaid
graph LR
Relation --> Association
Relation --> Dependency
Association --> Class_Association
Association --> Object_Association
Class_Association --> Inheritance
Object_Association --> Simple_Association
Object_Association --> Composition
Object_Association --> Aggregation

```


### Association: Comunicate one to another object
#### __Class Association__
Inheritance Releationship

```mermaid
classDiagram
class Shape
class 2D
Shape<|--2D: extends
```
#### __Object Association__
1. **Simple**
```mermaid
classDiagram
class A
class B
A <-- B
```
2. **Aggregation**: Has independent existance
```mermaid
classDiagram
class Cupboard
class Room
class Table
Cupboard --o Room : has a
Room o-- Table: has a
```

3. **Composition**: Parts to built the object
```mermaid
classDiagram
class Leg
class Chair
class Seat
class Arm
Leg --* Chair : contains
Seat --* Chair: contains
Chair *-- Arm : contains
```
### Dependency
Class Dependent on another
```mermaid
classDiagram
class RegistrationManager{
    - addStudent(course, Student): void
}
class Student{
    - name: string
}
RegistrationManager ..> Student
```

### Relationships
```mermaid
classDiagram
class classA
class classB
class classC
class classD
class classE
class classF
class classG
class classH
class classI
class classJ
class classK
class classL
class classM
class classN
class classO
class classP
classA --|> classB : Inheritance
classC --* classD : Composition
classE --o classF : Aggregation
classG --> classH : Association
classI -- classJ : Link(Solid)
classK ..> classL : Dependency
classM ..|> classN : Realization
classO .. classP : Link(Dashed)

```