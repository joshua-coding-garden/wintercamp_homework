from flask import Flask
app = Flask(__name__)

@app.route('/file1')
def f1():
    fn = "poem.txt"
    infile = open(fn, "r")
    html = ''
    while True:
        line = infile.readline()
        if line == '': break
        html += line[:-1] + '<br>\n'
    infile.close()
    return html