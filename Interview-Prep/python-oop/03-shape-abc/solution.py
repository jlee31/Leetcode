"""Shape ABC — reference solution.  Run: python3 solution.py"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def name(self) -> str:
        ...


@dataclass
class Circle(Shape):
    radius: float

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def name(self) -> str:
        return "Circle"


@dataclass
class Rectangle(Shape):
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height

    def name(self) -> str:
        return "Rectangle"


def total_area(shapes) -> float:
    return sum(s.area() for s in shapes)


if __name__ == "__main__":
    shapes = [Circle(2.0), Rectangle(3.0, 4.0)]
    for s in shapes:
        print(f"{s.name()} area = {s.area():.2f}")
    print(f"Total: {total_area(shapes):.2f}")

    # Abstract enforcement: Shape() raises TypeError.
    try:
        Shape()
    except TypeError as e:
        print("Cannot instantiate Shape:", e)

# Notes:
# - @abstractmethod makes the class non-instantiable until ALL abstract methods
#   are overridden. A subclass that misses one is itself still abstract.
# - @dataclass generates __init__/__repr__/__eq__ from the annotated fields;
#   it composes fine with an ABC base.
# - Reach for ABC when you want a named contract + isinstance() checks; reach
#   for typing.Protocol when you only care about shape ("has these methods")
#   and don't want to force inheritance.
