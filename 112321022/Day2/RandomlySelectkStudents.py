from flask import Flask, request
import random
app = Flask(__name__)

@app.route('/random', methods=['GET', 'POST'])
def select():
    if request.method == "GET":
        html = '''
            <form method="POST">
            <textarea name="students" rows=7 cols=50></textarea>
            <br>Number of Sample:
            <select id="count" name="count"></select>
            <input type=submit><input type=reset>

            <script>
                const a = Array.from({ length: 7 }, (_, i) => 
                    `<option value="${i + 1}">${i + 1}</option>`
                );
                document.getElementById("count").innerHTML = a.join("");
            </script>
        '''
        return html
    else: # POST
        all = request.values['students'].split("\r\n")
        num = int(request.form['count'])
        students = random.sample(all, num)

        html = '<ol>\n'
        for i in students:
            html += '<li>{}</li>\n'.format(i)
        html += '</ol>\n'
        return html 