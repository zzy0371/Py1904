from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,Http404
# Create your views here.
from .models import Question,Choice

def index(request):
    print(request)
    print(dir(request))
    questions = Question.objects.all()
    return render(request,"polls/index.html",locals())


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
        # choice = Choice.objects.get(pk = choiceid)
        # choice.votes += 1
        # choice.save()
        Choice.objects.incresevotes(choiceid)


        # 没有重定向，如果刷新浏览器会 再次发起post请求，结果不对
        # return render(request,"polls/result.html",{"question":question})
        return redirect(reverse("polls:result", args=(id,)))


def result(request,id):
    # question = Question.objects.get(pk = id)
    get_object_or_404(Question,pk=id)
    return render(request, "polls/result.html",locals())