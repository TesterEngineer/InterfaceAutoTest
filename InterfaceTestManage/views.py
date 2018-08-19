#coding:utf-8
from django.shortcuts import render
from InterfaceTestManage.models import userInfo,project
from django.http import *
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

'''获取首页'''
def getIndex(request):

    username = request.session.get('username','')
    context = {'title': '欢迎进入接口测试页','username':username}
    return  render(request,'index.html',context)

'''统计页面'''
def welcome(request):
    context={'title':'主页统计页面'}
    return  render(request,'welcome.html',context)

'''登录'''
def login(request):
    if request.method == 'GET':
        #如果用户第一次点击了记住密码，先从Cookie里面取值，在填充。
        username=request.COOKIES.get('username','') #后面的空值是默认值，如果不填默认为None
        password = request.COOKIES.get('password','')
        context = {'title':'API接口自动化测试系统登录','username':username,'password':password}
        return  render(request,'login.html',context)
    else:
        #post发送请求，就是表单里面的请求进来了
        username = request.POST['username']
        password = request.POST['password']

        user = userInfo.objects
        user_info = user.filter(username=username,password=password)
        if user_info:
            #登录成功，如果存在用户名和密码
            #remeberPw = request.POST['remeberPw']
            request.session['username'] = username
            remeberPw = request.POST.get('remeberPw')
            redirect_index = HttpResponseRedirect('/index')
            if  remeberPw:
                print("用户记住了密码啊！！")
                redirect_index.set_cookie('username',username)
                redirect_index.set_cookie('password',password)

            return redirect_index
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

'''项目管理'''
def projectManager(request):
    if request.method == 'GET':
        projects = project.objects
        projectList = projects.filter()
        context = {'projectList':projectList}
        print(projectList)
        return  render(request,'project-list.html',context)

'''项目新增'''
def projectAdd(request):
    if request.method == 'GET':
        return  render(request,'project-add.html')
    if request.method == 'POST':
        projectName = request.POST.get('projectName')
        projectdesc = request.POST.get('projectdesc')
        username = request.session.get("username")
        project_info = project.objects
        if projectName:
            project_info.create(projectName=projectName,projectdesc=projectdesc,username=username)
            return HttpResponseRedirect('/projectList')
        else:
            context = '添加失败了，请重新添加'
            return JsonResponse({'context1':context})
        # print("s输出了什么？")
        # context1 = '添加失败了，请重新添加'
        # flag = False
        # return JsonResponse({'context1': context1,'flag':flag})
        #print('xxx')

def testajax(request):
    if request.method == "GET":
        return render(request, 'test.html')
    else:
        return  JsonResponse({'test':'hello js'})

