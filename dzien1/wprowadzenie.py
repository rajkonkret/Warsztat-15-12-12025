import sys

print('')
print('')
print('')
print('')

print("Pierwsza linia")
print('Pierwsza linia')
# Pierwsza linia
# Pierwsza linia

# ctrl / - komentowanie kodu
# print('Pierwsza linia")
#   File "C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien1\wprowadzenie.py", line 12
#     print('Pierwsza linia")
#           ^
# SyntaxError: unterminated string literal (detected at line 12)
"""
komentarz 
wielolinijkowy
dokumentacja"""

info = """Tekst
wielolinijkowy
    zachowuje
        formutanie"""
print(info)
# "Tekst
# wielolinijkowy
#     zachowuje
#         formutanie"
print(info)
print(info)
print(info)
print(info)
# ctrl d - kopiowanie linii

# typowanie dynamiczne
info = 90
print(info)
print(type(info))  # <class 'int'>, liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

info = "Radek"
print(info)  # Radek
print("12" + "89")  # 1289, połaczy teksty, konkatenacja
print(12 * "40")  # 404040404040404040404040

name = "Radek"
age = 56

# float - liczby zmiennoprzecinkowe
liczba = 36.6
print(type(liczba))  # <class 'float'>
print(0.1 + 0.9)  # 1.0
print(0.1 + 0.3)
print(0.1 + 0.2)  # 0.30000000000000004, bład zaokrąglenia
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal() - pozwalaja obejśc błąd zaokrąglenia, do obliczen na pieniądzach

# boolean
# True, False
print(int(True))  # 1

print(bool(100))  # True
print(bool("Radek"))  # True

# kolekcje
# moze przechowuje dowolna ilośc i dowolne typy na raz

# lista - mutowalna, zachowuje kolejność przy dodawaniu
imiona = ["Jan", "Piotr", "Anna", "Nadia", "Michał"]
print(imiona)
# ['Jan', 'Piotr', 'Anna', 'Nadia', 'Michał']
#     0     1        2         3       4
#     -5     -4      -3        -2      -1
print(imiona[1])  # Piotr
print(imiona[-1])  # Michał, ostatni element

# slicowanie - fragment listy
print(imiona[2:4])  # ['Anna', 'Nadia'] indeksy 2 i 3
print(imiona[1:])  # ['Piotr', 'Anna', 'Nadia', 'Michał'], z ostatnim włacznie

print(imiona[10:25])  # []
print(imiona[-2:0])  # []
print(imiona[0:-2])  # ['Jan', 'Piotr', 'Anna']

imiona_p = imiona[::2]  # [stop:start:krok], ['Jan', 'Piotr', 'Anna'], co drugą

lista_p = []
lista_p2 = list()

lista_p.append("Karol")
print(lista_p)  # ['Karol']
lista_p.append("Radek")
lista_p.append("Tomek")
lista_p.append("Anna")
print(lista_p)  # ['Karol', 'Radek', 'Tomek', 'Anna']

lista_p.insert(1, 'Jan')
print(lista_p)  # ['Karol', 'Jan', 'Radek', 'Tomek', 'Anna']
lista_p.append("Jan")
print(lista_p)
# ['Karol', 'Jan', 'Radek', 'Tomek', 'Anna', 'Jan']
lista_p.remove("Jan")  # pierwszy napotkany
print(lista_p)  # ['Karol', 'Radek', 'Tomek', 'Anna', 'Jan']

# garbage collector

del imiona[3]
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Michał']

del lista_p2
# print(lista_p2) # NameError: name 'lista_p2' is not defined. Did you mean: 'lista_p'?

# enumerate() - numeruje kolekcje
imen = enumerate(imiona, 111)
print(imen)  # <enumerate object at 0x000001DB202FA340>
# for i in imen:
#     print(i)
# # (111, 'Jan')
# # (112, 'Piotr')
# # (113, 'Anna')
# # (114, 'Michał')

for i in imen:
    print(i[0], i[1])
# 111 Jan
# 112 Piotr
# 113 Anna
# 114 Michał

for index, wartosc in imen:
    # f - string format
    print(f"index -> {index}, wartosc -> {wartosc}")
# 111 Jan
# 112 Piotr
# 113 Anna
# 114 Michał

index, wartosc = (114, 'Michał')
print("index -> {}, wartosc -> {}".format(index, wartosc))  # index -> 114, wartosc -> Michał
print("index:", index, "wartośc:", wartosc)  # index: 114 wartośc: Michał
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
print("index:", index, "wartośc:", wartosc, sep="---")  # index:---114---wartośc:---Michał

