from django.shortcuts import render
# MVT  中核心V视图
# 接受请求，处理数据，返回相应
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("这里是首页   <a href='/list/'>跳转到列表页</a> ")

def list(request):
    s = """
    <br>
    <a href='/detail/1/'>跳转到详情页1</a> 
    <br>
    <a href='/detail/2/'>跳转到详情页2</a> 
    <br>
    <a href='/detail/3/'>跳转到详情页3</a> 
    """
    return HttpResponse("这里是列表页 %s"%(s,))

def detail(request,id):
    return HttpResponse("这里是%s详情页 <a href='/'>跳转到首页</a> "%(id,))