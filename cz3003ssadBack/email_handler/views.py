from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
	result = send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,['timothy_lee@outlook.com'], fail_silently=False)
	return HttpResponse(result)