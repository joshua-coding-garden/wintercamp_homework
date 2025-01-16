from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def fruit():
    html = '''
    <form method="POST" action='/amount'>
    <textarea name="fruit" rows=30 cols=40></textarea>
    <br><input type=submit> <input type=reset>
    '''
    return html

@app.route('/amount', methods=['POST'])
def amount():
    v = request.values['fruit']
    lines = v.rstrip().split('\n')
    fruit_dict = {}

    for line in lines:
        key, value = line.split(' ')
        if(key not in fruit_dict.keys()):
            fruit_dict[key] = int(value)
        else:
            fruit_dict[key] += int(value)
    
    html = '<ul>'
    for key in fruit_dict:
        html += f'<li>{key} {fruit_dict[key]}</li>'
    html += '<ul>'

    return html