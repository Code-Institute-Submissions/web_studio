from django.test import TestCase

from .models import Appointment



class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        appointment = Appointment.objects.create(name='new item')
        self.assertFalse(appointment.done)

    def test_appointment_string_method_returns_name(self):
        appointment = Appointment.objects.create(name='new item')
        self.assertEqual(str(appointment), 'new item')
