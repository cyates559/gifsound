#!pyenv/bin/python

# AUTHORS: Erick Shaffer, Carsen Yates
# DATE: 11/14/2017
# PURPOSE: This file controls all the flask routes for gifsound

# TODO: Instead of putting all the data in the url for posts, maybe we can parse JSON?
# TODO: Create some internal API Key hash or use some other library for routes that use DB
# TODO: Create Shell Scripts to seed the database

from flask import Flask, render_template, jsonify
from Controller.link_controller import *
from Controller.user_controller import *
from marshmallow import pprint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/featured')
def featured():
    return render_template('featured.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/api/register/<user_name>/<email>/<password>/<int:role>/<api_key>',
           methods=['POST', 'PUT', 'GET'])
def register(user_name, email, password, role, api_key):
    response = create_user(user_name, email, password, role)


@app.route('/api/create/link/<name>/<user_id>/<full_link>/<gif_link>/<yt_link>/<api_key>',
           methods=['POST', 'PUT'])
def create_gif_sound(name, user_id, full_link, gif_link, yt_link, api_key):
    create_link(name, user_id, full_link, gif_link, yt_link)


@app.route('/api/user_info/<int:user_id>/<api_key>', methods=['POST', 'GET'])
def get_user_info(user_id, api_key):
    user = get_user(user_id)
    schema = UserSchema()
    result = schema.dumps(user[0])
    return result


@app.route('/api/user_info/<api_key>', methods=['POST', 'GET'])
def get_all_users_info(api_key):
    return get_all_users()


@app.route('/api/links/<api_key>', methods=['POST', 'GET'])
def get_links(api_key):
    return get_all_links()


@app.route('/smoke_test/<int:test>', methods=['POST', 'GET'])
def smoke_test(test):
    return 'hi'


@app.route('/api/create_tables/<api_key>', methods=['GET', 'POST', 'PUT'])
def create_tables(api_key):
    create_user_table()
    create_link_table()


if __name__ == '__main__':
    app.run()
