from django.db import models

# Create your models here.

class Project(models.Model):
    project_number = models.CharField(max_length=32, blank=False, null=False)
    started = models.BooleanField(default=False, blank=False, null=False)
    wireframes = models.BooleanField(default=False, blank=False, null=False)
    update_after_wireframes = models.BooleanField(default=False, blank=False, null=False)
    started_on_site = models.BooleanField(default=False, blank=False, null=False)
    development_link_sent = models.BooleanField(default=False, blank=False, null=False)
    development_link = models.CharField(max_length=500,blank=True)
    client_approved = models.BooleanField(default=False, blank=False, null=False)
    domain_hosting = models.BooleanField(default=False, blank=False, null=False)
    done = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.project_number
