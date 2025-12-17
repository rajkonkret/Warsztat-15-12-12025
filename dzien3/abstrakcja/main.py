from prototyp import Prototyp
from xyz import XYZ
from regular import Regular

# nie mozna stworzyc obiektu klasy abstrakcyjnej
# TypeError: Can't instantiate abstract class Prototyp without an implementation
# for abstract methods 'info', 'policz'
# pr = Prototyp(5)

xyz1 = XYZ(1, 2, 3)
print(xyz1.info("xyz 001"))
print(f"Policz: {xyz1.policz()}")
# xyz 001xyz 001xyz 001
# Policz: 5
xyz1.msg()  # Metoda nieabstrakcyjna klasy abstrakcyjnej

rg = Regular(3, 6)
print(rg.info("Tekst"))
print(f"Policz: {rg.policz()}")
rg.msg()
# Wiadomość: Tekst
# Policz: 2.0
# Metoda nieabstrakcyjna klasy abstrakcyjnej

lista = [rg, xyz1]  # obiekty różnych klas
# polimorfizm
# obiekty róznych klas możemy potraktować jak
# obiekty jednej wspólnej klasy
# zapewnia nam to klasa abstrakcyjna
for i in lista:
    print(i.policz())
# 2.0
# 5
