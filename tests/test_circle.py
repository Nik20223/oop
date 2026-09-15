from math import pi

import pytest

from src.circle import Circle
from src.figure import Figure


@pytest.mark.parametrize("radius", [1, 2, 0.5, 10])
def test_area_and_perimeter(radius):
    circle = Circle(radius)
    assert circle.area == pytest.approx(pi * radius**2)
    assert circle.perimeter == pytest.approx(2 * pi * radius)


def test_circle_is_a_figure():
    assert isinstance(Circle(1), Figure)


@pytest.mark.parametrize("radius", [0, -1, -2.5])
def test_non_positive_radius_raises(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_add_area_sums_areas():
    assert Circle(1).add_area(Circle(1)) == pytest.approx(2 * pi)
