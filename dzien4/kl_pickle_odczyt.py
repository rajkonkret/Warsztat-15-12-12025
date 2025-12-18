import pickle
from kl_dataclass import Person

# rb - odczyt bajtowy
with open('dane.pckl', "rb") as file:
    p = pickle.load(file)

print(50 * "-")
print(p)
# [Person(first_name='Jan', last_name='Kowalski', id=1),
# Person(first_name='Maciek', last_name='Arbuz', id=2)]
print(type(p))  # <class 'list'>

for person in p:
    person.greets()
# My name is: Jan
# My name is: Maciek
