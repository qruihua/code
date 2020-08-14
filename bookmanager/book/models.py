from django.db import models

# Create your models here.
"""
2个表

书籍表             --->   类
id	name
1	西游记
2	三国演义

人物表             --->    类
id	name	gender	book
1	孙悟空	False	1
2	白骨精	True	1
3	曹操	    False	2
4	貂蝉	    True	2

class 模型类名(models.Model):
    字段名=models.类型(选项)
    
    类型 和 选项明天会重点讲解 今天就是先了解一下
"""
class BookInfo(models.Model):
    # django会自动为我们生成一个id的主键
    #id

    # CharField 对应数据库中的 varchar(M)
    name=models.CharField(max_length=10)


# 今天晚上把面向对象的内容 回顾一下
class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField(default=False)  #设置默认值
    #外键
    # 主表数据删除,on_delete=models.CASCADE 从表数据也跟着删除
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

"""
1.定义类 (定义了类,但是不会自动创建表)
2.我们需要迁移
    2.1 先生成迁移文件
        python manage.py makemigrations
    2.2 执行迁移文件 -- 就创建了数据表
        python manage.py migrate
3.
"""





