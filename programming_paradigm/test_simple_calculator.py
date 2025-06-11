import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add("10", "5"), 15.0)
        self.assertEqual(self.calc.add("ten", 5), "Error: Please enter numeric values only.")

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract("20", "7"), 13.0)
        self.assertEqual(self.calc.subtract(5, "five"), "Error: Please enter numeric values only.")

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply("6", "7"), 42.0)
        self.assertEqual(self.calc.multiply("three", 4), "Error: Please enter numeric values only.")

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide("9", "3"), 3.0)
        self.assertEqual(self.calc.divide(10, 0), "Error: Cannot divide by zero.")
        self.assertEqual(self.calc.divide("ten", 2), "Error: Please enter numeric values only.")

if __name__ == '__main__':
    unittest.main()

