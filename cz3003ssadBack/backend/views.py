from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json
from backend.models import Crisis, CrisisCoordinates, CrisisMode, Dispatch
from backend import postToFacebook, postToTwitter
from smshandler.views import generateSms
# Create your views here.


@csrf_exempt
def submitCrisis(request):
    received_json_data = json.loads(request.body.decode('utf-8'))
    disaster = received_json_data["disaster"]
    severity = received_json_data["severity"]
    shapeType = received_json_data["type"]
    description = received_json_data["description"]
    location = received_json_data["location"]
    time = received_json_data["time"]
    name = received_json_data["name"]
    coordinates = received_json_data["coordinates"]
    crisis = Crisis(disaster=disaster, severity=severity, shapeType=shapeType,
                    description=description, location=location, name=name, time=time)
    crisis.save()
    print(crisis)
    for coord in coordinates:
        coordinate = CrisisCoordinates(crisis=crisis, latitude=coord[
                                       "lat"], longitude=coord["lng"])
        coordinate.save()
    return HttpResponse(received_json_data)


@csrf_exempt
def approveCrisis(request, crisisID):
    crisis = Crisis.objects.filter(id=crisisID)
    crisis.approved = True
    crisis.save()
    return HttpResponse(crisis)


@csrf_exempt
def closeCrisis(request, crisisID):
    crisis = Crisis.objects.filter(id=crisisID)
    crisis.closed = True
    crisis.save()
    return HttpResponse(crisis)


@csrf_exempt
def getApprovedCrisis(request):
    data = json.dumps([c.get_json()
                       for c in Crisis.objects.filter(closed=False, approved=True)])
    return HttpResponse(data)


@csrf_exempt
def getUnapprovedCrisis(request):
    data = json.dumps([c.get_json()
                       for c in Crisis.objects.filter(closed=False, approved=False)])
    return HttpResponse(data)


@csrf_exempt
def sendDispatch(request, crisisID, dispatcher):
    crisis = Crisis.objects.filter(id=crisisID)
    dispatch = Dispatch(crisis=crisis, dispatcher=dispatcher)
    # TODO SMS HANDLER
    generateSms(request, '91007606', 'hello world')
    return HttpResponse(dispatch)


@csrf_exempt
def toggleCrisisModeOn(request):
    mode = CrisisMode(inCrisis=True)
    return HttpResponse(mode)


@csrf_exempt
def toggleCrisisModeOff(request):
    mode = CrisisMode(inCrisis=False)
    return HttpResponse(mode)


@csrf_exempt
def sendToTwitter(request, crisisID):
    crisis = Crisis.objects.filter(id=crisisID)
    tweet = crisis.name + " " + crisis.description + " at " + crisis.location
    for i in range(0, len(tweet), 140):
        postToTwitter.main(tweet[i:i + 140])
    return HttpResponse(crisis)


@csrf_exempt
def sendToFacebook(request, crisisID):
    crisis = Crisis.objects.filter(id=crisisID)
    postToFacebook.main(crisis.name, crisis.description)
    return HttpResponse(crisis)
