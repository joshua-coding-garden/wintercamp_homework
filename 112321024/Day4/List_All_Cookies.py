from flask import Flask, url_for, request, make_response
app = Flask(__name__)
@app.route('/')

def index():
    html = '''
        <form action = "/setcookie" method = "POST">
        <p>Key: <input type='text' name='key'></p>
        <p>Value: <input type='text' name='value'></p>
        <p><input type = 'submit' value = 'Login'></p>
        </form>'''
    return html

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
    html = '''This page set the cookie.  Click <A HREF="{}">here</A> to
        see the coockie.'''.format(url_for('getcookie'))
    resp = make_response(html)
    resp.set_cookie(key, value)
    return resp

@app.route('/getcookie')
def getcookie():
    cookies = request.cookies
    cookies_list = '<ul>'
    for key, value in cookies.items():
        cookies_list += f'<li>{key}: {value}</li>'
    cookies_list += '</ul>'
    return f'<h1>All cookies:</h1>{cookies_list}'