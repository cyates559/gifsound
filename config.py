#!pyenv/bin/python

## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: config.py
## ABSTRACT: This file parses the settings.yml file
## AUTHORS: Erick Shaffer
## DATE: 
import yaml

with open('settings.yml', 'r') as f:
    settings = yaml.load(f)
