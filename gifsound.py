#!pyenv/bin/python

## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: gifsound.py
## ABSTRACT: This file controls all the flask routes for gifsound
## AUTHORS: Erick Shaffer, Carsen Yates
## DATE: 11/14/2017

#Github: https://github.com/Fatburger3/gifsound


from flask import Flask, render_template, redirect, url_for, json
import os
from Controller.link_controller import *
from Controller.user_controller import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

import youtube
import urllib.parse

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
	return render_template('dashboard.html')


@login_manager.user_loader
def load_user(user_id):
	return get_user(user_id)


@app.route('/login/<username>/<password>', methods=['GET', 'POST'])
def login(username, password):
	data = {}
	code = 0
	user = get_user_by_username(username)
	if user and bcrypt.check_password_hash(user.password, password):
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


@app.route('/logout', methods=['POST', 'GET'])
def logout():
	data = {}
	logout_user()
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
	user = get_user_by_username(user_name)
	data = {}
	code = 0
	if user is not None:
		data = {"signup": "Username is taken"}
		code = 400
		data["username"] = "None"
	else:
		code = 200
		user = create_user(app, user_name, email, pw_hash, 1)
		return user
	return app.response_class(
		response=json.dumps(data),
		status=code,
		mimetype='application/json'
	)


def create_gif_sound(name, full_link, gif_link, yt_id):
	if current_user.is_authenticated:
		create_link(name, current_user.user_id, full_link, gif_link, yt_id)
	else:
		create_link(name, None, full_link, gif_link, yt_id)


@app.route('/api/user_info', methods=['POST', 'GET'])
@login_required
def get_user_info(user_id, api_key):
	user = get_user(user_id)
	schema = UserSchema(many=True)
	result = schema.dumps(user)
	return result.data


@app.route('/api/links', methods=['POST'])
def get_links():
	links = get_all_links()
	schema = LinkSchema(many=True)
	result = schema.dumps(links)
	return result


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

# Extracts a URL that has been embedded in another URL
def unquote_url(url):
	return urllib.parse.unquote(url)

# Tests the view_combo route
@app.route('/testview/')
def test_view_combo():
	return redirect(
		url_for('view_combo', gif_url='https://media4.giphy.com/avatars/100soft/WahNEDdlGjRZ.gif', yt_url='https://www.youtube.com/watch?v=knrHPneSN10')
	)

# Displays a gif and a youtube video together on the same page using the provided URLs
@app.route('/view/gif/<path:gif_url>/yt/<path:yt_url>/')
def view_combo(gif_url, yt_url):
	gif_url = unquote_url(gif_url)
	yt_url = unquote_url(yt_url)
	yt_id = youtube.get_video_id(yt_url)
	showinfo = 1  # Enable Title and video controls
	rel = 0  # Uhh I don't know
	start = 0  # starting point of video
	video = f'https://www.youtube.com/embed/{yt_id}?rel={rel}&amp;showinfo={showinfo}&amp;start={start}'
	full_link = '/view/gif/' + gif_url + '/yt/' + yt_url
	if check_if_exists(full_link):
		update_link_view_count(full_link)
	return render_template('view.html', gif=gif_url, video=video)


@app.route('/view/name/<name>/gif/<path:gif_url>/yt/<path:yt_url>/')
def create_view_combo(name, gif_url, yt_url):
	gif_url = unquote_url(gif_url)
	yt_url = unquote_url(yt_url)
	yt_id = youtube.get_video_id(yt_url)
	showinfo = 1  # Enable Title and video controls
	rel = 0  # Uhh I don't know
	start = 0  # starting point of video
	video = f'https://www.youtube.com/embed/{yt_id}?rel={rel}&amp;showinfo={showinfo}&amp;start={start}'
	full_link = '/view/gif/' + gif_url + '/yt/' + yt_url
	if check_if_exists(full_link):
		update_link_view_count(full_link)
	else:
		create_gif_sound(name, full_link, gif_url, yt_url)
	return render_template('view.html', gif=gif_url, video=video)

if __name__ == '__main__':
	app.run()
