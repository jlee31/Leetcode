"""BUG: add_item seems to "remember" items across unrelated calls. Why?
Run: python3 bug.py
"""


def add_item(item, cart=[]):   # <-- look hard at this default argument
    cart.append(item)
    return cart


if __name__ == "__main__":
    cart1 = add_item("apple")
    print("cart1:", cart1)          # expected: ['apple']

    cart2 = add_item("banana")      # a brand-new, separate cart... right?
    print("cart2:", cart2)          # expected: ['banana']  -- but what prints?
