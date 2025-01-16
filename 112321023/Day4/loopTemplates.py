from flask import Flask, render_template

app = Flask(__name__)

@app.route('/loop')
def loop():
    students = ['Alice', 'Bob', 'Carol', 'Daniel', 'Emily', 'Fanny']
    return render_template('line.html', lines=students)