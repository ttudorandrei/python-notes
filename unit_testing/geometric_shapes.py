class Square:
    def __init__(self, side_length):
        self.name = "Square"
        self.side_length = side_length

    def __repr__(self):
        return repr(f"Shape(type={self.name})")

    def __str__(self):
        return repr(f"This is a {self.name} shape. The side size is {self.side_length}")

    def get_perimeter(self):
        return self.side_length * 4

    def get_area(self):
        return self.side_length ** 2

    def get_number_enclosing(self, another_square):
        return self.get_area() / another_square.get_area()


class Rectangle(Square):
    def __init__(self, side_length, side_width):
        super().__init__(side_length)
        self.name = "Rectangle"
        self.side_length = side_length
        self.side_width = side_width

    def __repr__(self):
        return repr(f"Shape(type={self.name})")

    def __str__(self):
        return repr(f"This is a {self.name} shape. The length is {self.side_length}"
                    f" and the width is {self.side_width}")

    def get_perimeter(self):
        return 2 * (self.side_length + self.side_width)

    def get_area(self):
        return self.side_length * self.side_width


print(Square(5).__repr__())
print(Rectangle(5, 3).__repr__())
print(Square(5).__str__())
print(Rectangle(5, 3).__str__())
