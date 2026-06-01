"""BankAccount — fill in the TODOs.  Run: python3 starter.py"""


class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance=0.0):
        # TODO: store owner, balance, transaction count in "private" attrs
        ...

    # TODO: @property balance  (read-only)
    # TODO: @property owner     (read-only)
    # TODO: @property transaction_count (read-only)

    def deposit(self, amount):
        ...  # TODO: validate positive, update balance + count

    def withdraw(self, amount):
        ...  # TODO: validate positive, reject overdraft, update

    def __repr__(self):
        ...  # TODO


if __name__ == "__main__":
    acct = BankAccount("Joseph", 100.0)
    acct.deposit(50.0)
    acct.withdraw(30.0)
    print(acct)
    try:
        acct.balance = 999  # should raise AttributeError (read-only)
    except AttributeError:
        print("balance is read-only ✓")
    try:
        acct.withdraw(1000.0)
    except InsufficientFunds as e:
        print("Rejected:", e)
