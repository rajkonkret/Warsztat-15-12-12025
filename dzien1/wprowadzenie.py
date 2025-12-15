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
print(type(info)) # <class 'int'>, liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

