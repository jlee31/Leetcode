# Exercise: BankAccount (Encapsulation)

Design a `BankAccount` class that enforces its own invariants. A user of the
class should never be able to put it into an invalid state.

## Requirements

- Construct with an owner name and an optional starting balance (default 0).
- `deposit(amount)` — adds to the balance. Reject non-positive amounts.
- `withdraw(amount)` — subtracts, but **never allow the balance to go negative**.
  Reject non-positive amounts and overdrafts.
- `balance()` — read-only accessor (must be a `const` method).
- `owner()` — read-only accessor.
- Track a transaction count (how many successful deposits + withdrawals).
- On a rejected operation, throw `std::invalid_argument` (bad amount) or
  `std::runtime_error` (overdraft). Return type is up to you otherwise.

## Design questions to answer out loud

1. Which members are `private`? Why should `balance_` never be public?
2. Why is `balance()` marked `const`?
3. Should the constructor be `explicit`? What breaks if it isn't?
4. Where do you validate — in the constructor, the mutators, or both?

## Stretch goals

- Make the amount type robust (cents as integers vs. floating-point dollars —
  discuss the floating-point pitfall).
- Add `transfer(other, amount)` between two accounts atomically.
