"""przeciążenie operatorów - czyli nadanie operatorowi nowych funkcji
operacje arytmetyczne:
__add__(self, other) - dodawanie
__sub__(self, other) - odejmowanie
__mul__(self, other) - mnożenie
__truediv__(self, other) - dzielenie
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'x, y: {self.x}, {self.y}'

    def __add__(self, other): # własna implementacja operatora + (dodawania)
        a = self.x + other.x
        b = self.y + other.y
        return Point(a, b)

    def __sub__(self, other): # własna implementacja operatora - (odejmowania)
        a = self.x - other.x
        b = self.y - other.y
        return Point(a, b)

    def __mul__(self, other): # własna implementacja operatora * (mnożenia)
        a = self.x * other.x
        b = self.y * other.y
        return Point(a, b)

    def __truediv__(self, other): # własna implementacja operatora / (dzielenia)
        a = self.x / other.x
        b = self.y / other.y
        return Point(a, b)

def main():
    """print(5 + 5)
    print(int.__add__(5, 5)) # operacja dodawania wywołuje niejawnie specjalną funkcję __add__"""

    point_1 = Point(5, 5)
    point_2 = Point(5, 5)
    print('---------------------')
    point_3 = point_1 + point_2
    print(f'__add__\t{point_3}')
    print('---------------------')
    point_4 = point_1 - point_2
    print(f'__sub__\t{point_4}')
    print('---------------------')
    point_5 = point_1 * point_2
    print(f'__mul__\t{point_5}')
    print('---------------------')
    point_6 = point_1 / point_2
    print(f'__truediv__\t{point_6}')


main()