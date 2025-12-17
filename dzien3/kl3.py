from pprint import pprint


class ContactList(list['Contact']):

    def search(self, name):
        matching_contact = []
        for c in self:  # pod self będzie lista
            if name.casefold().strip() in c.name.casefold().strip():
                matching_contact.append(c)
        return matching_contact


class Contact:
    # all_contact = []  # lista wspólna dla wszystkich obiektów klasy
    all_contacts = ContactList()  # lista wspólna dla wszystkich obiektów klasy
    x = "Test"

    def __init__(self, name, email):
        """

        :param name:
        :param email:
        """
        self.name = name
        self.email = email
        # dodajemy wszystkie obiekty do listy
        Contact.all_contacts.append(self)

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


class Friend(Suplier):
    """
    Klasa dziedziczy po klasie Suplier
    """

    def __init__(self, name, email, phone="000000000"):
        super().__init__(name, email)  # super() - musimy wywołac metode __init__ z klasy nadrzędnej
        self.phone = phone

    def __repr__(self):
        return f"{self.name} {self.email} +48{self.phone}"


c1 = Contact("Radek", "radek@wp.pl")
c2 = Contact("Anna", "anna@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)  # [Radekradek@wp.pl, Annaanna@wp.pl, Tomektomek@wp.pl]
# bez obiektu
print(Contact.all_contacts)  # [Radekradek@wp.pl, Annaanna@wp.pl, Tomektomek@wp.pl]
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
print(sup1.all_contacts)
print(Suplier.all_contacts)
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

# print(Contact.all_contact.search("Radek"))  # AttributeError: 'list' object has no attribute 'search'


contact_list = ContactList()
print(contact_list)  # []
print(contact_list.search("Radek"))

print(Contact.all_contacts.search("Radek"))  # [Radek radek@wp.pl]
osoba = Contact.all_contacts.search("Radek")

print(osoba)
print(osoba[0].name)  # Radek
print(osoba[0].email)  # radek@wp.pl

f1 = Friend("Marek", "marek@wp.pl")
f2 = Friend("Kamil", "kamil@wp.pl")
print(f1, f2)
# Marek marek@wp.pl +48000000000 Kamil kamil@wp.pl +48000000000

print(Contact.all_contacts)
# [Radek radek@wp.pl, Anna anna@wp.pl, Tomek tomek@wp.pl, Kasia kasia@wp.pl, Marek marek@wp.pl +48000000000, Kamil kamil@wp.pl +48000000000]

print(Contact.all_contacts.search("Kamil"))  # [Kamil kamil@wp.pl +48000000000]

f3 = Friend("Aneta", "aneta@onet.pl", "980987654")
print(f3)  # Aneta aneta@onet.pl +48980987654

print(Contact.all_contacts)
# [Radek radek@wp.pl, Anna anna@wp.pl,
# Tomek tomek@wp.pl, Kasia kasia@wp.pl,
# Marek marek@wp.pl +48000000000,
# Kamil kamil@wp.pl +48000000000,
# Aneta aneta@onet.pl +48980987654]

pprint(Contact.all_contacts)
# [Radek radek@wp.pl,
#  Anna anna@wp.pl,
#  Tomek tomek@wp.pl,
#  Kasia kasia@wp.pl,
#  Marek marek@wp.pl +48000000000,
#  Kamil kamil@wp.pl +48000000000,
#  Aneta aneta@onet.pl +48980987654]
