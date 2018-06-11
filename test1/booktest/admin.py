from django.contrib import admin
from models import *

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date']
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','content','gender']


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)