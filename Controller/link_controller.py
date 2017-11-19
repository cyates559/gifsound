from Controller.session_controller import *
from Model.link_model import *


def create_link_table():
    Base.metadata.create_all(bind=get_engine())


def get_all_user_links(user_id):
    session = get_session()
    link_ids = session.query(Link).filter(Link.user_id == user_id)
    return link_ids


def get_all_links():
    session = get_session()
    links = session.query(Link, Link.name, Link.link, Link.views)
    return links


def get_link(link_id):
    session = get_session()
    try:
        link = session.query(Link).filter(Link.id == link_id)
    except exc.SQLAlchemyError:
        return None
    return link


def create_link(name, user_id, full_link, gif_link, yt_link):
    link = Link()
    link.name = name
    link.user_id = user_id
    link.full_link = full_link
    link.gif_link = gif_link
    # link.yt_link = yt_link
    # try:
    #     session_commit(link)
    # except exc.SQLAlchemyError:
    #     return False

