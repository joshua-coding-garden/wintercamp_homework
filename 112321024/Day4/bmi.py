from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi():
    if request.method == 'GET':
        html = """<form method='POST'>
        <input type=text name=height><br>
        <input type=text name=weight><br>
        <input type=submit>"""
        return html
    else: # POST
        h = int( request.values['height'] )
        w = int( request.values['weight'] )
        bmi = float("{:5.2f}".format(w / (h/100)**2))
        return render_template('bmi.html', height=h, weight=w, bmi=bmi)