print("a: %i b: %s" % (index, wartosc))  # a: 114 b: Michał

nowe_imie = imiona  # kopia referencji
lista_copy = imiona.copy()

print(nowe_imie)
print(imiona)
print(id(imiona))  # 1282569981888
print(id(nowe_imie))
print(id(lista_copy))  # 2232957418944

nowe_imie.append("Radek")
print(nowe_imie)
print(imiona)
print(lista_copy)
# ['Jan', 'Piotr', 'Anna', 'Michał', 'Radek']
# ['Jan', 'Piotr', 'Anna', 'Michał', 'Radek']
# ['Jan', 'Piotr', 'Anna', 'Michał']

pimie = imiona[:]  # nowa lista
qimie = list(imiona)
print(id(pimie))  # 1942732038848
print(id(qimie))  # 1942769581248
print(id(lista_copy))  # 1942769581376

# krotka - tupla
# kolekcja niemutowalna
# pozwala lepiej zarządzac pamięcią
# miasto = 'Kraków', "Lublin", "Płock", "Łódź"
miasto = ('Kraków', "Lublin", "Płock", "Łódź")
print(type(miasto))  # <class 'tuple'>
print(miasto)  # ('Kraków', 'Lublin', 'Płock', 'Łódź')

krotka_jen = ("Radek",)
print(type(krotka_jen))  # <class 'tuple'>

print(miasto.index("Łódź"))  # index 3
print(miasto.count("Łódź"))  # wystepuje 1 raz

# del miasto[0] # TypeError: 'tuple' object doesn't support item deletion
del miasto
# print(miasto)  # NameError: name 'miasto' is not defined

# zbiór , set
# nie przechowuje duplikatów
# nie posiadają indeksu
# nie zachowuja kolejności

drzewa = {'jodła', "buk", "Świerk", "dąb", "klon"}
print(drzewa)  # {'dąb', 'Świerk', 'klon', 'jodła', 'buk'}

drzewa.add("osika")
drzewa.add("osika")
drzewa.add("osika")
print(drzewa)  # {'dąb', 'buk', 'osika', 'Świerk', 'jodła', 'klon'}
print(type(drzewa))  # <class 'set'>
pusty_zbior = set()
print(pusty_zbior)  # set()

lista = [1, 2, 3, 4, 4, 7, 7, 6, 5, 1, 2, 3]
zbior = set(lista)
print(zbior)  # {1, 2, 3, 4, 5, 6, 7}

# słownik - para typu: klucz:wartosc
# odpowiednik jsona -> {"name":"John", "age":30, "car":null}
pusty_slownik = {}
print(type(pusty_slownik))  # <class 'dict'>
print(pusty_slownik)  # {}

pusty_slownik = dict()
print(type(pusty_slownik))  # <class 'dict'>
print(pusty_slownik)  # {}
osoba = {
    "id": 89,
    "imie": "Tadeusz",
    "rok": 1976,
    "miasto": "Łódź",
}
print(osoba)
# {'id': 89, 'imie': 'Tadeusz', 'rok': 1976, 'miasto': 'Łódź'}
print(type(osoba))  # <class 'dict'>

print(osoba['miasto'])
# print(osoba['Miasto']) # KeyError: 'Miasto'

print(osoba.get("miasto"))  # Łódź
print(osoba.get("Miasto"))  # None -> odpowiednik null
print(osoba.get("Miasto", "default"))  # default

osoba['imie'] = "Radek"
print(osoba)
# {'id': 89, 'imie': 'Radek', 'rok': 1976, 'miasto': 'Łódź'}

print(osoba.keys())  # dict_keys(['id', 'imie', 'rok', 'miasto'])
print(osoba.values())  # dict_values([89, 'Radek', 1976, 'Łódź'])
print(osoba.items())
# dict_items([('id', 89), ('imie', 'Radek'), ('rok', 1976), ('miasto', 'Łódź')])

lista = [1, 2, 3, 4, 4, 7, 7, 6, 5, 1, 2, 3]
print(dict.fromkeys(lista))
#  {1: None, 2: None, 3: None, 4: None, 7: None, 6: None, 5: None}
print(list(dict.fromkeys(lista)))
# [1, 2, 3, 4, 7, 6, 5] nie tracimy kolejności
