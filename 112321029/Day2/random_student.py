from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/text', methods=['GET', 'POST'])
def text():
    if request.method == "GET":
        html = '''<form method="POST">
        <textarea name="students" rows=4 cols=50></textarea>
        <br>Number of Sample:
        <select name="num">
        '''
        for i in range(1, 11):
            html += f'<option value="{i}">{i}</option>'
        html += '''</select>
        <input type="submit"> <input type="reset">
        </form>'''
        return html
    else:
        students = request.values['students'].split("\r\n")
        num = int(request.values['num'])
        
        if len(students) < num:
            num = len(students)
            
        sampled_students = random.sample(students, num)
        html = '<ol>\n'
        for student in sampled_students:
            html += f'<li>{student}</li>\n'
        html += '</ol>\n'
        return html

