import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_addition1(self): #succeeds
        result = calc.addition(10, 0)
        self.assertEqual(result, 10)

    def test_addition2(self): #fails
        result = calc.addition("Hello", "World")
        self.assertEqual(result, 10)

    def test_subtraction1(self): #succeeds
        result = calc.subtraction("10", "5")
        self.assertEqual(result, 5)

    def test_subtraction2(self): #fails
        result = calc.subtraction(False, "5")
        self.assertEqual(result, 0)

    def test_multiplication1(self): #succeeds
        result = calc.multiplication(5, 7)
        self.assertEqual(result, 35)

    def test_multiplication2(self): #fails
        result = calc.multiplication(True, "5")
        self.assertEqual(result, 0)

    def test_division1(self): #succeeds
        result = calc.division(10, 2)
        self.assertEqual(result, 5)

    def test_division2(self): #fails
        result = calc.division(10, 0)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()