import pytest

from src.figure import Figure
from src.rectangle import Rectangle


@pytest.mark.parametrize(
    "width, height, area, perimeter",
    [
        (3, 4, 12, 14),
        (1, 1, 1, 4),
        (5, 5, 25, 20),
        (2.5, 4, 10, 13),
        (10, 1, 10, 22),
    ],
)
def test_area_and_perimeter(width, height, area, perimeter):
    rectangle = Rectangle(width, height)
    assert rectangle.area == pytest.approx(area)
    assert rectangle.perimeter == pytest.approx(perimeter)


def test_rectangle_is_a_figure():
    assert isinstance(Rectangle(2, 3), Figure)


@pytest.mark.parametrize("width, height", [(0, 5), (5, 0), (-1, 5), (5, -1), (0, 0)])
def test_non_positive_sides_raise(width, height):
    with pytest.raises(ValueError):
        Rectangle(width, height)


def test_add_area_sums_areas():
    assert Rectangle(2, 3).add_area(Rectangle(4, 5)) == pytest.approx(26)
