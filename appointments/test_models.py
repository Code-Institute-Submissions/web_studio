from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Appointment


class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        appointment = Appointment.objects.create(name='new item')
        self.assertFalse(appointment.done)

    def test_create_edit_delete_appointment(self):
        # CREATING APPOINTMENT
        self.appointment = Appointment.objects.create(
            name='customer name',
            email='some@email.com',
            phone_num='0876707891',
            time_slot='1',
            site_type='2',
            project='big project',

            done=False
        )

        # get newly created appointment
        appointment = Appointment.objects.get(id=self.appointment.id)
        # assert it is right one
        self.assertEqual(appointment.project, 'big project')
        # https://stackoverflow.com/a/58242905 self.appointment.id

        # only signed in users can update appointment
        self.user = User.objects.create_user(username='customer name', password='password', email='some@email.com')
        self.client.login(username='customer name', password='password')

        # make sure appointment is users appointment
        self.assertEqual(appointment.email, self.user.email)

        # getting form with the appointment
        appointment_id = self.appointment.id
        update_url = reverse('edit_appointment', args=(appointment_id,))

        request = self.client.get(update_url)

        form = request.context['form']
        data = form.initial

        # EDITING APPOINTMENT
        data['project'] = 'updated project'

        # posting the form
        self.client.post(update_url, data)

        # retrieving the form and checking for updated value
        request = self.client.get(update_url)

        self.assertEqual(request.context['form'].initial['project'], 'updated project')

        # check that we have 1 appointment
        appointments = Appointment.objects.all()
        self.assertTrue(len(appointments) == 1)
