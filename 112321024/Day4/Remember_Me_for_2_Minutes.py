from flask import Flask, url_for, request, make_response
import datetime
app = Flask(__name__)
@app.route('/')

def index():
    return '''
        <form action = "/setcookie" method = "POST">
        <p>Username: <input type = 'text' name = 'username'></p>
        <p>Password: <input type = 'text' name = 'password'></p>
        <p><input type = 'submit' value = 'Login'></p>
        </form>'''

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    now = datetime.datetime.utcnow()
    expire_time = now + datetime.timedelta(minutes=2)

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    html = f'Hello {username}'
    resp = make_response(html)
    resp.set_cookie(username,password,expires=expire_time)
    return resp
