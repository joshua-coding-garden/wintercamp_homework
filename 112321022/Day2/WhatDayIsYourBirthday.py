from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/whatday', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        html = '''
            <form action=/whatday method="POST">
            <input type=date name=birthday>
            <input type=submit>
            </form>
        '''
        return html
    else:
        temp = ['一', '二', '三', '四', '五', '六', '日']
        str = request.form.get('birthday')
        birthday = datetime.strptime(str, '%Y-%m-%d')
        num = birthday.isoweekday()
        day = temp[num-1]
        html = "{} is 星期{}".format(str, day)
        return html