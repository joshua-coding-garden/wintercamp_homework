from flask import Flask
app = Flask(__name__)

@app.route('/')
def show():
    return ''' 
    <html>
    <head>
        <title>Exercise</title>
    </head>
    <body>
        <h1>Your Own Image Files</h1>
        <table border="1">
        <tr><td>Whisper of the Heart 001</td><td><img src="/static/mimi001.jpg" width="300"></td></tr>
        <tr><td>Whisper of the Heart 037</td><td><img src="/static/mimi037.jpg" width="300"></td></tr>
        </table>
    </body>
    </html>'''