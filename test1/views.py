from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("HttpResponse()方法向前端页面返回字符串，render()向浏览器返回html文档等")
    return render(request,"loginPage.html")