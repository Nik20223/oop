from src.square import Square
from src.triangle import Triangle


def test_example_from_task():
    square = Square(10)
    triangle = Triangle(13, 14, 15)

    assert square.area == 100
    assert triangle.area == 84
    assert triangle.add_area(square) == 184
