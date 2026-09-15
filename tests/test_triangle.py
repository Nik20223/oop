import pytest

from src.figure import Figure
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize(
    "first, second, third, area, perimeter",
    [
        (3, 4, 5, 6, 12),
        (13, 14, 15, 84, 42),
        (5, 5, 6, 12, 16),
        (6, 8, 10, 24, 24),
    ],
)
def test_area_and_perimeter(first, second, third, area, perimeter):
    triangle = Triangle(first, second, third)
    assert triangle.area == pytest.approx(area)
    assert triangle.perimeter == pytest.approx(perimeter)


def test_triangle_is_a_figure():
    assert isinstance(Triangle(3, 4, 5), Figure)


@pytest.mark.parametrize(
    "sides",
    [
        (1, 2, 3),
        (1, 2, 10),
        (10, 2, 1),
        (2, 10, 1),
        (5, 1, 1),
    ],
)
def test_triangle_inequality_violation_raises(sides):
    with pytest.raises(ValueError):
        Triangle(*sides)


@pytest.mark.parametrize(
    "sides",
    [
        (0, 4, 5),
        (4, 0, 5),
        (4, 5, 0),
        (-1, 4, 5),
        (4, -5, 5),
    ],
)
def test_non_positive_sides_raise(sides):
    with pytest.raises(ValueError):
        Triangle(*sides)


def test_add_area_sums_areas():
    assert Triangle(13, 14, 15).add_area(Triangle(3, 4, 5)) == pytest.approx(90)


def test_add_area_with_another_figure_type():
    assert Triangle(13, 14, 15).add_area(Square(10)) == pytest.approx(184)
