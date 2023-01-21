from abc import ABC, abstractmethod

#python do not have interface so we use abm
#By using the abc module and the @abstractmethod decorator, the Expression class is indicating that any class that subclasses it must provide an implementation for the plus method. 
#this allows us to add not only Money
class Expression(ABC):
    @abstractmethod
    def plus(self, addend):
        pass

#doesn't really do anything here, just to pass the test
class Bank:
    def reduce(self, source, to):
        return Money(10, "USD")

#In Python, we don't have a built-in keyword like "protected" in Java, but we have a convention to use a single leading underscore (_) before the name of an attribute or method to indicate that it is intended for internal use and should not be accessed from outside the class. 
class Money(Expression):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    #no need code below! In the original code, currency() is a method, in python currency is an attribute. You should use self.currency instead of self.currency().
    # def currency(self):
    #     return self.currency
    #dollar method creates a new instance of the Dollar class and returns it, with the amount passed as an argument.
    #franc method creates a new instance of the Franc class and returns it, with the amount passed as an argument.
    #Both these methods are defined as static methods, which means that they can be called on the class itself, rather than on an instance of the class. So, you don't have to create an instance of Money class to call these methods, you can directly call them on Money class.
    #"money = Money.dollar(5)" 初始化由父类里这两个函数代劳，用不到子类里的初始化，子类里面自然也就不需要重载父类的初始化了   
    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")
    
    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")
        
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend):
        return Money(self.amount + addend.amount, self.currency)

    #notice no more type checks here, only value checks (trap)
    #now we add type check, noticeIt is not correct to replace "return self._amount == other._amount and type(self) == type(other)" with "return isinstance(self, other) and self._amount == other._amount" 
    #The intended behavior of the code is to check if two objects are of the same class and have the same value for the attribute '_amount'. The proposed replacement "return isinstance(self, other) and self._amount == other._amount" only check if the two objects are instances of the same class and have the same value for the attribute '_amount'.    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

class Dollar(Money):
    #The Money class has constructor __init__(self, amount) which is initializing the amount attribute and the Dollar and Franc classes inherit from Money, they also inherit the amount attribute, so there is no need to initialize it again in the Dollar and Franc classes.
    #but since in java book there is an inheritance and override for child class constructor we will add it here
    #you can omit contructors, but not recommended
    def __init__(self, amount, currency):
        super().__init__(amount, currency) 

class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

     
