# coding=utf-8
from django.db import models

# Create your models here.
class Recruit(models.Model):
    class Meta:
        permissions = (
            ("go_anywhere", "Is staff"),
            )

class Candidate(models.Model):
    user_name= models.CharField(max_length=30)
    real_name= models.CharField(blank=True,max_length=30,verbose_name='姓名')
    gender   = models.CharField(blank=True,max_length=10,verbose_name='性别')
    birthday = models.DateField(blank=True,null = True,verbose_name='生日')
    email    = models.EmailField(blank=True,verbose_name='电子邮件')
    phone    = models.CharField(max_length=20,blank=True,verbose_name='电话')
    homeland = models.CharField(blank=True,max_length = 10,verbose_name='家乡')
    major    = models.CharField(blank=True,max_length = 20,verbose_name='专业')
    speciality = models.CharField(blank=True,max_length = 40,verbose_name='特长')
    note     = models.TextField(blank=True,verbose_name='自我介绍')
    state    = models.IntegerField()
    score    = models.IntegerField(blank=True,null = True)
    remark1  = models.TextField(blank=True)
    remark2  = models.TextField(blank=True)
    remark3  = models.TextField(blank=True)
    other    = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.user_name, self.real_name)

from django.forms import ModelForm
from recruit.models import Candidate

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        readonly_fields = ['user_name']
        fields = ['real_name', 'gender', 'birthday', 'phone',
            'email', 'homeland', 'major', 'speciality','note']

class Exam(models.Model):
    exam_time= models.CharField(max_length=30,verbose_name='笔试时间')
    location = models.CharField(max_length=30,verbose_name='笔试地点')
    max_num  = models.IntegerField(verbose_name='该场考试容量')
    note     = models.TextField(blank=True,verbose_name='备注')
class Exam_list(models.Model):
    exam_id  = models.IntegerField(verbose_name='考试场次')
    user_name= models.CharField(max_length=30,verbose_name='姓名')
