from django.test import TestCase

from products.models import Product


class TestProductView(TestCase):
    def test_product_blog_page(self):
        self.product = Product.objects.create(
            name='blog',
            price=299,
        )
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/blog.html')

    def test_product_website_page(self):
        self.product = Product.objects.create(
            name='website',
            price=999,
        )
        response = self.client.get('/website/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/website.html')

    def test_product_online_store_page(self):
        self.product = Product.objects.create(
            name='online-store',
            price=1999,
        )
        response = self.client.get('/online-store/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/online_store.html')
