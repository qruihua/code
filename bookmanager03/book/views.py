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