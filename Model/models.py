from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from marshmallow import Schema, fields


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(255), unique=True)
    email = Column('email', String(255), unique=True)
    password = Column('password', String(60))
    role = Column('role', Integer)
    views = Column('view_count', Integer, default=0)
    status = Column('status', Integer, default=1)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    link = relationship("Link", backref='user', single_parent=True, lazy='joined')


class Link(Base):
    __tablename__ = 'link'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    user_id = Column('user_id', Integer, ForeignKey("user.id"), nullable=True)
    full_link = Column('full_link', String(500))
    gif_link = Column('gif_link', String(500))
    yt_link = Column('yt_link', String(500))
    views = Column('view_count', Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class LinkSchema(Schema):
    name = fields.Str()
    full_link = fields.String()
    user_id = fields.Integer()
    yt_link = fields.String()
    gif_link = fields.String()
    views = fields.Integer()
    time_created = fields.DateTime()
    # user = fields.Nested('UserSchema')


class UserSchema(Schema):
    username = fields.Str()
    email = fields.Email()
    role = fields.Integer()
    views = fields.Integer()
    time_created = fields.DateTime()
    link = fields.Nested('LinkSchema', many=True)



