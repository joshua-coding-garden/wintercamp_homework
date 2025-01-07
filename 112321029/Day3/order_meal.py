from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/list')
def f1():
    menu = "lunch.txt"
    infile = open(menu, "r")
    html = '<table border><tr><th></th><th>Item</th><th>price</th></tr>'
    while True:
        line = infile.readline()
        temp = line.split(':')
        html += '<tr>'
        if line == '': break
        for i in temp:
            html += '<td>' + f'{i}' + '</td>'
        html += '</tr>'
    html += '</table>'
    infile.close()
    return html

@app.route('/order')
def f2():
    html = '''<form action='/accept'>
    <input type=text name=name>
    <select name=mealId>'''
    menu = "lunch.txt"
    infile = open(menu, "r")
    while True:
        line = infile.readline()
        if line == '':
            break
        temp = line.strip().split(':')
        v = temp[0]
        result = f'{temp[1]} (${temp[2]})'
        html += f'<option value="{v}">{result}</option>'
    html += '<input type=submit></form>'
    infile.close()
    return html

@app.route('/accept')
def f3():
    name = request.args.get('name')
    meal_id = request.args.get('mealId')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    record = f"{current_time} {name} {meal_id}\n"
    with open("order.txt", "a") as outfile:
        outfile.write(record)
    return "we receive your order!"

@app.route('/total')
def f4():
    menu = {}
    p = {}
    price = 0
    with open("lunch.txt", "r") as infile:
        while True:
            line = infile.readline()
            if line == '':
                break
            temp = line.strip().split(':')
            meal_id = temp[0]
            meal_name = temp[1]
            meal_price = temp[2]
            menu[meal_id] = meal_name
            p[meal_id] = int(meal_price)

    html = '<table border><tr><th>Time</th><th>Name</th><th>Meal</th></tr>'
    with open("order.txt", "r") as infile:
        while True:
            line = infile.readline()
            if line == '':
                break
            temp = line.strip().split()
            time = f"{temp[0]} {temp[1]}"
            name = temp[2]
            meal_id = temp[3]
            meal_name = menu.get(meal_id, "Unknown Meal")
            meal_price = p.get(meal_id, 0)
            price += meal_price
            html += f"<tr><td>{time}</td><td>{name}</td><td>{meal_name}(${meal_price})</td></tr>"
    html += f'<tr><td></td><td>Total</td><td>${price}</td></tr></table>'
    return html
