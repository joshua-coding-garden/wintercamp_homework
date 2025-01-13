from flask import Flask, url_for, request, make_response
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    user_id = request.cookies.get('userID')
    html = f'''
    <form action = "/setcookie" method = "POST">
        <p><h3>Enter userID</h3></p>
        <p><input type = 'text' name = 'nm' value = '{user_id if user_id else ""}'></p>
        <p><input type = 'submit' value = 'Login'></p>
    </form>'''
    return html

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.values['nm']
    now = datetime.datetime.utcnow()
    expire_time = now + datetime.timedelta(minutes=3)
    html = '''This page sets the cookie. Click <A HREF="{}">here</A> to see the cookie.'''.format(url_for('getcookie'))
    resp = make_response(html)
    resp.set_cookie('userID', user, expires=expire_time)
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    if name:
        return f'<h1>Welcome {name}!</h1>'
    else:
        return '<h1>No userID found in cookies!</h1>'