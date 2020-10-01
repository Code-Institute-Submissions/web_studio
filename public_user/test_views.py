from django.contrib.auth.models import User
from django.test import TestCase


class TestViews(TestCase):
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'public_user/index.html')

    def test_portfolio_page(self):
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'public_user/portfolio.html')

    def test_howitworks_page(self):
        response = self.client.get('/how-it-works/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'public_user/howitworks.html')

    def test_freelancer_page(self):
            response = self.client.get('/register_form/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'freelancers/register_form.html')

    def test_user_can_login(self):
        self.user = User.objects.create_user(username='Test User', password='password')
        self.client.login(username='Test User', password='password')
        response = self.client.get('/profile/')
        self.assertTemplateUsed(response, 'appointments/profile.html')
