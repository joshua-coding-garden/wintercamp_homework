from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <form action="/whatday" method="GET">
        <input type="date" name="birthday" required>
        <input type="submit" value="Submit">
    </form>
    '''
    return html

@app.route('/whatday')
def whatday():
    birthday_str = request.args.get('birthday')
    birthday_date = datetime.strptime(birthday_str, '%Y-%m-%d')
    weekday_number = birthday_date.isoweekday()
    weekdays = {
        1: "星期一",
        2: "星期二",
        3: "星期三",
        4: "星期四",
        5: "星期五",
        6: "星期六",
        7: "星期日"
        }
    weekday_name = weekdays[weekday_number]
    return f"{birthday_str} is {weekday_name}"
