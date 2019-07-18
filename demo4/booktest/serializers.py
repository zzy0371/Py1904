from rest_framework import serializers
from .models import *
class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = ["title","pub_date","url"]

class HeroInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = ["name","skill","book","url"]
