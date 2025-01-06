from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    html = '''
        <link rel="shortcut icon" href="/static/favicon.ico">
        <b>嗚啦呀哈 呀哈嗚啦~</b>
     '''
    return html
