from chat_listener import chat_listener
from twitch_api import twitch_api
from pymongo import MongoClient
import pprint as pp
import threading

class master_thread():

    def __init__(self):
        self.api = twitch_api()
        self.channels = {}
        self.stop_event = threading.Event()

    def load_current_top_streams(self, stream_count):
        stream_json = api.get_streams(limit=stream_count)
        for stream in stream_json['streams']:
            #only load english streams for now
            if stream['channel']['language'] == 'en':
                #add the channel to our dict with value = False where
                #value is whether a thread using this channel has launched or not.
                #also no duplicates in case this needs to be called again later
                if not self.channels[stream['channel']['name']:
                    self.channels[stream['channel']['name']] = False

    def launch_all(self):
        for key, value in self.channels.iteritems():
            if not value:
                self.launch_process(key)

    def launch_process(self, channel):
        t = threading.Thread(target=build_chat_listener, args=[channel, self.stop_event])
        t.start()
        self.channel[channel] = True

    def stop_all(self):
        self.stop_event.set()
    
    def check_for_errors(self):
        #do something to check the output of the chat listener for some sort of error
        return
 

if __name__ == '__main__':
    api = twitch_api()
    #top_games_json = api.get_games_top(1, 0)
    #pp.pprint(top_games_json)

    channels = []

    get_str_json = api.get_streams(limit=10)
    #pp.pprint(get_str_json)
    for stream in get_str_json['streams']:
        print stream['channel']['language']
        if stream['channel']['language'] == 'en':
            channels.append(stream['channel']['name'])
    
    print channels
    
    chat = chat_listener()
    chat.login_routine()
    chat.join_channel(channels[0])
    chat.chat_loop()
    """
    chat1 = chat_listener()
    chat1.login_routine()
    chat1.join_channel('taketv')
    chat1.print_loop()
    
    chat2 = chat_listener()
    chat2.login_routine()
    chat2.join_channel('esl_lol')
    chat2.print_loop()"""

    
