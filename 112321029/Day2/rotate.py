from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    html = """<img id='photo' />
<script>
const urls = ['http://poet.ncnu.org/Photo/starwar1.jpg',
'http://poet.ncnu.org/Photo/starwar2.jpg',
'http://poet.ncnu.org/Photo/starwar3.jpg']
let n = 0;
function rotate() {
  n = (n + 1 ) % urls.length;
  document.getElementById('photo').src = urls[n];
}
setInterval(rotate, 3000);
</script>
"""
    return html
