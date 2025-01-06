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
def whatday():
    birthday_str = request.values['birthday']
    birthday = datetime.strptime(birthday_str,'%Y-%m-%d')

    weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    weekday = weekdays[birthday.isoweekday() - 1]

    return f"{birthday_str} is {weekday}"