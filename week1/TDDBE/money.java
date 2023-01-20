abstract class Money {
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

    // Money times(int multiplier) {
    //     return new Money(amount * multiplier, currency);
    //     }
    // }

class Franc extends Money{
    Franc(int amount, String currency) {
        super(amount, currency);
        }

    // Money times(int multiplier) {
    //     return new Money(amount * multiplier, currency);
    //     }

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