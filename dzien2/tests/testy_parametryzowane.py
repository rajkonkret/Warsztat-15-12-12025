import pytest


def divide(a, b):
    return a / b


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (12, 4, 3),
    ]
)
def test_divide_ok(a, b, expected):
    assert divide(a, b) == expected


# testy_parametryzowane.py::test_divide_ok[10-2-5] PASSED                                                                                                                                                                     [ 33%]
# testy_parametryzowane.py::test_divide_ok[9-3-3] PASSED                                                                                                                                                                      [ 66%]
# testy_parametryzowane.py::test_divide_ok[12-4-3] PASSED

@pytest.mark.parametrize("a,b",
                         [
                             (1, 0),
                             (5, 0),
                             # (5, 1)
                         ])
def test_divide_raises(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)
# with - context manager
# testy_parametryzowane.py::test_divide_raises[1-0] PASSED                                                                                                                                                                    [ 80%]
# testy_parametryzowane.py::test_divide_raises[5-0] PASSED
