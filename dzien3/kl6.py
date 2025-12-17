class A:
    """
    Klasa A
    """

    def method(self):
        print("Metoda z kalsy A")


a = A()
a.method()  # Metoda z kalsy A


class B:
    """
    Klasa B
    """

    def method(self):
        print("Metoda z kalsy B")


b = B()
b.method()  # Metoda z kalsy B


# dziedziczenie po wielu klasach
class C(B, A):
    """
    Klasa dziedziczy po klasie B i A
    """


c = C()
c.method()  # Metoda z kalsy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    """
    Klasa dziedziczy po A i B
    """


d = D()
d.method()  # Metoda z kalsy A
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


class E(A, B):
    def method(self):
        print("Metoda z kalsy E")


e = E()
e.method()  # Metoda z kalsy E
print(E.__mro__)


# (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

class F(A, B):
    """
    Chcemy użyć metodu z klasy B
    """

    def method(self):
        B.method(self)  # jawnie wskazujemy z jakiej klasy użyc metody, przekazujemy obiekt


f = F()
f.method()  # Metoda z kalsy B
print(F.__mro__)


# (<class '__main__.F'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

class G(A, B):
    def method(self):
        super().method()  # super() - klasy nadrzędna, tutaj klasa: A
        print("Dopisane")
        B.method(self)


g = G()
g.method()
# Metoda z kalsy A
# Dopisane
# Metoda z kalsy B

print(G.__mro__)


# (<class '__main__.G'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# problem dziedziczenia po wielu klasach
# kolejnośc dziedziczenia ma znaczenie
# class H(A, F):
#     def method(self):
#         super().method()
#         print("Dopisane")
#         B.method(self)
#
#
# print(H.__mro__)
# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, F

class H(F, A):
    def method(self):
        super().method()
        print("Dopisane")
        B.method(self)

print(H.__mro__)
# (<class '__main__.H'>, <class '__main__.F'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
