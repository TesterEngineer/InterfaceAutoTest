#coding:utf-8
from django.shortcuts import render
from InterfaceTestManage.models import userInfo
from django.http import *

# Create your views here.

'''获取首页'''
def getIndex(request):
    context = {'title':'欢迎进入接口测试页'}
    return  render(request,'index.html',context)

'''统计页面'''
def welcome(request):
    context={'title':'主页统计页面'}
    return  render(request,'welcome.html',context)

'''登录'''
def login(request):
    if request.method == 'GET':
        context = {'title':'API接口自动化测试系统登录'}
        return  render(request,'login.html',context)
    else:
        #
        return  HttpResponseRedirect('/index')

'''注册'''
def reigster(request):
    if request.method == 'GET':
        content={'title':'注册账号'}
        return render(request,'user-add.html',content)
    else:
        username= request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        #TODO 角色这块后面再做
        password = request.POST['password']

        user_info = userInfo.objects
        #将数据进行注册
        #后台对获取的数据进行校验,之后在传递.
        user_info.create(username=username,password=password,phone=phone)
        return HttpResponseRedirect('/login')
