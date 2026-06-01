# Interview Prep

Hands-on practice material for technical interviews. Each track is a folder of
self-contained exercises with a **prompt**, **starter code**, and a **solution**
kept in a separate file so you can practice cold and check yourself after.

## Tracks

| Folder | Focus | Languages |
|---|---|---|
| [cpp-oop/](cpp-oop/) | Object-oriented design: encapsulation, polymorphism, RAII, move semantics | C++ |
| [python-oop/](python-oop/) | Classes, dunder methods, properties, ABCs, dataclasses | Python |
| [debugging/](debugging/) | Diagnose & fix broken programs: segfaults, leaks, races, logic bugs | C++ / Python |
| [systems-design/](systems-design/) | High-level design prompts + low-level design (LLD) coding | Language-agnostic / Python |
| [ml-prep/](ml-prep/) | ML concepts, implement-from-scratch, ML system design | Python |

## How to practice

1. Open a track's `README.md` for the exercise list and recommended order.
2. Read the exercise `prompt.md`. **Don't look at the solution.**
3. Work in `starter.*` (or the `bug.*` file for debugging) until it works.
4. Compare against `solution.*` / `fix.*` and read the *why*.

## Running things

```bash
# C++ (C++17)
g++ -std=c++17 -Wall -Wextra -g starter.cpp -o starter && ./starter

# C++ with sanitizers (great for the debugging track)
g++ -std=c++17 -g -fsanitize=address,undefined starter.cpp -o starter && ./starter

# Python (3.10+)
python3 starter.py
```

## Suggested 2-week rotation

- **Days 1–3:** cpp-oop + python-oop (one exercise each per day)
- **Days 4–5:** debugging drills (timed — aim to find the bug in <10 min)
- **Days 6–8:** systems-design (one HLD prompt + one LLD per day)
- **Days 9–11:** ml-prep (concepts + one from-scratch impl per day)
- **Days 12–14:** mixed mock — pick one from each track, no notes

> Tip: for OOP/LLD exercises, narrate your design tradeoffs out loud as if an
> interviewer is in the room. The reasoning matters as much as the code.
