#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import *

'''登录'''
def login(request):
    print("-----------------------")
    return  render(request,'login.html')

'''注册'''
def reigster(request):
    if request.method == 'GET':
        content={'title':'注册账号'}
        return render(request,'user-add.html',content)
