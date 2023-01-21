//excellent exmaple of ploymorphism -- the method of Money reduce(){}
//In the given Java code, the reduce method is a part of the Expression interface, which means that any class that implements this interface must also implement a reduce method. This method takes a single parameter to, which is a string representing a currency. It returns a Money object.
//The reduce method is used to convert an Expression object (such as a Sum object or a Money object) to a single Money object with a specific currency. The Bank class has a reduce method that takes an Expression object and a string representing a currency and calls the reduce method on that Expression object, passing in the currency string as a parameter.
//In the case of Money object, the reduce method simply returns the Money object itself, since it is already in the desired currency. But in the case of Sum object, it will convert the Sum object to a single Money object by adding the amounts of the augend and addend Money objects and creating a new Money object with the sum of those amounts and the desired currency.
interface Expression {
    Money reduce(Bank bank, String to);
    //The plus() method is used to add two monetary expressions together. The plus() method takes an Expression object as a parameter, and it returns a new Expression object that represents the sum of the two expressions. The returned object is typically an instance of the Sum class.
    //In the case of the Money class, the plus() method creates a new Sum object, with the current Money object as the "augend" (the first value being added) and the Expression object passed as the "addend" (the second value being added).
    //In the case of the Sum class, the plus() method creates a new Sum object, with the current Sum object as the "augend" and the Expression object passed as the "addend".
    //This method is used as a way to represent monetary expressions in a tree-like structure, where each Sum object is a node, and it has two children, the augend and addend.
    //This design allows you to express complex monetary expressions as a tree of simple expressions, and then reduce the entire tree to a single value in a given currency.
    Expression plus(Expression addend);
}

private class Pair {
    private String from;
    private String to;
    Pair(String from, String to) {
        this.from= from;
        this.to= to;
        }

    public boolean equals(Object object) {
        Pair pair= (Pair) object;
        return from.equals(pair.from) && to.equals(pair.to);
        }

    public int hashCode() {
        return 0;
        }
    }

class Bank {
    //The reduce() method in the Money class and Sum class takes an additional Bank object as a parameter. This is because the reduce() method in these classes needs to use the exchange rate information stored in the Bank object to convert the Money object's currency to the desired currency.
    //When the reduce() method is called on a Sum object, the Bank object is used to reduce each of the Money objects in the sum to the desired currency, and then the amounts are added together to get the final amount in the desired currency.
    //In the case of Bank class reduce() method, this method takes an Expression object and a currency as parameter, and calls the reduce() method of the Expression object, passing itself as the first argument. This way, the Expression object can use the exchange rate information stored in the Bank object to perform the conversion.
    Money reduce(Expression source, String to) {
        return source.reduce(this, to);
        }
    //The method uses a ternary operator, which is a shorthand way of writing an if-else statement. The ternary operator has the following syntax:
    //condition ? value if true : value if false;
    //...and since Hashtable and Integer are built-in functions, we would just use these
    private Hashtable rates = new Hashtable();
    int rate(String from, String to) {
        if (from.equals(to)) return 1;
        Integer rate = (Integer) rates.get(new Pair(from, to));
        return rate.intValue();
        }
    
    void addRate(String from, String to, int rate) {
        rates.put(new Pair(from, to), new Integer(rate));
        }
}

class Sum implements Expression {
    Expression augend;
    Expression addend;

    public Expression plus(Expression addend) {
        return null;
     }

    Sum(Expression augend, Expression addend) {
        this.augend= augend;
        this.addend= addend;
        }
    
    //In the original code, the augend and addend expressions are simply added together, regardless of their currency. However, in the new code, the reduce() method is called on each of the augend and addend expressions, passing in the Bank and the desired currency as parameters. This causes each expression to be converted to the desired currency using the exchange rate information stored in the Bank, before being added together. This way, the final result is in the desired currency and is correct.
    public Money reduce(Bank bank, String to) {
        int amount= augend.reduce(bank, to).amount + addend.reduce(bank, to).amount;
        return new Money(amount, to);
        }
    }

class Money implements Expression{
    Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
        }

    String currency() {
        return currency;
        }

    static Money dollar(int amount) {
        return new Money(amount, "USD");
        }

    static Money franc(int amount) {
        return new Money(amount, "CHF");
        }

    Expression times(int multiplier) {
        return new Money(amount * multiplier, currency);
        }

    public Money reduce(Bank bank, String to) {
        int rate = bank.rate(currency, to);
        return new Money(amount / rate, to);
        }

    public Expression plus(Expression addend) {
        return new Sum(this, addend);
        }

    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount && currency().equals(money.currency());
    }
}

class Dollar extends Money{
    //override Money's constructor
    Dollar(int amount, String currency) {
        super(amount, currency);
        }

class Franc extends Money{
    Franc(int amount, String currency) {
        super(amount, currency);
        }

public void testMixedAddition() {
    Expression fiveBucks= Money.dollar(5);
    Expression tenFrancs= Money.franc(10);
    Bank bank= new Bank();
    bank.addRate("CHF", "USD", 2);
    Money result= bank.reduce(fiveBucks.plus(tenFrancs), "USD");
    assertEquals(Money.dollar(10), result);
    }

public void testIdentityRate() {
    assertEquals(1, new Bank().rate("USD", "USD"));
    }

public void testReduceMoneyDifferentCurrency() {
    Bank bank= new Bank();
    bank.addRate("CHF", "USD", 2);
    Money result= bank.reduce(Money.franc(2), "USD");
    assertEquals(Money.dollar(1), result);
    }


public void testPlusReturnsSum() {
    Money five= Money.dollar(5);
    Expression result= five.plus(five);
    Sum sum = (Sum) result;
    assertEquals(five, sum.augend);
    assertEquals(five, sum.addend);
    }

public void testReduceSum() {
    Expression sum = new Sum(Money.dollar(3), Money.dollar(4));
    Bank bank = new Bank();
    Money result = bank.reduce(sum, "USD");
    assertEquals(Money.dollar(7), result);
    }

public void testReduceMoney() {
    Bank bank= new Bank();
    Money result= bank.reduce(Money.dollar(1), "USD");
    assertEquals(Money.dollar(1), result);
    }    

public void testDifferentClassEquality() {
    assertTrue(new Money(10, "CHF").equals(new Franc(10, "CHF")));
    }        

public void testCurrency() {
    assertEquals("USD", Money.dollar(1).currency());
    assertEquals("CHF", Money.franc(1).currency());
    }    

public void testMultiplication() {
    Money five = Money.dollar(5);
    assertEquals(Money.dollar(10), five.times(2));
    assertEquals(Money.dollar(15), five.times(3));
    }

public void testEquality() {
	assertTrue(Money.dollar(5).equals(Money.dollar(5)));
	assertFalse(Money.dollar(5).equals(Money.dollar(6)));
	assertFalse(Money.franc(5).equals(Money.dollar(5)));
	}

public void testFrancMultiplication() {
	Money five = Money.franc(5);
	assertEquals(Money.franc(10), five.times(2));
	assertEquals(Money.franc(15), five.times(3));
	}