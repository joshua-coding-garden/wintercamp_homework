from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/text',methods = ['GET','POST'])
def text():
    if request.method == "GET":
        html = '''<form method = "POST">
        <textarea name = "students" rows = 10 cols = 50></textarea>
        <br>
        Number of Samples:
        <select name = "numbers" id="numbers">
            <option value = "1">1</option>
            <option value = "2">2</option>
            <option value = "3">3</option>
            <option value = "4">4</option>
            <option value = "5">5</option>
            <option value = "6">6</option>
            <option value = "7">7</option>
            <option value = "8">8</option>
            <option value = "9">9</option>
            <option value = "10">10</option>
        </select>
        <input type = submit value = "Select">
        <input type = reset value = "Reset" onclick = "resetoption()">

        <script>
            function resetoption(){
                const select = document.getElementById('nmubers');
                select.innerHTML = '<option value="1">1</option>';
                const table = document.getElementById('students');
                table.innerHTML = '';
            }
        </script>'''
        return html
    else:
        student_data = request.values['students'].split("\r\n")
        num_sample = int(request.values['numbers'])
        if len(student_data) < num_sample:
            return "Not enough students<a href='/text'>Go Back</a>"

        selected_students = random.sample(student_data, num_sample)
        result_html = '''
            <ol>{}</ol>
            <a href="/text">Go Back</a>
        '''.format(''.join(f'<li>{student}</li>' for student in selected_students))
        return result_html