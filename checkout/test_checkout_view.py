from django.test import TestCase


class TestCheckoutView(TestCase):
    def test_index_page(self):
        response = self.client.get('/checkout/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')



