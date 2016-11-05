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
        'link': '#',
        'caption': 'Latest News',
        'description': description,
        'picture': 'https://s-media-cache-ak0.pinimg.com/564x/5f/6b/64/5f6b64420bbb41837b8d540ac325fb37.jpg'
    }
    # post status
    status = api.put_wall_post(message='Pig Alert', attachment=attachment)


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
