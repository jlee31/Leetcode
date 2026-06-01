# Exercise: Vector2D (Operator Overloading / Dunder Methods)

Implement an immutable 2D vector class supporting arithmetic and comparison
via Python's special ("dunder") methods.

## Requirements

Implement `Vector2D(x, y)` with:

- `__repr__` → `Vector2D(1, 2)`
- `__eq__` → component-wise equality (and a matching `__hash__` so it can go
  in a `set`/`dict`)
- `__add__`, `__sub__` → vector + vector
- `__mul__` and `__rmul__` → scalar multiplication (`v * 3` **and** `3 * v`)
- `__abs__` → Euclidean magnitude
- `__iter__` → yields x then y (so `x, y = v` unpacking works)
- `dot(other)` → dot product

Make instances **immutable** (use `__slots__` or properties; don't allow
reassigning `x`/`y` after construction).

## Design questions to answer out loud

1. Why pair `__eq__` with `__hash__`? What breaks in a `set` if you don't?
2. What's `__rmul__` for — when does Python call it instead of `__mul__`?
3. Why might you return `NotImplemented` (not raise) for unsupported operand
   types?
4. How does `__iter__` enable tuple unpacking `x, y = v`?

## Stretch goals

- Add `__getitem__` so `v[0]`/`v[1]` work.
- Make it a `@dataclass(frozen=True)` instead and compare the boilerplate saved.
