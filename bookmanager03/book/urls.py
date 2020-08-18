from django.urls import path
from book.views import index,readbook,login,login_json,header,detail
from book.views import jsonresponse,to_index
from book import views

from django.urls import converters
# converters 转换器 -- 验证数据的
"""
自定义转换器 
1. 定义转换器类(需求)
2. 要添加到系统的 转换器列表中
3. 使用

"""

class MobileConverter:
    # 正则的属性 必须这么写
    regex='1[3-9]\d{9}'

    # 验证之后的数据,要给视图函数
    def to_python(self,value):
        # value 就是要验证的数据
        return value
#converter, type_name
#converter  -- 转换器类
# type_name -- 名字,这个名字就是 类似于 <int:xxxx> int
converters.register_converter(MobileConverter,'mobile')

urlpatterns = [
    path('index/',index),
    #http://127.0.0.1:8000/1/100/
    # 1/100/
    # 分类id/书籍id/
    # <book_id> 我们可以理解为占位符,它就接收了这个位置的数据
    #
    # path('<cat_id>/<book_id>/',readbook),
    # # 模拟登录
    # path('login/',login),
    # path('login_json/',login_json),
    # path('header/',header),
    # path('detail/',detail),
    # path('jsonresponse/',jsonresponse),
    # path('to_index/',to_index),

    ################
    # register/13312341234/
    # tieba_id 期望是整形!!!
    # 怎么约束数据呢???
    # path('p/<int:tieba_id>/',views.baidu_tieba),
    path('register/<mobile:phone>/',views.tieba_register),


    path('login/',views.tieba_login),
    path('get_cookie/',views.get_cookie),

    # 设置session
    path('set_session/',views.set_session),
    path('get_session/',views.get_session),


]
