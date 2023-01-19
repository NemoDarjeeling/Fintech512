class Dollar:
    def __init__(self, amount):
        self.amount = amount
    
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, other): # override of original __eq__
        return isinstance(other, Dollar) and self.amount == other.amount       
