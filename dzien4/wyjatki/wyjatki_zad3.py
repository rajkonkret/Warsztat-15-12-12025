class MyExceptions(Exception):

    def __init__(self, message):
        super().__init__(message)

    @staticmethod
    def sprawdz_wprowadzona_wartosc(wartosc):
        if wartosc < 0:
            raise MyExceptions("Liczba musi być większa od zera")
        if wartosc > 10_000:
            raise MyExceptions("Liczba za duża")


try:
    x = int(input("Podaj liczbę większą od zera"))
    MyExceptions.sprawdz_wprowadzona_wartosc(x)
except MyExceptions as e:
    print("Bład:", e)
else:
    print("Podana wartość:", x)
finally:
    print("koniec")
# Podaj liczbę większą od zera-10
# Bład: Liczba musi być większa od zera
# koniec
