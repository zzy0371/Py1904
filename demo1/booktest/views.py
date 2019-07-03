from django.shortcuts import render
# MVT  中核心V视图
# 接受请求，处理数据，返回相应
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo,HeroInfo

def index(request):
    return render(request,"booktest/index.html",{"username":"zzy"})
def list(request):
    books = BookInfo.objects.all()
    return render(request,"booktest/list.html",{"books":books})

def detail(request,id):
    book = BookInfo.objects.get(pk=id)
    return render(request,"booktest/detail.html",{"book":book})