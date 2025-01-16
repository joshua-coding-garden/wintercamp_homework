from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    import os
    import glob
    aList = glob.glob("*")
    html = "<OL>\n"
    for f in aList:
        if os.path.isdir(f):
            html += "<LI> [DIR] " + f + "</LI>\n"
        elif os.path.isfile(f):
            html += "<LI><A HREF='/openfile/{}'>{}</A></LI>\n".format(f, f)
    html += "</OL>\n"
    return html

@app.route('/openfile/<fn>')
def openfile(fn):
    import html
    f = open(fn, "r")
    s = f.read()
    f.close()
    return '<pre>' + html.escape(s) + '</pre>'