from django.test import TestCase

from .forms import AppointmentForm


class TestAppointmentForm(TestCase):
    def test_appointment_name_is_required(self):
        form = AppointmentForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = AppointmentForm(
            {
                'name': 'This is customer name',
                'email': 'some@email.com',
                'phone_num': '0876707891',
                'time_slot': '1',
                'site_type': '2',
                'project': 'big project',


            }
        )

        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AppointmentForm()
        self.assertEqual(form.Meta.fields,
                         ('name', 'email', 'time_slot', 'site_type', 'project',  'done', 'phone_num',
                          'notes','paid_for'))
