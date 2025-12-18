# class Person:
#     def __init__(self, fn, ln, id):
#         self.fn = fn
#         self.ln = ln
#         self.id = id
#
#
# p1 = Person("Jan", "Kowalski", 1)
# print(p1)  # <__main__.Person object at 0x000001E5C03B8830>
# # __str__, __repr__

import pickle
from dataclasses import dataclass

"""Add dunder methods based on the fields defined in the class.

   Examines PEP 526 __annotations__ to determine fields.

   If init is true, an __init__() method is added to the class. If repr
   is true, a __repr__() method is added. If order is true, rich
   comparison dunder methods are added. If unsafe_hash is true, a
   __hash__() method is added. If frozen is true, fields may not be
   assigned to after instance creation. If match_args is true, the
   __match_args__ tuple is added. If kw_only is true, then by default
   all fields are keyword-only. If slots is true, a new class with a
   __slots__ attribute is returned.
   """


@dataclass()
class Person:
    first_name: str
    last_name: str
    id: int

    def greets(self):
        print("My name is:", self.first_name)


p2 = Person("Jan", "Kowalski", 1)
print(p2)  # Person(first_name='Jan', last_name='Kowalski', id=1)
p3 = Person("Maciek", "Arbuz", 2)
# Person(first_name='Jan', last_name='Kowalski', id=1)
p2.greets()
p3.greets()
# My name is: Jan
# My name is: Maciek

people = [p2, p3]

# pickle - serializacja i deserializacja obiektów
# wb - wymagania biblioteki pickle
with open('dane.pckl', "wb") as f:
    pickle.dump(people, f)
