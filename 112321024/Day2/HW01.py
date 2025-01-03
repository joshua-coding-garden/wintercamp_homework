from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    html = '<table border>\n'
    for i in range(1, 10):
        html += '<tr>'
        for j in range(1, 10):
            if(i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
                html += "<td>{} * {} = {}</td>".format(i, j, i*j)
            else:
                html += '<td style="background-color: magenta;">{} * {} = {}</td>'.format(i, j, i*j)
        html += '</tr>\n'
    html += '</table>\n'
    return html