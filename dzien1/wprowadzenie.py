import sys

print('')
print('')
print('')
print('')

print("Pierwsza linia")
print('Pierwsza linia')
# Pierwsza linia
# Pierwsza linia

# ctrl / - komentowanie kodu
# print('Pierwsza linia")
#   File "C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien1\wprowadzenie.py", line 12
#     print('Pierwsza linia")
#           ^
# SyntaxError: unterminated string literal (detected at line 12)
"""
komentarz 
wielolinijkowy
dokumentacja"""

info = """Tekst
wielolinijkowy
    zachowuje
        formutanie"""
print(info)
# "Tekst
# wielolinijkowy
#     zachowuje
#         formutanie"
print(info)
print(info)
print(info)
print(info)
# ctrl d - kopiowanie linii

# typowanie dynamiczne
info = 90
print(info)
print(type(info))  # <class 'int'>, liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

info = "Radek"
print(info)  # Radek
print("12" + "89")  # 1289, połaczy teksty, konkatenacja
print(12 * "40")  # 404040404040404040404040

name = "Radek"
age = 56

# float - liczby zmiennoprzecinkowe
liczba = 36.6
print(type(liczba))  # <class 'float'>
print(0.1 + 0.9)  # 1.0
print(0.1 + 0.3)
print(0.1 + 0.2)  # 0.30000000000000004, bład zaokrąglenia
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal() - pozwalaja obejśc błąd zaokrąglenia, do obliczen na pieniądzach
