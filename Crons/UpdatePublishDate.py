# -*- coding: utf-8 -*-
import sys

from pymysql.cursors import DictCursor

sys.path.append(r'/home/BingquLee/Project/CrawlerSchedulerFBV')
from global_config import conn
from global_utils import today


def update_publish_date():
    cursor = conn.cursor(DictCursor)
    sql = "SELECT * FROM jobs WHERE publish_freq='Everyday' ORDER BY publish_time ASC"
    cursor.execute(sql)
    update_data = cursor.fetchall()
    print(update_data)
    if update_data:
        update_sql = """
            UPDATE jobs SET
                publish_time = CASE id
                %s
                END,
                status = CASE id
                %s
                END
            WHERE id in (%s)
        """
        update_sql = update_sql % (
            '\n'.join(['WHEN {} THEN "{}"'.format(i["id"], '{} {}'.format(today(), i["publish_time"].split(' ')[-1])) for i in update_data]),
            '\n'.join(['WHEN {} THEN {}'.format(i["id"], 0) for i in update_data]),
            ','.join([str(i["id"]) for i in update_data]),
        )
        print(update_sql)
        cursor.execute(update_sql)
        conn.commit()
    else:
        pass
    cursor.close()


if __name__ == '__main__':
    update_publish_date()

