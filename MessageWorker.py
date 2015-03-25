import threading
# -*- coding: utf-8 -*-

class MessageReceiver(threading.Thread):

    def __init__(self, client, connection):

        self.daemeon = True
        self.listener = client
        self.connection = connection
        super(MessageReceiver, self).__init__()

    def run(self):
        while True:
            data = self.connection.recv(1024).strip()
            if data:
                self.listener.receive_message(data, self.connection)