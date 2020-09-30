from django.test import TestCase

from .models import Product


class TestModels(TestCase):

    def test_product_string_method_returns_name(self):
        product = Product.objects.create(name='consultation')
        self.assertEqual(str(product), 'consultation')
