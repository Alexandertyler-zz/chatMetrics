from chat_listener import chat_listener

if __name__ == '__main__':
    chat1 = chat_listener()
    chat1.login_routine()
    chat1.join_channel('taketv')
    chat1.print_loop()
    
    chat2 = chat_listener()
    chat2.login_routine()
    chat2.join_channel('esl_lol')
    chat2.print_loop()
