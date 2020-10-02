from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from appointments.models import Appointment
from freelancers.models import Freelancer
from projects.models import Project


class TestProjectView(TestCase):

    def test_project_preview_page(self):
        self.user = User.objects.create_user(username='Test User', password='password',email='email@email.com')
        self.appointment = Appointment.objects.create(
            name='customer name',
            email=self.user.email,
            phone_num='0876707891',
            time_slot='1',
            site_type='2',
            project='big project',
            password='password',
            done=False
        )
        self.project = Project.objects.create(project_number=self.appointment.project_number)

        self.client.login(username='Test User', password='password')

        response = self.client.get('/profile/')

        self.assertTemplateUsed(response, 'appointments/profile.html')


        project_number = self.project.project_number

        preview_url = reverse('project', args=(project_number,))

        self.client.get(preview_url)

        self.assertEqual(response.status_code, 200)




