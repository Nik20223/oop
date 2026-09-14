from .rectangle import Rectangle


class Square(Rectangle):
    """Квадрат, задаваемый стороной."""

    def __init__(self, side: float) -> None:
        super().__init__(side, side)
