import sqlite3

def init_schemas():
    init_users_db()
    init_lists_db()
    init_tasks_db()

def init_db(dbname_str, sql_req_str):
    connection = sqlite3.connect(dbname_str, check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        sql_req_str
    )
    connection.commit()
    cursor.close()
    connection.close()

def init_users_db():
    db_name      = 'users.db'
    req_string = """CREATE TABLE IF NOT EXISTS users(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(16),
            password VARCHAR(32)
    );"""
    init_db(db_name, req_string)
    
def init_tasks_db():
    db_name   = 'tasks.db'
    req_string= """CREATE TABLE IF NOT EXISTS tasks(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                list_id VARCHAR(16),
                description VARCHAR(100)
        );"""
    init_db(db_name, req_string)

def init_lists_db():
    db_name   = 'lists.db'
    req_string= """CREATE TABLE IF NOT EXISTS lists(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(16),
                title VARCHAR(100)
        );"""
    init_db(db_name, req_string)
