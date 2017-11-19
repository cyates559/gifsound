#!pyenv/bin/python

# AUTHORS: Erick Shaffer, Carsen Yates
# DATE: 11/14/2017
# PURPOSE: This file controls all the flask routes for gifsound
from flask import Flask, render_template
import json
from config import settings
from Controller.link_controller import *
from Controller.user_controller import *

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


@app.route('/register/<user_name>/<email>/<password>/<int:role>/<api_key>',
           methods=['POST', 'PUT'])
def register(user_name, email, password, role, api_key):
    response = create_user(user_name, email, password, role)
    if response is False:
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/api/create/link/<name>/<user_id>/<full_link>/<gif_link>/<yt_link>/<api_key>',
           methods=['POST', 'PUT'])
def create_gif_sound(name, user_id, full_link, gif_link, yt_link, api_key):
    create_link(name, user_id, full_link, gif_link, yt_link)


@app.route('/api/user_info/<int:user_id>/<api_key>', methods=['GET'])
def get_user_info(user_id, api_key):
    user = get_user(user_id)
    d = {}
    for u in user:
        print(u)
    return 'hi'


@app.route('/api/user_info/<api_key>', methods=['POST'])
def get_all_users_info(api_key):
    return get_all_users()


@app.route('/api/links/<api_key>', methods=['POST'])
def get_links(api_key):
    return get_all_links()


@app.route('/smoke_test', methods=['POST', 'GET'])
def smoke_test():
    return json.dumps({'success': True, 'name': 'test',  'test': 'hello'}), 200, {'ContentType': 'application/json'}


@app.route('/api/create_tables/<api_key>', methods=['GET, POST'])
def create_tables():
    create_user_table()
    create_link_table()
    return 'hi'

if __name__ == '__main__':
    app.run()

