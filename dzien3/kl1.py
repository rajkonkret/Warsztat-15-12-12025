# klasy - element programowania obiektowego
# szablon, przepis
# zawiera cechy (zmienne) i metody (funkcje)
# obiekt (instancja) klasy - zbudowany wg przepisu
# klasa musi byc najpierw zadekalrowana
# tworzenie obiektu uruchamia metode inicjalizującą (__init__) - konstruktor
# hermetyzacja, dziedzicenie, polimorfizm, abstrakcja
import math


# PascalCase, UpperCamelCase
class MyFirstClass:
    """
    Klasa w pythonie
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca (konstruktor)
        :param x:
        :param y:
        """

        # self - obiekt przekazyna do klasy
        self.x = x
        self.y = y
        # self.move(x, y)

    def move(self, x: int, y: int) -> None:
        """
        Zmienia x i y obiektu na nowe wartości
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def calculate(self, other: "MyFirstClass") -> float:
        """
        For a two dimensional point (x, y), gives the hypotenuse
    using the Pythagorean theorem:  sqrt(x*x + y*y).
        :param other:
        :return:
        """

        return math.hypot(self.x - other.x, self.y - other.y)

    def reset(self):
        self.move(0, 0)

    def __str__(self):
        return f"{self.x, self.y}"


ob = MyFirstClass()
print(MyFirstClass.__doc__)  # Klasa w pythonie
#  pydoc -b - serwer dokumentacji
#  pydoc -w .\kl1.py - dokumentacja w html
print(ob.x)
print(ob.y)
print(ob)
# <__main__.MyFirstClass object at 0x000001E29A528830>
# po dodaniu __str__
# (0, 0)

point1 = MyFirstClass(5, 9)
print(point1)  # (5, 9)
point1.move(56, 98)
print(point1)  # (56, 98)

# reset()
point1.reset()
print(point1)  # (0, 0)

point2 = MyFirstClass()
point2.move(78, 45)
print(point2)  # (78, 45)
