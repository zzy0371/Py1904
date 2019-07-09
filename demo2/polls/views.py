from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,Http404
# Create your views here.
from .models import Question,Choice,PollsUser
from django.contrib.auth import login as lgi ,logout as lgo ,authenticate
from .forms import *
def checklogin(fun):
    def check(request,*args):
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
        else:
            return redirect(reverse("polls:login"))
    return check


@checklogin
def index(request):
    questions = Question.objects.all()
    return render(request,"polls/index.html",{"questions":questions})



@checklogin
def detail(request,id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        return HttpResponse("id非法")
    except Question.MultipleObjectsReturned:
        return HttpResponse("id非法")
    if request.method == "GET":
        return render(request, "polls/detail.html",locals())
    elif request.method == "POST":
        choiceid = request.POST.get("choice")
        Choice.objects.incresevotes(choiceid)
        return redirect(reverse("polls:result", args=(id,)))

@checklogin
def result(request,id):
    question = get_object_or_404(Question,pk=id)
    return render(request, "polls/result.html",locals())

def login(request):
    lgf = LoginForm()
    rgf = RegistForm()
    if request.method == "GET":
        return render(request,'polls/login.html',{"lgf":lgf,"rgf":rgf})
    elif request.method == "POST":
        # username = request.POST.get("username")
        # password = request.POST.get("password")

        lgf = LoginForm(request.POST)
        if lgf.is_valid():
            username = lgf.cleaned_data["username"]
            password = lgf.cleaned_data["password"]
            user = authenticate(request,username = username,password=password)
            if user:
                lgi(request,user)
                return redirect(reverse("polls:index"))
            else:
                return render(request, 'polls/login.html', {"errors": "登录失败","lgf":lgf,"rgf":rgf})
        else:
            return render(request, 'polls/login.html', {"errors": "登录失败","lgf":lgf,"rgf":rgf})

def logout(request):
    lgo(request)
    return redirect(reverse("polls:login"))
def regist(request):
    if request.method == "POST":
        rgf = RegistForm(request.POST)
        if rgf.is_valid():
            # 先返回一个user 此时没有保存数据库应为密码还没有加密
            user = rgf.save(commit=False)
            # 对user用户设置密码 加密过得密码
            user.set_password(rgf.cleaned_data["password"])
            # 保存数据库
            user.save()
            return redirect(reverse("polls:login"))
        else:
            lgf = LoginForm()
            rgf = RegistForm()
            return render(request, 'polls/login.html', {"errors": "注册失败","lgf":lgf,"rgf":rgf})

        # username =request.POST.get("username")
        # password = request.POST.get("password")
        #
        # try:
        #     user = PollsUser.objects.create_user(username=username, password=password)
        # except:
        #     user = None
        #
        # if user:
        #     return redirect(reverse("polls:login"))
        # else:
        #     return render(request, 'polls/login.html', {"errors":"注册失败"})

    else:
        return HttpResponse("错误")


"""
from django.contrib.auth import login as lgi ,logout as lgo ,authenticate

is_authenticated
request.user
request.user.is_authenticated
objects.create_user
user.set_password()
user.check_password()

"""
