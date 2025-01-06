from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    html = '''
        <link rel="shortcut icon" href="/static/favicon.ico">
        <h1>Hello World</h1>
    '''
    return html