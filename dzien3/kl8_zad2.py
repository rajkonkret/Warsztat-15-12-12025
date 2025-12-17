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
            name = input("Podaj imię kontaktu:")
            number = input("Podaj numer telefonu kontaktu(tylko cyfry):")
            if not number.isdigit():
                raise ValueError("Numer telefonu powinien zawierac cyfry")
            else:
                contacts[name.lower()] = number
                print("Kontakt został dodany")
        elif odp == "2":
            name = input("Podaj imię kontaktu do usunięcia")
            if name.lower() in contacts:
                # del contacts[name.lower()]
                contacts.pop(name.lower())
                print(f"Kontakt {name} został usunięty")
        elif odp == "3":
            name = input("Podaj imię kontaktu do wyszukania")
            if name.lower() in contacts:
                print(f"Kontakt {name.capitalize()} nr telefonu: {contacts[name.lower()]}")
        elif odp == "4":
            print(f"Lista kontaktów: {contacts}")
        elif odp == "5":
            break
        else:
            print("Błędny wybór")
    except Exception as e:
        print("Błąd:", e)
