from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        html = '''<form method="POST">
        <textarea name="students" rows=4 cols=50></textarea>
        <input type=submit value='Submit'>'''
        return html
    else:
        dict={}
        submit = request.values['students'].split("\r\n")
        for line in submit:
            fruit, amount = line.split()
            if(fruit in dict):
                dict[fruit]+=int(amount)
            else:
                dict[fruit]=int(amount)
        
        html = '<l>\n'
        for i,j in dict.items():
            html +=f'<li>{i} {j}\n'
        html += '</l>\n'
        return html
