from django.http import HttpResponse
from django.shortcuts import render


from django.http import HttpRequest

# Create your views here.
def index(request):


    ##############################################
    """
    http://ip:port/path1/path2/?key1=value1&key2=value
    我们的路经 是由 2部分组成  ? 是一个分割符
    ?前边是 http://ip:port/path1/path2/        路由
    ?后边是 key1=value1&key2=value             查询字符串
    """

    # score=100
    # #
    # books=BookInfo.objects.all()
    # 肯定得执行一次, 因为要把数据库的数据查询出来,放到缓存里
    # [book.id for book in books ]  使用缓存
    # [book.id for book in books ]  使用缓存
    # [book.id for book in books ]  使用缓存

    # [book.id for book in BookInfo.objects.all()] #没有 用缓存
    # [book.id for book in BookInfo.objects.all()] #没有 用缓存
    # [book.id for book in BookInfo.objects.all()] #没有 用缓存
    return HttpResponse('ok ')


"""
http://127.0.0.1:8000/1/100/

1/100/
"""
# def readbook(request,book_id):
# def readbook(request,book_id,cat_id):
def readbook(request,cat_id,book_id):

    # content='book_id {} ,cat_id ~~~~~ {}'.format(book_id,cat_id)

    #################GET########################
    print(request.GET)
    #<QueryDict: {'keyword': ['abc']}>
    # Dict  -- 字典
    # request.GET 获取 查询字符串
    # request.GET.get 获取字典数据
    # keyword=request.GET.get('keyword')
    # print(keyword)
    # BookInfo.objects.filter(name__contains=keyworks)

    keyword=request.GET.getlist('keyword')
    print(keyword)
    return HttpResponse('ok')


def login(request):

    # form-data 数据 我们是通过 request.POST 来接收
    print(request.POST)

    return HttpResponse("login")


"""
只是和python的字典很像
{
    "key":value,
    "girl-firends":["Tom","Rose"]
}


{
"code":0,
"whwswswws":"iIIh6i 8s1UjYQvkpfogpQg==",
"openall":1,
"openalltouch":1,
"processtype":1
}
"""

def login_json(request):

    # 接收非表单数据 用 request.body
    # 1.接收数据
    body=request.body
    # print(body)
    # b'{\n\t"username":"itcast",\n\t"password":"123"\n}'

    # 2. 对bytes数据进行解码
    #
    body_str = body.decode()
    """
    body.decode() 数据是  JSON形式的字符串 --- 字符串
    {
        "username":"itcast",
        "password":"123"
    }
    """
    # 3. 将 JSON形式的字符串 转换为字典
    import json
    body_dict = json.loads(body_str)
    # body_dict 就是字典了
    print(body_dict)
    return HttpResponse('json')



