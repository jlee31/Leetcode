# Exercise: UniquePtr (RAII, Rule of Five, Move Semantics)

Implement a minimal `UniquePtr<T>` — a smart pointer that exclusively owns a
heap object and frees it automatically. This is the canonical question for
testing whether you *really* understand C++ resource management.

## Requirements

- `UniquePtr(T* p = nullptr)` takes ownership of `p`.
- Destructor `delete`s the owned pointer.
- **Non-copyable**: copy constructor and copy assignment are `= delete`
  (two owners would double-free).
- **Movable**: move constructor and move assignment transfer ownership and
  leave the source null.
- `operator*`, `operator->`, `get()`, `release()`, `reset()`,
  and `explicit operator bool()`.

## Design questions to answer out loud

1. **Rule of Five**: which 5 special members are in play, and what's your choice
   for each (define / default / delete)?
2. Why must a moved-from `UniquePtr` be left `nullptr`?
3. Why is `operator bool` `explicit`?
4. What's the difference between `release()` and `reset()`?
5. How does this differ from `std::shared_ptr` (ownership model)?

## Stretch goals

- Implement the move-assignment using the copy-and-swap... no — explain why
  copy-and-swap doesn't apply here, and use the move-and-swap idiom instead.
- Add a custom deleter template parameter.
