from flask import Flask, request
app = Flask(__name__)

@app.route('/form')
def form():
    html = """<form method='POST' action='/bmi'>
    <input type=text name=height><br>
    <input type=text name=weight><br>
    <input type=submit>"""
    return html

@app.route('/bmi', methods=['POST'])
def bmi():
    h = int( request.values['height'] )
    w = int( request.values['weight'] )
    bmi = w / (h/100)**2
    html = '''Height: {}<br>
    Weight: {}<br>
    BMI: {:5.2f}'''.format(h, w, bmi)
    return html