from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi():
    if request.method == 'GET':
        return render_template('bmi_form.html')
    else:   # POST
        h = int( request.values['HEIGHT'] )
        w = int( request.values['WEIGHT'] )
        bmi = float("{:5.2f}".format(w / (h/100)**2))
    return render_template('bmi.html', height=h, weight=w, bmi=bmi)