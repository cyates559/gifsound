#!pyenv/bin/python

# AUTHORS: Erick Shaffer, Carsen Yates
# DATE: 11/14/2017
# PURPOSE: This file controls all the flask routes for gifsound
import os
from flask_environments import Environments
from flask import Flask, render_template, url_for
from controller import *

app = Flask(__name__)
env = Environments(app)
env.from_yaml(os.path.join(os.getcwd(), 'myapp', 'config.yml'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/featured')
def featured():
    return render_template('featured.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register')
def register():
    return 1


@app.route('/api/create/link/<gif_link>/<yt_link>')
def create_gif_sound():
    return 1


@app.route('api/user_info/<id>/<api_key>')
def get_user_info(id, api_key):
    getUser(id)
    return render_template('about.html')


@app.route('api/user_info/<api_key>')
def get_all_user_info(api_key):
    getUser(id)
    return render_template('about.html')


@app.route('api/links/<api_key>')
def get_links(api_key):
    return 1


if __name__ == '__main__':
    app.run()
