from django.shortcuts import render

from .models import Product


def blog(request):
    blog_price = Product.objects.get(name='blog').price
    context = {
        'blog_price': round(blog_price)
    }
    return render(request, 'products/blog.html', context)


def website(request):
    website_price = Product.objects.get(name='website').price
    context = {
        'website_price': round(website_price)
    }
    return render(request, 'products/website.html', context)


def online_store(request):
    online_store_price = Product.objects.get(name='online-store').price
    context = {
        'online_store_price': round(online_store_price)
    }
    return render(request, 'products/online_store.html', context)
