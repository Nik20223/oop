from abc import ABC, abstractmethod


class Figure(ABC):
    """Базовый класс геометрической фигуры."""

    @abstractmethod
    def get_area(self) -> float:
        """Площадь фигуры."""

    @abstractmethod
    def get_perimeter(self) -> float:
        """Периметр фигуры."""

    @property
    def area(self) -> float:
        return self.get_area()

    @property
    def perimeter(self) -> float:
        return self.get_perimeter()

    def add_area(self, figure: "Figure") -> float:
        if not isinstance(figure, Figure):
            raise ValueError(
                f"Ожидалась геометрическая фигура, получено {type(figure).__name__}"
            )
        return self.get_area() + figure.get_area()
