#coding=utf-8
import django.utils.timezone as timezone

from django.db import models

# Create your models here.
class BaseTable(models.Model):
    create_time = models.DateTimeField('创建时间', default=timezone.now())
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = '公有字段表'
        db_table = 'BaseTable'

class userInfo(BaseTable):
    username = models.CharField('用户名',max_length=8,unique=True,null=False)
    phone = models.CharField('联系手机号',max_length=11,null=False)
    email = models.EmailField('邮箱',max_length=11,null=False)
    role = models.IntegerField('用户角色',null=True)
    password = models.CharField('密码',max_length=16,null=False)

    class Meta:
        verbose_name = '用户信息表'
        db_table = 'userInfo'


class project(BaseTable):
    projectName = models.CharField('项目名称',max_length=10)
    projectdesc = models.TextField('项目说明',null=False)
    username = models.CharField('操作人',max_length=10,null=False)
    class Meta:
        verbose_name = '项目表'
        db_table = 'project'