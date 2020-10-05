from django.test import TestCase


class TestFreelancerView(TestCase):
    def test_register_freelancer_page(self):
        response = self.client.get('/register_form/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'freelancers/register_form.html')
