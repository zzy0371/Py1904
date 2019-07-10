from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import ArticleForm
# Create your views here.

class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        return render(request,'blog/index.html',locals())

class SingleView(View):
    def get(self,request,id):
        article = Article.objects.all()

        return render(request,'blog/single.html')
    def post(self,request,id):
        return render(request,'blog/single.html')

class AddArticleView(View):
    def get(self,request):
        af = ArticleForm()
        return render(request,'blog/addarticle.html',locals())
    def post(self,request):
        af = ArticleForm(request.POST)
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))
        return HttpResponse("添加失败")

