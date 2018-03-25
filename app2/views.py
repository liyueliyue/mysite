from django.shortcuts import render,HttpResponse

# Create your views here.
def add(request):
    if request.method == 'post':
        return render(request,'loginPage.html')
    else:
        a = request.GET.get('a',0)
        b = request.GET.get('b',0)
        c = int(a) + int(b)
        return HttpResponse(str(c))
def add2(request,a,b):
    return HttpResponse(str(int(a)+int(b)))
def add3(request):
    return render(request,"sum.html")
# 处理加法逻辑
def add_action(request):
    if request.method == "GET": # GET POST 必须是大写
        return HttpResponse("两数之和是1")
    else:
        a = request.POST.get('a',0)
        b = request.POST.get('b',0)
        c = int(a) + int(b)
        return render(request,"sum.html",{"sum":c})