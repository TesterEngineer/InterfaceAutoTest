#coding=utf-8


from django.db import models

# Create your models here.
class BaseTable(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = '公有字段表'
        db_table = 'BaseTable'

'''用户'''
class userInfo(BaseTable):
    username = models.CharField('用户名',max_length=8,unique=True,null=False)
    phone = models.CharField('联系手机号',max_length=11,null=False)
    email = models.EmailField('邮箱',max_length=11,null=False)
    role = models.IntegerField('用户角色',null=True)
    password = models.CharField('密码',max_length=16,null=False)

    class Meta:
        verbose_name = '用户信息表'
        db_table = 'userInfo'

'''项目管理'''
class project(BaseTable):
    projectName = models.CharField('项目名称',max_length=10)
    projectdesc = models.TextField('项目说明',null=False)
    username = models.CharField('操作人',max_length=10,null=False)
    class Meta:
        verbose_name = '项目表'
        db_table = 'project'


'''环境管理'''
class Environment(BaseTable):
    path_name=models.CharField('环境名称',null=True,max_length=30)
    host = models.CharField('主机名称',null=True,max_length=50)
    port = models.CharField('端口号',null=False,max_length=8)
    envir_descript = models.TextField('环境简介',null=False)
    username = models.CharField('操作人', max_length=10, null=False)

    class Meta:
        verbose_name = '环境配置表'
        db_table = 'enviroment'