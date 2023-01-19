import unittest
from money import Dollar

class TestSquare(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(five.amount, 10)

if __name__ == '__main__':
    unittest.main()