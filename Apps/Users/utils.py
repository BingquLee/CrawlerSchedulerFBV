<<<<<<< HEAD
from global_config import conn


def add_users_util(user_id, session_id):
    cursor = conn.cursor()
    sql = """INSERT INTO users (uid, session_id) 
                        VALUES 
                        ('%s', '%s')""" % (user_id, session_id)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return True


def delete_user_util(user_id):
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE uid={}".format(user_id)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return True


def get_users_util():
    cursor = conn.cursor()
    sql = "Select * From users ORDER By uid ASC"
    data = cursor.execute(sql).fetchall()
    users_list = [{"user_id": i[0], "session_id": i[1]} for i in data]
    cursor.close()
    return users_list
=======
from global_config import conn


def add_users_util(user_id, session_id):
    cursor = conn.cursor()
    sql = """INSERT INTO users (uid, session_id) 
                        VALUES 
                        ('%s', '%s')""" % (user_id, session_id)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return True


def delete_user_util(user_id):
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE uid='{}'".format(user_id)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return True


def get_users_util():
    cursor = conn.cursor()
    sql = "Select * From users ORDER By uid ASC"
    data = cursor.execute(sql).fetchall()
    users_list = [{"user_id": i[0], "session_id": i[1]} for i in data]
    cursor.close()
    return users_list
>>>>>>> c7c3fae9169c3514cca359cf767c0ddb4fe4061d
