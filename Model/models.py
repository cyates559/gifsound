from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from marshmallow import Schema, fields
from flask_bcrypt import Bcrypt

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    def __int__(self, username, email, password, role):
        self.username = username
        self.email = email
        self._password = password
        self.role = role

    user_id = Column('id', Integer, primary_key=True)
    username = Column('username', String(255), unique=True)
    email = Column('email', String(255), unique=True)
    _password = Column('password', String(60))
    role = Column('role', Integer)
    views = Column('view_count', Integer, default=0)
    is_active = Column('is_active', Boolean, default=True)
    is_authenticated = Column('is_authenicated', Boolean, default=False)
    is_anonymous = Column('is_anonymous', Boolean, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    link = relationship("Link", backref='user', single_parent=True, lazy='joined')

    def get_id(self):
        return self.user_id


    @hybrid_property
    def password(self):
        return self.password()





class Link(Base):
    __tablename__ = 'link'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    user_id = Column('user_id', Integer, ForeignKey("user.id"), nullable=True)
    full_link = Column('full_link', String(500))
    gif_link = Column('gif_link', String(500))
    yt_link = Column('yt_link', String(500))
    views = Column('view_count', Integer, default=0)
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



