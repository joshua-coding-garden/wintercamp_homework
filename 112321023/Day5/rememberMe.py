from flask import Flask, request, make_response, redirect
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return f"<h1>Hello {username}!</h1>"
    else:
        html = '''
        <form action="/setcookie" method="POST">
        <span>Username</span>
        <input type='text' name='username'><br>
        <span>Password</span>
        <input type='password' name='password'><br>
        <input type='submit' value='Login'>
        </form>'''
        return html

@app.route('/setcookie', methods=['POST'])
def set_cookie():
    dictionary = {'jason':'123'}
    username = request.values['username']
    password = request.values['password']

    
    if(username in dictionary and password == dictionary[username]):
        response = make_response(redirect('/')) #重新導向
        expire_time = datetime.utcnow() + timedelta(minutes=2)
        response.set_cookie('username', username, expires=expire_time)
        return response
    else:
        return "Username or Password error."