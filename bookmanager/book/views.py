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
    context = {
        'name':'想了解更多吗?点击我哦'
    }
    # 参数1: 请求   就是 浏览器发起的请求.把这个请求 先给模板.模板用不用是另外一回事
    # 参数2: 模板文件
    return render(request,'book/index.html',context=context)
    # return HttpResponse('ok')

