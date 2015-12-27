Now that threading is finished, to do a trial run of this project run chat_listener.py

python chat_controller.py

This will run the default setup that grabs the top two streams with the most viewers.
If the stream is in english it will add it to a list and launch a new thread that opens
an irc channel to the chat. This will then log the user, channel and comment. The program
sleeps for one second then sends a kill all signal to the threads and exits.


TODO:
  * Figure out the right method for storing data in the database.
    - A count for occurences of entry by the same person?
    - Store on chat comment and only count refs to it then surface the top comments?
    - Number of unique channels?
  
  * Write the entire front end for surfacing the data from the db
    - Probably going to be somestatic page at first with angular elements.
    - How should I design the data? Graphs or something else?

