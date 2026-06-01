"""BUG: all the generated functions return the same number. Why?
Run: python3 bug.py
"""


def make_multipliers():
    funcs = []
    for i in range(3):
        funcs.append(lambda x: x * i)   # <-- what does this lambda capture?
    return funcs


if __name__ == "__main__":
    times0, times1, times2 = make_multipliers()
    print(times0(10))   # expected 0
    print(times1(10))   # expected 10
    print(times2(10))   # expected 20
    # ...but they all print the same thing. What and why?
