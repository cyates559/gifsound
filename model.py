from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    '')
Base = declarative_base()


class Links(Base):
    __tablename__ = 'links'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    link = Column('link', String(500))
    views = Column('view_count', Integer)

    def __repr__(self):
        return "<Links(name = '%s', link='%s', views='%s)>" % (
            self.name, self.link, self.views
        )


class Users(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(255), unique=True)
    password = Column('password', String(60))
    links = Column('link_id', Integer)
    views = Column('view_count', Integer)

    def __repr__(self):
        return "<Links(username = '%s', links='%s)>" % (
            self.username, self.links
        )

Base.metadata.create_all(bind=engine)
