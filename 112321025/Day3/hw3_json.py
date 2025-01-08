from flask import Flask, request
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return '''<form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file" accept=".json">
        <input type="submit">
        </form>'''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_path = 'uploaded.json'
    file.save(file_path)
    f = open(file_path, "r")
    data = json.load(f)
    f.close()
    
    count = {}
    for entry in data:
        fruit = entry['fruit']
        quantity = entry['quantity']
        if fruit in count:
            count[fruit] += quantity
        else:
            count[fruit] = quantity
            
    os.remove(file_path)
    html = '<ul>'
    for fruit, quantity in count.items():
        html += '<li>{} {}</li>'.format(fruit, quantity)
    html += '</ul>'
    return html
