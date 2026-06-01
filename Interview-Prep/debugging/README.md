# Debugging Track

Each folder contains a **`bug`** file with a real defect, a **`hints.md`** (read
only if stuck), and a **`fix`** file with the correction and an explanation.

Goal: read the buggy program, predict what it does, run it, and diagnose the
defect — ideally before opening hints. Time-box yourself to ~10 minutes each.

## Exercises

### C++
- **[cpp/01-dangling-pointer/](cpp/01-dangling-pointer/)** — returns a reference
  to a local. Classic UB.
- **[cpp/02-memory-leak/](cpp/02-memory-leak/)** — `new` without `delete` on
  an early-return path.
- **[cpp/03-off-by-one/](cpp/03-off-by-one/)** — loop bound overruns the buffer.

### Python
- **[python/01-mutable-default/](python/01-mutable-default/)** — the famous
  mutable default argument trap.
- **[python/02-closure-late-binding/](python/02-closure-late-binding/)** —
  closures capture the variable, not its value.

## Your debugging toolkit

**C++**
```bash
# AddressSanitizer catches use-after-free, buffer overflow, leaks:
g++ -std=c++17 -g -fsanitize=address,undefined bug.cpp -o bug && ./bug

# Valgrind (alternative leak/UB detector):
valgrind --leak-check=full ./bug

# Step through with a debugger:
g++ -std=c++17 -g bug.cpp -o bug && lldb ./bug   # (or gdb)
```

**Python**
```bash
python3 -X dev bug.py        # enables extra runtime checks/warnings
python3 -m pdb bug.py        # interactive debugger; `b`, `n`, `s`, `p var`
```

## A method for the interview

1. **Reproduce** — get a deterministic failing case.
2. **Localize** — bisect: where does state first go wrong? (prints / breakpoints)
3. **Hypothesize** — name the root cause, not just the symptom.
4. **Fix & verify** — change one thing; confirm the repro now passes.
5. **Generalize** — is this bug pattern elsewhere in the code?
