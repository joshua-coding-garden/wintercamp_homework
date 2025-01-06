from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
    html = '''<table border>
        <tr><th>ura</th><th><IMG SRC=/static/ura.png></th><td>
        <tr><th>yaha</th><th><IMG SRC=/static/rabbit.png></th><td>
        '''
    return html
