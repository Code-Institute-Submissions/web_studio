from django.test import TestCase

from .models import Order


class TestModels(TestCase):

    def test_customer_name_repr_method_returns_name(self):
        order = Order.objects.create(name='Customer Name')
        self.assertEqual(repr(order), 'Customer Name')
