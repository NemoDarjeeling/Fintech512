#In Python, we don't have a built-in keyword like "protected" in Java, but we have a convention to use a single leading underscore (_) before the name of an attribute or method to indicate that it is intended for internal use and should not be accessed from outside the class. 
class Money:
    def __init__(self, amount):
        self.amount = amount
        
    def __eq__(self, other):
        return self.amount == other.amount

class Dollar(Money):
    #override of protected method in class Money
    def __init__(self, amount):
        super().__init__(amount)
    
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)  

class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)
    
    def times(self, multiplier):
        return Franc(self.amount * multiplier)
     
