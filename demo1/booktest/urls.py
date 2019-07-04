from . import views
from django.conf.urls import url
app_name = "booktest"
# 应用路由配置
urlpatterns = [
    # 访问对应的路由可以执行对应的视图函数
    url(r'^$',views.index,name="index"),
    url(r'^list/$',views.list,name="list"),
    url(r'^detail/(\d+)/$',views.detail,name="detail"),

    url(r'^deletebook/(\d+)/$',views.deletebook,name="deletebook"),

    url(r'^deletehero/(\d+)/$',views.deletehero,name="deletehero"),
    url(r'^addhero/(\d+)/$',views.addhero,name="addhero"),
]

"""
匹配  ： 
1，输入网址格式需要和路由有列表格式匹配（）
2，路由列表格式需要和视图函数格式匹配（）
参数问题
"""