# Hints — memory leak on early return

1. Trace every path out of `process`. Is `delete[]` reached on all of them?
2. The `n <= 0` branch `return false;`s *before* the `delete[]`.
3. This is exactly the bug RAII exists to prevent: tie the resource's lifetime
   to an object so it's freed no matter how the scope exits (early return,
   exception, ...).
4. Best fix: stop using `new`/`delete` entirely. Use
   `std::vector<int>` (or `std::unique_ptr<int[]>`) and the cleanup is automatic.
5. Lesser fix: `delete[] buf;` before the early `return`. Works, but every new
   exit path re-introduces the risk. Prefer RAII.
