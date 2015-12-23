from chat_listener import chat_listener

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client.chat_logs

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

    
