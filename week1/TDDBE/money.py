class Dollar:
    def __init__(self, amount):
        self._amount = amount
    
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def __eq__(self, other): # override of original __eq__
        return isinstance(other, Dollar) and self._amount == other._amount 
    
    # setting amount private to Dollar, but can access the value of amount attribute by calling dollar.amount instead of dollar._amount 
    @property
    def amount(self):
        return self._amount      
