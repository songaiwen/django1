#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from models import *


def index(request):

    # context = {
    #     'title':'django首页',
    #     'list':range(10)
    # }
    # return render(request, 'booktest/index.html',context)
    # return HttpResponse('hello world')
    list = BookInfo.objects.all()
    context = {
        'booklist':list
    }
    return render(request,'booktest/index2.html',context)


def detail(request,id):
    list = BookInfo.objects.get(id=id).heroinfo_set.all()
    context = {
        'herolist':list

    }
    return render(request,'booktest/detail.html',context)

