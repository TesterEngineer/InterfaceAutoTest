#coding:utf-8


from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from InterfaceTestManage.models import userInfo,project
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.

def login_check(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('username'):
            return HttpResponseRedirect('/login')
        return func(request, *args, **kwargs)
        #func(request, *args, **kwargs)
    return wrapper



'''获取首页'''
@login_check
def getIndex(request):

    username = request.session.get('username','')
    context = {'title': '欢迎进入接口测试页','username':username}
    return  render(request,'index.html',context)

'''统计页面'''
@login_check
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
        count = user_info.count()
        if  count:
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
            #return  request.getRequestDispatcher().forward('/index')

        else:
            print('用户名或密码错误')
            context = {'message':'用户名或密码错误'}
            return JsonResponse(context)



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
@login_check
def projectManager(request,id):
    if request.method == 'GET':
        projects = project.objects
        projectList = projects.all()
        paginator = Paginator(projectList, 8)
        firstPage =id
        #默认id的值传递为0
        if int(firstPage) > 0:
            pages = paginator.page(int(firstPage))
        else:
            firstPage =1
            pages = paginator.page(1)
        projectList =pages.object_list
        #print("-------------"+pages.has_next())
        context = {'projectList':projectList,'pageList':paginator,'currentPag':int(firstPage),"pages":pages}
        print(projectList)
        return  render(request,'project-list.html',context)

'''项目新增'''
@login_check
def projectAdd(request):
    if request.method == 'GET':
        context={'title':'增加项目','btn':'增加'}
        return  render(request,'project-add.html',context)
    if request.method == 'POST':
        projectName = request.POST.get('projectName','')
        projectdesc = request.POST.get('projectdesc','')
        username = request.session.get("username",'')
        project_info = project.objects
        if projectName:
            project_info.create(projectName=projectName,projectdesc=projectdesc,username=username)
            #return HttpResponseRedirect('/api/projectManager/0')
            #context = ''
            context={'sucess':'添加成功啦'}
            return  JsonResponse(context)
            #return HttpResponseRedirect('/api/projectManager/0')
        else:
            context = '添加失败了，请重新添加'
            return JsonResponse({'error':context})


@login_check
def projectEdit(request,id):
    if request.method == 'GET':
        project_obj = project.objects
        project_info = project_obj.get(id=id)
        context = {'projectName':project_info.projectName,'projectdesc':project_info.projectdesc,'btn':'编辑','id':id}
        return render(request,'project-add.html',context)
    elif request.is_ajax():
        projectName = request.POST.get('projectName')
        projectdesc = request.POST.get('projectdesc')
        if int(id):
            project_obj = project.objects
            project_info = project_obj.filter(id=id)
            try:
                project_info.update(projectName=projectName,projectdesc=projectdesc)
                context = {'sucess': '编辑项目成功咯'}
            except:
                context = {'success':'编辑失败了'}
        return JsonResponse(context)

@login_check
def projectDelete(request,id):
    if len(id) > 0:
        project.objects.filter(id=id).delete()
        context={"success":"删除成功！"}
        return  JsonResponse(context)


@login_check
def logout(request):
    #request.session['username'] = None
    if request.method == 'GET':
        try:
            del request.session['username']
        except KeyError:
            print(KeyError)
    return  HttpResponseRedirect('/login')

#关键字参数，key-value映射关系，与位置无关，所以当位置改变，值不变
def name(request,month,year):
    return HttpResponse('name:%s--%s' %(year,month))