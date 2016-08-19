from __future__ import unicode_literals
from django.db import models

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    trip_begin = models.DateField()
    trip_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("loginreg.User")
    travelers = models.ManyToManyField("loginreg.User", related_name = 'whatever')