def header(request):

    print(request.method)
    if request.method == 'GET':
        print('GET')
    elif request.method == 'POST':
        print('POST')
    else:
        print(request.method)

    # 获取请求头的数据
    print(request.META)
    """
    {'PATH': '/home/ubuntu/.virtualenvs/py3_django_40/bin:/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/local/rabbitmq/sbin', 'LC_MEASUREMENT': 'zh_CN.UTF-8', 'XAUTHORITY': '/run/user/1000/gdm/Xauthority', 'XMODIFIERS': '@im=fcitx', 
    'LC_TELEPHONE': 'zh_CN.UTF-8', 
    'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/local/share:/usr/share:/var/lib/snapd/desktop',
     'GDMSESSION': 'ubuntu', 
     'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path', 
     'LC_TIME': 'zh_CN.UTF-8', 'PAPERSIZE': 'a4', 'TEXTDOMAINDIR': '/usr/share/locale/', 'GTK_IM_MODULE': 'fcitx', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path', 'PS1': '(py3_django_40) ', 'XDG_CURRENT_DESKTOP': 'ubuntu:GNOME', 'SSH_AGENT_PID': '2161', 'QT4_IM_MODULE': 'fcitx', 'LC_PAPER': 'zh_CN.UTF-8', 'SESSION_MANAGER': 'local/python:@/tmp/.ICE-unix/2070,unix/python:/tmp/.ICE-unix/2070', 'USERNAME': 'ubuntu', 'LOGNAME': 'ubuntu', 'PWD': '/home/ubuntu/Desktop/40/code/bookmanager03', 'IM_CONFIG_PHASE': '2', 'PYCHARM_HOSTED': '1', 'LANGUAGE': 'zh_CN', 'GJS_DEBUG_TOPICS': 'JS ERROR;JS LOG', 'PYTHONPATH': '/home/ubuntu/Desktop/40/code/bookmanager03:/home/ubuntu/software/pycharm-2019.1.3/helpers/pycharm_matplotlib_backend:/home/ubuntu/software/pycharm-2019.1.3/helpers/pycharm_display', 'SHELL': '/bin/bash', 'LC_ADDRESS': 'zh_CN.UTF-8', 'GIO_LAUNCHED_DESKTOP_FILE': '/usr/share/applications/pycharm.desktop', 'OLDPWD': '/home/ubuntu/software/pycharm-2019.1.3/bin', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'GTK_MODULES': 'gail:atk-bridge', 'VIRTUAL_ENV': '/home/ubuntu/.virtualenvs/py3_django_40', 'CLUTTER_IM_MODULE': 'xim', 'TEXTDOMAIN': 'im-config', 'XDG_SESSION_DESKTOP': 'ubuntu', 'SHLVL': '0', 'LC_IDENTIFICATION': 'zh_CN.UTF-8', 'LC_MONETARY': 'zh_CN.UTF-8', 'QT_IM_MODULE': 'fcitx', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/etc/xdg', 'LANG': 'zh_CN.UTF-8', 'XDG_SESSION_ID': '2', 'XDG_SESSION_TYPE': 'x11', 'DISPLAY': ':0', 'LC_NAME': 'zh_CN.UTF-8', 'PYCHARM_DISPLAY_PORT': '42981', 'PYTHONIOENCODING': 'UTF-8', 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1', 'DESKTOP_SESSION': 'ubuntu', 'USER': 'ubuntu', 'XDG_MENU_PREFIX': 'gnome-', 'GIO_LAUNCHED_DESKTOP_FILE_PID': '88808', 'QT_ACCESSIBILITY': '1', 'WINDOWPATH': '2', 'LC_NUMERIC': 'zh_CN.UTF-8', 'GJS_DEBUG_OUTPUT': 'stderr', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'XDG_SEAT': 'seat0', 'DJANGO_SETTINGS_MODULE': 'bookmanager03.settings', 'PYTHONUNBUFFERED': '1', 'GNOME_SHELL_SESSION_MODE': 'ubuntu', 'XDG_VTNR': '2', 'XDG_RUNTIME_DIR': '/run/user/1000', 'HOME': '/home/ubuntu', 'TZ': 'UTC', 'RUN_MAIN': 'true', 'SERVER_NAME': 'localhost', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/header/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_USER_AGENT': 'PostmanRuntime/7.13.0', 'HTTP_ACCEPT': '*/*', 'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_POSTMAN_TOKEN': '42f16f3b-5c5e-4c9f-b8bc-979835ebb826', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'HTTP_CONNECTION': 'keep-alive', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x7f6414dc5a90>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}

    """
    http_itcast=request.META['HTTP_ITCAST']
    print(http_itcast)
    return HttpResponse('header')



def detail(request):

    # content 不能是对象
    # content 就是响应体的数据

    # content_type 响应数据的类型
    # MIME 类型
    # 语法格式: 大类/小类
    # text/html  application/json

    # status 响应状态码
    # 200 表示成功
    response = HttpResponse(content='内容',content_type='text/html',status=200)
    #设置响应头的数据
    response['itcast']='aaaaa'

    return response

from django.http import JsonResponse
def jsonresponse(request):


    userinfo = {
        'user_id':123,
        'username':'itcast'
    }
    # data  传递的是字典
    return JsonResponse(userinfo)

    # userinfo = {
    #     'user_id':123,
    #     'username':'itcast'
    # }
    #
    # # json.dumps 是将字段转换为字符串
    # import json
    # user_str=json.dumps(userinfo)
    #
    # return HttpResponse(user_str)

from django.shortcuts import redirect
def to_index(request):

    return redirect('/detail')
    # redirect 重定向 如果跳转到其他网址页面 必须以http://开头
    # return redirect('www.itcast.cn')  错误的!!!
    return redirect('http://www.itcast.cn')

"""
缓存 的概念
当前 
    内存  -- 读取数据非常快.断电数据没有了
    硬盘  -- 读取速度比较慢. 断电数据存在
    
mysql的数据默认是存储在 硬盘
缓存的概念 -- 把硬盘的数据读取到内存 

"""
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


