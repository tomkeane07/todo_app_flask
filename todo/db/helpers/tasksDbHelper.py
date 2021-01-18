import sqlite3
from ..schemas import db

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))
    description = db.Column(db.String(200), nullable=False)

def do_taskDB_req(req_string):
    connection = sqlite3.connect('tasks.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(req_string)

    sql_object = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return sql_object

def seed_task(list_id, description):
    req_string = """
        INSERT INTO tasks(
            list_id,
            description
        )
        VALUES(
            '{list_id}',
            '{description}'
        );
    """.format(user_id=list_id, description=description)
    do_taskDB_req( req_string )

def remove_task(task_id):
    req_string = """
        DELETE FROM tasks WHERE task_id = '{task_id}';
     """.format(task_id=task_id)
    do_taskDB_req( req_string )