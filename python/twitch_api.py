import requests
import pprint

class twitch_api:

    def __init__(self):
        #derp do nothing for now
        self.ops = { 'client_id': 'rk5jc5h3ossghumsqhq6mciwzmyce'}
   

    def get_featured_streams(self, limit=25, offset=0):
        ops = {'limit': limit, 'offset': offset}
        ops.update(self.ops)

        r = requests.get('https://api.twitch.tv/kraken/streams/featured', params=ops)
        print (r.url)
        pprint.pprint(r.json())

if __name__ == '__main__':
    api = twitch_api()
    api.get_featured_streams()
