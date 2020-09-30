from django.test import TestCase

from products.models import Product


class TestCheckoutView(TestCase):
    def test_checkout_blog_page(self):
        self.product = Product.objects.create(
            name='blog',
            price=299,

        )
        response = self.client.get('/checkout/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_website_page(self):
        self.product = Product.objects.create(
            name='website',
            price=999,

        )
        response = self.client.get('/checkout/website/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_online_store_page(self):
        self.product = Product.objects.create(
            name='online-store',
            price=1999,

        )
        response = self.client.get('/checkout/online-store/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
