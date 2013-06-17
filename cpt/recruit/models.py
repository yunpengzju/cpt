from django.db import models

# Create your models here.
class Recruit(models.Model):
        # ...
	class Meta:
		permissions = (
			("go_anywhere", "Is staff"),
		)
		
class Candidate(models.Model):
    name     = models.CharField(max_length=30)
    gender   = models.CharField(max_length=10)
    birthday = models.DateField(null = True)
    email_address = models.EmailField(blank=True)
    phone    = models.CharField(max_length=20,blank=True)
    homeland = models.CharField(max_length = 10)
    major    = models.CharField(max_length = 20)
    speciality = models.CharField(max_length = 40)
    note     = models.TextField(blank=True)
    state    = models.IntegerField()
    score    = models.IntegerField()
    remark1  = models.TextField(blank=True)
    remark2  = models.TextField(blank=True)
    remark3  = models.TextField(blank=True)
    other    = models.TextField(blank=True)
     
    def __unicode__(self):
		return u'%s %s' % (self.f_name, self.l_name)
	
