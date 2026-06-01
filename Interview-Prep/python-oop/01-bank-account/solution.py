"""BankAccount — reference solution.  Run: python3 solution.py"""


class InsufficientFunds(Exception):
    """Raised when a withdrawal exceeds the available balance."""


class BankAccount:
    def __init__(self, owner, balance=0.0):
        if balance < 0:
            raise ValueError("starting balance cannot be negative")
        self._owner = owner
        self._balance = balance
        self._txn_count = 0

    # Read-only properties: no setter is defined, so assignment raises
    # AttributeError. The underscore-prefixed backing attr is "private" by
    # convention (Python does not hard-enforce access).
    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @property
    def transaction_count(self):
        return self._txn_count

    @staticmethod
    def _require_positive(amount):
        if amount <= 0:
            raise ValueError("amount must be positive")

    def deposit(self, amount):
        self._require_positive(amount)
        self._balance += amount
        self._txn_count += 1

    def withdraw(self, amount):
        self._require_positive(amount)
        if amount > self._balance:
            raise InsufficientFunds(
                f"tried to withdraw {amount}, balance is {self._balance}"
            )
        self._balance -= amount
        self._txn_count += 1

    @classmethod
    def from_dict(cls, data):
        """Alternative constructor: BankAccount.from_dict({'owner':..., ...})."""
        return cls(data["owner"], data.get("balance", 0.0))

    def __repr__(self):
        return (f"BankAccount(owner={self._owner!r}, balance={self._balance}, "
                f"txns={self._txn_count})")


if __name__ == "__main__":
    acct = BankAccount("Joseph", 100.0)
    acct.deposit(50.0)
    acct.withdraw(30.0)
    print(acct)  # BankAccount(owner='Joseph', balance=120.0, txns=2)

    try:
        acct.balance = 999
    except AttributeError:
        print("balance is read-only ✓")

    try:
        acct.withdraw(1000.0)
    except InsufficientFunds as e:
        print("Rejected:", e)

# Notes:
# - __repr__ is for developers (unambiguous, ideally reconstructable). __str__
#   is for end users; if only __repr__ is defined, str() falls back to it.
# - !r in the f-string calls repr() on the value (quotes the string).
# - A read-only @property with no setter is the idiomatic "private with getter".
