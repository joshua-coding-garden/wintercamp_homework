from flask import Flask, request
import json
import os
app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <form action='/upload' method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="upload">
    </form>
    '''
    return html

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    file = 'uploaded.json'
    f.save(file)

    infile = open(file, 'r')
    s = json.load(infile)
    infile.close()

    data = {}
    for line in s:
        fruit = line['fruit']
        quantity = line['quantity']
        if fruit in data:
            data[fruit] += quantity
        else:
            data[fruit] = quantity
    os.remove(file)

    html = '<ul>'

    for fruit, quantity in data.items():
        html += '<li>{} {}</li>'.format(fruit, quantity)
    html += '</ul>'

    return html