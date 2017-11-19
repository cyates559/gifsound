from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(255), unique=True)
    email = Column('email', String(255), unique=True)
    password = Column('password', String(60))
    role = Column('role', Integer)
    views = Column('view_count', Integer, default=0)

    def __repr__(self):
        return "<Links(username = '%s', links='%s)>" % (
            self.username, self.links
        )