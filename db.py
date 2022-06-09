#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sqlite3
from time import strftime
filename = strftime("save\\jd-assistant_%Y_%m.db")

def save_db(order_id, order_vercode, amount, username, order_time):
    """保存数据到sqlite
    """
    # filename = "weread.db"

    # 判断文件是否存在
    if os.path.exists(filename):
        # 处理数据并写入
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO JDORDER(order_id, order_vercode, amount, username, order_time) VALUES(?,?,?,?,?)", 
                (order_id, order_vercode, amount, username, order_time))
        conn.commit()
        conn.close()
    else:
         # 创建数据库 处理数据并写入
        path = os.path.dirname(os.getcwd() +'\\save\\') # 判断db目录是否存在
        if not os.path.exists(path):
            os.makedirs(path)
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        c.execute("CREATE TABLE JDORDER \
            (order_id TEXT NOT NULL UNIQUE,\
                order_vercode TEXT NOT NULL,\
                amount TEXT NOT NULL,\
                username TEXT NOT NULL,\
                order_time TEXT NOT NULL)")

        c.execute("INSERT OR IGNORE INTO JDORDER(order_id, order_vercode, amount, username, order_time) VALUES(?,?,?,?,?)", 
                    (order_id, order_vercode, amount, username, order_time))
        conn.commit()
        conn.close()


def query_db(order_id):
    """查询数据是否已经存在
    """
    if os.path.exists(filename):
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        c.execute("SELECT * FROM JDORDER WHERE order_id=?",[order_id])
        result = c.fetchone()
        conn.commit()
        conn.close()
        return result


if __name__== "__main__":
    order_time = '2022/5/6'
    order_id = '2443156891680'
    order_vercode = '232068573372'
    amount = '255'
    username = 'huaisha1224'
    # res = query_db(order_id)
    # if res:
    #     print(res)
    # else:
    #     save_db(order_id, order_vercode, amount, username, order_time)