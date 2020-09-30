from django.test import TestCase

from .forms import OrderForm


class TestOrderForm(TestCase):
    def test_order_name_is_required(self):
        form = OrderForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ('name', 'email', 'street1', 'city', 'post_code', 'country'))
