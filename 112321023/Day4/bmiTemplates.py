from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi():
    if request.method == 'GET':
        return render_template('bmi_form.html')
    else: # POST
        h = int( request.values['height'] )
        w = int( request.values['weight'] )
        bmi = "{:5.2f}".format(w / (h/100)**2)
        float(bmi)
        return render_template('bmi.html', height=h, weight=w, bmi=float(bmi))