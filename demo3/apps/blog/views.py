from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import ArticleForm,CommentForm
# Create your views here.
from django.core.paginator import Paginator,Page

def getpage(request,object_list,per_num):
    pagenum = request.GET.get("page")
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    return page


class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        # paginator = Paginator(articles,1)
        # print(paginator.page_range) #[1,5]
        # print(paginator.object_list) #
        # print(paginator.num_pages) #4
        # print(paginator.count) #4
        # page = paginator.get_page(3)
        # print(page)
        # print(page.paginator is paginator )
        # print(page.object_list)
        # print(page.number)
        # print(page.next_page_number())
        # print(page.previous_page_number())
        # print(page.has_next())
        # print(page.has_previous())

        page = getpage(request,articles,1)

        return render(request,'blog/index.html',{"page":page,"ads":ads})

class SingleView(View):

    def get(self,request,id):
        article = get_object_or_404(Article, pk=id)
        article.views += 1
        article.save()
        cf = CommentForm()
        return render(request,'blog/single.html',{"article":article,"cf":cf})
    def post(self,request,id):
        article = get_object_or_404(Article, pk=id)
        cf = CommentForm(request.POST)
        comment = cf.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(reverse("blog:single", args=(article.id,)))

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

class ArchivesView(View):
    def get(self,request,year,month):
        articles = Article.objects.filter(create_time__year=year, create_time__month=month)
        page = getpage(request, articles, 1)
        return render(request,"blog/index.html",{"page":page})

