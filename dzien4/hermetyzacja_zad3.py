class Car:

    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        """
        Getter - umoliwiad czytanie pola .model
        :return:
        """
        print("wypisuje model.")
        return self.__model


car = Car("Opel")
print(car.model)
# wypisuje model.
# Opel
