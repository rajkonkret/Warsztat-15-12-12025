# dekorator - funkcja, przyjmuje inną funkcję jako argument
# dodaje, modyfikuje działąnie tej funkcji
# wykorzystuje mechanizm funkcji wewnętrznej


def dekor(func):
    def wew():
        print("Dekorator. dodatkowy napis")
        return func()

    return wew


@dekor  # użycie dekoratora
def nasza_funkcja():
    print("Funkcja, którą chcemy udekorować")


nasza_funkcja()
# Funkcja, którą chcemy udekorować
# po dodaniu dekoratora
# Dekorator. dodatkowy napis
# Funkcja, którą chcemy udekorować
