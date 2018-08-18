#coding:utf-8
from django.shortcuts import render
from InterfaceTestManage.models import userInfo
from django.http import *
from django.utils.datastructures import MultiValueDictKeyError

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
        username = request.POST['username']
        password = request.POST['password']


        user = userInfo.objects
        user_info = user.filter(username=username,password=password)
        if user_info:
            #登录成功，如果存在用户名和密码
            #remeberPw = request.POST['remeberPw']
            remeberPw = request.POST.get('remeberPw')
            if  remeberPw:
                print("用户记住了密码啊！！")
            #    request.COOKIES['login_pw']=
            return HttpResponseRedirect('/index')
        else:
            print('用户名或密码错误')
            return HttpResponseRedirect('/login')



'''注册'''
def register(request):
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
        if(username is not None and len(username) <=8 and password is not None
            and  len(password)<=16 ):
            try:
                user_info.create(username=username,password=password,phone=phone)
                return HttpResponseRedirect('/login')
            except MultiValueDictKeyError as error:
                #如果想html页面通知发生错误了？比如500之内的。。
                print("用户名重复了啊")
                return HttpResponseRedirect('/register')

            # user_info.create(username=username,password=password,phone=phone)
            # return HttpResponseRedirect('/login')
        else:
            fail='注册失败,请重新注册'
            print("注册失败")
            return  HttpResponseRedirect('/register')
