from flask import Flask, request
import random  
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        html='''<form method="POST">
        <textarea name="students" rows=4 cols=50></textarea><br>
        Number of Samples:
        <select name="people">
            <option value=1>1</option>
            <option value=2>2</option>
            <option value=3>3</option>
            <option value=4>4</option>
            <option value=5>5</option>
            <option value=6>6</option>
            <option value=7>7</option>
        </select>
        <input type=submit>
        <input type=reset>
        </form>'''
        return html
    else: 
        students = request.values['students'].split("\r\n")
        n=int(request.values['people']) 
        chose=random.sample(students, n)
        html = '<ol>\n'
        for line in chose:
            html += '<li>' + line + '\n'
        html += '</ol>\n'
        return html
