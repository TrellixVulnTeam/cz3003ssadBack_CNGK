from django.shortcuts import render
from django.db import models
from .models import Crisis, CrisisCoordinates
import json

# Create your views here.

def createCrisis(request):
    data = request.POST or None
    parsedData = json.loads('{"coordinates":[{"lat":1.3692446411800197,"lng":103.7388002872467},{"lat":1.3891515919773985,"lng":103.76901268959045},{"lat":1.350023980066177,"lng":103.77038598060608}],"disaster":"Zombie","type":"Polygon","name":"Area1","time":"2016-10-12T05:22:39.952Z","description":""}')
    disaster = parsedData['disaster']
    shapeType = parsedData['type']
    name = parsedData['name']
    time = parsedData['time']
    description = parsedData['description']
    coordinates = parsedData['coordinates']
    print(coordinates)
    crisis = Crisis(disaster=disaster, name=name, shapeType=shapeType, description=description)
    crisis.save()
    for latlng in coordinates:
        crisisCoordinates = CrisisCoordinates(crisis=crisis, latitude=latlng['lat'], longitude=latlng['lng'])
        crisisCoordinates.save()
    return render(request, 'crisis/createCrisis.html')
