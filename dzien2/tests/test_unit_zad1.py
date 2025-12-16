import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

# dzien2/tests/test_unit_zad1.py::MyTestCase::test_something
#
# ============================== 1 failed in 0.09s ==============================
# FAILED        [100%]
# dzien2\tests\test_unit_zad1.py:4 (MyTestCase.test_something)
# False != True
#
# Expected :True
# Actual   :False
# <Click to see difference>
