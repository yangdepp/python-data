# coding:utf-8

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add():
    a = request.form.get("num1")
    b = request.form.get("num2")
    a = int(a)
    b = int(b)
    return '{"status":0,"result":%d}' % (a * b)


app.run()
