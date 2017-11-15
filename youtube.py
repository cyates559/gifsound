#!pyenv/bin/python

# AUTHOR: Carsen Yates
# DATE: 11/15/2017
# PURPOSE: To embed youtube videos like a pro

import urllib.parse

def get_embed_url(main_url):

	id=None
	# User gave us the url we are looking for, so we are done here.
	if 'youtube.com/embed/' in main_url:
		return main_url

	# Extract from mini url
	elif 'youtu.be' in main_url:
		r = urllib.parse.urlparse(main_url)
		id = r.path.replace('/', '')
		print(id)

	# Extract from regular youtube url
	elif 'youtube.com/watch?' in main_url:
		r = urllib.parse.urlparse(main_url)
		id = urllib.parse.parse_qs(r.query)['v'][0]

	# Error: Couldn't parse YouTube Url
	if id == None:
		return None

	return f'https://www.youtube.com/embed/{id}'


# Some tests, these should all print the same URL
print(get_embed_url('https://www.youtu.be/8y7XGmORIXM?t=1m'))
print(get_embed_url('https://www.youtube.com/embed/8y7XGmORIXM?t=1m'))
print(get_embed_url('https://www.youtube.com/watch?randomarg=1&v=8y7XGmORIXM&anotherrandomarg=1'))