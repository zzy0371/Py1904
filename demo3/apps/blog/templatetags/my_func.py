"""
自定义模板表达式
扩展Django原有功能
"""

from django.template import library
register = library.Library()
from blog.models import Article

@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by("-create_time")[:num]

@register.simple_tag
def gettimes():
    times = Article.objects.dates("create_time","month","DESC")
    return times






@register.filter
def mylower(value):
    return value.lower()

@register.filter
def myjoin(value,spl):
    return spl.join(value)

@register.filter
def myjoin2(value,spl,s):
    return spl.join(value) + s