import unittest
# if you want to access Dollar by just import money, you have to use its fully-qualified name everytime you mention it in your code
from money import Dollar, Franc, Money, Bank, Sum, Expression, Pair

class TestMoney(unittest.TestCase):
    def test_identity_rate(self):
        bank = Bank()
        self.assertEqual(bank.rate("USD", "USD"), 1)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(result, Money.dollar(1))

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        result = five.plus(five)       
        self.assertEqual(result.augend, five)
        self.assertEqual(result.addend, five)

    def test_reduce_sum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD") 
        self.assertEqual(result, Money.dollar(7)) 

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(result, Money.dollar(1))   

    #different class, same currency, should be equal
    def test_dif_class_equality(self):
        self.assertEqual(Money(10, "CHF"), Franc(10, "CHF"))

    def test_currency(self):
        self.assertEqual(Money.dollar(1).currency, "USD")
        self.assertEqual(Money.franc(1).currency, "CHF")

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(five.times(2), Money.dollar(10))
        self.assertEqual(five.times(3), Money.dollar(15))

    # when you use the assertEqual() or assertNotEqual() method provided by unittest.TestCase to check if two objects are equal or not, it will use the __eq__() method of the objects to determine equality if it is defined. If the __eq__() method is not defined, it will use the default implementation, which compares the memory addresses of the objects to check for equality.
    def test_equality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))   
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))
        self.assertNotEqual(Money.franc(5), Money.dollar(6))     

    def test_franc_multiplication(self):
        five = Money.franc(5)
        self.assertEqual(five.times(2), Money.franc(10))
        self.assertEqual(five.times(3), Money.franc(15))

if __name__ == '__main__':
    unittest.main(verbosity = 2)
    