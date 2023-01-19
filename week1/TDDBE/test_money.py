import unittest
from money import Dollar

class TestSquare(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(product.amount, 10)
        product = five.times(3)
        self.assertEqual(product.amount, 15)

if __name__ == '__main__':
    unittest.main(verbosity = 2)