from flask import Flask
app = Flask(__name__)

@app.route('/weekday/<year>/<month>/<day>')
def weekday(year, month, day):
    return "{:04}-{:02}-{:02}".format(int(year), int(month), int(day))

# @app.route('/weekday/<int:year>/<int:month>/<int:day>')
# def weekday(year, month, day):
#     return "{:04}-{:02}-{:02}".format(year, month, day)