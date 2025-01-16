from flask import Flask, url_for, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <form action = "/setcookie" method = "POST">
    <p><h3>Enter userID</h3></p>
    <p><input type = 'text' name = 'nm'></p>
    <p><input type = 'submit' value = 'Login'></p>
    </form>'''
    return html

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.values['nm']
        html = '''This page set the cookie. Click <A HREF="{}">here</A> to
        see the coockie.'''.format(url_for('getcookie'))
        resp = make_response(html)
        resp.set_cookie(user)
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies #request.cookies is a dict
    html = '<h1>'
    for k in name: #for key in dict
        html += f'welcome {k} <br>'
    html += '</h1>'
    return html