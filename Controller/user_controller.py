## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: user_controller.py
## ABSTRACT: 
## AUTHORS: Erick Shaffer
## DATE: 

import json
from Model.models import *
from Controller.session_controller import *

def create_user_table():
    Base.metadata.create_all(bind=get_engine())


def get_user(user_id):
    session = get_session()
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
    except exc.SQLAlchemyError:
        return False
    return user


def get_user_by_username(username):
    session = get_session()
    try:
        return session.query(User).filter(User.username == username).first()
    except exc.SQLAlchemyError:
        return None


def get_all_users():
    session = get_session()
    try:
        users = session.query(User).all()
    except exc.SQLAlchemyError:
        return False
    return users


def create_user(app, username, email, password, role):
    user = User()
    user.username = username
    user.email = email
    user.password = password
    user.role = role
    data = {}
    code = 0
    try:
        session_commit(user)
    except exc.SQLAlchemyError:
        code = 400
        data['status'] = "Error"
        return app.response_class(
            response=json.dumps(data),
            status=code,
            mimetype='application/json'
        )
    data['status'] = "Success"
    code = 200
    return app.response_class(
        response=json.dumps(data),
        status=code,
        mimetype='application/json'
    )
