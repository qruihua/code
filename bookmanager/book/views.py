from django.shortcuts import render

# Create your views here.
"""
视图函数

Python函数 
1. 要求函数的第一个参数是 请求的实例对象
2. 要求函数有响应的返回
"""
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):

    return HttpResponse('ok')

