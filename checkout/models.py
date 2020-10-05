import uuid

from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    project_number = models.CharField(default=False, max_length=32, null=False)
    product_type = models.CharField(max_length=30, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    street1 = models.CharField(max_length=50, null=False, blank=False, default='')
    city = models.CharField(max_length=50, null=False, blank=False, default='')
    post_code = models.CharField(max_length=50, null=False, blank=False, default='')
    country = models.CharField(max_length=50, null=False, blank=False, default='')
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    def __repr__(self):
        return self.name
