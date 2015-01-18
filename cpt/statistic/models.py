# coding=utf-8
from django.db import models

# Create your models here.
class Statistic(models.Model):
    site_views = models.IntegerField(verbose_name="全站访问量", default=0)