import sqlite3
from ..schemas import db


class Lists(db.Model):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(100), nullable=False)

def do_taskDB_req(req_string):
    connection = sqlite3.connect('lists.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(req_string)

    sql_object = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return sql_object

def seed_list(user_id, description):
    req_string = """
        INSERT INTO lists(
            user_id,
            description
        )
        VALUES(
            '{user_id}',
            '{description}'
        );
    """.format(user_id=user_id, description=description)
    do_taskDB_req( req_string )

def remove_task(list_id):
    req_string = """
        DELETE FROM lists WHERE list_id = '{list_id}';
     """.format(list_id=list_id)
    do_taskDB_req( req_string )