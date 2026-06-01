# Exercise: Shape ABC (Abstract Base Classes + dataclasses)

Recreate the shape hierarchy in Python using `abc.ABC` to enforce the interface,
and `@dataclass` to cut constructor boilerplate.

## Requirements

- `Shape(ABC)` with `@abstractmethod def area(self)` and
  `@abstractmethod def name(self)`. Instantiating `Shape()` must raise
  `TypeError`.
- `Circle` and `Rectangle` as `@dataclass`es that subclass `Shape` and
  implement both methods.
- A `total_area(shapes)` function.
- Demonstrate that forgetting to implement `area` in a subclass makes that
  subclass un-instantiable too.

## Design questions to answer out loud

1. What does `abc.ABC` / `@abstractmethod` give you that plain duck typing
   doesn't?
2. Can a `@dataclass` subclass an ABC? What does `@dataclass` generate?
3. When is an ABC overkill (i.e., when is duck typing fine)?
4. `Protocol` (structural typing) vs `ABC` (nominal) — when would you reach for
   each?

## Stretch goals

- Rewrite using `typing.Protocol` instead of `ABC` and compare.
