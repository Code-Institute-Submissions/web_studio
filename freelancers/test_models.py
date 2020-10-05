from django.contrib.auth.models import User
from django.test import TestCase

from .models import Freelancer


class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        freelancer = Freelancer.objects.create(name='new item')
        self.assertFalse(freelancer.on_the_job)

    def test_appointment_string_method_returns_name(self):
        freelancer = Freelancer.objects.create(name='new item')
        self.assertEqual(str(freelancer), 'new item')

    def test_can_freelancer_create_account(self):
        # freelancer is creating account
        self.freelancer = Freelancer.objects.create(
            name='freelancer name',
            email='some@email.com',
            phone_num='0876707891',
            skills='skills',
            portfolio_link='portfolio_link',
            about='about',

        )

        self.user = User.objects.create_user(username='freelancer name', password='password', email='some@email.com')
        self.client.login(username='freelancer name', password='password')
        # we will log him in with his credential
        self.client.login(email='some@email.com', password='password')
        response = self.client.get('/freelancer/')
        self.assertTemplateUsed(response, 'freelancers/dashboard.html')

    def test_freelancer_can_update_his_details(self):
        self.freelancer = Freelancer.objects.create(
            name='freelancer name',
            email='some@email.com',
            phone_num='0876707891',
            skills='skills',
            portfolio_link='portfolio_link',
            about='about',

        )
        Freelancer.objects.filter(name=self.freelancer.name).update(skills='new skils')

        # value needs to be reloaded from the database.
        self.freelancer.refresh_from_db()
        self.assertEqual(self.freelancer.skills, 'new skils')
