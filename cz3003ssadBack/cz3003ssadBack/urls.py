"""cz3003ssadBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from email_handler import views as emailViews
from backend import views as backendViews
from smshandler import views as smsViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^email/$', emailViews.index, name="email_handler"),

    url(r'^sms/$', smsViews.index, name="sms_handler"),
    url(r'^sms/generateSms/$', smsViews.generateSms, name="send_sms"),

    url(r'^submitCrisis/$', backendViews.submitCrisis, name="crisis_submission"),
    url(r'^approveCrisis/(?P<crisisID>[0-9]+)$',
        backendViews.approveCrisis, name="crisis_approve"),
    url(r'^closeCrisis/(?P<crisisID>[0-9]+)$',
        backendViews.closeCrisis, name="crisis_close"),
    url(r'^getApprovedCrisis/$', backendViews.getApprovedCrisis,
        name="crisis_retrieval_approved"),
    url(r'^getUnapprovedCrisis/$', backendViews.getUnapprovedCrisis,
        name="crisis_retrieval_unapproved"),
    url(r'^sendDispatch/(?P<crisisID>[0-9]+)/$', backendViews.sendDispatch,
        name="send_dispatch"),
    url(r'^toggleCrisisModeOn/$', backendViews.toggleCrisisModeOn,
        name="crisis_mode_on"),
    url(r'^toggleCrisisModeOff/$', backendViews.toggleCrisisModeOff,
        name="crisis_mode_off"),
    url(r'^sendToTwitter/(?P<crisisID>[0-9]+)$', backendViews.sendToTwitter,
        name="send_to_twitter"),
    url(r'^sendToFacebook/(?P<crisisID>[0-9]+)$', backendViews.sendToFacebook,
        name="send_to_facebook"),
]
