import uuid

from django.db import models


# Appointment model




class Appointment(models.Model):
    email = models.CharField(max_length=50, blank=False, null=False)
    phone_num = models.CharField(max_length=50, blank=False, null=False,default=0)
    name = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    time_slot = models.CharField(max_length=50, default=False, blank=False, null=False)
    site_type = models.CharField(max_length=50, default=False, blank=False, null=False)
    project = models.CharField(max_length=500, blank=False, null=False)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    done = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.name

