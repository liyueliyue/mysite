"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app1 import views
from app2 import views as add_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index),
# name可以用在templates，models，views...中得到对应的网址，相当于给网址起个名字，
# 只要这个名字不变，网址变了也能通过名字获取到。
    url(r'^add/$',add_views.add,name="add"),
    url(r'^add/(\d+)/(\d+)$',add_views.add2 ,name="add2"),
    url(r'^add3/$',add_views.add3,name="add3"),
    url(r'^add_action/$',add_views.add_action),
    # url(r'^home/$',views.returnString,name="home"),
    # url(r'^home/$',views.returnList),
    # url(r'^home/$',views.returnDic),
    # url(r'^home/$',views.returnDic2),
    # url(r'^home/$',views.returnForIf),
    url(r'^home/(\d+)/(\d+)$',views.sum)
]
