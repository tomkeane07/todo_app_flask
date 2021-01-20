import sqlite3
from ..schemas import db
from flask_user import login_required, UserManager, UserMixin
from sqlalchemy.sql import exists

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')

def seed_user(username, password):
    if user_exists(username) == True:
        raise Exception("user already exists")
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

def verify_user(username, password):
    return db.session.query(exists().where(User.username==username and User.password==password)).scalar()

def user_exists(username):
    return db.session.query(exists().where(User.username==username )).scalar()

def getUser_byUsername_asDict(username):
    return hide_password_for_view(
        db.session.query(User).filter_by(username=username)
        .first().__dict__
    )

def hide_password_for_view(user_dict):
    del user_dict["password"]
    del user_dict["_sa_instance_state"]
    return user_dict