class Contact:
    all_contact = []  # lista wspólna dla wszystkich obiektów klasy
    x = "Test"

    def __init__(self, name, email):
        """

        :param name:
        :param email:
        """
        self.name = name
        self.email = email
        # dodajemy wszystkie obiekty do listy
        Contact.all_contact.append(self)

    # repr, dwa obiekty,
    def __repr__(self):  # __repr__ dopisuje __str__ jesli nie ma
        return f"{self.name} {self.email}"


# dziedziczenie
class Suplier(Contact):
    """
    Klasa dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


c1 = Contact("Radek", "radek@wp.pl")
c2 = Contact("Anna", "anna@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contact)  # [Radekradek@wp.pl, Annaanna@wp.pl, Tomektomek@wp.pl]
# bez obiektu
print(Contact.all_contact)  # [Radekradek@wp.pl, Annaanna@wp.pl, Tomektomek@wp.pl]
print(c1.x)
print(Contact.x)
c2.x = "test2"
print(Contact.x)
print(c2.x)
# Test
# Test
# Test
# test2
print(c1.x)  # Test
sup1 = Suplier("Kasia", "kasia@wp.pl")
print(sup1)  # Kasia kasia@wp.pl
print(sup1.all_contact)
print(Suplier.all_contact)
# [Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl, Kasia kasia@wp.pl]
# [Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl, Kasia kasia@wp.pl]
# c1.order()  # AttributeError: 'Contact' object has no attribute 'order'
sup1.order("kawa")  # kawa zamówiono od Kasia

print(c1)
print(c2)
print(c3)
print(sup1)
# Radek radek@wp.pl
# Anna anna@wp.pl
# Tomek tomek@wp.pl
# Kasia kasia@wp.pl
