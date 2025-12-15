# funkcja wew, funkcja zagnieżdzona
# dekorator -  ma konstrukcję zbliżoną do funkcji wewnętrznej
# funkcja wyższego rzędu - funkcja która jako argument przyjmuje inną funkcję
def fun1():
    print("To jest funkcja1")

    def fun2():
        print("To jest fun2")

    # fun2() # zwraca wartosc funkcji

    return fun2  # zwróćenie adresu funkcji


fun1()
new_fun = fun1()
print(new_fun)  # <function fun1.<locals>.fun2 at 0x000001CFFC397320>
print(type(new_fun))  # <class 'function'>

new_fun()
new_fun()
new_fun()
new_fun()
# To jest fun2
# To jest fun2
# To jest fun2
# To jest fun2

# zrobic fukcje plik
# funkcja pryzjmuje parametr: zapis, odczyt
# w zależności od parametru zwróci odpowiednią funkcję

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
fh = open('test.txt', "w")
fh.write("Zapisano\n")
fh.close()


def plik(arg):
    def zapis():
        print("Zapis danych do pliku")

    def odczyt():
        print("Odczyt danych z pliku...")

    def pusta():
        print("Pusta operacja")

    match arg.casefold():
        case "zapis":
            return zapis  # zwracamy adres funkcji
        case "odczyt":
            return odczyt
        case _:
            return pusta


zapis_pliku = plik("zapis")
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()
zapis_pliku()

odczyt_pliku = plik("odczyt")
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()
odczyt_pliku()

pusta = plik("pusta")
pusta()  # Pusta operacja
