from flask import render_template

from . import app

@app.route('/')
def hello_world():
    hello = "Hello, World!"
    return render_template('home.html', content=hello)
