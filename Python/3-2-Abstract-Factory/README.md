# Abstract Factory (Abstract & Concrete)
Allows you to create families of the related obbject without specifing the concrete class.

## Problem
||Chair | Sofa | Coffee Table |
|--|--|--|--|
|Art Deco| ADC | ADS| ACT |
| Victorian| VC | VS| VCT |
| Morden| MC | MS | MCT |

We need to create individual furniture so that they match the family

## When to Implement?
1. When your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility.
2. Consider implementing the Abstract Factory when you have a class with a set of Factory Methods that blur its primary responsibility.

## Pros and Cons
### Pros
- Products you’re getting from a factory are compatible with each other.
- Avoid tight coupling
- Single Responsibility Principle. Move creator code
- Open Close Principle

### Cons
- Increases complexity due to so many sub classes
