#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    提交数据到石墨文档
"""
import requests
import random

def shimo(content, username,pname,amount):
   """提交数据到石墨文档表单收集器
   """
   # 石墨文档提交数据格式
   data = {
   "duration" : 5,
   "formRev" : 1,
   "responseContent" : [
      {
         "guid" : "GT11OwKe",
         "text" : {
            "content" : "xxx"
         },
         "type" : 0
      },
      {
         "guid" : "xAjdyg6y",
         "text" : {
            "content" : "xxx"
         },
         "type" : 0
      },
      {
         "guid" : "JcTnexA2",
         "text" : {
            "content" : "xxx"
         },
         "type" : 0
      }
   ],
   "userFinger" : "-1",
   "userName" : "xxxx"
}
   url = "https://shimo.im/api/newforms/forms/R13j82B45dh4bvk5/submit" #真实地址  GT11OwKe/xAjdyg6y/JcTnexA2
   #url = "https://shimo.im/api/newforms/forms/pdGc9jGYtdxyTydt/submit"  #测试地址  xrmD2uAq/LE4te1MF

   data['duration'] = random.randint(10,50)
   data['responseContent'][0]['text']['content'] = content
   data['responseContent'][1]['text']['content'] = pname
   data['responseContent'][2]['text']['content'] = amount
   data['userName'] = username
   #data['userName'] = "JD助手"
   response = requests.post(url, json=data)  #用post方式提交数据
   if response.status_code == 200 or 204:
      #print(response.status_code)
      return "提交成功"
   else:
      return "提交失败"

if __name__ == '__main__':
   content = '7102298241802'
   username = "怀沙"
   pname = "iPhone 13"
   amount = '253'
   shimo(content, username, pname,amount)