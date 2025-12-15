# funkcje wyższego rzędu

def witaj(imie):
    return f"Miło Cię widzieć {imie}"


def konkurs(imie, miejsce, punkty):
    return f"Uczestnik konkursu: {imie}, miejsce: {miejsce}, liczba punktów: {punkty}"


def bonus(punkty):
    if punkty > 50:
        bn = punkty + 10
    else:
        bn = punkty
    return f"Liczba punktów z bonusem: {bn}"


def osoba(funkcja, *args):
    # funkcja wyższego rzędu
    # *args - dowolną ilośc argumentów pozycyjnych
    return funkcja(*args)


def multiosoba(*args):
    print(bonus(args[2]))
    konkurs(*args)
    return "Opublikowano wyniki konkursu"


print(osoba(witaj, "Leon"))  # Miło Cię widzieć Leon
print(osoba(konkurs, "Leon", "Kraków", 70))
# Uczestnik konkursu: Leon, miejsce: Kraków, liczba punktów: 70

print(multiosoba("Anna", "Toruń", 88))


# Liczba punktów z bonusem: 98
# Opublikowano wyniki konkursu

def fun_args(*args):  # argumenty pozycyjne
    print(args)


fun_args()  # ()
fun_args(1, 2, 3)  # (1, 2, 3)
fun_args(1, 2, 3, 4, 5, 6, 7, 8)  # (1, 2, 3, 4, 5, 6, 7, 8)


def fun_kwargs(**kwargs):  # dowolna ilośc argumentów nazwanych
    print(kwargs)


fun_kwargs(a=10)
fun_kwargs(a=10, b=10)
fun_kwargs(a=10, b=10, name="Radek")


# {'a': 10}
# {'a': 10, 'b': 10}
# {'a': 10, 'b': 10, 'name': 'Radek'}

def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()
all_args(1, 2, 3)
all_args(a=10)
all_args(1, 2, a=10)
# () {}
# (1, 2, 3) {}
# () {'a': 10}
# (1, 2) {'a': 10}

#                        ^
# SyntaxError: positional argument follows keyword argument
# all_args(a=10, 1, 2)
