from functools import total_ordering


class Number:
    def __init__(self, value):
        self.values = value


num1 = Number(5)
num2 = Number(10)

# print(num1 < num2)
# TypeError: '<' not supported between instances of 'Number' and 'Number'
print(num1.values < num2.values)  # True


#  # prefer __lt__ to __le__ to __gt__ to __ge__
# __eq__, __lt_
@total_ordering
class Number2:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


num3 = Number2(5)
num4 = Number2(10)

print(num3 < num4)  # True
num5 = Number2(10)
print(num5 == num4)

print(num5 > num3)  # True

print(5 + 5)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point1 = Point(1, 4)
point2 = Point(7, 8)

# print(point1 + point2) # TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
wynik = point2 + point1
print("Wynik:", wynik)  # Wynik: Point(8, 12)
