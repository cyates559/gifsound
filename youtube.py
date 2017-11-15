#!pyenv/bin/python

# AUTHOR: Carsen Yates
# DATE: 11/15/2017
# PURPOSE: To embed youtube videos like a pro

import urllib.parse

def get_embed_url(main_url):

	id=None
	# User gave us the url we are looking for, so we are done here.
	if 'https://youtube.com/embed/' in main_url:
		return main_url

	# We need to extract the id from the url to produce the embed url
	elif 'youtu.be' in main_url:
		r = urllib.parse.urlparse(main_url)
		id = r.path.replace('/', '')

	elif 'youtube.com/watch?v=' in main_url:
		r = urllib.parse.urlparse(main_url)
		id = urllib.parse.parse_qs(r.query)['v'][0]

	if id == None: # Error: Couldn't parse YouTube Url
		return None

	return f'https://youtube.com/embed/{id}'


# Some tests, these should all print the same URL
print(get_embed_url('https://www.youtu.be/8y7XGmORIXM?t=1m'))
print(get_embed_url('https://www.youtube.com/watch?v=8y7XGmORIXM'))
print(get_embed_url('https://www.youtube.com/watch?v=8y7XGmORIXM&start=1'))