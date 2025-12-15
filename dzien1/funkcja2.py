# funkcja wew, funkcja zagnieżdzona

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
