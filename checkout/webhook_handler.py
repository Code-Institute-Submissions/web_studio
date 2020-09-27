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

    def _send_confirmation_email(self, email, order_id, receipt_url, name):
        """Send the user a confirmation email"""
        cust_email = email
        # subject = render_to_string(
        #     'checkout/confirmation_emails/confirmation_email_subject.txt',
        #     {'order_id': order_id})
        # body = render_to_string(
        #     'checkout/confirmation_emails/confirmation_email_body.txt',
        #     {'order_id': order_id, 'contact_email': settings.DEFAULT_FROM_EMAIL ,'receipt_url':receipt_url,'name':name})
        #
        # send_mail(
        #     subject,
        #     body,
        #     settings.DEFAULT_FROM_EMAIL,
        #     [cust_email]
        # )
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
                     'customer_name': name,
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
            self._send_confirmation_email(billing_details.email, pid, receipt_url, billing_details.name)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    name=billing_details.name,

                    email=billing_details.email,

                    grand_total=grand_total,
                    stripe_pid=pid,
                )

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(billing_details.email, pid, receipt_url, billing_details.name)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
