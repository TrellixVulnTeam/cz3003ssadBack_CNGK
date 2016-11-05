from twitter import *


def main(message):
    access_token = '791147479064608768-ZIYXWXQdGYw0PKGCJGJjonUg29MbBa2'
    access_token_secret = '91RWJrpaL5zXq7sA3d7XScR0ZM3VV1e60utrU0XPmFobE'
    consumer_key = 'YOVzu2PHcTw0GVbsotzC52eVP'
    consumer_secret = '3r36K862Or2USMkjTH5jIn7031KqzvMQFaJQyram5rxrGHqvhu'

    twitterHandler = Twitter(auth=OAuth(
        access_token, access_token_secret, consumer_key, consumer_secret))

    # Edit variable status to post your tweets
    twitterHandler.statuses.update(status=message)
