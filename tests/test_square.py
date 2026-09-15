import pytest

from src.figure import Figure
from src.rectangle import Rectangle
from src.square import Square


@pytest.mark.parametrize("side, area, perimeter", [(10, 100, 40), (1, 1, 4), (2.5, 6.25, 10)])
def test_area_and_perimeter(side, area, perimeter):
    square = Square(side)
    assert square.area == pytest.approx(area)
    assert square.perimeter == pytest.approx(perimeter)


def test_square_inherits_from_rectangle_and_figure():
    square = Square(5)
    assert isinstance(square, Rectangle)
    assert isinstance(square, Figure)


def test_square_is_rectangle_with_equal_sides():
    square = Square(7)
    assert square._width == square._height == 7


def test_formulas_are_inherited_from_rectangle():
    square = Square(4)
    plain_rectangle = Rectangle(4, 4)
    assert square.get_area() == plain_rectangle.get_area()
    assert square.get_perimeter() == plain_rectangle.get_perimeter()


@pytest.mark.parametrize("side", [0, -1, -2.5])
def test_non_positive_side_raises(side):
    with pytest.raises(ValueError):
        Square(side)


def test_add_area_sums_areas():
    assert Square(10).add_area(Square(5)) == pytest.approx(125)
