import requests
import pprint

class twitch_api(object):
#The functions defined in this
#use an ordering format resembling
#the url used for the call

    def __init__(self):
        #derp do nothing for now
        self.ops = { 'client_id': ''}

    def get_streams_featured(self, limit=25, offset=0):
        ops = {'limit': limit, 'offset': offset}
        ops.update(self.ops)
        r = requests.get('https://api.twitch.tv/kraken/streams/featured', params=ops)
        return r.json()

    def get_games_top(self, limit=25, offset=0):
        ops = {'limit': limit, 'offset': offset}
        ops.update(self.ops)
        r = requests.get('https://api.twitch.tv/kraken/games/top', params=ops)
        return r.json()

    def get_streams(self, game=None, channel=None, limit=25, offset=25, 
            client_id=None, stream_type=None):
        args = {'game': game, 'channel': channel, 'limit': limit, 'offset': offset,
                'client_id': client_id, 'stream_type': stream_type}
        ops = {}
        for key, value in args.iteritems():
            if value:
                ops[key] = value

        r = requests.get('https://api.twitch.tv/kraken/streams', params=ops)
        return r.json()


if __name__ == '__main__':
    api = twitch_api()
    api.get_featured_streams()
