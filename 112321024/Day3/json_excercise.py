from flask import Flask,request
import json
import os

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def upload_json():
    if request.method == 'GET':
        html = '''<br>Upload a JSON file</br>
            <form method = 'POST' enctype="multipart/form-data">
                <input type="file" name="file" accept=".json">
                <input type="submit" value="Upload">
            </form>'''
        return html
    else:
        file = request.files['file']
        temp_file = 'upload.json'
        file.save(temp_file)

        with open(temp_file, 'r') as f:
            data = json.load(f)

        fruit_totals = {}
        for item in data:
            fruit = item['fruit']
            amount = item['quantity']
            fruit_totals[fruit] = fruit_totals.get(fruit,0) + amount
        
        os.remove(temp_file)

        html = '<ul>'
        for fruit,total in fruit_totals.items():
            html += f"<li>{fruit} {total}</li>"
        html += '</ul>'
        return html
