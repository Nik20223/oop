import math

import pytest

from src import Circle, Rectangle, Square, Triangle
from src.figure import Figure


def test_figure_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Figure()


def test_abstract_methods_are_declared():
    assert {"get_area", "get_perimeter"} <= Figure.__abstractmethods__


def test_all_figures_inherit_from_figure():
    figures = (
        Triangle(3, 4, 5),
        Rectangle(2, 3),
        Square(2),
        Circle(1),
    )
    assert all(isinstance(figure, Figure) for figure in figures)


def test_area_and_perimeter_properties_delegate_to_methods():
    rectangle = Rectangle(2, 3)
    assert rectangle.area == rectangle.get_area()
    assert rectangle.perimeter == rectangle.get_perimeter()


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (Triangle(3, 4, 5), Square(2), 6 + 4),
        (Square(2), Rectangle(2, 3), 4 + 6),
        (Circle(1), Circle(1), 2 * math.pi),
    ],
)
def test_add_area_returns_sum_of_areas(first, second, expected):
    assert first.add_area(second) == pytest.approx(expected)


@pytest.mark.parametrize("not_a_figure", [42, 3.14, "figure", None, [1, 2, 3], object()])
def test_add_area_raises_value_error_for_non_figure(not_a_figure):
    with pytest.raises(ValueError):
        Square(2).add_area(not_a_figure)
