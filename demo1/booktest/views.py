from django.shortcuts import render,redirect,reverse
# MVT  中核心V视图
# 接受请求，处理数据，返回相应
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import BookInfo,HeroInfo
from django.views.generic import View,TemplateView,ListView

class IndexTemplateView(TemplateView):
    template_name = "booktest/index.html"
    def get_context_data(self, **kwargs):
        return {"username":"zzy"}

class IndexView(View):
    def get(self,request):
        return render(request, "booktest/index.html", {"username": "zzy"})

def index(request):
    return render(request,"booktest/index.html",{"username":"zzy"})

class ListView(ListView):
    model = BookInfo
    template_name = "booktest/list.html"
    context_object_name = "books"

    # def get_queryset(self):
    #     return BookInfo.objects.all()


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
        gender = request.POST.get("gender")
        gender1 = request.POST.get("gender1")
        HeroInfo.objects.addhero(name,content,book,gender,gender1)
        # hero = HeroInfo()
        # hero.name = name
        # hero.content = content
        # hero.book = book
        # hero.gender = gender
        # hero.type = gender1
        # hero.save()
        return redirect(reverse("booktest:detail",args=(id,)))

def deletehero(request,id):
    hero = HeroInfo.objects.get(pk = id)
    bookid = hero.book.id
    hero.delete()
    return redirect( reverse("booktest:detail",args=(bookid,) ) )



"""
正常请求：一次请求返回一次响应
重定向：发起一次请求302    在处理过程中再次发起请求  返回响应200 

"""