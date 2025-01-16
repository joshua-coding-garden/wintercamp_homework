from flask import Flask

app = Flask(__name__)

@app.route('/file1')
def f1():
    infile = open("static/poem01.txt", "r")
    html = infile.read()
    infile.close()
    return html

@app.route('/file2')
def f2():
    fn = "static/poem01.txt"
    infile = open(fn, "r")
    html = ''
    while True:
        line = infile.readline()
        if line == '':
            break
        html += line[:-1] + '<br>\n'
    infile.close()
    return html

@app.route('/file3')
def f3():
    infile = open('static/poem01.txt', "r")
    aList = infile.readlines()
    html = ''
    for line in aList:
        html += line[:-1] + '<br>\n'
    infile.close()
    return html

@app.route('/file4')
def f4():
    infile = open('static/poem01.txt', "r")
    html = ''
    for line in infile:
        html += line[:-1] + '<br>\n'
        infile.close()
    return html