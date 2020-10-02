from django.test import TestCase

from .forms import ProductForm


class TestProductForm(TestCase):
    def test_product_name_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_product_price_is_required(self):
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_product_form_with_price_and_name_is_valid(self):
        form = ProductForm({'price': '299', 'name': 'blog'})

        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, ('name', 'price'))
