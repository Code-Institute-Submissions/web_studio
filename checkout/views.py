from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
import stripe
from django.conf import settings
# Create your views here.
from django.views.decorators.http import require_POST
# import OrderForm

def checkout(request,type):

    context={
        'type':type
    }

    return render(request, 'checkout/checkout.html',context)


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={

            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# def checkout2(request):
#     order_form = OrderForm()
#     stripe_public_key = settings.STRIPE_PUBLIC_KEY
#     stripe_secret_key = settings.STRIPE_SECRET_KEY
#     template = 'checkout/checkout.html'
#     total = int(settings.COURSE_PRICE)
#     stripe_total = total * 100
#
#     stripe.api_key = stripe_secret_key
#     intent = stripe.PaymentIntent.create(
#         amount=stripe_total,
#         currency=settings.STRIPE_CURRENCY
#
#     )
#
#     context = {
#         'order_form': order_form,
#         'stripe_public_key': stripe_public_key,
#         'client_secret': intent.client_secret,
#         'user': request.user.username.split('__order__')[0],
#
#     }
#     if request.method == 'POST':
#         form_data = {
#             'full_name': request.POST['full_name'],
#             'email': request.POST['email'],
#             'password': request.POST['password'],
#             'grand_total': total,
#
#         }
#
#         order_form = OrderForm(form_data)
#         if order_form.is_valid():
#
#             """
#                CREATE NEW USER
#             """
#             try:
#                 """
#                     CHECK IF USER WITH THIS EMAIL ALREADY EXISTS
#                     AND IF YES SEND MESSAGE BACK TO USE DIFFERENT EMAIL
#
#
#                    ADDING pid TO USER NAME TO MAKE IT UNIQUE, TO AVOID
#                    NOT UNIQUE NAME ERROR, BECAUSE USERS CAN HAVE THE SAME
#                    NAMES...
#                 """
#
#                 def email_present(email):
#                     if User.objects.filter(email=email).exists():
#                         return True
#
#                     return False
#
#                 order = order_form.save(commit=False)
#                 pid = request.POST.get('client_secret').split('_secret')[0]
#                 order.stripe_pid = pid
#                 order.grand_total = total
#                 order.password = ''
#                 order.save()
#                 new_user = User.objects.create_user(request.POST['full_name'] + '__order__' + pid,
#                                                     request.POST['email'],
#                                                     request.POST['password'])
#                 new_user.save()
#
#                 messages.success(request, 'Your account was created successfully \ Please login with your '
#                                           'credentials.')
#
#                 return redirect(reverse('checkout_success', args=[order.order_number]))
#
#
#
#             except:
#                 messages.error(request, 'There was an error with your form. \
#                                                Please double check your information.')
#                 context['order_form'] = order_form
#
#
#
#
#
#         else:
#             messages.error(request, 'There was an error with your form. \
#                         Please double check your information.')
#             context['order_form'] = order_form
#
#     """
#            A view to return checkout page
#     """
#     return render(request, template, context)
#
#
# def checkout_success(request, order_number):
#     """
#     Handle successful checkouts
#     """
#
#     order = get_object_or_404(Order, order_number=order_number)
#
#     messages.success(request, f'Order successfully processed! \
#         Your order number is {order_number}. A confirmation \
#         email will be sent to {order.email}.')
#
#     # if 'bag' in request.session:
#     #     del request.session['bag']
#
#     template = 'checkout/checkout_success.html'
#     context = {
#         'order': order,
#         'user': request.user.username.split('__order__')[0],
#     }
#
#     return render(request, template, context)

def checkout_success(request,order_number):

    context={
      'order_number':order_number
    }

    return render(request, 'checkout/checkout_success.html',context)
