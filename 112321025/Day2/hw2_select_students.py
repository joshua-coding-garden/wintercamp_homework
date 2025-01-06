from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/sampling', methods=['GET', 'POST'])
def sampling():
    if request.method == "GET":
        html = '''<form method="POST">
            <textarea name="students" rows=10 cols=50></textarea>
            <br>Number of Samples:
            <select name="number">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
            </select>
            <button type="submit">Select</button>
            <button type="reset">Reset</button>
        </form>'''
        return html
    else:
        students = request.values['students'].split("\r\n")
        n = int(request.values['number'])
        if n > len(students):
            return '<h1>' + "{} exceeds the total number of students!".format(n) + '</h1>'
        else:
            result = random.sample(students, n)
            html = '<ol>\n'
            for line in result:
                html += '<li>' + line + '</li>\n' 
            html += '</ol>\n'
            return html 