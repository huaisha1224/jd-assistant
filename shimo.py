#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    提交数据到石墨文档
"""
import requests
import random

def shimo(content, username):
   """提交数据到石墨文档表单收集器
   """
   # 石墨文档提交数据格式
   data = {
      "duration" : 55,
      "formRev" : 1,
      "responseContent" : [
         {
            "guid" : "3LloZtJ7", #xrmD2uAq/3LloZtJ7
            "text" : {
               "content" : "xxxxxxxx"
            },
            "type" : 0
         }
      ],
      "userFinger" : "-1",
      "userName" : "xxxxx"
   }

   url = "https://shimo.im/api/newforms/forms/xpVxJQJjT3GJ8WhJ/submit" #真实地址 
   #url = "https://shimo.im/api/newforms/forms/pdGc9jGYtdxyTydt/submit"  #测试地址 

   data['duration'] = random.randint(10,50)
   data['responseContent'][0]['text']['content'] = content
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
   shimo(content, username)
   # for x in vercode:
   #    shimo(x)
   #    print(x)
