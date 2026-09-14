from math import pi

from .figure import Figure


class Circle(Figure):
    """Круг, задаваемый радиусом."""

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Радиус круга должен быть положительным")
        self._radius = radius

    def get_area(self) -> float:
        return pi * self._radius**2

    def get_perimeter(self) -> float:
        return 2 * pi * self._radius
