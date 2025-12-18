# stworzyc klasę Boat
#  dodac pole predkosc prywatne
#  dodac metody do odczytu i zapisu tego pola: speedometer, accelrate
class Boat:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0

    def sail(self):
        self.__speed += 10

    def speedometer(self):
        print(f"Speed is {self.__speed} knots.")
        self.__test()

    def __test(self):
        print("All tested")


boat = Boat("Omega", 2025)
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.speedometer()
# print(boat.__speed)  # AttributeError: 'Boat' object has no attribute '__speed'

# metoda prywatna - nie można jej uzyc poza klasą
# boat.__test() # AttributeError: 'Boat' object has no attribute '__test'
# Speed is 50 knots.
# All tested
