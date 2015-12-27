from chat_listener import chat_listener
from twitch_api import twitch_api
from pymongo import MongoClient
import pprint as pp
import threading
import time

class master_thread():

    def __init__(self):
        self.api = twitch_api()
        self.channels = {}
        self.stop_event = threading.Event()

    def load_current_top_streams(self, stream_count):
        stream_json = self.api.get_streams(limit=stream_count)
        for stream in stream_json['streams']:
            #only load english streams for now
            if stream['channel']['language'] == 'en':
                #add the channel to our dict with value = False where
                #value is whether a thread using this channel has launched or not.
                #also no duplicates in case this needs to be called again later
                if not stream['channel']['name'] in self.channels:
                    self.channels[stream['channel']['name']] = False

    def build_chat_listener(self, channel, stop_event):
        chat = chat_listener()
        chat.login_routine()
        chat.join_channel(channel)
        chat.chat_loop(stop_event)

    def launch_all(self):
        for key, value in self.channels.iteritems():
            if not value:
                self.launch_process(key)

    def launch_process(self, channel):
        print "Launching thread " + channel
        t = threading.Thread(target=self.build_chat_listener, args=[channel, self.stop_event])
        t.start()
        self.channels[channel] = True

    def stop_all(self):
        self.stop_event.set()
    
    def check_for_errors(self):
        #do something to check the output of the chat listener for some sort of error
        return
 

if __name__ == '__main__':
    master = master_thread()
    master.load_current_top_streams(2)
    master.launch_all()
    time.sleep(1)
    master.stop_all()
