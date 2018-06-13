#coding=utf-8
from django.shortcuts import render,redirect
from models import BookInfo,HeroInfo,AreaInfo
from datetime import date
from django.db.models import F,Q,Avg,Min,Sum,Count
# Create your views here.
def index(request):
    # list = BookInfo.books.filter(id=1)
    # list = BookInfo.books.filter(btitle__contains='传')
    # list = BookInfo.books.filter(btitle__endswith='部')
    # list = BookInfo.books.filter(btitle__isnull=False)
    # list = BookInfo.books.filter(pk__in=[1,3,5])
    # list = BookInfo.books.filter(id__gt=3)
    # list = BookInfo.books.exclude(id=3)
    # list = BookInfo.books.filter(bpub_date__year=1980)
    # list = BookInfo.books.filter(bpub_date__gt=date(1986,1,1))

    #关联查询
    # list = BookInfo.books.filter(heroinfo__hcontent__contains='八')
    # list = HeroInfo.objects.filter(hbook__btitle='天龙八部')

    #F两个字段进行比较
    #阅读量大于等于评论量
    # list = BookInfo.books.filter(bread__gte=F('bcommet'))
    # list = BookInfo.books.filter(bread__gte=F('bcommet') * 2)

    #聚合函数
    # result = BookInfo.books.aggregate(Sum('bread'))
    # print(result)
    result = BookInfo.books.aggregate(Count('bcommet'))

    print(result)

    #逻辑与
    # list = BookInfo.books.filter(bread__gt=20,id__lt=3)
    # list = BookInfo.books.filter(bread__gt=20,).filter(id__lt=3)


    #逻辑或
    # list = BookInfo.books.filter(Q(bread__gt=20) | Q(id__lt=3))

    #非not
    list = BookInfo.books.filter(~Q(id=3))






    # list=BookInfo.books.all()
    context = {
        'booklist':list
    }

    # context = {
    #     'herolist':list
    # }


    # return render(request,'booktest/index2.html',context)
    return render(request, 'booktest/index.html', context)

def add(request):
    book = BookInfo.books.create('流星蝴蝶剑', date(2017,1,1))
    book.save()
    #重定向
    return redirect('/')

def delete(request,id):
    book = BookInfo.books.get(id=id)
    book.isdelete = True
    book.save()
    return redirect('/')

def area(request):
    city = AreaInfo.objects.get(atitle='广州市')
    qulist = city.areainfo_set.all()
    sheng = city.aParent
    context = {
        'sheng':sheng,
        'qulist':qulist,
        'city':city
    }

    return render(request, 'booktest/area.html',context)