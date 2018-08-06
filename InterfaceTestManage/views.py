#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import *

def login(request):
    print("-----------------------")
    return  render(request,'login.html')