from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    html = '''<form action=/whatday>
    <input type=date name=birthday>
    <input type=submit>
    </form>'''
    return html

@app.route('/whatday')
def bmi():
    bir = request.values['birthday']
    temp = datetime.strptime(bir, "%Y-%m-%d")
    w = temp.isoweekday()
    wname = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    
    
    html = f'''{bir} is {wname[w - 1]}'''
    return html
