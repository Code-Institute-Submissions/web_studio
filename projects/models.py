from django.db import models

# Create your models here.

class Project(models.Model):
    project_number = models.CharField(max_length=32, blank=False, null=False)
    started = models.BooleanField(null=False, blank=False, default=False)
    wireframes = models.BooleanField(null=False, blank=False, default=False)
    update_after_wireframes = models.BooleanField(null=False, blank=False, default=False)
    started_on_site = models.BooleanField(null=False, blank=False, default=False)
    development_link_sent = models.BooleanField(null=False, blank=False, default=False)
    development_link = models.CharField(max_length=500,blank=True)
    client_approved = models.BooleanField(null=False, blank=False, default=False)
    domain_hosting = models.BooleanField(null=False, blank=False, default=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.project_number
