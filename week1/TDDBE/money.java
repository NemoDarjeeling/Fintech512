//excellent exmaple of ploymorphism -- the method of Money reduce(){}
//In the given Java code, the reduce method is a part of the Expression interface, which means that any class that implements this interface must also implement a reduce method. This method takes a single parameter to, which is a string representing a currency. It returns a Money object.
//The reduce method is used to convert an Expression object (such as a Sum object or a Money object) to a single Money object with a specific currency. The Bank class has a reduce method that takes an Expression object and a string representing a currency and calls the reduce method on that Expression object, passing in the currency string as a parameter.
//In the case of Money object, the reduce method simply returns the Money object itself, since it is already in the desired currency. But in the case of Sum object, it will convert the Sum object to a single Money object by adding the amounts of the augend and addend Money objects and creating a new Money object with the sum of those amounts and the desired currency.
interface Expression {
    Money reduce(String to);
}

class Bank {
    Money reduce(Expression source, String to) {
        return source.reduce(to);
        }  
}

class Sum implements Expression {
    Money augend;
    Money addend;
    Sum(Money augend, Money addend) {
        this.augend = augend;
        this.addend = addend;
        }
    public Money reduce(String to) {
        int amount = augend.amount + addend.amount;
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

    Money times(int multiplier) {
        return new Money(amount * multiplier, currency);
        }

    public Money reduce(String to) {
        return this;
        }

    Expression plus(Money addend) {
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