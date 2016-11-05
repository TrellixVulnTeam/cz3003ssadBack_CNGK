from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json
from backend.models import Crisis, CrisisCoordinates
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
    # crisis.save()
    print(crisis)
    for coord in coordinates:
        coordinate = CrisisCoordinates(crisis=crisis, latitude=coord[
                                       "lat"], longitude=coord["lng"])
        # coordinate.save()
    return HttpResponse(received_json_data)


@csrf_exempt
def getCrisis(request):
    data = json.dumps([c.get_json() for c in Crisis.objects.all()])
    # allCrisis = Crisis.objects.all()
    # JSONSerializer = serializers.get_serializer("json")
    # json_serializer = JSONSerializer()
    # json_serializer.serialize(allCrisis)
    # data = json_serializer.getvalue()
    print(data)
    return HttpResponse(data)
