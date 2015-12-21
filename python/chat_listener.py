import sys
import socket
import time

class chat_listener:

    def __init__(self):
        self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def login_routine(self, server='irc.twitch.tv',
      port='6667', nick='ChatMetrics', 
      oauth='oauth:2t96i2zewlhfs2uvbeceb5dw9en4sq', channel=None):

        #default server is irc.twitch.tv
        #default port is 6667
        #default nick is ChatMetrics
        try:
            self.ircsock.connect((server, int(port)))
        except:
            print('Unable to connect to %s on port %s' % server, port)
        self.ircsock.send('USER %s\r\n' % nick)
        self.ircsock.send('PASS %s\r\n' % oauth)
        self.ircsock.send('NICK %s\r\n' % nick)

    def join_channel(self, channel):
        self.ircsock.send('JOIN #%s\r\n' % channel)

    def pong(self):
        print 'Ponging'
        self.ircsock.send('PONG tmi.twitch.tv\r\n')

    def print_loop(self):
        while 1:
            try:
                ircmsg = self.ircsock.recv(2048)
                ircmsg = ircmsg.strip('\n\r')
                if ircmsg.find('PING tmi.twitch.tv') != -1:
                    self.pong()
                print ircmsg
                time.sleep(0.2)
            except:
                time.sleep(0.2)
                continue

if __name__ =='__main__':
    chat = chat_listener()
    chat.login_routine()
    chat.join_channel('taketv')
    chat.print_loop()
