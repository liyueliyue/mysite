from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("HttpResponse()方法向前端页面返回字符串，render()向浏览器返回html文档等")
    return render(request,"loginPage.html")
# 通过{{}}向前端页面返回字符串
def returnString(request):
    list1 = ["html",'css','python','django','bootrasp3','']
    return render(request,"home.html",{"name":"我是一个字符串。"})
# 向前端页面返回列表
def returnList(request):
    list1 = ["html",'css','python','django','bootrasp3','']
    return render(request,"home.html",{'list1':list1})
# 向前端页面返回字典1
def returnDic(request):
    dic = {'百度':'http://www.baidu.com','京东':'http://www.jd.com','淘宝':'http://www.taobao.com'}
    return render(request,'home.html',{'dic':dic})
# 向前端页面返回字典2
def returnDic2(request):
    dic = {'key':'京东','value':'http://www.jd.com/'}
    return render(request,'home.html',{'dic2':dic})