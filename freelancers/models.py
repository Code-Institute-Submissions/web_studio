from django.db import models


class Freelancer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_num = models.CharField(max_length=50, blank=False, null=False, default=0)
    about = models.CharField(max_length=500, blank=False, null=False)
    skills = models.CharField(max_length=500, blank=False, null=False)
    portfolio_link = models.CharField(max_length=500, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    on_the_job = models.BooleanField(null=False, blank=True, default=False)
    current_project = models.CharField(default='',max_length=50,blank=True)
    total_jobs = models.IntegerField(default=0, blank=False, null=False)


    def __str__(self):
        return self.name
