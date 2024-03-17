# Factory Design Pattern
A component responsible solely for the wholesale (not piecewise) creation of the objects.

## Why?

## When to Implement?
1. When you don’t know beforehand the exact types and dependencies of the objects your code should work with.

2. When you want to provide users of your library or framework with a way to extend its internal components.

3. When you want to provide users of your library or framework with a way to extend its internal components.

## Pros and Cons
### Pros
- Avoid tight coupling
- Single Responsibility Principle. Move creator code
- Open Close Principle

### Cons
- Increases complexity due to so many sub classes
