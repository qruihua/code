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

