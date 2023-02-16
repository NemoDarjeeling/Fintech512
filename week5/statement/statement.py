import math
# where do actual data for schema.sql stored in? in sqlite instances.
# method = "GET"(not executed?) or "POST"? used for interaction between html and .py files
# key! id = 3, fname = patrick, lname = morrison, title = prof, room = teer_203; id is the key, it has to be unique
# what should I do? open the test.html in browser and modify statement.js? when following the instructions in the book and the code seprated to 3 different files, still works? yes... you can try out following exactly the book.
# what do json file do? test cases? they are data files, copies from the book.
# possibility to replace js file with python file? where can I get more information on how to do this? It is an extra work about using interactions between html and js, or py and server. further instructions will be there.
# what does the example type in js command line do? using the temp variables before the breakpoint and test with your possible solution, not actually making changes to the original js file.
def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result

