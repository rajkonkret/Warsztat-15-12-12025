def count_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


c_d = count_down(3)
c_u = count_up_to(3)

for n in c_u:
    print(n)

for n in c_d:
    print(n)


def combined(gen1, gen2):
    yield from gen1
    yield from gen2


c_d = count_down(3)
c_u = count_up_to(3)

c = combined(c_u, c_d)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

for i in c:
    print(i)

dane = [x for x in range(5)]
print(dane)  # [0, 1, 2, 3, 4]
print(type(dane))  # <class 'list'>

# generator skłądane
dane2 = (x for x in [1, 2, 3, 4, 5])
print(type(dane2))  # <class 'generator'>
print(dane2)  # <generator object <genexpr> at 0x0000026FAF452A80>

print(next(dane2))  # 1
print(next(dane2))  # 2
print(next(dane2))  # 3
print(next(dane2))  # 4
print(next(dane2))  # 5


# print(next(dane2))  # StopIteration

def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))  # 1
print(next(g3))  # 2
print(next(g3))  # 3
print(next(g3))  # 4
print(next(g3))  # 5
