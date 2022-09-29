import datetime

from django.http import response, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from .models import user


def hello(request):
    return HttpResponse("hello")

def list_user(request):
    users = user.objects.all()
    return render(request,"user_list.html",{"users":users})
@csrf_exempt
def add_user(request):
    request.encoding = 'utf-8'
    if request.method == 'GET':
        return render(request,"add.html")
    else:
        #处理add数据
        t = datetime.datetime.now()
        user.objects.create(name=request.POST.get('name'),age=request.POST.get('age'),sex=request.POST.get('sex'),create_time=t)
        return list_user(request)


def delete(request,sid):
    u = user.objects.get(id=sid)
    u.delete()
    return list_user(request)

@csrf_exempt
def update(request,sid):
    u = user.objects.get(id=sid)
    if request.method == 'GET':
        return render(request,"update.html",{"user":u})
    else:
        #处理更新数据
        u.name=request.POST.get('name')
        u.age=request.POST.get('age')
        u.sex=request.POST.get('sex')
        u.save()
        return list_user(request)


