# -*- coding: utf-8 -*-
import time
import sys

from pymysql.cursors import DictCursor

sys.path.append(r'/home/BingquLee/Project/CrawlerSchedulerFBV')

from Crawlers.Tiktok.TiktokUploader import video_uploader
from global_config import conn
from global_utils import ts2date_min


def get_jobs():
    cursor = conn.cursor(DictCursor)
    sql = "SELECT * FROM jobs WHERE publish_time <= '%s' and status=0 ORDER BY publish_time ASC" % ts2date_min(int(time.time()))
    cursor.execute(sql)
    job_list = cursor.fetchall()
    job_id_list = [str(i["id"]) for i in job_list]
    sql_update_job_status_temp = """
        UPDATE jobs SET
            status = CASE id
                %s
            END
        WHERE id IN (%s)
    """ % ('\n'.join(["WHEN {} THEN 1".format(str(i)) for i in job_id_list]), ','.join(job_id_list))
    cursor.execute(sql_update_job_status_temp)
    conn.commit()
    for job in job_list:
        print(job)
        if job["channel"] == 'Tiktok':
            #sql_update_job = "UPDATE jobs SET status=1 WHERE id='{}'".format(job[0])
            #cursor.execute(sql_update_job)
            #conn.commit()
            file_error_count = 0

            file_sql = "SELECT * FROM files WHERE status=0 AND account='{}' LIMIT {}".format(job["account"], job["file_amount"])
            cursor.execute(file_sql)
            file_list = cursor.fetchall()
            for file in file_list:
                # print('file_name', r'Videos/{}/To_{}/{}.mp4'.format(file[1], file[2], file[0]))
                try:
                    video_uploader(job["account"], r'Videos/{}/To_{}/{}.mp4'.format(file["channel"], file["account"], file["id"]), job["text"])
                    file_update_sql = "UPDATE files SET status=1 WHERE id='{}';".format(file["id"])
                    cursor.execute(file_update_sql)
                    conn.commit()
                except Exception as e:
                    file_update_sql = "UPDATE files SET status=-1 WHERE id='{}';".format(file["id"])
                    cursor.execute(file_update_sql)
                    conn.commit()
                    # raise e
                    file_error_count -= 1
                    print('file_name', r'Videos/{}/To_{}/{}.mp4'.format(file["channel"], file["account"], file["id"]))
                    continue
            if file_error_count != 0:
                sql_update_job = "UPDATE jobs SET status={} WHERE id='{}'".format(file_error_count, job["id"])
                cursor.execute(sql_update_job)
                conn.commit()

    cursor.close()


if __name__ == '__main__':
    get_jobs()

