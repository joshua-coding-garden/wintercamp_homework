from flask import Flask, make_response

app = Flask(__name__)

@app.route('/response')
def resp():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response