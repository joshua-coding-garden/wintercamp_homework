from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    html = '''<form action="/whatday">
        <input type=date id="birthday" name=birthday required>
        <input type=submit>
    </form>'''
    return html

@app.route('/whatday')
def what_day():
    birthday_str = request.values['birthday']
    date = datetime.strptime(birthday_str, '%Y-%m-%d')
    weekday = date.isoweekday()
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekday_chinese = weekdays[weekday - 1]
    return "{} is {}".format(birthday_str, weekday_chinese)