abstract class Money {
    protected int amount;

    static Money dollar(int amount) {
        return new Dollar(amount);
        }

    static Money franc(int amount) {
        return new Franc(amount);
        }

    abstract Money times(int multiplier);

    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount && getClass().equals(money.getClass());
        }
}

class Dollar extends Money{
    //子类没有constructor父类就要有，父类没有子类就要有
    Dollar(int amount) {
        this.amount= amount;
        }
    Dollar times(int multiplier) {
        return new Dollar(amount * multiplier);
        }
    }

class Franc extends Money{
    Franc(int amount) {
        this.amount= amount;
        }
    Franc times(int multiplier) {
        return new Franc(amount * multiplier);
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