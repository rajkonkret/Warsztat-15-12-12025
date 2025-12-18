# metody statyczne - nie potrzebują obiektu klasy

class Matematyka:

    # def dodaj(self, a, b):
    #     return a + b

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


# kalk = Matematyka()
# print(kalk.dodaj(5, 6))

print(Matematyka.dodaj(5, 90))  # 95
print(Matematyka.dodaj(67, 90))  # 157
print(Matematyka.dodaj(45, 45))  # 90
print(Matematyka.dodaj(52, 190))  # 242

print(Matematyka.odejmij(56, 7))  # 49
