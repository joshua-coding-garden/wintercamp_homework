from flask import Flask,request
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def read_fruit():
    if request.method == "GET":
        html = '''<form method = "POST">
        <textarea name = "fruits" rows = 10 cols = 50></textarea>
        <input type = submit value = "Submit">'''
        return html
    else:
        fruit_totals = {}
        fruit_data = request.form['fruits'].split('\n')
        for line in fruit_data:
            parts = line.split()
            fruit = parts[0]
            amount = int(parts[1])

            if fruit in fruit_totals:
                fruit_totals[fruit] += amount;
            else:
                fruit_totals[fruit] = amount;
    
        result = '<ul>'
        for fruit, amount in fruit_totals.items():
            result += f'<li>{fruit} {amount}</li>'
        result += '</ul>'
        return result