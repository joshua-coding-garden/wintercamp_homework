from flask import Flask,request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def read_lunch_file():
    lunch_choices = []
    infile = open("lunch.txt","r",encoding="utf-8")
    for line in infile:
        parts = line.split(":")

        index = parts[0]
        item = parts[1]
        price = parts[2]
        lunch_choices.append((index,item,price))
    return lunch_choices

@app.route('/list')
def show_lunch_list():
    lunch_choices = read_lunch_file()
    html = '''<table border>
            <tr><th></th><th>item</th><th>price</th></tr>'''
    for index, item, price in lunch_choices[1:]:
        html += '''<tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>'''.format(index, item, price)
    return html

@app.route('/order')
def order_lunch():
    lunch_choices = read_lunch_file()
    html = '''<form method='POST' action='/accept'>
        <input type=text name=name>
        <select name=mealId>
        <option value=0>Item ($price)</option>'''
    for index, item, price in lunch_choices[1:]:
        html += '''<option value={}>{}(${})</option>'''.format(index, item, price)
    html += '''</select><input type=submit>
        </form>'''
    return html

@app.route('/accept',methods = ['POST'])
def accept_order():
    lunch_choices = read_lunch_file()
    name = request.values['name']
    meal_id = request.values['mealId']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    outfile = open('order.txt','a',encoding='utf-8')
    outfile.write('{} {} {}\n'.format(timestamp,name,meal_id))
    return "Order received from {}: {} at {}".format(name,meal_id,timestamp)

@app.route('/total')
def total_order():
    lunch_choices = read_lunch_file()
    total_price = 0

    html = '<table border><tr><th>Time</th><th>Name</th><th>Meal</th></tr>'

    infile = open("order.txt","r",encoding="utf-8")
    for line in infile:
        parts = line.split()
        time = f"{parts[0]} {parts[1]}"
        name = parts[2]
        meal_id = parts[3]
        meal_name,price = next(((item,price) for index, item, price in lunch_choices if index == str(meal_id)),(None,None))
        html += f"<tr><td>{time}</td><td>{name}</td><td>{meal_name}(${price})</td></tr>"
        total_price += int(price)

    html += f"<tr><td></td><td>Total</td><td>${total_price}</tr></table>"
    return html
