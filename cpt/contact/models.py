# coding=utf-8
from django.db import models

class Contact(models.Model):
    number    = models.IntegerField(primary_key=True, verbose_name='队员编号') #editable=False
    nickname  = models.CharField(max_length=30, verbose_name='登录名')
    name      = models.CharField(max_length=30, verbose_name='姓名')
    gender    = models.CharField(max_length=10, blank=True, verbose_name='性别')
    birthday  = models.DateField(blank=True, null=True, verbose_name='生日')
    phone     = models.CharField(max_length=30, blank=True, verbose_name='手机')
    email     = models.EmailField(blank=True, null=True, verbose_name='电子邮箱')
    apartment = models.CharField(max_length=30, blank=True, verbose_name='所属部门')
    major     = models.CharField(max_length=30, blank=True, verbose_name='专业')
    job       = models.CharField(max_length=30, blank=True, verbose_name='目前职业')
    place     = models.CharField(max_length=100, blank=True, verbose_name='居住地')
    note      = models.TextField(blank=True, verbose_name='自我介绍')
    
    def __unicode__(self):
        return str(self.number) + ": " + self.name
    
    class Meta:
        permissions = (
            ("is_member", "Is member"),
        )

from django.forms import ModelForm
from contact.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        readonly_fields = ['number', 'nickname']
        fields = ['name', 'gender', 'birthday', 'phone',
            'email', 'apartment', 'major', 'job', 'place', 'note']

