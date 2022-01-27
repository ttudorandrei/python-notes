from unit_testing.simplecalc import SimpleCalc
import unittest

# define a Class that inherits from testCase


class CalcTests(unittest.TestCase):

    # store the imported simplecalc in the variable called "calc"
    calc = SimpleCalc()

    # we call the function
    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calc.subtract(10, 5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_multiply(self):
        actual = self.calc.multiply(0.4, -80.9)
        expected = -32.36
        self.assertAlmostEqual(actual, expected)

    def test_divide(self):
        actual = self.calc.divide(100, 2)
        expected = 50
        self.assertEqual(actual, expected)
