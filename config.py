#!pyenv/bin/python
## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: models.py
## ABSTRACT: ORM models used by sql alchemy. These are the models that are used to
## create database schema and interact with database with objects.
## AUTHORS: Erick Shaffer
## DATE: 12/10/17
import yaml

with open('settings.yml', 'r') as f:
    settings = yaml.load(f)
