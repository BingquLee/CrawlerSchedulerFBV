# -*- coding: utf-8 -*-
import hashlib
import sys

from pymysql.cursors import DictCursor

sys.path.append(r'/home/BingquLee/Project/CrawlerSchedulerFBV')

from global_config import conn
from global_utils import read_files


def add_file_to_db():
    cursor = conn.cursor(DictCursor)
    sql = "SELECT * FROM files"

    video_list = read_files(r'Videos')
    file_video_name_set = set(video_list)
    cursor.execute(sql)
    db_video_name_set = set(["Videos/{}/To_{}/{}.mp4".format(i["channel"], i["account"], i["name"]) for i in cursor.fetchall()])
    sub_set = file_video_name_set - db_video_name_set
    if sub_set:

        insert_sql = """
            INSERT INTO
            files (name, channel, account, status, id)
            VALUES
            %s
        """
        insert_sql = insert_sql % ','.join(['("{}", "{}", "{}", "{}", "{}")'.format(i.split('/')[-1].split('.')[0], i.split('/')[-3], i.split('/')[-2].split('_')[-1], 0, hashlib.md5(i.encode(encoding='UTF-8')).hexdigest()) for i in sub_set])
        print(insert_sql)
        cursor.execute(insert_sql)
        conn.commit()
    else:
        pass
    cursor.close()


if __name__ == '__main__':
    add_file_to_db()
