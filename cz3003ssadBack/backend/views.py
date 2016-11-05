from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
import json
# Create your views here.


@csrf_exempt
def submitCrisis(request):
    received_json_data = json.loads(request.body.decode('utf-8'))
    print(received_json_data)
    html = received_json_data
    return HttpResponse(html)
