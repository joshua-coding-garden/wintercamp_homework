from flask import Flask
app = Flask(__name__)

@app.route('/')
def f1():
    html = '''
    <table border="1" style="border-collapse: collapse;">
        <tr>
            <td>Blue achieve</td>
            <td><img src="/static/122098390_p0_master1200.jpg" width="800" height="auto"></td>
        </tr>
        <tr>
            <td>Make in abyss</td>
            <td><img src="/static/faputan.png" width="800" height="auto"></td>
        </tr>
    </table>
    '''
    return html
