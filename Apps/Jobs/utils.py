import time

from global_config import conn
from global_utils import ts2datetime


def set_jobs_util(channel, account, publish_time, publish_freq, text, file_amount, status):
    update_ts = int(time.time())
    update_dt = ts2datetime(update_ts)
    cursor = conn.cursor()
    sql = """INSERT INTO jobs (channel, account, publish_time, publish_freq, text, file_amount, status, update_ts, update_dt) 
                    VALUES 
                    ('%s', '%s', '%s', '%s', '%s', %s, %s, '%s', '%s')""" % (channel, account, publish_time, publish_freq, text, file_amount, status, update_ts, update_dt)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return True


def get_jobs_util(channel):
    cursor = conn.cursor()
    sql = "Select * From jobs WHERE channel = '{}' ORDER By publish_time ASC, status ASC".format(channel)
    cursor.execute(sql)
    data = cursor.fetchall()

    item_list = [{"channel": i[1], "account": i[2], "publish_time": i[3], "publish_freq": i[4], "text": i[5], "file_amount": i[6], "status": i[7], "id": i[0]} for i in data]
    cursor.close()
    return item_list


def delete_job_util(job_id):
    cursor = conn.cursor()
    sql = "DELETE FROM jobs WHERE id={}".format(job_id)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return True


def get_accounts_util(channel):
    cursor = conn.cursor()
    sql = "SELECT account_id, session_id FROM accounts WHERE channel='{}' ORDER By account_id ASC".format(channel)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    users_list = [{"user_id": i[0], "session_id": i[1]} for i in data]
    cursor.close()
    return users_list
