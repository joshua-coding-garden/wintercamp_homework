from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    html = '''<form method='POST' action=/whatday> 
    <input type=date name=birthday> 
    <input type=submit>
    </form>'''
    return html

@app.route('/whatday', methods=['POST'])
def weather():
    weekdays = ['一', '二', '三', '四', '五', '六', '日']
    v = request.values['birthday']
    
    birthday = datetime.strptime(v, '%Y-%m-%d')
    w = birthday.isoweekday()

    # year, month, day = v.split('-')
    # year = int(year)
    # month = int(month)
    # day = int(day)
    # w = datetime(year, month, day).isoweekday()
    return f"{v} 星期{weekdays[w - 1]}"