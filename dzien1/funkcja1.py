#  funkcja - fragment kodu, który można wykonac w dowolnym momencie
# funkcja musi najpierw zostac zadeklarowana
# wywołanie funkcji uruchamia kod
from typing import Tuple


# deklaracja funkcji
def odejmij():
    print(10 - 4)


odejmij()  # 6


def odejmij(a, b, c):
    print(a - b - c)


odejmij(4, 5, 6)  # -7


# argumenty o wartosciach domyslnych
# symulowanie przeciązannia funkcji liczbą argumentów
def odejmij(a=0, b=0, c=0):
    print(a, b, c)


# przekazywanie argumentów po pozycji
odejmij()
odejmij(1, 2)
odejmij(1, 2, 3)  # 1 2 3

# po nazwie
odejmij(c=90)
odejmij(b=90, a=89, c=87)  # 89 90 87

# mieszane
odejmij(10, 2, c=9)
odejmij(10, c=90)


# 10 2 9
# 10 0 90

# SyntaxError: positional argument follows keyword argument
# odejmij(a=10, 4,5)

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(odejmij() + odejmij(56, 90))

# funkcje zwracające wynik
def mnozenie(a, b):
    return a * b  # zwraca wynik


print(mnozenie(5, 6))  # 30
zmienna = mnozenie(7, 56)
print("Zmienna:", zmienna)  # Zmienna: 392

print(mnozenie(5, 6) + mnozenie(7, 90))  # 660


# tylko podpowiedzi
def mnozenie2(a: int, b: int) -> Tuple[int, int, int]:
    return a, b, a * b  # zwraca krotke


print(mnozenie2(5, 6))
print(mnozenie2("a", 9))
# (5, 6, 30)
# ('a', 9, 'aaaaaaaaa')

a: int = "Radek"
print(a)  # Radek
print(type(a))  # <class 'str'>

wynik = mnozenie2(2, 8)
print(wynik)
print(f"{wynik[0]} * {wynik[1]} = {wynik[2]}")  # 2 * 8 = 16

a, b, wynik = mnozenie2(8, 9)
print(f"{a} * {b} = {a * b}")  # 8 * 9 = 72

# narzędzia skanowania kodu
# mypy
# pip install mypy
# pip list
#  cd .\dzien1\ - wejscie do własciwego katalogu
# (.venv) PS C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien1> mypy .\funkcja1.py
# funkcja1.py:8: note: "odejmij" defined here
# funkcja1.py:15: error: Name "odejmij" already defined on line 8  [no-redef]
# funkcja1.py:19: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:24: error: Name "odejmij" already defined on line 8  [no-redef]
# funkcja1.py:30: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:31: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:34: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcja1.py:35: error: Unexpected keyword argument "b" for "odejmij"  [call-arg]
# funkcja1.py:35: error: Unexpected keyword argument "a" for "odejmij"  [call-arg]
# funkcja1.py:35: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcja1.py:38: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:38: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcja1.py:39: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:39: error: Unexpected keyword argument "c" for "odejmij"  [call-arg]
# funkcja1.py:69: error: Argument 1 to "mnozenie2" has incompatible type "str"; expected "int"  [arg-type]
# funkcja1.py:73: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# funkcja1.py:81: error: Incompatible types in assignment (expression has type "int", variable has type "tuple[int, int, int]")  [assignment]
# Found 16 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien1>

# rzutowanie
print(int("2") + int("4"))  # 6
print("2" + str(2))  # 22
