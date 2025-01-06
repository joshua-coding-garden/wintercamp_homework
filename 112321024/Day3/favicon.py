from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def display():
    html = '''
        <link rel="shortcut icon" href="/static/Logo_KGHS.ico">
        <br>Welcome KGHS</br>
        <br>Nice to meet you!!</br>'''
    return html
