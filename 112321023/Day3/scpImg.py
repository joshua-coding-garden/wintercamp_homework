from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    html = '<table border="1">'
    html += '<tr>'
    html += '<td>' + 'Python' + '</td>'
    html += '<td>' + '<IMG SRC=/static/python.jpg width=200>' + '</td>'
    html += '</tr>'
    html += '</table>'
    return html