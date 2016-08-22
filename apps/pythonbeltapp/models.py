from __future__ import unicode_literals
from django.db import models

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    trip_begin = models.DateField()
    trip_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey("loginreg.User", related_name = "creator")
    travelers = models.ManyToManyField("loginreg.User", related_name = "travelers") # User.objects.get(id=request.session['id']).travelers.all is what the related name "travelers" allows you to do. That would give you all of the trips of the User.id referenced is traveling on
    def __repr__(self):
        return self.destination + " " + self.creator.name + " " + str(self.travelers.all())
