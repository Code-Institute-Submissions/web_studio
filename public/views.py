
from django.shortcuts import render,HttpResponse
from .models import Order

# Create your views here.
def index(request):
    orders = Order.objects.all()
    context = {
        "orders":orders
    }
    return render(request, 'public/index.html', context)

def blog(request):

    return render(request, 'public/blog.html')
def website(request):

    return render(request, 'public/website.html')
def online_store(request):

    return render(request, 'public/online_store.html')
def get_in_touch(request):

    return render(request, 'public/get_in_touch.html')
def testimonials(request):

    return render(request, 'public/testimonials.html')


