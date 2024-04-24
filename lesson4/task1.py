import math


class Square:
    def __init__(self, square_side):
        self.side_length = square_side

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length


side = float(input("side: "))
square = Square(side)
print("S: ", square.area())
print("P: ", square.perimeter())
