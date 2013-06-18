from django.db import models

# Create your models here.
class Recruit(models.Model):
    class Meta:
    permissions = (
        ("go_anywhere", "Is staff"),
        )
