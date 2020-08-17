from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    return HttpResponse('ok')


###############关联查询#############################
"""
查询书籍为1的所有人物信息

查询人物为1的书籍信息
"""
from book.models import BookInfo,PeopleInfo

book=BookInfo.objects.get(id=1)
book.peopleinfo_set.all()

person=PeopleInfo.objects.get(id=1)
#person.book 的值 是这个人物 关联的模型 的实例对象数据
person.book
person.book.commentcount


###############关联查询过滤查询############################

# 查询图书，要求图书人物为"郭靖"


# BookInfo.objects.filter(关联模型类名小写__字段__运算符=值)
# __ 2个连续的下划线


BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
#或者
BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')



#  我们在查询多的数据的时候,条件为1的
# 模型类名.objects.filter(外键__字段__运算符=值)
# 查询书名为“天龙八部”的所有人物

PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__name__exact='天龙八部')
# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)




