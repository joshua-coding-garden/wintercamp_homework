from flask import Flask
import json
import os

app = Flask(__name__)

@app.route('/')
def fruit():
    fn = "static/fruit.json"
    f = open(fn, 'r')

    total_dict = {}

    dictList = json.load(f)
    for item in dictList:
        if(item['fruit'] not in total_dict.keys()):
            total_dict[item['fruit']] = int(item['quantity'])
        else:
            total_dict[item['fruit']] += int(item['quantity'])
    
    html = '<ul>'
    for key in total_dict:
        html += f'<li>{key} {total_dict[key]}</li>'
    html += '</ul>'

    f.close()
    os.remove(fn)

    return html