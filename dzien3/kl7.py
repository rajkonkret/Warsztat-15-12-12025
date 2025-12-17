# stworzenie ksiązki telefonicznej z wykorzystaniem petli while
# dodaj kontakt, usun kontakt, wyszukaj kontakt, wyswietl kontakt - klas

# -----
# Stworzyc system zarządzania biblioteką
# Book
# 3 dodanie ksiązek, wypozyczenie, zwrot ksiazki
# lista dostepnych
# lista wypożyczonych
# dodac kalsę Library i ew. usera
# title, author, isbn
# obsłużyć błędy

contacts = {}
while True:
    print(f"""
1. Dodaj kontakt
2. Usuń kontakt
3. Wyszukaj kontakt
4. Wyświetl listę kontaktów
5. Koniec""")

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
