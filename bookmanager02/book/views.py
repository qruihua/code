from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

    return HttpResponse('ok')

######################z增加数据#######################################

"""
Model --> ORM --> 面向对象操作数据库

我们在进行增删改查的时候 就采用面向对象的操作

"""
# 方式1
from book.models import BookInfo

book=BookInfo(
    name='葵花宝典',
    pub_date='2020-1-2',
    readcount=100
)

# 必须调用 对象的save方法 数据才会保存到数据中
"""
save方法的本质是 获取到对象的属性和属性值,调用ORM的数据保存方法
转换为一条sql语句,然后让mysql去执行
"""
book.save()

# 方式2
# 数据可以直接保存
# objects 相当于模型的管理属性

book=BookInfo.objects.create(
    name='django',
    pub_date='2005-1-1',
    readcount=666,
    commentcount=999
)

#######################修改数据##################################

# 方式1
# 1. 先查询出某一个对象
# select * from bookinfo where id=6
book=BookInfo.objects.get(id=6)
# 2.调用对象的属性来赋值
book.name='Flask'
book.readcount=1000
# 3. 调用save方法
book.save()

# 方式2
# select * from bookinfo where id=6
BookInfo.objects.filter(id=6).update(name='爬虫',
                                     readcount=789,
                                     commentcount=123,
                                     pub_date='2010-1-1')









# class Person(object):
#     name=''
#     age=10
#
#     def eat(self):
#         print('eat')
#
#     @staticmethod
#     def play(self):
#         pass
#
# #创建一个对象 实例化
# p=Person()
# p.eat()