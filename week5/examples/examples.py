from flask import Flask, render_template
# dude, you forget to set the BluePrint "/examples"!
app = Flask(__name__, static_url_path='/static')
# make it possible to run flask app by .py file name
# static is a norm, includes is a older one, but static is a predetermined built-in folder for flask to find js and data

import math

invoice = {
    "customer": "BigCo",
    "performances": [
        {"playID": "Hamlet", "audience": 55},
        {"playID": "As You Like It", "audience": 35},
        {"playID": "Othello", "audience": 40}
    ]
}

plays = {
    "Hamlet": {"name": "Hamlet", "type": "tragedy"},
    "As You Like It": {"name": "As You Like It", "type": "comedy"},
    "Othello": {"name": "Othello", "type": "tragedy"}
}
# put all needed data here

def format_as_dollars(amount):
    return f"${amount:0,.2f}"
# used for formatting

def get_amount_for_performance(perf):
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

    return this_amount
# used for calculating cost for each performance

def get_total_amount():
    total_amount = 0
    for perf in invoice['performances']:
        total_amount += get_amount_for_performance(perf)
    return total_amount
# add all cost for performances

def get_volume_credits():
    volume_credits = 0
    for perf in invoice['performances']:
        volume_credits += max(perf['audience'] - 30, 0)
        if "comedy" == plays[perf['playID']]["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
    return volume_credits
# calculate volume credits

@app.route('/statement')
def statement():
    return render_template('statement.html', customer = invoice["customer"], performances = invoice["performances"], plays = plays, format_as_dollars = format_as_dollars, get_amount_for_performance = get_amount_for_performance, get_total_amount=get_total_amount(), volume_credits=get_volume_credits())
# render 
# just write a function which writes html in statement.py file!

@app.route('/stockchart')
def stockchart():
    return render_template('index.html')