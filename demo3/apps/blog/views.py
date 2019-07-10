from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import *
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

