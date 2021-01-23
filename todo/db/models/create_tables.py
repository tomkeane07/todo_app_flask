from .User import User
from .List import List
from .Task import Task

def create_tables(app, db):
    with app.app_context():
        db.create_all()