# Python OOP Track

Python-idiomatic OOP. Same design pillars as the C++ track, but exercising
Python-specific tools: dunder methods, `@property`, abstract base classes, and
`@dataclass`.

## Exercises (recommended order)

1. **[01-bank-account/](01-bank-account/)** — Encapsulation with `@property`
   and a read-only balance. Compare your approach to the C++ version.
2. **[02-vector2d/](02-vector2d/)** — Operator overloading via dunder methods
   (`__add__`, `__eq__`, `__repr__`, `__abs__`, ...).
3. **[03-shape-abc/](03-shape-abc/)** — Abstract base classes with
   `abc.ABC` / `@abstractmethod`, plus `@dataclass`.

## What interviewers probe in Python OOP

- **`@property`** vs. public attributes — when to use which; how to make a
  read-only or validated attribute.
- **Dunder methods** — `__repr__` vs `__str__`, `__eq__` + `__hash__` pairing,
  `__add__`/`__radd__`, `__len__`, `__iter__`.
- **`__slots__`** — memory savings and the tradeoff (no `__dict__`).
- **ABCs** — enforcing an interface; `abstractmethod`; why duck typing isn't
  always enough.
- **Class vs static vs instance methods** — `@classmethod` (alt constructors),
  `@staticmethod`.
- **`@dataclass`** — what it generates (`__init__`, `__repr__`, `__eq__`),
  `frozen=True`, `field(default_factory=...)`.

## Run

```bash
python3 solution.py
```
