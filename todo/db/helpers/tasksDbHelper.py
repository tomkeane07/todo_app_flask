from ..db import db
from ..models.Task import Task

def seed_task(list_id, description):
    task = Task(list_id=list_id, description=description)
    db.session.add(list)
    db.session.commit()

# def remove_task(task_id):
#     db.session.delete(Task).where(List.list_id==list_id)

def getAllTasks(list_id=None):
    if list_id is None:
        return Task.query.all()
    return Task.query.filter_by(list_id=list_id)