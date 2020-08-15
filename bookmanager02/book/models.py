from django.db import models

# Create your models here.
"""
一个类 --> 一个表

class 模型类名(models.Model):
    字段名=model.类型(选项)

字段名 不要采用 Python关键 MySQL关键字 也不要使用 连续的下划线(__)
类型 不建议大家死记
    数据库的时候类型 -- 类型 
字段的选项
    CharField 必须设置 max_length
    verbose_name Admin站点显示(当做一个注释)
create table bookinfo (
    id int primary key auto_incrment,
    name varchar(5) not null default '',
)

我们的表 默认的表名是 自应用名_模型类名
我们可以修改表名


1.定义模型
2.迁移模型
    2.1 生成迁移文件 (系统帮我们生成一个文件,这个文件就是将类转换为数据表的一个文件)
"""

class BookInfo(models.Model):
    # 系统会自动为我们添加id主键
    name=models.CharField(max_length=10,verbose_name='书籍名字')
    # 发布日期
    pub_date=models.DateField(null=True)
    #阅读量
    readcount=models.IntegerField(default=0)
    #评论量
    commentcount=models.IntegerField(default=0)
    #是否删除
    is_delete=models.BooleanField(default=False)

    class Meta:
        db_table='bookinfo'         # 修改表明
        verbose_name='Admin站点里显示'


