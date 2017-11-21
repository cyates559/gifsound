#!pyenv/bin/python

# AUTHOR: Carsen Yates
# DATE: 11/15/2017
# PURPOSE: To embed youtube videos like a pro

import urllib.parse


def get_video_id(main_url):
    vid = None
    # User gave us the url we are looking for, so we are done here.
    if 'youtube.com/embed/' in main_url:
        return main_url

    # Extract from mini url
    elif 'youtu.be' in main_url:
        r = urllib.parse.urlparse(main_url)
        vid = r.path.replace('/', '')

    # Extract from regular youtube url
    elif 'youtube.com/watch?' in main_url:
        r = urllib.parse.urlparse(main_url)
        vid = urllib.parse.parse_qs(r.query)['v'][0]

    # Error: Couldn't parse YouTube Url
    return vid