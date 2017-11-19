import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


def get_engine():
    return create_engine(settings['development']['mysql']['engine'], echo=settings['development']['other']['debug'])


def session_commit(entry):
    session = get_session()
    session.add(entry)
    session.commit()
    session.close()


def get_session():
    Session = sessionmaker(bind=get_engine())
    session = Session()
    return session
