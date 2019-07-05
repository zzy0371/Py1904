from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    desc = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc

class ChoiceManager(models.Manager):
    def incresevotes(self,id):
        c = self.get(pk = id)
        c.votes += 1
        c.save()

class Choice(models.Model):
    desc = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    objects = ChoiceManager()
    def __str__(self):
        return self.desc

class Temp(models.Model):
    title = models.CharField(verbose_name="标题", help_text="标题", max_length=20)
    desc = models.CharField(verbose_name="描述", help_text="描述", max_length=20,null=True,blank=True,db_column="描述")
    class Meta:
        verbose_name = "Temp表"
        verbose_name_plural = "Temp表"
        db_table = "temptable"
        ordering = ["title","-desc"]

class MyUser(models.Model):
    telephone = models.CharField(max_length=11,)
    default_user = models.OneToOneField(User, on_delete=models.CASCADE)


class Account(models.Model):
    username = models.CharField(max_length=20)

class Contact(models.Model):
    telephone = models.CharField(max_length=20)
    acc = models.OneToOneField(Account,on_delete=models.CASCADE)

class Host(models.Model):
    name = models.CharField(max_length=20)

class Application(models.Model):
    name = models.CharField(max_length=20)
    h = models.ManyToManyField(Host)




