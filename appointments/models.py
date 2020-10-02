import uuid

from django.db import models


# Create your models here.

class Appointment(models.Model):
    project_number = models.CharField(default=False,max_length=32, null=False, editable=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    phone_num = models.CharField(max_length=50, blank=False, null=False, default=0)
    name = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    time_slot = models.CharField(max_length=50, default=False, blank=False, null=False)
    site_type = models.CharField(max_length=50, default=False, blank=False, null=False)
    project = models.TextField(max_length=500, blank=False, null=False)
    notes = models.TextField(default='',max_length=500, blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    done = models.BooleanField(null=False, blank=False, default=False)



    def _generate_project_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.project_number:
            self.project_number = self._generate_project_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_number

    def __repr__(self):
        return self.name


