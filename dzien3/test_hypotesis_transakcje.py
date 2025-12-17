from hypothesis import given, strategies as st

from transakcje import (
    filter_transactions,
    map_transactions,
    reduce_transactions,
    process_transactions
)

transaction_type_strategy = st.sampled_from(["income", "expense"])
currency_strategy = st.sampled_from(["USD", "EUR", "PLN"])

transaction_strategy = st.fixed_dictionaries(
    {
        "id": st.integers(min_value=1, max_value=10_000),
        "type": transaction_type_strategy,
        "amount": st.integers(min_value=0, max_value=1_000_000),
        "currency": currency_strategy,
    }
)

transaction_list_strategy = st.lists(transaction_strategy, max_size=50)


@given(transaction_list_strategy, transaction_type_strategy)
def test_filter_tranasctions_keep_only_given_type(transactions, ttype):
    filtered = filter_transactions(transactions, ttype)

    assert all(tr['type'] == ttype for tr in filtered)


# map_transactions
@given(transaction_list_strategy, currency_strategy)
def test_map_transactions_lenght_matches(transactions, currency):
    mapped = map_transactions(transactions, currency)

    assert len(mapped) == len(transactions)

# test_hypotesis.py::test_addition_is_comutative PASSED                                                                                                                                                                        [ 50%]
# test_hypotesis.py::test_absolute_is_non_negative PASSED
