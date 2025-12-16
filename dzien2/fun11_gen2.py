import time


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
