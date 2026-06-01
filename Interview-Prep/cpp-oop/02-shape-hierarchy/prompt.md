# Exercise: Shape Hierarchy (Polymorphism)

Build an abstract `Shape` base class and concrete `Circle` and `Rectangle`
subclasses. Then compute the total area of a heterogeneous collection of shapes
through base-class pointers.

## Requirements

- `Shape` is **abstract**: it has a pure virtual `double area() const = 0` and a
  pure virtual `std::string name() const = 0`.
- `Shape` has a **virtual destructor** (critical — see questions).
- `Circle(radius)` and `Rectangle(width, height)` implement both methods.
- Write a free function `double totalArea(const std::vector<std::unique_ptr<Shape>>&)`.
- In `main`, build a `vector<unique_ptr<Shape>>`, add a few shapes, print each
  shape's name + area, then the total.

## Design questions to answer out loud

1. **Why must `~Shape()` be virtual?** What is undefined behavior here without it?
2. What does `= 0` mean and why can't you instantiate `Shape` directly?
3. Why `std::unique_ptr<Shape>` in the container instead of `Shape` by value?
   (Hint: object slicing.)
4. What does `override` buy you on the derived methods?

## Stretch goals

- Add a `Triangle`. Did you have to touch `totalArea`? (Open/Closed Principle.)
- Add `virtual void scale(double factor)` and apply it polymorphically.
