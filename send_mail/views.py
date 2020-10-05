import json
import os

import requests
from django.shortcuts import render

# Create your views here.

def send_mail(mail_details):
    request_url = "https://api.eu.mailgun.net/v3/globtopus.com/messages"
    key = os.getenv('MAILGUN_API_KEY')
    requests.post(request_url, auth=('api', key), data={
        'from': 'marcellidesigns marcelkolarcik@gmail.com',
        'to': mail_details['to'],
        'subject':  mail_details['subject'],
        "template":  mail_details['template'],
        "h:X-Mailgun-Variables":
            json.dumps(
                mail_details['template_vars'])
    })
    pass
