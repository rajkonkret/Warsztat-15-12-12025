from prototyp import Prototyp
from xyz import XYZ

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
