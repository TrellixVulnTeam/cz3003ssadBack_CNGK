from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import requests


# Create your views here.
def index(request):
    postdata = {
        'device': settings.SMS_ID,
        'email': settings.SMS_EMAIL,
        'password': settings.SMS_PW,
        'number': '91007606',
        'message': "AUTO MESSAGE, LET ME KNOW IF YOU SEE IT",
    }
    r = requests.post(settings.SMS_GATEWAY_URL, data=postdata)
    print(r.status_code)
    print(r.text)
    return HttpResponse("Hello, world. You're at the sms index.")
