from ..db import db
from ..models.List import List
from .tasksDbHelper import get_all_tasks

def seed_list_and_return_list_id(user_id, title):
    list = List(user_id=user_id, title=title)
    db.session.add(list)
    db.session.flush()
    list_id = list.id
    db.session.commit()
    return list_id

def remove_list(list_id):
    List.query.filter_by(id=list_id).delete()
    db.session.commit()

def populate_list(list_id):
    return get_all_tasks(list_id)

def get_all_lists():
    return List.query.all()

def get_users_lists(user_id):
    return db.session.query(List).filter_by(user_id=user_id).all()

def get_list_by_id(list_id):
    return db.session.query(List).filter_by(id=list_id).first()

def get_users_lists_as_list_tuples(user_id):
    users_lists = get_users_lists(user_id)
    list_of_tuples = [(l.id, l.title) for l in users_lists]
    return list_of_tuples