import sqlite3
from ..schemas import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))
    description = db.Column(db.String(200), nullable=False)

def seed_task(list_id, description):
    task = Task(list_id=list_id, description=description)
    db.session.add(list)
    db.session.commit()

def remove_task(task_id):
    db.session.delete(List).where(list_id==list_id)