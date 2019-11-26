# -*- coding: utf-8 -*-
import time
import os

from pymysql.cursors import DictCursor

from global_config import proxies_conn


def ts2datetime(ts):
    return time.strftime('%Y-%m-%d', time.localtime(ts))


def ts2date_min(ts):
    return time.strftime('%Y-%m-%d %H:%M', time.localtime(ts))


def date_min2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M')))


def today():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def read_files(direction='.'):
    file_list = []
    for file_path, dirs, fs in os.walk(direction):
        # print(file_path, dirs, fs)
        for f in fs:
            if file_path == '.' or file_path == '.\\.idea' or file_path == '.\\.ipynb_checkpoints':
                continue
            file_list.append(os.path.join(file_path, f))
            pass
    return file_list


def get_proxy(country):
    cursor = proxies_conn.cursor(DictCursor)
    sql = "SELECT * FROM {} ORDER BY score DESC LIMIT 1,1".format(country)
    cursor.execute(sql)
    proxy = cursor.fetchall()[0]
    print(proxy)
    return proxy


if __name__ == '__main__':
    get_proxy('US')
