from django.test import TestCase

from .models import Freelancer


class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        freelancer = Freelancer.objects.create(name='new item')
        self.assertFalse(freelancer.on_the_job)

    def test_appointment_string_method_returns_name(self):
        freelancer = Freelancer.objects.create(name='new item')
        self.assertEqual(str(freelancer), 'new item')
