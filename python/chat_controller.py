from chat_listener import chat_listener
from twitch_api import twitch_api
import subprocess32 as subprocess
import pprint as pp

from pymongo import MongoClient

class chat_process():

    def __init__(self):
        self.channel = ''
        self.proc = None

    def launch_process(self):
        self.proc = subprocess.Popen(['python', 'chat_listener.py', self.channel], stdout=subprocess.PIPE, stderr=subprprocess.PIPE)
        self.out, self.err = self.proc.communicate()
    
    def check_for_errors(self):
        #do something to check the output of the chat listener for some sort of error
        return
    
    def kill_process(self):
        #send a kill command to the chart_listener process
        return


if __name__ == '__main__':
    api = twitch_api()
    #top_games_json = api.get_games_top(1, 0)
    #pp.pprint(top_games_json)

    get_str_json = api.get_streams(limit=1)
    pp.pprint(get_str_json)

    
    """
    chat = chat_listener()
    chat.login_routine()
    chat.join_channel('WagamamaTV')
    chat.
    chat1 = chat_listener()
    chat1.login_routine()
    chat1.join_channel('taketv')
    chat1.print_loop()
    
    chat2 = chat_listener()
    chat2.login_routine()
    chat2.join_channel('esl_lol')
    chat2.print_loop()"""

    
