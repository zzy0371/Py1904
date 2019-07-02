from django.db import models
# MVT 中的M 数据没模型
# ORM对象
# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    # ORM 中book为BookInfo的实例  但是数据库中book存储的仍然为id
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

"""
每一个模型类都自带管理器 objects
save()
delete()
.all()
一对多的关系
多找一： 多方实例名.关系字段名
一找多: 一方实例名.多方类名小写_set.all()
"""

