# prostokąt, trapez, koło, kwadrat, trójkąt
from prostokat import Prostokat
from kwadrat import Kwadrat

kw = Kwadrat(5)
print(f"Pole figury {kw.__class__.__name__}: {kw.policz_pole()} ")

print(50 * "-")
pr1 = Prostokat(5, 10)
print(f"Pole figury {pr1.__class__.__name__}: {pr1.policz_pole()} ")
print(type(pr1))
# --------------------------------------------------
# Pole figury Prostokat: 50
# <class 'prostokat.Prostokat'>

print(50 * "-")
pr2 = Prostokat(5, 5)
print(f"Pole figury {pr2.__class__.__name__}: {pr2.policz_pole()} ")
print(type(pr2))
# --------------------------------------------------
# Pole figury Kwadrat: 25
# <class 'dzien3.figury.kwadrat.Kwadrat'>
