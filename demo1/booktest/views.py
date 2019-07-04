from django.shortcuts import render,redirect,reverse
# MVT  中核心V视图
# 接受请求，处理数据，返回相应
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
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

def deletebook(request,id):
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return redirect( reverse("booktest:list") )


def addhero(request,id):
    book = BookInfo.objects.get(pk=id)
    if request.method == "GET":
        return render(request,"booktest/addhero.html",{"book":book})
    elif request.method == "POST":
        name = request.POST.get("username")
        content = request.POST.get("content")
        hero = HeroInfo()
        hero.name = name
        hero.content = content
        hero.book = book
        hero.save()
        return redirect(reverse("booktest:detail",args=(id,)))

def deletehero(request,id):
    hero = HeroInfo.objects.get(pk = id)
    bookid = hero.book.id
    hero.delete()
    # return HttpResponse("删除成功")

    # return HttpResponseRedirect("/detail/"+ str(bookid) +  "/")

    # result = reverse("booktest:detail", args=(bookid,))
    # return redirect("/detail/"+ str(bookid) + "/")
    return redirect( reverse("booktest:detail",args=(bookid,) ) )



"""
正常请求：一次请求返回一次响应
重定向：发起一次请求302    在处理过程中再次发起请求  返回响应200 

"""