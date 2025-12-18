# gemini, chatgpt, grok, claude
# codex
#  copilot, tabnine

# napisz funkcję obliczającą średnią ocen
def oblicz_srednia_ocen(oceny):
    if not oceny:
        return 0
    return sum(oceny) / len(oceny)
# napisz funkcję sprawdzającą czy student zdał egzamin
def czy_student_zdal(ocena):
    return ocena >= 50
# napisz funkcję konwertującą stopnie Celsjusza na Fahrenheita
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# napisz funkcję sprawdzającą czy liczba jest parzysta
def czy_liczba_parzysta(liczba):
    return liczba % 2 == 0

# dopisz klasę Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Author: {self.author!r}, Tytuł: {self.title!r}, ISBN: {self.isbn!r}"

# użyj tej klasy do stworzenia obiektu książki
moja_ksiazka = Book("Python Programming", "John Doe", "1234567890")
print(moja_ksiazka)

# stwórz kalsę Library z metodami dodawania i wypożyczania książek
class Library:
    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dodaj_ksiazki(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    def fun_wypozycz_ksiazke(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.append(book)
                self.dostepne_ksiazki.remove(book)
                return book
        raise Exception("nie ma takiej ksiązki")

# napisz kalsę Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f"{self.year} {self.make} {self.model}"

# użyj tej klasy do stworzenia obiektu samochodu
moj_samochod = Car("Toyota", "Corolla", 2020)
print(moj_samochod)
# stwórz klasę Garage z metodami dodawania i usuwania samochodów
class Garage:
    def __init__(self):
        self.samochody = []

    def dodaj_samochod(self, car: "Car"):
        self.samochody.append(car)

    def usun_samochod(self, make, model):
        for car in self.samochody:
            if car.make == make and car.model == model:
                self.samochody.remove(car)
                return car
        raise Exception("Nie ma takiego samochodu w garażu")
# napisz klasę SqliteCM jako context manager do obsługi bazy danych SQLite
import sqlite3
class SqliteCM:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()

# uzyj bazy danych sqlitealcjemy dla kals book i library
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
engine = create_engine('sqlite:///library.db', echo=True)
Base = declarative_base()
class BookDB(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    isbn = Column(String, unique=True)

    def __repr__(self):
        return f"Author: {self.author!r}, Tytuł: {self.title!r}, ISBN: {self.isbn!r}"
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
# dodaj książkę do bazy danych
nowa_ksiazka = BookDB(title="Python Programming", author="John Doe", isbn="1234567890")
session.add(nowa_ksiazka)
session.commit()
# pobierz wszystkie książki z bazy danych
ksiazki = session.query(BookDB).all()
print(ksiazki)
# wypisz tytuły książek
for k in ksiazki:
    print(k.title)
