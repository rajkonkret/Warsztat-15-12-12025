# -----
# Stworzyc system zarządzania biblioteką
# Book
# 3 dodanie ksiązek, wypozyczenie, zwrot ksiazki
# lista dostepnych
# lista wypożyczonych
# dodac kalsę Library i ew. usera
# title, author, isbn
# obsłużyć błędy

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Author: {self.author!r}, Tytuł: {self.title!r}, ISBN: {self.isbn!r}"


class Library:
    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dostepne_ksiazki(self):
        return self.dostepne_ksiazki

    def fun_wypozyczone_ksiazki(self):
        return self.wypozyczone_ksiazki

    def fun_dodaj_ksiazki(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    def fun_zwroc_ksiazke(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.remove(book)
                self.dostepne_ksiazki.append(book)
                return book
        raise Exception("Ksiązka nie znaszej biblioteki")

    def fun_wypozycz_ksiazke(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.append(book)
                self.dostepne_ksiazki.remove(book)
                return book
        raise Exception("nie ma takiej ksiązki")


library = Library()

while True:
    print(f"""
1. Dodaj ksiązkę
2. Wypożycz ksiązkę
3. Pokaż dostępne
4. Pokaż wypożyczone
5. Zwróc ksiązkę
6. Koniec""")

    try:
        odp = input("Wybierz opcję")  # str

        if odp == "1":
            author = input("Podaj autora:")
            title = input("Podaj tytuł:")
            isbn = input("Podaj isbn:")
            library.fun_dodaj_ksiazki(Book(title, author, isbn))
        elif odp == "2":
            isbn = input("Podaj isbn:")
            book = library.fun_wypozycz_ksiazke(isbn)
            print(f"Ksiązka została wypożyczona: {book}")
        elif odp == "3":
            print(f"Dostępne ksiązki: {library.fun_dostepne_ksiazki()}")
        elif odp == "4":
            print(f"Wypożyczone ksiązki: {library.fun_wypozyczone_ksiazki()}")
        elif odp == "5":
            isbn = input("Podaj isbn ksiązki, którą chcesz zwrócic:")
            book = library.fun_zwroc_ksiazke(isbn)
            if book:
                print(f"Ksiązka została zwrócona: {book}")
        elif odp == "6":
            break
        else:
            print("Błędny wybór")
    except Exception as e:
        print("Błąd:", e)
