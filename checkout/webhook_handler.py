import json
import os
import time

import requests
from django.http import HttpResponse

from .models import Order


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, billing_details, order_id, receipt_url,product_type):
        """Send the user a confirmation email"""
        cust_email = billing_details.email

        """
        email to customer
        """
        request_url = "https://api.mailgun.net/v3/sandbox55fe83fc981d49c3874fc22b7dff254f.mailgun.org/messages"
        key = os.getenv('MAILGUN_API_KEY')
        recipient = cust_email
        requests.post(request_url, auth=('api', key), data={
            'from': 'marcellidesigns marcelkolarcik@gmail.com',
            'to': recipient,
            'subject': 'Thank you for your order',
            "template": "marcellidesigns_customer_purchase",
            "h:X-Mailgun-Variables":
                json.dumps(
                    {'welcome': 'Thank you for your order',
                     'product_type': product_type,
                     'customer_name': billing_details.name,
                     'receipt_url': receipt_url,
                     'order_id': order_id,

                     'welcome_team': 'Marcelli Designs', })
        })
        """
        email to owner
        """
        request_url = "https://api.mailgun.net/v3/sandbox55fe83fc981d49c3874fc22b7dff254f.mailgun.org/messages"
        key = os.getenv('MAILGUN_API_KEY')

        requests.post(request_url, auth=('api', key), data={
            'from': 'marcellidesigns marcelkolarcik@gmail.com',
            'to': 'marcelkolarcik@gmail.com',
            'subject': 'New order',
            "template": "marcellidesigns_customer_purchase_owner",
            "h:X-Mailgun-Variables":
                json.dumps(
                    {'welcome': 'New purchase',
                     'product_type': product_type,
                     'customer_email': cust_email,
                     'receipt_url': receipt_url,
                     'order_id': order_id,
                     'welcome_team': 'Marcelli Designs', })
        })

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """

        intent = event.data.object
        pid = intent.id
        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)
        receipt_url = intent.charges.data[0].receipt_url
        product_type = self.request.session.get('product_type')

        order_done = False
        attempt = 1
        while attempt <= 5:
            order_done = Order.objects.filter(stripe_pid=pid).exists()
            if order_done:
                break
            else:

                attempt += 1
                time.sleep(1)
        if order_done:
            self._send_confirmation_email(billing_details, pid, receipt_url,product_type )
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    name=billing_details.name,
                    email=billing_details.email,
                    street1=billing_details.address.line1,
                    post_code=billing_details.address.line2,
                    city=billing_details.address.city,
                    country=billing_details.address.country,

                    grand_total=grand_total,
                    total=grand_total,
                    stripe_pid=pid,
                )

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(billing_details, pid, receipt_url,product_type)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        intent = event.data.object
        product_type = self.request.session.get('product_type')
        billing_details = intent.charges.data[0].billing_details
        request_url = "https://api.mailgun.net/v3/sandbox55fe83fc981d49c3874fc22b7dff254f.mailgun.org/messages"
        key = os.getenv('MAILGUN_API_KEY')
        """
        IF THERE IS ERROR WITH PURCHASE WE WILL SEND EMAIL TO OWNER OF THE SITE
        """
        requests.post(request_url, auth=('api', key), data={
            'from': 'marcellidesigns marcelkolarcik@gmail.com',
            'to': 'marcelkolarcik@gmail.com',
            'subject': 'Error with your order',
            "template": "marcellidesign_error_purchase_owner",
            "h:X-Mailgun-Variables":
                json.dumps(
                    {'welcome': 'Error while purchasing',
                     'body': 'There was an error while customer was trying to buy one of your products.',
                     'product_type': product_type,
                     'customer_email': billing_details.email,
                     'customer_name': billing_details.name,
                     'welcome_team': 'Marcelli Designs', })
        })
        """
                IF THERE IS ERROR WITH PURCHASE WE WILL SEND EMAIL TO CUSTOMER
        """
        requests.post(request_url, auth=('api', key), data={
            'from': 'marcellidesigns marcelkolarcik@gmail.com',
            'to': billing_details.email,
            'subject': 'Error with your order',
            "template": "marcellidesigns_error_purchasing",
            "h:X-Mailgun-Variables":
                json.dumps(
                    {'welcome': 'Error while purchasing',
                     'body': 'There was an error during the purchase, your card was not charged',
                     'product_type': product_type,
                     'customer_email': billing_details.email,
                     'customer_name': billing_details.name,
                     'welcome_team': 'Marcelli Designs', })
        })
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
