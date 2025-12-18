from daty import Dates
from metody_statyczne_zad2 import Klakulator

print(f"Wartość wynosi: {Klakulator.oblicz(4, 65, 89)}")
# Wartość wynosi: 6141

date = Dates("18-12-2025")
date_format_db = "18/12/2025"

date_with_dash = Dates.to_dash_date(date_format_db)
d1 = date.get_date()
d2 = date_with_dash

if d1 == d2:
    print("Takie same daty")
    print(f"{d1} = {d2}")
else:
    print("Różne daty")
    print(f"{d1} != {d2}")
# Takie same daty
# 18-12-2025 = 18-12-2025
