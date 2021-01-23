from flask.globals import session
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
    return make_dict_object_useable(
        db.session.query(User).filter_by(username=username)
        .first().__dict__
    )

def make_dict_object_useable(user_dict):
    del user_dict["password"]
    del user_dict["_sa_instance_state"]
    return user_dict

def set_users_main_list(user_id, list_id):
    user = db.session.query(User).filter_by(id=user_id).first()
    user.main_list_id = list_id
    db.session.commit()
