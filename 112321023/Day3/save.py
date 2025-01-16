from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <link rel="shortcut icon" href="/static/favicon.ico">
    <form action='/upload' method='POST'
    enctype = "multipart/form-data"> Select a file to upload:
    <input type="file" name="file"><br> <input type="submit">
    </form>'''
    return html

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    if f.filename != '':
        f.save('static/'+f.filename)
        return 'File <a href="static/{}">{}</a> uploaded successfully'.format(f.filename, f.filename)
    else:
        return 'Please select a file.'