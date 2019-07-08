from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,Http404
# Create your views here.
from .models import Question,Choice


def checklogin(fun):
    def check(request,*args):
        # username = request.COOKIES.get("username")
        username = request.session.get("username")
        print(username,"++++++++++++")
        if username:
            return fun(request,*args)
        else:
            return redirect(reverse("polls:login"))
    return check


@checklogin
def index(request):
    questions = Question.objects.all()
    # username = request.COOKIES.get("username")
    username = request.session.get("username")
    return render(request,"polls/index.html",locals())



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


        # 没有重定向，如果刷新浏览器会 再次发起post请求，结果不对
        # return render(request,"polls/result.html",{"question":question})
        return redirect(reverse("polls:result", args=(id,)))

@checklogin
def result(request,id):
    # question = Question.objects.get(pk = id)
    get_object_or_404(Question,pk=id)
    return render(request, "polls/result.html",locals())

def login(request):
    if request.method == "GET":
        return render(request,'polls/login.html')
    elif request.method == "POST":
        # 检测用户名密码是否对应
        # 1登录成功需要存储cookie
        # response = redirect(reverse("polls:index"))
        # response.set_cookie("username",request.POST.get("username"))
        # return response

        # 2使用session存储信息
        request.session["username"] = request.POST.get("username")
        return redirect(reverse("polls:index"))

def logout(request):
    # print(dir(request.COOKIES))
    # res = redirect(reverse("polls:login"))
    # res.delete_cookie("username")
    # return res

    request.session.flush()
    return redirect(reverse("polls:login"))

