from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/list')
def list_items():
    infile = open('lunch.txt', "r")
    aList = infile.readlines()
    html = '<table border="1"><tr><th></th><th>Item</th><th>Price</th></tr>'
    for line in aList[1:]:
        a, b, c = line[:-1].split(':')
        html += '<tr><td>{}</td><td>{}</td><td>{}</td>'.format(a, b, c)
    html += '</table>'
    infile.close()
    return html

@app.route('/order')
def order():
    infile = open('lunch.txt', "r")
    aList = infile.readlines()
    html = '''<form action='/accept' method='POST' enctype = "multipart/form-data">
            <input type="text" name="name">
            <select name=mealId>'''
    for line in aList:
        a, b, c = line[:-1].split(':')
        html += '<option value="{}">{}(${})</option>'.format(a, b, c)
    html += '</select><input type=submit></form>'
    return html

@app.route('/accept', methods=['POST'])
def accept():
    name = request.values['name']
    mealId = request.values['mealId']
    infile = open('lunch.txt', "r")
    aList = infile.readlines()
    meal = ""
    for line in aList:
        a, b, c = line[:-1].split(':')
        if a == mealId:
            meal = "{}(${})".format(b, c)
            break
    infile.close()
    d1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = "{} {} {}\n".format(d1, name, meal)
    f = open("order.txt", "a")
    f.write(line)
    f.close()
    return "{} orders {}.".format(name, meal)

@app.route('/total')
def total():
    infile = open("order.txt", "r")
    aList = infile.readlines()
    html = '<table border="1"><tr><th>Time</th><th>Name</th><th>Meal</th></tr>'
    total_price = 0
    for line in aList:
        date, time, name, meal = line[:-1].split()
        price = int(meal.split('$')[-1].strip(')'))
        total_price += price
        html += '<tr><td>{} {}</td><td>{}</td><td>{}</td></tr>'.format(date, time, name, meal)
    html += '<tr><td></td><td>Total</td><td>${}</td></tr>'.format(total_price)
    html += '</table>'
    return html