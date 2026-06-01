"""Vector2D — reference solution.  Run: python3 solution.py"""
import math


class Vector2D:
    # __slots__ removes the per-instance __dict__: less memory, and blocks
    # adding new attributes (helps immutability).
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

    def __repr__(self):
        return f"Vector2D({self._x}, {self._y})"

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self._x == other._x and self._y == other._y

    # Must be consistent with __eq__: equal objects MUST hash equal.
    def __hash__(self):
        return hash((self._x, self._y))

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self._x - other._x, self._y - other._y)

    def __mul__(self, scalar):
        # v * 3
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar):
        # 3 * v  -> Python tries int.__mul__(3, v) first, gets NotImplemented,
        # then falls back to Vector2D.__rmul__(v, 3).
        return self.__mul__(scalar)

    def __abs__(self):
        return math.hypot(self._x, self._y)

    def __iter__(self):
        yield self._x
        yield self._y

    def dot(self, other):
        return self._x * other._x + self._y * other._y


if __name__ == "__main__":
    a = Vector2D(1, 2)
    b = Vector2D(3, 4)
    print(a + b)                    # Vector2D(4, 6)
    print(2 * a)                    # Vector2D(2, 4)
    print(abs(b))                   # 5.0
    print(a.dot(b))                 # 11
    print(a == Vector2D(1, 2))      # True
    x, y = a
    print(x, y)                     # 1 2
    print({a, b, Vector2D(1, 2)})   # {Vector2D(1, 2), Vector2D(3, 4)}

# Notes:
# - Returning NotImplemented (a singleton, not an exception) lets Python try
#   the reflected operation or raise TypeError with a good message.
# - If you define __eq__ but not __hash__, Python sets __hash__ = None and the
#   object becomes unhashable — can't be a dict key or set member.
# - Compare all this boilerplate to: @dataclass(frozen=True) gives __init__,
#   __repr__, __eq__, and __hash__ for free (you'd still add the operators).
