"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 这个是固定写法.
# urlpatterns = []
"""
当用户在浏览器中输入网址后, 
用户的网址会顺次和我们的 urlpatterns 中的每一项进行比较
如果一致,则进入到响应的视图中
如果不一致,则继续往下比较.
直到所有的每一项都比较完成.如果最终都没有一致的,则返回 404


http://127.0.0.1:8000/admin/

我们的路由: http://ip:port/path/?key=value&key=value
其中 http://ip:port/  和 ?key=value&key=value 是不进行路由匹配的

"""
from book.views import index
urlpatterns = [
    path('admin/', admin.site.urls),

    # 参数1: 路由
    # 参数2: 视图函数名
    path('index/',index),
]
