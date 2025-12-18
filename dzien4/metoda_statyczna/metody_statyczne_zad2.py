# starsze podejście
class Klakulator:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def oblicz(x, y, z):
        return (x + y) * z


Klakulator.oblicz = staticmethod(Klakulator.oblicz)
