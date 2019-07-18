from django.shortcuts import render
# from django.views.generic import View
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.
class BookInfoViewSet(viewsets.ModelViewSet):
    queryset = BookInfo.objects.all().order_by("-pub_date")
    serializer_class = BookInfoSerializer


class HeroInfoViewSet(viewsets.ModelViewSet):
    queryset =  HeroInfo.objects.all().order_by("-name")
    serializer_class = HeroInfoSerializer