"""
ORM最终也是转换为了sql语句来执行

我们可以通过查看 sql语句 有没有执行,来判断 它是否惰性执行


"""

############################0818代码###########################################################################


def baidu_tieba(request,tieba_id):


    return HttpResponse(tieba_id)


def tieba_register(request,phone):


    return HttpResponse(phone)


##########################cookie#############################
"""
1. cookie 是保存 在 浏览器端的!!!!
2. cookie 是服务器生成,设置的!!!!
3. cookie 的数据是 key-value 形式的
4. cookie 是基于域名的(访问这个网址设置的cookie,只有这个网址能获取).
    当我们在浏览器中,访问这个域名的时候,浏览器会携带所有cookie

模拟一个场景,模拟登录, 我们登录的时候传递用户名
服务器把用户名保存在cookie中

1. 看到效果
2. 深入理解这个流程
"""
def tieba_login(request):

    # 0. 获取用户名
    username=request.GET.get('username')

    response = HttpResponse('set_cookie')

    # 1.设置cookie 是调用 response 实例对象的 set_cookie 方法
    # max_age= 设置cookie的有效期
    # 秒数 返回响应开始,之后max_age秒过期
    response.set_cookie(key='username', value=username,max_age=10000)
    response.set_cookie(key='user_id', value='123')
    response.set_cookie(key='phono', value='http://www.baidu.com')

    # 删除cookie 删除cookie的本质是设置max_age = 0
    # response.delete_cookie()
    return response


def get_cookie(request):

    print(request.COOKIES)
    username=request.COOKIES.get('username')

    # user=User.ojects.get
    # {'user_id': '123', 'phono': 'http://www.baidu.com'}
    # 字典数据
    return HttpResponse(username)


"""
1. session 是保存在服务器端
2. 默认保存在 数据库中
3. 我们的session依赖于cookie技术
    
        当我们第一次 设置session的时候,我们的数据不仅会保存在数据库中,
        还是生成一个 session_key.这个session_key 会设置到cookie中
        我们的浏览器接收到这个cookie,会保存
        
        我们第二次及其之后的请求,都会携带这个cookie,这个时候我们读取session
        信息的时候,就是凭借这个cookie信息来验证的
4. 我们一般采用session技术实现状态保持
    一般我们会在 登录之后,设置session.
"""

def set_session(request):

    # 1. 设置session
    request.session['user_id']=1234567890
    # 删除某一个数据
    # del  request.session[key]

    # 如果value是一个整数，session将在value秒没有活动后过期。
    # 如果value为0，那么用户session的Cookie将在用户的浏览器关闭时过期。
    # 如果value为None，那么session有效期将采用系统默认值， 默认为两周
    request.session.set_expiry(None)

    return HttpResponse('set_session')

def get_session(request):

    # 1. 获取session
    # user_id=request.session['user_id']
    # get 不容易异常
    user_id=request.session.get('user_id')
    # User.objects.get(id=user_id)

    # 2. 删除session数据.
    # 只是删除session内容,key保留
    # request.session.clear()

    # 3. 删除session的数据,同时把sesion的key也删除
    # 从数据库里删除数据了
    # request.session.flush()

    return HttpResponse(user_id)

#####################################
# 视图函数 既可以 get也可以post
def jd_register(request):

    # GET
    # POST
    print(request.method)
    if request.method == 'GET':
        return HttpResponse('get')
    elif request.method == 'POST':
        return HttpResponse('post')
    else:
        return HttpResponse('other')

    return HttpResponse('jd_register')


####################定义类视图#############################

# class 类名(父类):
#     属性
#     方法
from django.views import View
class RegisterView(View):

    # 我们用GET方式 请求的
    def get(self,request):

        return HttpResponse('view get')

    # 我们用POST方式,请求的
    def post(self,request):

        return HttpResponse('view post')





# class Person:

# class Person(object):
#
#     #属性
#     name=''
#     age=0
#
#     #方法 -- 实例方法,对象方法
#     def eat(self):
#         print('eat')
#
#     # 静态方法
#     @staticmethod
#     def play():
#         print('static')
#
#
#     @classmethod
#     def learn(cls):
#         print('classmethod')
#
#
# p = Person()
# # p 实例对象
# p.eat()
# #静态方法
# Person.play()
# #类方法
# Person.learn()










