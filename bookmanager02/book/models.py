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
    # 当我们在人物的模型中,定义了外键之后, 系统会自动的为当前
    # 外键的模型添加一个 属性
    # 关联模型小写_set
    #  peopleinfo_set = [PeopleInfo,PeopleInfo,....]
    # 先记住书写形式
    class Meta:
        db_table='bookinfo'         # 修改表明
        verbose_name='Admin站点里显示'


    def __str__(self):
        return self.name

# 只要模型有改变,我们就要生成迁移文件,然后执行迁移
class PeopleInfo(models.Model):

    # 枚举类型
    GENDER_CHOICE=(
        (0,'male'),
        (1,'female')
    )

    name=models.CharField(max_length=20)
    #性别
    gender=models.SmallIntegerField(choices=GENDER_CHOICE,default=0)
    #描述
    description=models.CharField(max_length=100)
    #是否删除
    is_delete=models.BooleanField(default=False)
    # 外键
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table='peopleinfo'

    def __str__(self):
        return self.name
"""
黑帮老大    1           入狱--判处枪决

黑帮小弟    n       ①劫狱不让老大死  ② 不管 老大死就死   ③ 小弟跟着死


书籍      1

人物      n
    书籍的外键

西游记  -- 孙悟空 猪八戒 唐僧
"""