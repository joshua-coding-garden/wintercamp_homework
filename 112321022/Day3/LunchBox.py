from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/list')
def list():

    infile = open('lunch.txt', "r")
    html = '''
        <form action='/tatol'>
        <input type="submit" value="Tatol">
        </form>
        <form action='/order'>
        MENU:
        <table border>
    '''
    for line in infile:
        html += '<tr>'
        line = line.strip()
        temp = line.split(':')
        if temp[0] == "0":
            for i in temp:
                html += '<th>' + (i if i != "0" else '') + '</th>'
        else:
            for i in temp:
                html += '<td>' + i + '</td>'
        html += '</tr>'
    html += '''
        </table>
        <input type="submit" value="Order">
        </form>
    '''
    infile.close()
    return html

@app.route('/order')
def order():
    infile = open('lunch.txt', "r")
    option = ''
    for line in infile:
        line = line.strip()
        temp = line.split(':')
        id = temp[0]
        i = temp[1]
        p = temp[2]
        option += "<option value='{}:{}(${})' {}> {} (${})</option>".format(id, i, p, ("disabled selected" if temp[0] == '0' else ''), i, p)
    infile.close()

    html = '''
        <form method='POST' action='/accept'>
        <input id="name" name="name" type="text" oninput="f1()">
        <select id="item" name="item">{}</select>
        <input id="b1" type="submit" value="Submit" onClick="f2()" disabled>
        </form>

        <script>
            function f1() {{
                var a = document.getElementById('name').value;
                document.getElementById('b1').disabled = (a.trim() == '');
            }}
            function f2() {{
                var name = document.getElementById('name').value;
                var item = document.getElementById('item').value.split(':')[1];
                alert(name + ' orders ' + item);
            }}
        </script>
    '''.format(option)
    return html

@app.route('/accept', methods=['POST'])
def accept():
    apfile = open('order.txt', 'a')
    n = request.values['name']
    i = request.values['item']
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now + ' ' + n + ' ' + i[:1], file=apfile)
    apfile.close()

    html = '''
        <form action='/list'>
        {} orders {}
        <br/>
        <input type="submit" value="OK">
        </form>
    '''.format(n, i[2:]) 
    return html

@app.route('/tatol')
def tatol():
    data = {}
    infile = open('lunch.txt', "r")
    for line in infile:
        line = line.strip()
        t = line.split(':')
        data[t[0]] = t[1] + '($' + t[2] + ')'
    infile.close()

    tatolfile = open('order.txt', 'r')
    html = '''
        <table border>
            <tr>
                <th>Time</th><th>Name</th><th>Meal</th>
            </tr>
    '''
    price = 0

    for line in tatolfile:
        line = line.strip()
        temp = line.split(' ')
        meal = data.get(temp[3], 'error')
        price += int(meal.split('$')[1][:-1])
        html += '''
            <tr>
                <td>{}</td><td>{}</td><td>{}</td>
            </tr>
        '''.format(temp[0] + ' ' + temp[1], temp[2], meal)
    tatolfile.close()

    html += '''
            <tr>
                <td></td><td>Tatol</td><td>${}</td>
            </tr>
        </table>
        <form action='/list'>
        <input type="submit" value="Back">
        </form>
    '''.format(price)

    return html
