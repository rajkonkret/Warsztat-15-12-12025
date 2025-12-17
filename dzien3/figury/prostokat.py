from dzien3.figury.kwadrat import Kwadrat
from figura import Figura


class Prostokat(Figura):
    # decyduje jaki obiekt storzyc
    def __new__(cls, a, b):
        if a == b:
            return Kwadrat(bok=a)
        return object.__new__(Prostokat)

    def policz_pole(self):
        return self.a * self.b
