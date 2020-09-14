from django.db import models


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    done = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.name
