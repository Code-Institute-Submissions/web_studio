
from django.shortcuts import render,HttpResponse
from .models import Order

# Create your views here.
def index(request):
    orders = Order.objects.all()
    context = {
        "orders":orders
    }
    return render(request,'public/index.html',context)

