import requests

class twitch_api:

    def __init__(self):
        #derp do nothing for now

    def get_featured_streams(self, limit=25, offset=0):
        ops = {'limit': limit, 'offset': offset}
        r = requests.get('https://api.twitch.tv/kraken/streams/featured', params=ops)
        print (r.url)
        print (r.text)

if __name__ == '__main__':
    api = twitch_api()
    api.get_featured_streams()
