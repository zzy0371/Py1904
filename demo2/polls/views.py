from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.
from .models import Question,Choice

def index(request):
    questions = Question.objects.all()
    return render(request,"polls/index.html",locals())


def detail(request,id):
    question = Question.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "polls/detail.html",locals())
    elif request.method == "POST":
        choiceid = request.POST.get("choice")
        # choice = Choice.objects.get(pk = choiceid)
        # choice.votes += 1
        # choice.save()
        Choice.objects.incresevotes(choiceid)


        # 没有重定向，如果刷新浏览器会 再次发起post请求，结果不对
        # return render(request,"polls/result.html",{"question":question})
        return redirect(reverse("polls:result", args=(id,)))


def result(request,id):
    question = Question.objects.get(pk = id)
    return render(request, "polls/result.html",locals())