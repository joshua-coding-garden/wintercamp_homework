from flask import Flask, request
import random
app = Flask(__name__)

@app.route('/random', methods=['GET', 'POST'])
def text():
    if request.method == "GET":
        html = '''
        <form method="POST">
            <textarea name="students" rows=8 cols=50 ></textarea><br>
            <br>Number of Sample:
            <input type="number" name="k" min="1">
            <input type="submit"> 
            <input type="Reset">
        </form>
        '''
        return html
    else:  # POST 
       
        students = request.values['students'].split("\r\n")
        k = int(request.values.get('k', 1))  
        if k > len(students):
            return "The number of people selected cannot exceed the total number of students, please go back and re-enter."

        selected_students = random.sample(students, k)
        html = '<ol>\n'
        for student in selected_students:
            html += f'<li>{student}</li>\n'
        html += '</ol>\n'
        return html
