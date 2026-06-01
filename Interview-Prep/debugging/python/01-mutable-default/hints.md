# Hints — mutable default argument

1. When is the default value `[]` created — once at function-definition time, or
   fresh on every call?
2. Answer: **once**, when the `def` is executed. Every call that doesn't pass
   `cart` shares the *same* list object. So `cart2` is actually
   `['apple', 'banana']`.
3. Confirm it: `print(add_item.__defaults__)` after the calls — the list grew.
4. Fix idiom: default to `None`, then create a new list inside the function:
   ```python
   def add_item(item, cart=None):
       if cart is None:
           cart = []
       cart.append(item)
       return cart
   ```
5. This applies to any mutable default: `[]`, `{}`, `set()`, or an object.
