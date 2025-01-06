from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
    html = '''<table border>
        <tr><th>dog</th><th><IMG SRC=/static/1000004801.jpg></th><td>'''
    return html