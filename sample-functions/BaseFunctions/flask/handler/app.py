#!/usr/bin/python
from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/hello')
def hello():
    if "name" in request.args:
        return render_template('hello.html', name=request.args["name"])
    else:
        return render_template('hello.html', name="stranger")


@app.route('/test')
def test():
    if "name" in request.args:
        return render_template('hello.html', name=request.args["name"])
    else:
        return render_template('hello.html', name="testy McTest Face")

if __name__ == '__main__':
    app.run(debug=True)
