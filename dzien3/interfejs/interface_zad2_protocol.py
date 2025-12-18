from typing import Protocol


# realizacja idei interfejsu za pomocą Protocol
class Foo(Protocol):
    def bar(self) -> None: ...


class A:
    def bar(self) -> None:
        print("Metoda bar z klasy A")


class B:
    def bar(self) -> None:
        print("Metoda bar z klasy B")


def use(foo: Foo) -> None:
    foo.bar()


use(A())
use(B())
# Metoda bar z klasy A
# Metoda bar z klasy B
