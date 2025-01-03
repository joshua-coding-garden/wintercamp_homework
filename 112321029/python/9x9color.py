from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    html = '<table border="1">\n'
    for i in range(1, 10):
        html += '<tr>\n'
        for j in range(1, 10):
            if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                html += '<td>{} * {} = {}</td>\n'.format(i, j, i*j)
            else:
                html += '<td style="background-color: yellow;">{} * {} = {}</td>\n'.format(i, j, i*j)
        html += '</tr>\n'
    html += '</table>\n'
    return html
