import unittest

from square import Square # the class you want to test

class TestSquare(unittest.TestCase): # ??what is unittest.TestCase??
    def test_area(self): # new function
        square = Square(10) # initialize with 10
        area = square.area() # compute area
        self.assertEqual(area, 100) # compare computed area and right area

    def test_length_with_wrong_type(self):
        with self.assertRaises(TypeError):
            square = Square('10')

    def test_length_with_zero_or_negative(self):
        with self.assertRaises(ValueError):
            square = Square(0)
            square = Square(-1)

# if __name__ == '__main__':
#     unittest.main(verbosity = 2) # To get more detailed information on the test result, you pass the verbosity argument with the value 2

