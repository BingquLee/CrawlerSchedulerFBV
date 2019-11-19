import time

from pymysql.cursors import DictCursor

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
    cursor = conn.cursor(DictCursor)
    sql = "Select * From jobs WHERE channel = '{}' ORDER By publish_time ASC, status ASC".format(channel)
    cursor.execute(sql)
    data = cursor.fetchall()

    item_list = [{"channel": i["channel"], "account": i["account"], "publish_time": i["publish_time"], "publish_freq": i["publish_freq"], "text": i["text"], "file_amount": i["file_amount"], "status": i["status"], "id": i["id"]} for i in data]
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
    cursor = conn.cursor(DictCursor)
    sql = "SELECT account_id, session_id FROM accounts WHERE channel='{}' ORDER By account_id ASC".format(channel)
    cursor.execute(sql)
    data = cursor.fetchall()
    users_list = [{"user_id": i["account_id"], "session_id": i["session_id"]} for i in data]
    cursor.close()
    return users_list
