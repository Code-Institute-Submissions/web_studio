from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Appointment


# Create your tests here.
class TestViews(TestCase):

    def test_get_add_appointment_page(self):
        response = self.client.get('/appointments/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/appointment.html')

    def test_get_edit_appointment_page(self):
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

        # only signed in users can update appointment
        self.user = User.objects.create_user(username='Test User', password='password', email='some@email.com')
        self.client.login(username='Test User', password='password')

        # make sure appointment is users appointment
        self.assertEqual(self.appointment.email, self.user.email)

        response = self.client.get(f'/edit/appointment/{self.appointment.id}')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/edit_appointment.html')

    def test_can_create_appointment(self):
        response = self.client.get('/appointments/')
        self.assertTemplateUsed(response, 'appointments/appointment.html')
        # user is creating appointment
        response = self.client.post('/appointments/', {
            'name': 'customer name',
            'email': 'some@email.com',
            'phone_num': '0876707891',
            'time_slot': '1',
            'site_type': '2',
            'project': 'big project',
            'password': 'password',
            'notes': 'Write notes about project',
            'done': False})

        self.assertRedirects(response, '/accounts/login/')
        # we will log him in with his credential
        self.client.login(username='customer name', password='password')
        response = self.client.get('/profile/')
        self.assertTemplateUsed(response, 'appointments/profile.html')

    def test_create_edit_delete_appointment(self):
        # CREATING APPOINTMENT
        self.appointment = Appointment.objects.create(
            name='customer name',
            email='some@email.com',
            phone_num='0876707891',
            time_slot='1',
            site_type='2',
            project='big project',
            done=False,

        )
        # only signed in users can update appointment
        self.user = User.objects.create_user(username='customer name', password='password', email='some@email.com')
        self.client.login(username='customer name', password='password')
        # get newly created appointment
        appointment = Appointment.objects.get(id=self.appointment.id)



        # assert it is right one
        self.assertEqual(appointment.project, 'big project')
        # https://stackoverflow.com/a/58242905 self.appointment.id

        # getting form with the appointment
        appointment_id = self.appointment.id
        update_url = reverse('edit_appointment', args=(appointment_id,))
        delete_url = reverse('delete_appointment', args=(appointment_id,))
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

        # DELETING APPOINTMENT
        # assert it's not paid for yet
        self.assertFalse(appointment.paid_for)

        self.client.delete(delete_url)

        # check that we have 0 appointments
        appointments = Appointment.objects.all()
        self.assertTrue(len(appointments) == 0)