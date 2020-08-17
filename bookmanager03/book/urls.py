from django.urls import path
from book.views import index,readbook,login,login_json,header,detail
from book.views import jsonresponse,to_index
urlpatterns = [
    path('index/',index),
    #http://127.0.0.1:8000/1/100/
    # 1/100/
    # 分类id/书籍id/
    # <book_id> 我们可以理解为占位符,它就接收了这个位置的数据
    #
    path('<cat_id>/<book_id>/',readbook),
    # 模拟登录
    path('login/',login),
    path('login_json/',login_json),
    path('header/',header),
    path('detail/',detail),
    path('jsonresponse/',jsonresponse),
    path('to_index/',to_index),

]
