"""Shape ABC — fill in the TODOs.  Run: python3 starter.py"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


class Shape(ABC):
    ...  # TODO: @abstractmethod area(self); @abstractmethod name(self)


# TODO: @dataclass class Circle(Shape): radius: float ...
# TODO: @dataclass class Rectangle(Shape): width: float; height: float ...


def total_area(shapes):
    ...  # TODO: sum of areas


if __name__ == "__main__":
    shapes = []  # TODO: [Circle(2.0), Rectangle(3.0, 4.0)]
    for s in shapes:
        print(f"{s.name()} area = {s.area():.2f}")
    print("Total:", total_area(shapes))
