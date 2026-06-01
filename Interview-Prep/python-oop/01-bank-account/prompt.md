# Exercise: BankAccount (Encapsulation, the Pythonic way)

Same spec as the C++ version, but Python idioms differ. Python has no truly
private members — you use a leading underscore convention plus `@property`.

## Requirements

- `BankAccount(owner, balance=0.0)`.
- `deposit(amount)` / `withdraw(amount)` with the same validation rules:
  positive amounts only; no overdraft.
- `balance` is a **read-only property** — `acct.balance` works, but
  `acct.balance = 5` raises `AttributeError`.
- `owner` read-only property.
- `transaction_count` read-only property.
- Raise `ValueError` for bad amounts, and a custom `InsufficientFunds`
  exception for overdrafts.
- Implement `__repr__` so the object prints usefully.

## Design questions to answer out loud

1. Why `@property` for `balance` instead of a public `self.balance`?
2. What does the leading underscore (`self._balance`) communicate? Is it enforced?
3. When would you define a custom exception class vs. reuse `ValueError`?
4. What's the difference between `__repr__` and `__str__`?

## Stretch goals

- Add a `@classmethod from_dict(cls, data)` alternative constructor.
- Add `__slots__` and explain what it changes.
