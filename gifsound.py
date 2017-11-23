#!pyenv/bin/python

# AUTHORS: Erick Shaffer, Carsen Yates
# DATE: 11/14/2017
# PURPOSE: This file controls all the flask routes for gifsound

# TODO: Instead of putting all the data in the url for posts, maybe we can parse JSON?
# TODO: Create Shell Scripts to seed the database
# TODO: Update http methods to be correct.
from flask import Flask, render_template, jsonify, redirect, url_for, session, json
from config import settings
import os
from Controller.link_controller import *
from Controller.user_controller import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required

app = Flask(__name__)
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/featured')
def featured():
    return render_template('featured.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return 'hi'


# following guide on
# https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager.user_loader
# Might not need with flask_login
# TODO: This needs to return the user object
@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)


@app.route('/login/<username>/<password>', methods=['GET', 'POST'])
def login(username, password):
    data = {}
    code = 0
    user = get_user_by_username(username)
    if bcrypt.check_password_hash(user.password, password):
        login_user(user)
        data['login'] = True
        data['name'] = username
        code = 200
    else:
        data['login'] = False
        code = 401

    return app.response_class(
        response=json.dumps(data),
        status=code,
        mimetype='application/json'
    )


@app.route('/api/logout', methods=['POST'])
def logout():
    data = {}
    session.pop('user')
    data['logged_out'] = True
    code = 200
    return app.response_class(
        response=json.dumps(data),
        status=code,
        mimetype='application/json'
    )


@app.route('/register/<user_name>/<email>/<password>',
           methods=['POST', 'PUT'])
def register(user_name, email, password):
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    response = create_user(app, user_name, email, pw_hash, 1)
    return response


@app.route('/api/create/link/<name>/<int:user_id>/<path:full_link>/<path:gif_link>/<yt_id>/<api_key>',
           methods=['POST', 'PUT'])
def create_gif_sound(name, user_id, full_link, gif_link, yt_id, api_key):
    if user_id > 0 and not None:
        user = get_user_info(user_id, api_key)
    create_link(name, user_id, full_link, gif_link, yt_id)


# This route will be used for the dashboard page.
# Before returning any data we want to make sure the user is logged in
# and the user id begin requested is the current user session.
# e.g We don't want anyone to hit this endpoint and get user data.
@app.route('/api/user_info/<int:user_id>/<api_key>', methods=['POST', 'GET'])
def get_user_info(user_id, api_key):
    user = get_user(user_id)
    schema = UserSchema(many=True)
    result = schema.dumps(user)
    return result.data


# this route seems insecure. Might want to remove before production
@app.route('/api/user_info', methods=['POST', 'GET'])
def get_all_users_info(api_key):
    return get_all_users()


@app.route('/api/links', methods=['POST', 'GET'])
def get_links(api_key):
    links = get_all_links()
    schema = LinkSchema(many=True)
    result = schema.dumps(links)
    return result


@app.route('/smoke_test/<int:test>', methods=['POST', 'GET'])
def smoke_test(test):
    return 'hi'


# This route is for debugging, will be removed in productions
@app.route('/api/create_tables/<api_key>', methods=['POST', 'PUT'])
def create_tables(api_key):
    create_user_table()
    create_link_table()
    data = {'status': 'success'}
    code = 200
    return app.response_class(
        response=json.dumps(data),
        status=code,
        mimetype='application/json'
    )


@app.route('/testview/')
def test_view_combo():
    return redirect(
        url_for('view_combo', gif_url='https://media4.giphy.com/avatars/100soft/WahNEDdlGjRZ.gif', yt_id='Hug0rfFC_L8'))


@app.route('/view/<path:gif_url>/<yt_id>/')
def view_combo(gif_url, yt_id):
    showinfo = 1  # Enable Title and video controls
    rel = 0  # Uhh I don't know
    start = 0  # starting point of video
    return render_template('view.html', gif=gif_url,
                           video=f'https://www.youtube.com/embed/{yt_id}?rel={rel}&amp;showinfo={showinfo}&amp;start={start}')


if __name__ == '__main__':
    app.run(debug=settings['development']['other']['debug'])
