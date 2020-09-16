from django.shortcuts import render

# Create your views here.

def checkout(request,type):

    context={
        'type':type
    }

    return render(request, 'checkout/checkout.html',context)
