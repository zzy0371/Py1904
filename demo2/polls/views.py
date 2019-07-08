from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,Http404
# Create your views here.
from .models import Question,Choice,PollsUser
from django.contrib.auth import login as lgi ,logout as lgo ,authenticate

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
    if request.method == "GET":
        return render(request,'polls/login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username = username,password=password)
        if user:
            lgi(request,user)
            return redirect(reverse("polls:index"))
        else:
            return render(request, 'polls/login.html', {"errors": "登录失败"})

def logout(request):
    lgo(request)
    return redirect(reverse("polls:login"))
def regist(request):
    if request.method == "POST":
        username =request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = PollsUser.objects.create_user(username=username, password=password)
        except:
            user = None

        if user:
            return redirect(reverse("polls:login"))
        else:
            return render(request, 'polls/login.html', {"errors":"注册失败"})


"""
from django.contrib.auth import login as lgi ,logout as lgo ,authenticate

is_authenticated
request.user
request.user.is_authenticated
objects.create_user
user.set_password()
user.check_password()

"""
