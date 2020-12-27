import sqlite3

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

def init_to_do_db(user_key):
    connection = sqlite3.connect('todolist.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS to_do_list(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(16),
                task VARCHAR(100)
        );"""
    )
    connection.commit()
    cursor.close()
    connection.close()