from figura import Figura


class Kwadrat(Figura):
    def __init__(self, bok):
        super().__init__(bok, bok)
        self.bok = bok

    def policz_pole(self):
        return self.bok ** 2
