import sys
import socket
import time

from pymongo import MongoClient

class chat_listener:

    def __init__(self):
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.chat_metrics
        self.collection = self.db.chat_logs
        self.log_count = 0

    def login_routine(self, server='irc.twitch.tv',
      port='6667', nick='ChatMetrics', 
      oauth='oauth:2t96i2zewlhfs2uvbeceb5dw9en4sq', channel=None):

        #default server is irc.twitch.tv
        #default port is 6667
        #default nick is ChatMetrics
        try:
            self.ircsock.connect((server, int(port)))
        except:
            print('Unable to connect to %s on port %s' % (server, str(port)))
        self.ircsock.send('USER %s\r\n' % nick)
        self.ircsock.send('PASS %s\r\n' % oauth)
        self.ircsock.send('NICK %s\r\n' % nick)
        
        #load buffer of login and dump
        login_msg = self.ircsock.recv(2048)
        print login_msg

    def join_channel(self, channel):
        self.ircsock.send('JOIN #%s\r\n' % channel)
        
        #load join channel buffer and dump it
        join_msg = self.ircsock.recv(2048)
        print join_msg

    def pong(self):
        print '!!!!!!!!!!!!!!\n!!!!!!!!!!!!!Ponging'
        self.ircsock.send('PONG tmi.twitch.tv\r\n')

    def decompose_message(self, message):
        print message
        chat_array = message.split(':', 2)
        print chat_array
        
        #separate out the user, if me, drop entry
        #also doing bug checking on list index failures
        try:
            user = chat_array[1].split('!')[0]
            if user == 'chatmetrics':
                return None
            
            channel = chat_array[1].split('#')[1].strip(' ')
            message = chat_array[2]
            msg_dict = {'user' : user,
                'channel' : channel,
                'message' : message}
            print msg_dict
            return msg_dict
        except:
            return None

    def insert_log(self, entry):
        chat_id = self.collection.insert_one(entry).inserted_id
        self.log_count += 1
        print '!!!!!!LOG COUNT = ' + str(self.log_count)

    def chat_loop(self):
        while 1:
            try:
                ircmsg = self.ircsock.recv(2048)
                ircmsg = ircmsg.split('\r\n')
                for msg in ircmsg:
                    if msg.find('PING :tmi.twitch.tv') != -1:
                        self.pong()
                    entry = self.decompose_message(msg)
                    if entry:
                        self.insert_log(entry)
                    time.sleep(0.2)
            except Exception as e:
                print e
                time.sleep(0.2)
                continue


if __name__ =='__main__':
    chat = chat_listener()
    chat.login_routine()
    chat.join_channel('wagamamatv')
    chat.chat_loop()