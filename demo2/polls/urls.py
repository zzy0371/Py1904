from django.conf.urls import url
from . import views
app_name = "polls"
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result,name='result'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^checkuser/$',views.checkuser,name='checkuser'),
    url(r'^verify/$',views.verify,name='verify'),
    url(r'^active/(.*?)/$',views.active,name='active'),

]