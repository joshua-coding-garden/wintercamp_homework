from flask import Flask, url_for, request, make_response
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    name = request.cookies.get('userID', '')
    html = '''
        <form action = "/setcookie" method = "POST">
        <p><h3>Enter userID</h3></p>
        <p><input type = 'text' name = 'nm' value={}></p>
        <p><input type = 'submit' value = 'Login'></p>
        </form>
    '''.format(name)
    return html

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.values['nm']
    html = '''
        This page set the cookie. 
        Click <A HREF="{}">here</A> to see the coockie.
    '''.format(url_for('getcookie'))
    resp = make_response(html)
    t = datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
    resp.set_cookie('userID', user, expires=t)
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome ' + name + '</h1>'