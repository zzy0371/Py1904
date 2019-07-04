"""demo1 URL Configuration
项目跟路由：用户在浏览器中输入的网址需要和路由匹配
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    # 在项目跟路由下通过url 以及 include指明应用路由的配置文件
    url('',include('booktest.urls',namespace="booktest")),
]

"""
解除硬编码
   硬编码：在静态文件写入超级链接绝对路径
    缺点：当路由地址发生变化，所有绝对路径编写的超级链接都需要更改
 解除硬编码可以避免绝对路径 
    1，使用应用命名空间
    2，使用路由的名字

"""