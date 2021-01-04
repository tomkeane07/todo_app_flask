import sqlite3

def do_taskDB_req(req_string):
    connection = sqlite3.connect('tasks.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(req_string)

    sql_object = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return sql_object

def seed_task(user_id, description):
    req_string = """
        INSERT INTO tasks(
            user_id,
            description
        )
        VALUES(
            '{user_id}',
            '{description}'
        );
    """.format(user_id=user_id, description=description)
    do_taskDB_req( req_string )

def remove_task(task_id):
    req_string = """
        DELETE FROM tasks WHERE task_id = '{task_id}';
     """.format(task_id=task_id)
    do_taskDB_req( req_string )