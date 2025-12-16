# assert - asercja
# x = 5
# assert x == 5
# assert x == 10
# dzien2/tests/test_transakcje.py:None (dzien2/tests/test_transakcje.py)
# dzien2\tests\test_transakcje.py:4: in <module>
#     assert x == 10
# E   assert 5 == 10

import transakcje as tr
import pytest


# map transactions
def test_map_transactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert tr.map_transactions(tr.transactions, "USD") == result


def test_filter_transactions_income():
    expected_list = [
        {'id': 1, "type": "income", "amount": 1000, "currency": "USD"},
        {'id': 3, "type": "income", "amount": 500, "currency": "USD"},
        {'id': 5, "type": "income", "amount": 700, "currency": "USD"},
        {'id': 7, "type": "income", "amount": 100, "currency": "EUR"},
    ]
    assert tr.filter_transactions(tr.transactions, "income") == expected_list


def test_reduce_transactions():
    assert tr.reduce_transactions([1000, 500, 700, 0]) == 2200


# (.venv) PS C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2\tests> pytest -v .\test_transakcje.py
# ====================================================================================================== test session starts =======================================================================================================
# platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2\tests
# collected 3 items
#
# test_transakcje.py::test_map_transactions_usd PASSED                                                                                                                                                                        [ 33%]
# test_transakcje.py::test_filter_transactions_income PASSED                                                                                                                                                                  [ 66%]
# test_transakcje.py::test_reduce_transactions PASSED                                                                                                                                                                         [100%]
#
# ======================================================================================================= 3 passed in 0.02s ========================================================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2\tests>

def test_transactions_processing():
    assert (tr.map_transactions(tr.filter_transactions(tr.transactions, "income"), "USD")
            == [1000, 500, 700, 0])


# (.venv) PS C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2\tests> pytest -v .\test_transakcje.py
# ====================================================================================================== test session starts =======================================================================================================
# platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2\tests
# collected 4 items
#
# test_transakcje.py::test_map_transactions_usd PASSED                                                                                                                                                                        [ 25%]
# test_transakcje.py::test_filter_transactions_income PASSED                                                                                                                                                                  [ 50%]
# test_transakcje.py::test_reduce_transactions PASSED                                                                                                                                                                         [ 75%]
# test_transakcje.py::test_transactions_processing PASSED                                                                                                                                                                     [100%]
#
# ======================================================================================================= 4 passed in 0.02s ========================================================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2\tests>

# def test_map_transactions_usd_wrong():
#     wrong = [1, 2, 3]
#     assert tr.map_transactions(tr.transactions, "USD") == wrong
#

# >       assert tr.map_transactions(tr.transactions, "USD") == wrong
# E       AssertionError: assert [1000, 200, 5..., 700, 0, ...] == [1, 2, 3]
# E
# E         At index 0 diff: 1000 != 1
# E         Left contains 4 more items, first extra item: 300
# E
# E         Full diff:
# E           [
# E         -     1,...
# E
# E         ...Full output truncated (13 lines hidden), use '-vv' to show
#
# test_transakcje.py:69: AssertionError
# ==================================================================================================== short test summary info =====================================================================================================
# FAILED test_transakcje.py::test_map_transactions_usd_wrong - AssertionError: assert [1000, 200, 5..., 700, 0, ...] == [1, 2, 3]
# ================================================================================================== 1 failed, 4 passed in 0.12s ===================================================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\Warsztat-15-12-12025\dzien2\tests>

# test parametryzowany - wykonanie testu na wielu zestawach parametrów

@pytest.mark.parametrize(
    "kind,currency,expected",
    [
        ("income", "USD", 1000 + 500 + 700),
        ("income", "EUR", 100),
        ("expense", "USD", 200 + 300),
        ("expense", "EUR", 400)
    ]
)
def test_process_transactions_param(kind, currency, expected):
    assert tr.process_transactions(tr.transactions, kind, currency) == expected
# test_transakcje.py::test_process_transactions_param[income-USD-2200] PASSED                                                                                                                                                 [ 62%]
# test_transakcje.py::test_process_transactions_param[income-EUR-100] PASSED                                                                                                                                                  [ 75%]
# test_transakcje.py::test_process_transactions_param[expense-USD-500] PASSED                                                                                                                                                 [ 87%]
# test_transakcje.py::test_process_transactions_param[expense-EUR-400] PASSED
