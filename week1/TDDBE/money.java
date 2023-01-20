class Money {
    protected int amount;
    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount && getClass().equals(money.getClass());
        }

class Dollar extends Money{
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
    Dollar five= new Dollar(5);
    assertEquals(new Dollar(10), five.times(2));
    assertEquals(new Dollar(15), five.times(3));
    }

public void testEquality() {
    assertTrue(new Dollar(5).equals(new Dollar(5)));
    assertFalse(new Dollar(5).equals(new Dollar(6)));
    assertTrue(new Franc(5).equals(new Franc(5)));
    assertFalse(new Franc(5).equals(new Franc(6)));
    assertFalse(new Franc(5).equals(new Dollar(5)));
    }

public void testFrancMultiplication() {
    Franc five= new Franc(5);
    assertEquals(new Franc(10), five.times(2));
    assertEquals(new Franc(15), five.times(3));
    }