from flask import Flask, request
import httpagentparser
app = Flask(__name__)
@app.route('/')
def index():
    # ua = request.user_agent.string
    ua = request.headers.get('User-Agent')
    html = '''User-Agent: {}'''.format( ua )
    html += '<br>{}'.format( httpagentparser.simple_detect(ua) )
    html += '<br>{}'.format( httpagentparser.detect(ua) )
    os, browser = httpagentparser.simple_detect(ua)
    html += '<br>Browse with <font color=green>{}</font> on ' \
    '<font color=green>{}</font>.'.format(browser, os)
    return html