from .figure import Figure


class Rectangle(Figure):
    """Прямоугольник, задаваемый шириной и высотой."""

    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Стороны прямоугольника должны быть положительными")
        self._width = width
        self._height = height

    def get_area(self) -> float:
        return self._width * self._height

    def get_perimeter(self) -> float:
        return 2 * (self._width + self._height)
