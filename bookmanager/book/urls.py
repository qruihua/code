from django.urls import path
from book.views import index


# 固定写法
urlpatterns = [
    path('index/',index)
]