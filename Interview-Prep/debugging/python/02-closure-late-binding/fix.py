"""FIX: capture the current value of i, not the variable.
Run: python3 fix.py
"""


def make_multipliers():
    funcs = []
    for i in range(3):
        # i=i binds the CURRENT value as a default arg (evaluated now, per loop).
        funcs.append(lambda x, i=i: x * i)
    return funcs


# Equivalent, arguably clearer — a factory gives each i its own scope:
def make_multipliers_factory():
    def multiplier(i):
        return lambda x: x * i
    return [multiplier(i) for i in range(3)]


if __name__ == "__main__":
    times0, times1, times2 = make_multipliers()
    print(times0(10))   # 0
    print(times1(10))   # 10
    print(times2(10))   # 20

# Takeaway: a closure captures the variable by reference, resolved at CALL time.
# To freeze a per-iteration value, bind it explicitly (default arg) or give it a
# fresh scope (factory function).
