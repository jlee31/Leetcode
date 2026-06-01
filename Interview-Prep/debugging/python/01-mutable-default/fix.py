"""FIX: sentinel default (None), build a fresh list inside the function.
Run: python3 fix.py
"""


def add_item(item, cart=None):
    if cart is None:        # fresh list per call when caller didn't pass one
        cart = []
    cart.append(item)
    return cart


if __name__ == "__main__":
    cart1 = add_item("apple")
    print("cart1:", cart1)          # ['apple']

    cart2 = add_item("banana")
    print("cart2:", cart2)          # ['banana']  -- now truly independent

# Takeaway: default argument values are evaluated ONCE at def time and reused.
# Never use a mutable object ([], {}, set()) as a default; use None + build it
# inside. (A frozen/immutable default like 0 or "" is fine.)
