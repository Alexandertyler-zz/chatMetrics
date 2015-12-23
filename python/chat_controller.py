from chat_listener import chat_listener
import subprocess32 as subprocess

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
    
    def kill_process(self):
        #send a kill command to the chart_listener process




if __name__ == '__main__':
    
    

    chat = chat_listener()
    chat.login_routine()
    chat.join_channel('WagamamaTV')
    chat.
    """chat1 = chat_listener()
    chat1.login_routine()
    chat1.join_channel('taketv')
    chat1.print_loop()
    
    chat2 = chat_listener()
    chat2.login_routine()
    chat2.join_channel('esl_lol')
    chat2.print_loop()"""

    
