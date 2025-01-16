from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/list')
def List():
    infile = open('static/list.txt', "r")
    aList = infile.readlines()
    html = '<table border="1">'
    for line in aList:
        html += '<tr>'
        items = line.split(':')
        for i in items:
            if(i == '0'):
                i = ''
            html += '<td>'
            html += i.rstrip() #去除字尾空白
            html += '</td>'
        html += '</tr>'
    infile.close()
    html += '</table>'
    return html

@app.route('/order')
def Order():
    html = '<form method="POST" action="/accept">'
    html += '<input type="text" name="name">'
    html += '<select name="mealId">'
    infile = open('static/list.txt', "r")
    aList = infile.readlines()
    for line in aList:
        items = line.split(':')
        html += f'<option value={items[0]}>' + items[1] + f'$({items[2].strip()})' + '</option>' #.strip()移除字串空白
    html += '</select>'
    html += '<input type=submit>'
    html += '</form>'
    return html

@app.route('/accept', methods=['POST'])
def Accept():
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    infile = open('static/order.txt', "a")
    name = request.values.get('name') #[]
    mealId = request.values.get('mealId')
    s = f'{t} {name} {mealId}'
    print(s, file=infile)
    infile.close()
    return 'We receive your order!'

@app.route('/total')
def Total():
    order_file = open('static/order.txt', "r")
    infile = open('static/list.txt', "r")

    oList = order_file.readlines()
    aList = infile.readlines()

    meal = "none"
    total = 0
    html = '<table border="1"><tr><td>Time</td><td>Name</td><td>Meal</td></tr>'
    for line in oList:
        date, clock, name, mealId = line.strip().split(' ')
        time = f"{date} {clock}"

        for line in aList:
            a, b, c = line.strip().split(':')
            if(mealId == a):
                meal = f'{b}$({c})'
                total += int(c)
                break
        html += f'<tr><td>{time}</td><td>{name}</td><td>{meal}</td></tr>'
    html += f'<tr><td></td><td>Total</td><td>{total}</td></tr></table>'

    order_file.close()
    infile.close()

    return html