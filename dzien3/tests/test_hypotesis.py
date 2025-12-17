from hypothesis import given
from hypothesis import strategies as st


@given(st.integers(), st.integers())
def test_addition_is_comutative(a, b):
    assert a + b == b + a


def absolute(x: int) -> int:
    if x < 0:
        # return x
        return -x
    return x


@given(st.integers())
def test_absolute_is_non_negative(x):
    result = absolute(x)
    assert result >= 0
# Expected :0
# Actual   :-1
