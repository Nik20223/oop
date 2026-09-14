from math import sqrt

from .figure import Figure


class Triangle(Figure):
    """Треугольник, задаваемый тремя сторонами."""

    def __init__(self, first_side: float, second_side: float, third_side: float) -> None:
        self._validate(first_side, second_side, third_side)
        self._first_side = first_side
        self._second_side = second_side
        self._third_side = third_side

    @staticmethod
    def _validate(first_side: float, second_side: float, third_side: float) -> None:
        if min(first_side, second_side, third_side) <= 0:
            raise ValueError("Стороны треугольника должны быть положительными")
        if (
            first_side + second_side <= third_side
            or first_side + third_side <= second_side
            or second_side + third_side <= first_side
        ):
            raise ValueError("Треугольника с такими сторонами не существует")

    def get_area(self) -> float:
        semiperimeter = self.get_perimeter() / 2
        return sqrt(
            semiperimeter
            * (semiperimeter - self._first_side)
            * (semiperimeter - self._second_side)
            * (semiperimeter - self._third_side)
        )

    def get_perimeter(self) -> float:
        return self._first_side + self._second_side + self._third_side
