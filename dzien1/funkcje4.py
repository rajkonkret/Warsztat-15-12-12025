# lambda - skrócony zapis funkcji
# lambda zwraca wynik
# funkcja anonimowa - nie ma nazwy, możliwosc uzycia w miejscu deklaracji


def liczmy(x, y):
    return x + y


print(liczmy(6, 9))  # 15

liczymy2 = lambda x, y: x + y
print(liczymy2(9, 87))  # 96

# mapowanie danych
lista = [1, 2, 5, 56, 78, 98, 100, 1115, 200, 500]

# zrobić listę z tymi wartościami do potęgi 2

lista_wyn = []
for i in lista:
    lista_wyn.append(i ** 2)
print(lista_wyn)
# [1, 4, 25, 3136, 6084, 9604, 10000, 1243225, 40000, 250000]

# list comprehensions
print([i ** 2 for i in lista])


# [1, 4, 25, 3136, 6084, 9604, 10000, 1243225, 40000, 250000]

def zmien(x):
    return x ** 2


lista_wyn2 = []
for i in lista:
    lista_wyn2.append(zmien(i))

print(lista_wyn2)  # [1, 4, 25, 3136, 6084, 9604, 10000, 1243225, 40000, 250000]

# map() - na kolekcji wykonuje funkcję
# funkcja wyższego rzędu
print(f"Zastosowanie map(): {list(map(zmien, lista))}")

# lambda jako funkcja anonimowa
print(f"Zastosowanie map(): {list(map(lambda z: z ** 2, lista))}")
# Zastosowanie map(): [1, 4, 25, 3136, 6084, 9604, 10000, 1243225, 40000, 250000]
print(f"Zastosowanie map(): {list(map(lambda z: z ** 3, lista))}")
print(f"Zastosowanie map(): {list(map(lambda z: z ** 4, lista))}")
# Zastosowanie map(): [1, 16, 625, 9834496, 37015056, 92236816, 100000000, 1545608400625, 1600000000, 62500000000]
print(f"Zastosowanie map(): {list(map(lambda z: z * 2, lista))}")

# filtrowanie danych
for i in lista:
    if i < 10:
        print(i, end=" : ")  # 1 : 2 : 5 :

print()

# filter() - filtrowanie danych

print(f"Użycie filter(): {list(filter(lambda x: x < 10, lista))}")
print(f"Użycie filter(): {list(filter(lambda x: x > 10, lista))}")
print(f"Użycie filter(): {list(filter(lambda x: x < 100, lista))}")
print(f"Użycie filter(): {list(filter(lambda x: x > 100, lista))}")
print(f"Użycie filter(): {list(filter(lambda x: x > 10 and x < 250, lista))}")
# Użycie filter(): [56, 78, 98, 100, 200]
print(f"Użycie filter(): {list(filter(lambda x: 10 < x < 250, lista))}")
# Użycie filter(): [56, 78, 98, 100, 200]

r0 = {'miasto': "Kielce"}
r1 = {"miasto": "Kielce", "ZIP": "25-900"}

print(r0['miasto'])
print(r1['miasto'])
# Kielce
# Kielce

print(r1['ZIP'])
# print(r0['ZIP'])  # KeyError: 'ZIP'

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
# 00-000
# 25-900

print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(min(lata))  # (2000, 29.7)

print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)

# (33.12, (2001, 33.12))
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))

print(max(map(lambda c: c[1], lata)))  # 33.12
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)

a = 10


def funkcja():
    a = 15  # zmienna o zasięgu lokalnym
    print(a)


funkcja()
print(a)  # 10


def funkcja_glob():
    global a  # zmienna globalna

    a = 15  # zmienia wartość dla zmiennej globalnej
    print(a)


funkcja_glob()
print(a)  # 15
