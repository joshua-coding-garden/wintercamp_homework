from flask import Flask, request
app = Flask(__name__)
@app.route('/form')
def form():
    html = """<form action='/bmi'>
    <input type=text name=height><br>
    <input type=text name=weight><br>
    <input type=submit>"""
    return html

@app.route('/bmi')
def bmi():
    h = int( request.values['height'] ) #request.values is dictionary
    w = int( request.values['weight'] )
    bmi = w / (h/100)**2
    html = '''Height: {}<br>
    Weight: {}<br>
    BMI: {:5.2f}'''.format(h, w, bmi)
    return html