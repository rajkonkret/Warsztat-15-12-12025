import unittest


def divide(a, b):
    return a / b


# PascalCase
class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()

# ============================= test session starts =============================
# collecting ... collected 2 items
#
# dzien2/tests/test_unit_zad2.py::TestDivide::test_divide PASSED           [ 50%]
# dzien2/tests/test_unit_zad2.py::TestDivide::test_divide_by_zero PASSED   [100%]
#
# ============================== 2 passed in 0.02s ==============================
#
# Process finished with exit code 0
