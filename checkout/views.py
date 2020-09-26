from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
import stripe
from django.conf import settings
from django.views.decorators.http import require_POST
from .forms import OrderForm
from .models import Order



@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={

            'username': request.POST.get('name'),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request,type):
    order_form = OrderForm()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    template = 'checkout/checkout.html'
    # setting total to 1999 in case user is messing with urls
    total = 1999
    if type == 'blog':
        total = int(settings.BLOG_PRICE)
    elif type == 'website':
        total = int(settings.WEBSITE_PRICE)
    elif type == 'store':
        total = int(settings.STORE_PRICE)

    # stripe amount in cents
    stripe_total = total * 100

    stripe.api_key = stripe_secret_key
    # create intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY

    )

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'user': request.user.username,
        'type': type,
        'grand_total': total,

    }
    if request.method == 'POST':
        form_data = {
            'name': request.POST.get('name'),
            'street1': request.POST.get('street1'),
            'city': request.POST.get('city'),
            'post_code': request.POST.get('post_code'),
            'country': request.POST.get('country'),
            'email': request.POST.get('email'),
            'product_type':type,
            'grand_total': total,
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # if order form is valid try to add order to DB

            try:
                order = order_form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.stripe_pid = pid
                order.grand_total = total
                order.product_type = type
                order.save()

                messages.success(request, 'Your order was created successfully ')

                return redirect(reverse('checkout_success', args=[order.order_number]))

            except:
                # else send notification to user, that something is wrong
                messages.error(request, 'There was an error with your form order form. \
                                               Please double check your information.')
                context['order_form'] = order_form





        else:
            # if form is not valid, send notification to user, that something is wrong
            messages.error(request, 'There was an error with your form \
                        Please double check your information.')
            context['order_form'] = order_form

    """
           A view to return checkout page
    """
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    order = get_object_or_404(Order, order_number=order_number)
    # if order was processed successfully

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'user': request.user.username,
    }

    return render(request, template, context)


