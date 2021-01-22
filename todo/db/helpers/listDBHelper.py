from ..db import db
from ..models.List import List
from .tasksDbHelper import getAllTasks

def seed_list(user_id, title):
    list = List(user_id=user_id, title=title)
    db.session.add(list)
    db.session.commit()

def remove_list(list_id):
    db.session.delete(List).where(list_id==list_id)

def populate_list(list_id):
    return getAllTasks(list_id)