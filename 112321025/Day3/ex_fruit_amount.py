from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def count():
    if request.method == "GET":
        return '''
        <html>
        <head>
            <title>Exercise</title>
        </head>
        <body>
            <h1>Fruit Amount</h1>
            <form method="POST">
            <textarea name="fruit" rows="10" cols="20"></textarea>
            <input type="submit">
            </form>
        </body>
        </html>'''
    else:
        count = {}
        aList = request.values['fruit'].split('\r\n')
        for item in aList:
            fruit, amount = item.split()
            amount = int(amount)
            if fruit in count:
                count[fruit] += amount
            else:
                count[fruit] = amount
        html = '<ul>'
        for fruit, quantity in count.items():
            html += '<li>{} {}</li>'.format(fruit, quantity)
        html += '</ul>'
        return html