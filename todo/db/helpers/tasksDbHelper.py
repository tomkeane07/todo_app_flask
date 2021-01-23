from ..db import db
from ..models.Task import Task

def seed_task(list_id, description):
    task = Task(list_id=list_id, description=description)
    db.session.add(task)
    db.session.commit()

def remove_task(task_id):
    Task.query.filter_by(id=task_id).delete()
    db.session.commit()

def get_all_tasks(list_id=None):
    return Task.query.all()

def get_list_tasks(list_id):
    tasks_as_tuple_list = db.session.query(Task).filter_by(list_id=list_id).all()
    return tasks_as_tuple_list

def get_task_by_id(task_id):
    return make_dict_object_useable(
        db.session.query(Task).filter_by(id=task_id).first().__dict__
    )

def make_dict_object_useable(task_dict):
    del task_dict["_sa_instance_state"]
    return task_dict
