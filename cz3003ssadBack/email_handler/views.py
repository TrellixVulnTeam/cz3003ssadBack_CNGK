from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


# Create your views here.
def index(request):
    result = send_mail('Subject here', 'Here is the message. Time: ' + str(datetime.now()), settings.EMAIL_HOST_USER, [
                       'timothy_lee@outlook.com'], fail_silently=False)
    print(result)
    return HttpResponse(result)
