from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Appointment


# Create your tests here.
class TestViews(TestCase):
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'public/index.html')

    def test_get_add_item_page(self):
        response = self.client.get('/consultations')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'public/consultation.html')

    def test_get_edit_item_page(self):
        item = Appointment.objects.create(name='New item')
        response = self.client.get(f'/edit/consultation/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'public/edit_consultation.html')

    def test_can_add_item(self):
        """
        public user is creating appointment

        """
        response = self.client.post('/consultations', {
            'name': 'customer name',
            'email': 'some@email.com',
            'phone_num': '0876707891',
            'time_slot': '1',
            'site_type': '2',
            'project': 'big project',
            'password': 'password',
            'done': False})

        self.assertRedirects(response, '/accounts/login/')
        """
        we will log him in with his credential
        """
        self.client.login(username='customer name', password='password')
        response = self.client.get('/profile')
        self.assertTemplateUsed(response, 'public/profile.html')

    def test_create_edit_delete_appointment(self):
        """
        CREATING APPOINTMENT

        """
        self.appointment = Appointment.objects.create(
            name='customer name',
            email='some@email.com',
            phone_num='0876707891',
            time_slot='1',
            site_type='2',
            project='big project',
            password='password',
            done=False
        )

        """
        get newly created appointment
        """
        appointment = Appointment.objects.get(id=self.appointment.id)
        """
        assert it is right one
        """
        self.assertEqual(appointment.project, 'big project')
        # https://stackoverflow.com/a/58242905 self.appointment.id

        """
        geting form with the appointment 
        """
        appointment_id = self.appointment.id
        update_url = reverse('edit_consultation', args=(appointment_id,))
        delete_url = reverse('delete_consultation', args=(appointment_id,))
        request = self.client.get(update_url)

        form = request.context['form']
        data = form.initial

        """
        EDITING APPOINTMENT
        """
        data['project'] = 'updated project'

        """
        posting the form
        """
        self.client.post(update_url, data)

        """
        retrieving the form and checking for updated value
        """
        request = self.client.get(update_url)

        self.assertEqual(request.context['form'].initial['project'], 'updated project')

        """
         DELETING APPOINTMENT
        """
        self.client.delete(delete_url)
        """
        try to get deleted appointment
        """
        #appointment = Appointment.objects.get(id=appointment_id)
        try:
            Appointment.objects.get(id=appointment_id)


        except Appointment.DoesNotExist:

            self.assertTrue(Appointment.DoesNotExist)





    def test_user_can_login(self):
        self.user = User.objects.create_user(username='Test User', password='password')
        self.client.login(username='Test User', password='password')
        response = self.client.get('/profile')
        self.assertTemplateUsed(response, 'public/profile.html')
