import unittest
from money import Dollar

class TestSquare(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(product.amount, 10)
        product = five.times(3)
        self.assertEqual(product.amount, 15)

    # when you use the assertEqual() or assertNotEqual() method provided by unittest.TestCase to check if two objects are equal or not, it will use the __eq__() method of the objects to determine equality if it is defined. If the __eq__() method is not defined, it will use the default implementation, which compares the memory addresses of the objects to check for equality.
    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))   
        self.assertNotEqual(Dollar(5), Dollar(6))

if __name__ == '__main__':
    unittest.main(verbosity = 2)