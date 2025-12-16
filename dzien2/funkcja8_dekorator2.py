# zrobić dekorator, który zmienia wynik dziłania funkcji na duże litery

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # uruchamiamy funkcję
        return result.upper()

    return wrapper  # zwracamy adres, referencję


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # uruchamiamy funkcję
        return "\033[1m" + result + "\033[0m"

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World"


print(greeting())  # Hello World


# HELLO WORLD
@uppercase_decorator
def greetings2(string):
    return f"Podałeś: {string}"


print(greetings2("Radek"))  # PODAŁEŚ: RADEK


@bold_decorator
def greetings3(string):
    return f"(bold)Podałeś: {string}"


print(greetings3("Test"))

# kolejność ma znaczenie
@bold_decorator
@uppercase_decorator
def greetings4(string):
    return f"(dwa)Podałeś: {string}"


print(greetings4("Test dwa"))
