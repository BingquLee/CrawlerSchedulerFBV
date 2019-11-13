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
