from ..db import db
from sqlalchemy.sql import exists
from ..models.User import User

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