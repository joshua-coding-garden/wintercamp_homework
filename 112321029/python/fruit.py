from flask import Flask, request
import json
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    html = '''
    <form action='/upload' method='POST' enctype="multipart/form-data">
        Select a file to upload:
        <input type="file" name="file"><br>
        <input type="submit">
    </form>
    '''
    return html

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    if f.filename != '':
        filepath = os.path.join(app.static_folder, f.filename)
        f.save(filepath)
        return f'''File <a href="static/{f.filename}">{f.filename}</a> uploaded successfully.
                <form action="/accumulate" method="POST">
                <input type="hidden" name="file" value="{f.filename}">
                <input type="submit" value="Accumulate Quantities"></form>'''
    else:
        return 'Please select a file.'

@app.route('/accumulate', methods=['POST'])
def accumulate():
    filename = request.form.get('file')
    filepath = os.path.join(app.static_folder, filename) 
    with open(filepath, "r") as infile:
        temp = json.load(infile)
    result = {}
    for item in temp:
        fruit = item.get("fruit")
        quantity = item.get("quantity", 0)
        if fruit in result:
            result[fruit] += quantity
        else:
            result[fruit] = quantity
    html = '<ul>'
    for fruit, quantity in result.items():
        html += f'<li>{fruit} {quantity}</li>'
    html += '</ul>'
    os.remove(filepath)
    return html
