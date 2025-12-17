from functools import reduce

transactions = [
    {'id': 1, "type": "income", "amount": 1000, "currency": "USD"},
    {'id': 2, "type": "expense", "amount": 200, "currency": "USD"},
    {'id': 3, "type": "income", "amount": 500, "currency": "USD"},
    {'id': 4, "type": "expense", "amount": 300, "currency": "USD"},
    {'id': 5, "type": "income", "amount": 700, "currency": "USD"},
    {'id': 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {'id': 7, "type": "income", "amount": 100, "currency": "EUR"},
]


# filtrowanie tranakcji po typie
# przemapowanie transakcji -> jesli trx w danej walucie to wartosc, wstawiamy kwote 0
# zsumujemy te transakcje -> reduce

# process_transactions() -> filtruje, mapuje, redukuje
# zwraca ten wynik

def filter_transactions(transactions, transaction_type):
    """
    Filtruje transakcje po typie transakcji ["income", "expense"]
    :param transactions:
    :param transaction_type: ["income", "expense"]
    :return:
    """
    return list(filter(lambda x: x['type'] == transaction_type, transactions))


def map_transactions(transactions, currency):
    """
    Mapuje transakcje spełniające warunek waluty na kwote w nowej liście
    :param transactions:
    :param currency: usd, eur
    :return: lista transakcji
    """

    return list(map(lambda x: x['amount'] if x['currency'] == currency else 0, transactions))


def reduce_transactions(mapped):
    """
    Zsumuje kwoty transakcji
    :param mapped:
    :return: wartość zsumowanych transakcji, int, float
    """
    return reduce(lambda x, y: x + y, mapped, 0)


def process_transactions(transactions, transaction_type, currency):
    filtered = filter_transactions(transactions, transaction_type)
    mapped = map_transactions(filtered, currency)
    total = reduce_transactions(mapped)

    return total


# testy jednostkowe
# def test_transactions_processing():
#     assert (map_transactions(filter_transactions(transactions, "income"), "USD")
#             == [1000, 500, 700, 0])


if __name__ == "__main__":
    print(process_transactions(transactions, "expense", "EUR"))  # 400

    # test_transactions_processing()
    # pip install pytest
    #  cd .\dzien2\
    # > pytest .\transakcje.py
    #  pytest -v  .\transakcje.py - szcegółowe dane

    # (.venv) PS C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2> pytest -v  .\transakcje.py
    # ====================================================================================================== test session starts =======================================================================================================
    # platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\.venv\Scripts\python.exe
    # cachedir: .pytest_cache
    # rootdir: C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2
    # collected 1 item
    #
    # transakcje.py::test_transactions_processing PASSED                                                                                                                                                                          [100%]
    #
    # ======================================================================================================= 1 passed in 0.01s ========================================================================================================
    # (.venv) PS C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2>