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


