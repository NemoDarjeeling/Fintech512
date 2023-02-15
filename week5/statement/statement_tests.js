describe("statement", function() {
  it("generates 'Refactoring' 2nd ed example output", function() {
    expected1 = "Statement for BigCo\n  Hamlet: $650.00 (55 seats)\n  As You Like It: $580.00 (35 seats)\n  Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n"
    assert.equal(statement(invoice1[0],plays1), expected1);
  });

    // Example adapted from https://github.com/emilybache/Theatrical-Players-Refactoring-Kata/blob/main/javascript/test/statement.test.js
    it("test missing play type (Bache Kata example output)", function() {
      //chai.expect(function() {statement(invoice2,plays2)}).to.throw("unknown type: history");
      assert.throws(() => statement(invoice2,plays2), "unknown type: history");
    });
});
