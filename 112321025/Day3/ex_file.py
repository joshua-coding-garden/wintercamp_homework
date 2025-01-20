from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    import os
    import glob

    aList = glob.glob("*")  # 獲取當前目錄中的所有項目
    html = "<OL>\n"          # HTML 清單標籤開始
    for f in aList:
        if os.path.isdir(f):  # 如果是資料夾
            html += "<LI> [DIR] " + f + "</LI>\n"
        elif os.path.isfile(f):  # 如果是檔案
            html += "<LI><A HREF='/openfile/{}'>{}</A></LI>\n".format(f, f)
    html += "</OL>\n"  # HTML 清單標籤結束
    return html

@app.route('/openfile/<fn>')
def openfile(fn):
    import html
    f = open(fn, "r")  # 開啟檔案
    s = f.read()       # 讀取檔案內容
    f.close()          # 關閉檔案
    return "<PRE>" + html.escape(s) + "</PRE>"