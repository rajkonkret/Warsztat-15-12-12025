import time
from itertools import zip_longest


def wznowienie(n, k):
    print("Wstrzymanie działania...")
    yield 1001
    print("'Wznowienie działania")
    yield n + k
    print("Działanie - dodawanie - wstrzymanie")
    print("Wznowienie działania")
    n = 3 * n
    yield n - k
    print("Wznowienie działania - mnożenie")
    yield n * k
    print("Wznowienie działania - dzielenie")
    yield n / k


print(20 * "-")

print(wznowienie(6, 7))  # <generator object wznowienie at 0x00000158CA358FB0>

print(list(wznowienie(6, 7)))
# Wstrzymanie działania...
# 'Wznowienie działania
# Działanie - dodawanie - wstrzymanie
# Wznowienie działania
# Wznowienie działania - mnożenie
# Wznowienie działania - dzielenie
# [1001, 13, 11, 126, 2.5714285714285716]

print(20 * "-")
for i in wznowienie(6, 8):
    if i == 1001:
        continue  # przerwij bieżące iterację, weź kolejny element
    time.sleep(1)
    print(f"Yield zwraca wartość: {i}")
# --------------------
# Wstrzymanie działania...
# 'Wznowienie działania
# Yield zwraca wartość: 14
# Działanie - dodawanie - wstrzymanie
# Wznowienie działania
# Yield zwraca wartość: 10
# Wznowienie działania - mnożenie
# Yield zwraca wartość: 144
# Wznowienie działania - dzielenie
# Yield zwraca wartość: 2.25

print(20 * "-")


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


# --------------------
# 1
# 4
# 9
# 16
# 25

def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)  # OK
        if command == "stop":
            break  # zatrzymanie generatora

        i += 1


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))

g5.send("OK")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2\fun11_gen2.py", line 94, in <module>
#     g5.send("stop")
#     ~~~~~~~^^^^^^^^
# StopIteration
try:
    g5.send("stop")
except StopIteration:
    print("Koniec danych")
except Exception as e:
    print("Bład:", e)


# stop
# Koniec danych


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib = fibo_with_index(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
# (0, 0)
# (1, 1)
# (2, 1)
# (3, 2)

for i, n in fibo_with_index(10):
    print(f"Pozycja: {i}, element: {n}")
# Pozycja: 0, element: 0
# Pozycja: 1, element: 1
# Pozycja: 2, element: 1
# Pozycja: 3, element: 2
# Pozycja: 4, element: 3

person = ['Radek', "Tomek", "Zenek", 'Ania', "Kasia"]
wiek = [34, 56, 57, 89]

for p, w in zip(person, wiek):
    print(p, w)
# Radek 34
# Tomek 56
# Zenek 57
# Ania 89

print(20 * "-")
zipped = zip_longest(person, wiek, fillvalue="Brak danych")
print(zipped)  # <itertools.zip_longest object at 0x0000029483DC36A0>

lista_zipped = list(zipped)  # wyczerpalismy dane z iteratora

for imie, wiek in zipped:
    print(imie, wiek)
# --------------------
# <itertools.zip_longest object at 0x000001A3120936A0>
# Radek 34
# Tomek 56
# Zenek 57
# Ania 89
# Kasia Brak danych
print(20 * "-")
for imie, wiek in zipped:
    print(imie, wiek)
# -------------------- dane wyczerpane
for imie, wiek in lista_zipped:
    print(imie, wiek)
    # dane z listy
# Radek 34
# Tomek 56
# Zenek 57
# Ania 89
# Kasia Brak danych
