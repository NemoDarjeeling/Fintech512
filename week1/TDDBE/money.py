from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, to_currency):
        pass

    @abstractmethod
    def plus(self, addend):
        pass

class Pair:
    def __init__(self, from_currency, to_currency):
        self.from_currency = from_currency
        self.to_currency = to_currency

    def __eq__(self, other):
        return self.from_currency == other.from_currency and self.to_currency == other.to_currency
    #In python, we don't have a built-in hashCode() method like in Java. Instead, Python uses the __hash__() method to determine the hash value of an object. The __hash__() method is a special method that is automatically called when an object is used as a key in a dictionary or as an element in a set.
    #In python, if a class wants to be hashable, it must implement the hash and eq methods. 
    def __hash__(self):
        return hash((self.from_currency, self.to_currency))

class Bank:
    #no built-in Hashtable class in python, it is just dictionary
    def __init__(self):
        self.rates = {}

    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)

    def rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1
        #In python, the get() method is a built-in method of the dict (dictionary) class, it works similar to the Hashtable's get() method in java. The get() method of the dict class is used to retrieve the value associated with a specific key. If the key is not found in the dictionary, it returns a default value (which can be specified as an argument to the get() method). If no default value is specified, it returns None
        rate = self.rates.get(Pair(from_currency, to_currency))
        return rate

    def add_rate(self, from_currency, to_currency, rate):
        self.rates[Pair(from_currency, to_currency)] = rate

class Sum(Expression):
    #now type of augend and addend is Expression, so we need abstract method in class Expression
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def plus(self, addend):
        return None

    def reduce(self, bank, to_currency):
        amount = self.augend.reduce(bank, to_currency).amount + self.addend.reduce(bank, to_currency).amount
        return Money(amount, to_currency)

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

    def reduce(self, bank, to_currency):
        rate = bank.rate(self.currency, to_currency)
        return Money(self.amount / rate, to_currency)

    def plus(self, addend):
        return Sum(self, addend)

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

     
