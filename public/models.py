import datetime
import uuid

from django.db import models


# Create your models here.
class Order(models.Model):
    site_type = models.CharField(max_length=1, default=False, blank=False, null=False)
    policies = models.BooleanField(default=False, blank=False, null=False)
    extra_pages = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    done = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.site_type


class Consultation(models.Model):

    email = models.CharField(max_length=50, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    time_slot = models.CharField(max_length=1, default=False, blank=False, null=False)
    site_type = models.CharField(max_length=1, default=False, blank=False, null=False)
    project = models.CharField(max_length=500, blank=False, null=False)

    done = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.email

    def _generate_consultation_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()




