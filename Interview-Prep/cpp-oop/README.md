# C++ OOP Track

Design-focused C++ exercises. Each tests a different pillar of OOP plus
C++-specific resource management.

## Exercises (recommended order)

1. **[01-bank-account/](01-bank-account/)** — Encapsulation & invariants.
   Build a `BankAccount` that can never go negative and validates its inputs.
2. **[02-shape-hierarchy/](02-shape-hierarchy/)** — Polymorphism & abstract
   base classes. Virtual dispatch, pure virtual methods, virtual destructors.
3. **[03-unique-ptr/](03-unique-ptr/)** — RAII, the Rule of Five, and move
   semantics. Implement a minimal `UniquePtr<T>`.

## What interviewers probe in C++ OOP

- **Virtual destructors** — deleting a derived object through a base pointer is
  UB without one. Always ask: "is this class meant to be a base?"
- **Rule of Zero/Three/Five** — if you manage a resource, you owe copy/move
  ctor, copy/move assignment, and destructor (or `= delete` them).
- **Pass by `const&`** for non-trivial types you don't intend to copy.
- **`explicit`** on single-arg constructors to avoid implicit conversions.
- **`const` correctness** — mark methods that don't mutate as `const`.
- **Move semantics** — `std::move`, when copies are elided, what a moved-from
  object looks like.

## Build

```bash
g++ -std=c++17 -Wall -Wextra -g solution.cpp -o solution && ./solution
```
