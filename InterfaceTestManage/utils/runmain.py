#-*- coding:utf-8 _*-
"""
@author:Duan jun ming
@file: runmain.py 处理请求运行
@time: 2018/09/20
qq:1032241157
"""
import requests
class runcase:

    def request_send(self,method,url,data):
        if method == 'POST':
            response = requests.post(url=url,data=data)
        elif method == 'GET':
            response=requests.get(url=url)
        return  response
