#!pyenv/bin/python

## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: gifsound.py
## ABSTRACT: This file controls all the flask routes for gifsound
## AUTHORS: Erick Shaffer, Carsen Yates
## DATE: 11/14/2017

# TODO: Instead of putting all the data in the url for posts, maybe we can parse JSON?
# TODO: Create some internal API Key hash or use some other library for routes that use DB
# TODO: Create Shell Scripts to seed the database
# TODO: Update http methods to be correct.

from flask import Flask, render_template, jsonify, redirect, url_for
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


@app.route('/api/register/<user_name>/<email>/<password>/<int:role>/<api_key>',
           methods=['POST', 'PUT', 'GET'])
def register(user_name, email, password, role, api_key):
    response = create_user(user_name, email, password, role)


@app.route('/api/create/link/<name>/<user_id>/<path:full_link>/<path:gif_link>/<yt_id>/<api_key>',
           methods=['POST', 'PUT'])
def create_gif_sound(name, user_id, full_link, gif_link, yt_id, api_key):
    if user_id > 0 and not None:
        user = get_user_info(user_id, api_key)
    create_link(name, user_id, full_link, gif_link, yt_id)


@app.route('/api/user_info/<int:user_id>/<api_key>', methods=['POST', 'GET'])
def get_user_info(user_id, api_key):
    user = get_user(user_id)
    schema = UserSchema(many=True)
    result = schema.dumps(user)
    return result.data


@app.route('/api/user_info/<api_key>', methods=['POST', 'GET'])
def get_all_users_info(api_key):
    return get_all_users()


@app.route('/api/links/<api_key>', methods=['POST', 'GET'])
def get_links(api_key):
    links = get_all_links()
    schema = LinkSchema(many=True)
    result = schema.dumps(links)
    return result


@app.route('/smoke_test/<int:test>', methods=['POST', 'GET'])
def smoke_test(test):
    return 'hi'


@app.route('/api/create_tables/<api_key>', methods=['POST', 'PUT'])
def create_tables(api_key):
    create_user_table()
    create_link_table()

# For testing the view_combo route (below)
@app.route('/testview/')
def test_view_combo():
    return redirect(url_for('view_combo', gif_url='https://media4.giphy.com/avatars/100soft/WahNEDdlGjRZ.gif', yt_id='Hug0rfFC_L8'))

# Display this gif and this video together
@app.route('/view/<path:gif_url>/<yt_id>/')
def view_combo(gif_url, yt_id):
    showinfo = 1 # Enable Title and video controls
    rel = 0 # Uhh I don't know
    start = 0 # starting point of video
    return render_template('view.html', gif=gif_url, video=f'https://www.youtube.com/embed/{yt_id}?rel={rel}&amp;showinfo={showinfo}&amp;start={start}')


if __name__ == '__main__':
    app.run()
