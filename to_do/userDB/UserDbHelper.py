import sqlite3
import userDB.schema

def do_userDB_req(req_string):
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(req_string)

    sql_object = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return sql_object

def seed_user(username, password):
    if user_exists(username) == True:
        raise Exception("user already exists")
    req_string = """
        INSERT INTO users(
            username,
            password
        )
        VALUES(
            '{username}',
            '{password}'
        );
    """.format(username=username, password=password)
    do_userDB_req( req_string )

def verify_user(username, password):
    req_string = """
        SELECT * FROM users
        WHERE username='{username}' AND password='{password}'
        ORDER BY pk DESC;
    """.format(username=username, password=password)
    if len(do_userDB_req(req_string)) > 0:
        return True
    else:
        return False


def user_exists(username):
    req_string = """
        SELECT *
        FROM users
        WHERE username = '{username}';
    """.format(username=username)
    return not do_userDB_req(req_string)
