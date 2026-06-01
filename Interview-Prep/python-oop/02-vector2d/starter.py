"""Vector2D — fill in the TODOs.  Run: python3 starter.py"""
import math


class Vector2D:
    __slots__ = ("_x", "_y")

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # TODO: __repr__
    # TODO: __eq__  and  __hash__
    # TODO: __add__, __sub__
    # TODO: __mul__, __rmul__ (scalar)
    # TODO: __abs__ (magnitude)
    # TODO: __iter__
    # TODO: dot(self, other)


if __name__ == "__main__":
    a = Vector2D(1, 2)
    b = Vector2D(3, 4)
    print(a + b)            # Vector2D(4, 6)
    print(2 * a)            # Vector2D(2, 4)
    print(abs(b))           # 5.0
    print(a.dot(b))         # 11
    print(a == Vector2D(1, 2))  # True
    x, y = a                # unpacking via __iter__
    print(x, y)             # 1 2
    print({a, b, Vector2D(1, 2)})  # set has 2 elements (a == dup)
