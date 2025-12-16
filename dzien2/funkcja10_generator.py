# generator - generuje wartości w momwncie kiedy są potrzebne
# lazy
# pozwalają osczędzic pamięć
import time


def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(100)


# 3 generator
def kwadrat2(n):
    for x in range(n):  # za kazdym dla kolejnych x
        yield x ** 2  # zwraca wartość obliczenia, pamięta kóre wykonał


kwa = kwadrat2(10)
print(type(kwa))  # <class 'generator'>
print(kwa)  # <generator object kwadrat2 at 0x000001F9DCD28FB0>

print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))

print("Zrób cokolwiek")
print("Kolejne zdania")
print(next(kwa))
# Zrób cokolwiek
# Kolejne zdania
# 81

# generator konczy działanie (brak danych)
# print(next(kwa))  # StopIteration

kwa2 = kwadrat2(10)
for k in kwa2:
    print(k)
    print("Przetwarzamy dane...")
    time.sleep(2)

# generator niezalezne od siebie
kwa3 = kwadrat2(10)
kwa4 = kwadrat2(10)

print(next(kwa3))  # 0
print(next(kwa3))  # 1
print(next(kwa3))  # 4

print(next(kwa4))  # 0
print(next(kwa4))  # 1

print(next(kwa3))  # 9
