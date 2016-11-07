import facebook
from twitter import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from backend.models import Crisis


def mainFacebook(message, description):
    cfg = {
        # pageID for the SSAD CM facebook page
        "page_id": "1128200493912565",
        # access token
        "access_token": "EAAQjZBye2W2MBAMzicaTgc16LDYyooPvQCpsPDfVLHpr6BFpbNedE4VbWdIx4JWck3wrFmM6YJpoieXen42FrFQ01w7nnbseBgpPlHbDDHIjDCxOybfypocSvX2nKHCRpafc6MWxYeujLbeolZCxjRa4CCR4yqU1eniZBEhoAZDZD"
    }

    api = get_api(cfg)
    # status information
    attachment = {
        'name': message,
        'link': 'https://www.google.com.sg/maps/place/Singapore/@1.3147297,103.776979,12z/data=!3m1!4b1!4m5!3m4!1s0x31da11238a8b9375:0x887869cf52abf5c4!8m2!3d1.352083!4d103.819836',
        'caption': 'Latest News',
        'description': description,
        'picture': 'http://www.sghomeonline.com/wp-content/uploads/2012/04/map_singapore.png'
    }
    # post status
    status = api.put_wall_post(message=message, attachment=attachment)


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    return graph
if __name__ == "__main__":
    main()


def mainTwitter(message):
    access_token = '791147479064608768-ZIYXWXQdGYw0PKGCJGJjonUg29MbBa2'
    access_token_secret = '91RWJrpaL5zXq7sA3d7XScR0ZM3VV1e60utrU0XPmFobE'
    consumer_key = 'YOVzu2PHcTw0GVbsotzC52eVP'
    consumer_secret = '3r36K862Or2USMkjTH5jIn7031KqzvMQFaJQyram5rxrGHqvhu'

    twitterHandler = Twitter(auth=OAuth(
        access_token, access_token_secret, consumer_key, consumer_secret))

    # Edit variable status to post your tweets
    twitterHandler.statuses.update(status=message)


@csrf_exempt
def sendToTwitter(request, crisisID):
    crisis = Crisis.objects.get(id=crisisID)
    tweet = crisis.disaster + " " + crisis.name + " " + \
        crisis.description + " at " + crisis.region + " " + crisis.location
    for i in range(0, len(tweet), 140):
        mainTwitter(tweet[i:i + 140])
    return HttpResponse(crisis)


@csrf_exempt
def sendToFacebook(request, crisisID):
    crisis = Crisis.objects.get(id=crisisID)
    title = crisis.disaster + " " + crisis.name + \
        " at " + crisis.region + " " + crisis.location
    description = crisis.description
    mainFacebook(title, description)
    return HttpResponse(crisis)
