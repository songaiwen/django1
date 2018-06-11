#coding=utf8
from django.db import models

# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField()

    def __str__(self):
        return self.title.encode('utf-8')

class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    #设置的外键
    book = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.name.encode('utf-8')

