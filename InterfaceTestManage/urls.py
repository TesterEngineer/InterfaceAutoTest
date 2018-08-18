# -*- coding: UTF-8 -*-
"""
@author:Duan jun ming
@file: urls.py
@time: 2018/08/06
qq:1032241157
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from InterfaceTestManage import views

urlpatterns = [
   url(r'^login$',views.login),
   url(r'^register$',views.reigster),
]
