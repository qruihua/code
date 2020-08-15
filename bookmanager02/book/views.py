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



####################删除数据###################################

# 方式1
# 1. 先查询出某一个对象
# select * from bookinfo where id=6
book=BookInfo.objects.get(id=6)
# 物理删除
book.delete()

# 物理删除  -- 从数据库中把数据直接删除
# 逻辑删除  -- 修改一个标记位.数据没有真正删除.

# 方式2
BookInfo.objects.filter(id=5).delete()

##########################查询###################################

# get  查询单一结果 就是一个或者没有.没有的化会报异常
# select * from bookinfo where id=1
book=BookInfo.objects.get(id=1)
# 模型类名.objects.get(字段名=值)
# 字段名 是我们的是属性就可以.只不过用id用的多
book=BookInfo.objects.get(name='天龙八部')

# 所有的结果
BookInfo.objects.all()
# 查询结果集 -- 实际就是一个列表
# <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 笑傲江湖>, <BookInfo: 雪山飞狐>]>
from book.models import PeopleInfo
PeopleInfo.objects.all().count()



#############################################################
"""
模型类名.objects.filter/exclude/get()

filter过滤出多个结果(0,1,n个) []
get过滤单一结果
exclude排除掉符合条件剩下的结果 (相当于not)

语法形式是一样的(以filter为例):
    filter(属性__运算符=值)   特别强调: 2个下划线
    
"""

# 查询编号为1的图书
# exact 是等于
BookInfo.objects.get(id__exact=1)
# 一般 等于我们就直接写
BookInfo.objects.get(id=1)

BookInfo.objects.filter(id__exact=1)
BookInfo.objects.filter(id=1)

# 结果对比区别
BookInfo.objects.get(id=1)
BookInfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
# select * from bookinfo where name is null
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
# select * from bookinfo where id=1 or id=3 or id=5
# select * from bookinfo where id in (1,3,5)
BookInfo.objects.filter(id__in=[1,3,5])
# 查询编号大于3的图书
# gt 大于         great
# gte 大于等于     equal
# lt 小于         less then litte
# lte 小于等于
BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书

BookInfo.objects.filter(pub_date__gt='1990-1-1')



#################F对象##################################
"""
之前的查询都是对象的属性与常量值比较，两个属性怎么比较呢？ 
答：使用F对象，被定义在django.db.models中。

查询阅读量大于等于评论量的图书。

filter(字段__运算符=F('字段值'))

"""
from django.db.models import F

BookInfo.objects.filter(readcount__gte=F('commentcount'))


##################Q对象##########################

# 查询阅读量大于20，并且编号小于3的图书


BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)

BookInfo.objects.filter(readcount__gt=20,id__lt=3)

# filter(Q()&Q()) 并且
# filter(Q(字段__运算符=值)|Q(字段__运算符=值)) 或者

# 查询阅读量大于20，或者 编号小于3的图书
from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))


# ~Q 非 not
# 查询id不为3
BookInfo.objects.filter(~Q(id=3))
BookInfo.objects.exclude(id=3)











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