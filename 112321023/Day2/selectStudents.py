from flask import Flask, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/sample', methods=['GET', 'POST'])
def text():
    if request.method == "GET":
        html = '''<form method="POST">
        <textarea id="students" name="students" rows=4 cols=50></textarea>
        <br>Number of Samples: <select id="num" name="num"></select>
        <input type=submit> <input type=reset>

        <script>
            document.getElementById("students").addEventListener("input", function () {
                select = document.getElementById("num");
                let arr = this.value.trim().split("\\n");
                
                select.innerHTML = ''

                for(let i = 1; i <= arr.length; i++){
                    option = document.createElement('option');
                    option.value = i;
                    option.innerHTML = i;
                    select.appendChild(option);
                }
            });
        </script>
        '''
        return html
    else: # POST
        students = request.values['students'].strip().split("\r\n")
        num = int(request.values['num'])

        sample = random.sample(students, num)

        html = '<ol>\n'
        for line in sample:
            html += '<li>' + line + '\n'
        html += '</ol>\n'
        return html