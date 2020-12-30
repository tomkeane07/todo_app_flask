import sqlite3

def init_schemas():
    init_users_db()
    init_tasks_db()

def init_users_db():
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(16),
                password VARCHAR(32)
        );"""
    )
    connection.commit()
    cursor.close()
    connection.close()

def init_tasks_db():
    connection = sqlite3.connect('tasks.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS tasks(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                list_id VARCHAR(16),
                description VARCHAR(100)
        );"""
    )
    connection.commit()
    cursor.close()
    connection.close()