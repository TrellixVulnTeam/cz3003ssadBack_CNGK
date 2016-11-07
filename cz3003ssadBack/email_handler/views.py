from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from datetime import datetime
from backend.models import Crisis, CrisisMode, Dispatch, CrisisCoordinates
from django.template import Context, Template
from django.template.loader import get_template

# Create your views here.
def index(request):
    # result = send_mail('Subject here', 'Here is the message. Time: ' + str(datetime.now()), settings.EMAIL_HOST_USER, [
    #                    'timothy_lee@outlook.com'], fail_silently=False)
    mode = CrisisMode.objects.order_by('-id')[0]
    #print(mode)
    if(mode):
        all_entries = Crisis.objects.filter(closed = False)
        crisis_count = all_entries.count()
        avg_sev = 0
        for entry in all_entries:
            avg_sev += entry.severity
        if(crisis_count > 0):
            avg_sev = avg_sev / crisis_count
        server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c = Context({'username':'some username','query_crisis' : all_entries ,'crisis_count': crisis_count,'avg_sev': avg_sev,'server_time': server_time})
        plaintext = get_template('email.txt')
        html = get_template('email.html')
        plaintext_content = plaintext.render(c)
        html_content = html.render(c)
        msg = EmailMultiAlternatives("Crisis Report", plaintext_content, settings.EMAIL_HOST_USER, ["timothy_lee@outlook.com"])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print(msg)
    else:
        plaintext_content = ERROR
    #print(result)
    return HttpResponse(html_content)
