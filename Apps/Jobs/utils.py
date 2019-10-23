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


def get_jobs_util(page_num, page_size):
    cursor = conn.cursor()
    sql = "Select * From jobs ORDER By publish_time DESC, status ASC LIMIT {}, {}".format((page_num - 1) * page_size, page_size)
    data = cursor.execute(sql).fetchall()
    item_list = [{"channel": i[1], "account": i[2], "publish_time": i[3], "publish_freq": i[4], "text": i[5], "file_amount": i[6], "status": i[7]} for i in data]
    return item_list
