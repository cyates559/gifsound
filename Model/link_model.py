from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Link(Base):
    __tablename__ = 'link'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    user_id = Column('user_id', Integer, nullable=True)
    full_link = Column('full_link', String(500))
    gif_link = Column('gif_link', String(500))
    yt_link = Column('yt_link', String(500))
    views = Column('view_count', Integer)

    def __repr__(self):
        return "<Links(name = '%s', link='%s', views='%s)>" % (
            self.name, self.link, self.views
        )
