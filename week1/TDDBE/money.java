abstract class Money {
    Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
        }

    static Money dollar(int amount) {
        return new Dollar(amount, "USD");
        }

    static Money franc(int amount) {
        return new Franc(amount, "CHF");
        }

    abstract Money times(int multiplier);

    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount && getClass().equals(money.getClass());
        }
}

class Dollar extends Money{
    //override Money's constructor
    Dollar(int amount, String currency) {
        super(amount, currency);
        }

    Money times(int multiplier) {
        return Money.dollar(amount * multiplier);
        }
    }

class Franc extends Money{
    Franc(int amount, String currency) {
        super(amount, currency);
        }

    Money times(int multiplier) {
        return Money.franc(amount * multiplier);
        }
    }
                     
public void testMultiplication() {
    Money five = Money.dollar(5);
    assertEquals(Money.dollar(10), five.times(2));
    assertEquals(Money.dollar(15), five.times(3));
    }

public void testEquality() {
	assertTrue(Money.dollar(5).equals(Money.dollar(5)));
	assertFalse(Money.dollar(5).equals(Money.dollar(6)));
	assertTrue(Money.franc(5).equals(Money.franc(5)));
	assertFalse(Money.franc(5).equals(Money.franc(6)));
	assertFalse(Money.franc(5).equals(Money.dollar(5)));
	}

public void testFrancMultiplication() {
	Money five = Money.franc(5);
	assertEquals(Money.franc(10), five.times(2));
	assertEquals(Money.franc(15), five.times(3));
	}