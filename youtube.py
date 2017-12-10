#!pyenv/bin/python

## TITLE: youtube.py
## COURSE: CST 205 - Multimedia Design & Programming
## AUTHORS: Carsen Yates
## DATE: 11/15/2017
## ABSTRACT: This file parses YouTube Video URLs and extracts the Video ID
## The Video ID can be further used to embed YouTube videos into webpages dynamically. 

import urllib.parse

# Takes a YouTube Video URL as input and returns the Video ID
# URLs come in three forms:
# 1) www.youtube.com/embed/<ID>
# 2) www.youtube.com/watch?v=<ID>
# 3) youtu.be/<ID>
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
