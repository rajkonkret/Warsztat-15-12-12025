from abc import ABC, abstractmethod


# interface -
# 3 posiada tylko metody abstrakcyjne
# dopuszcza się metode domyslną

class Interface(ABC):

    @abstractmethod
    def policz(self):
        pass
