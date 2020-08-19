from django.utils.deprecation import MiddlewareMixin

class Test1MiddleWare(MiddlewareMixin):

    def process_request(self,request):

        print("请求前执行11111")
        # username=request.COOKIES.get('username')
        # if username:
        #     # 查询数据库,查询这个用户
        #     print('信息信息')
        # else:
        #     print("用户没有cookie信息,是一个新用户")


    def process_response(self,request,response):
        # 视图已经处理了响应
        # 还没有给浏览器
        print("响应前执行111111")

        return response


class Test2MiddleWare(MiddlewareMixin):

    def process_request(self,request):

        print("请求前执行22222")
        # username=request.COOKIES.get('username')
        # if username:
        #     # 查询数据库,查询这个用户
        #     print('信息信息')
        # else:
        #     print("用户没有cookie信息,是一个新用户")


    def process_response(self,request,response):
        # 视图已经处理了响应
        # 还没有给浏览器
        print("响应前执行222222")

        return response