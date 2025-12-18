# print(2 / 0)
# # Traceback (most recent call last):
# #   File "C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien4\wyjatki\wyjatki_zad1.py", line 1, in <module>
# #     print(2 / 0)
# #           ~~^~~
# # ZeroDivisionError: division by zero

# raise ZeroDivisionError("Bład dzielenia")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien4\wyjatki\wyjatki_zad1.py", line 8, in <module>
#     raise ZeroDivisionError("Bład dzielenia")
# ZeroDivisionError: Bład dzielenia

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę całkowitą większą od zera:"))
    if x <= 0:
        raise MyException("Liczba musi być większa od zera")
except MyException:
    print("Wartość musi być większa od zera")
except ValueError as e:
    print("Bład wartości", e)
except Exception as e:
    print("Błąd:", e)
else:  # gdy nie ma błedu
    print("Działąnie na x:", x * 2)
finally:  # wykona się zawsze
    print("Koniec")
# Podaj liczbę całkowitą większą od zera:10
# Działąnie na x: 20
# Koniec
