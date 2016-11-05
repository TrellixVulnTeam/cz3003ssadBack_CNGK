import facebook


def main(message, description):
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
