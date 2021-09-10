#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pandas import DataFrame
import pandas as pd
from time import strftime
import os

def save_to_csv(dealtime,number,vercode, amount):
    """
    写入内容到csv
    """
    file_path = strftime("jd-assistant_%Y_%m.csv")  #按照当前系统时间创建文件

    #判断文件是否存在
    if os.path.exists(file_path):
        data = pd.DataFrame({'下单时间':dealtime, '订单号':number, '验证码':vercode, '实付金额':amount}, index=[0])
        data.to_csv(file_path, index=None, mode='a', header=None)
        #print('追加')
    else:
        data = pd.DataFrame({'下单时间':dealtime, '订单号':number, '验证码':vercode, '实付金额':amount}, index=[0])
        data.to_csv(file_path, index=None)
        #print('新增')


if __name__ == '__main__':
    time = ['2021-09-07 08:22:05']
    number = ['221697592258']
    vercode = ['7102298241802']
    amount = ['248.00']
    save_to_csv(time, number, vercode, amount)
