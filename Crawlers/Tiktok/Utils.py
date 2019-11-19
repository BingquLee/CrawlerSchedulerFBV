import sys

from pymysql.cursors import DictCursor

sys.path.append('/home/BingquLee/Project/CrawlerSchedulerFBV/')

from global_config import conn

def get_tag(text):
    text = text + ' '
    tag_list = []
    flag = False
    start = 0
    end = 0
    for i in range(len(text)):
        if text[i] == '#':
            start = i
            flag = True
        elif text[i] == ' ' and flag:
            end = i
            flag = False
        if end > start:
            item = {"start": start, "end": end, "type": 1, "hashtag_name": text[start + 1: end]}
            if item not in tag_list:
                tag_list.append(item)
    return tag_list


def get_sessionid_by_account(account, channel):

    cursor = conn.cursor(DictCursor)
    sql = "SELECT session_id FROM accounts WHERE account_id='{}' AND channel='{}'".format(account, channel)
    cursor.execute(sql)
    res = cursor.fetchone()
    print(res)
    session_id = res["session_id"] if res else ''
    return session_id



if __name__ == "__main__":
    session_id = get_sessionid_by_account("philring", "Tiktok")
    print(session_id)
