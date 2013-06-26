# coding=utf-8
from django.db import models
from contact.models import Contact

class Task(models.Model):
    title       = models.CharField(blank=True, max_length=100, verbose_name='标题')
    date        = models.DateField(blank=True, null=True, verbose_name='日期')
    time        = models.CharField(blank=True, max_length=100, verbose_name='时间')
    client      = models.CharField(blank=True, max_length=100, verbose_name='参观者')
    client_num  = models.CharField(blank=True, max_length=100, verbose_name='参观人数')
    content     = models.CharField(blank=True, max_length=100, verbose_name='内容')
    source      = models.CharField(blank=True, max_length=100, verbose_name='任务来源')
    contact_man = models.CharField(blank=True, max_length=100, verbose_name='联系人称谓')
    contact_way = models.CharField(blank=True, max_length=100, verbose_name='联系方式')
    priority    = models.CharField(blank=True, max_length=30, verbose_name='优先级')
    formal      = models.CharField(blank=True, max_length=30, verbose_name='是否正装')
    note        = models.TextField(blank=True, verbose_name='备注')
    expect_xietiao  = models.CharField(blank=True, max_length=30, verbose_name='协调员预期人数')
    expect_jiangjie = models.CharField(blank=True, max_length=30, verbose_name='讲解员预期人数')
    post_id     = models.IntegerField()
    post_man    = models.CharField(max_length=30, verbose_name='发布者')
    post_date   = models.DateField(verbose_name='发布日期', auto_now_add=True)
    state       = models.IntegerField()
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        permissions = (
            ("is_member", "Is member"),
            ("is_manage", "Is manage"),
        )

class Xietiao(models.Model):
    task   = models.IntegerField()
    member = models.IntegerField()

    def __unicode__(self):
        return str(self.task) + "," + str(self.member)

class Jiangjie(models.Model):
    task   = models.IntegerField()
    member = models.IntegerField()

    def __unicode__(self):
        return str(self.task) + "," + str(self.member)

from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'date', 'time', 'client', 'client_num',
            'content', 'source', 'contact_man', 'contact_way',
            'priority', 'formal', 'note', 'expect_xietiao', 'expect_jiangjie']
            # hide: post man/date, state, id


