from django.test import TestCase

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
        response = self.client.post('/consultations', {
            'name': 'This is customer name',
            'email': 'some@email.com',
            'phone_num': '0876707891',
            'time_slot': '1',
            'site_type': '2',
            'project': 'big project',
            'password': 'password',
            'done': False})

        self.assertRedirects(response, '/accounts/login/')

