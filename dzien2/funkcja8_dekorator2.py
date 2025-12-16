# zrobić dekorator, który zmienia wynik dziłania funkcji na duże litery
from functools import wraps

from colorama import Fore, Style, init


# pip install colorama

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


def color_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return Fore.RED + result + Style.RESET_ALL

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


@color_decorator
def greetings5(string):
    return f"(color)Podałeś: {string}"


print(greetings5("Kolor"))

print(greetings5.__name__)  # wrapper
# po dodaniu @wraps
# greetings5
# '__module__', '__name__', '__qualname__', '__doc__',
#                        '__annotate__', '__type_params__'
