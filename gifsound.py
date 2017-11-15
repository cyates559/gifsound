#!pyenv/bin/python

# AUTHORS: Erick Shaffer, Carsen Yates, Mimi Leon
# DATE: 11/14/2017
# PURPOSE: This file controls all the flask routes for gifsound


from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
