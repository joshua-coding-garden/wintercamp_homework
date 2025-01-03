from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    count = 1
    html = '<table border>\n'
    for i in range(1,10):
        html += '<tr>'
        for j in range(1,10):
            if(count & 1):
                html += '<td style="background-color: yellow;">{} * {} = {}</td>'.format(i,j,i*j)
            else:
                html += "<td>{} * {} = {}</td>".format(i,j,i*j)
            count += 1
        html += '</tr>\n'
    html += '</table>\n'
    return html    
