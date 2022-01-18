#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from time import strftime
import os
import csv

def save_to_csv(dealtime,number,vercode, amount):
    """
    写入内容到csv
    """
    dealtime = dealtime.split(' ')[0]   # 切割时间取年月日
    number = number + '\t'
    vercode = vercode + '\t'
    amount = amount[0]
    data = (dealtime, number, vercode, amount)
    file_path = strftime("jd-assistant_%Y_%m.csv")  # 按照当前系统时间创建文件

    # 判断文件是否存在
    if os.path.exists(file_path):
        # 处理数据并写入
        with open(file_path, 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
    else:
        # 创建文件 处理数据并写入
        header = ('下单时间', '订单号', '验证码', '实付金额')
        with open(file_path, 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
        
        with open(file_path, 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

if __name__ == '__main__':
    time = '2021-09-07 08:22:05'
    number = '221697592258'
    vercode = '7102298241802'
    amount = ['248.00']
    save_to_csv(time, number, vercode, amount)
