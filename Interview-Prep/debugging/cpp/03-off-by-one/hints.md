# Hints — off-by-one / buffer overrun

1. Valid indices for an array of size `n` are `0 .. n-1`. What's the last index
   the loop touches?
2. `i <= n` runs with `i == n` too, reading `a[n]` — one past the end. That's
   out-of-bounds: undefined behavior (garbage value, or a crash, or a silent
   wrong sum).
3. AddressSanitizer reports a **heap/stack-buffer-overflow** at `a[i]`.
4. Fix: `i < n`. The half-open range `[0, n)` is the C++ convention precisely
   because it makes the count obvious (`n` elements) and avoids this trap.
