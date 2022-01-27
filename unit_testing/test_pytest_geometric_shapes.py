from unit_testing.geometric_shapes import Rectangle, Square


def test_square_perimeter():
    square = Square(5)
    assert square.get_perimeter() == 20


def test_square_area():
    square = Square(5)
    assert square.get_area() == 25


def test_number_enclosing():
    square = Square(6)
    assert square.get_number_enclosing(Square(3)) == 4


def test_rectangle_perimeter():
    rectangle = Rectangle(3, 5)
    assert rectangle.get_perimeter() == 16


def test_rectangle_area():
    rectangle = Rectangle(3, 5)
    assert rectangle.get_area() == 15


