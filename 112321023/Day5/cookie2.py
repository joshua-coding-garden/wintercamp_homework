from flask import Flask, make_response
import datetime

app = Flask(__name__)


@app.route('/response')
def resp():
    response = make_response('<h1>This document carries a cookie!</h1>')
    now = datetime.datetime.utcnow()
    user = 'jason'
    expire_time = now + datetime.timedelta(minutes=1)
    response.set_cookie('userID', user, expires=expire_time)
    return response