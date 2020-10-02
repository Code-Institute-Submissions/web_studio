from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Freelancer


class TestFreelancerView(TestCase):
    def test_register_freelancer_page(self):

        response = self.client.get('/register_form/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'freelancers/register_form.html')
