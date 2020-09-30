from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                null=False, default=0)

    def __str__(self):
        return self.name
