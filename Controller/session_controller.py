
## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: session_controller.py
## ABSTRACT: Controller for sqlaclehmy. This commits items into the database and creates
## a database engine to be used by sqlalchemy.
## AUTHORS: Erick Shaffer
## DATE: 12/10/2017
from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker

from config import settings


def get_engine():
    return create_engine(
        settings['development']['mysql']['engine'], echo=settings['development']['mysql']['engine_debug'])


def session_commit(entry):
    session = get_session()
    session.add(entry)
    try:
        session.commit()
    except exc.SQLAlchemyError:
        return False
    session.close()


def get_session():
    try:
        Session = sessionmaker(bind=get_engine())
        session = Session()
    except exc.SQLAlchemyError:
        return False
    return session
