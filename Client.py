import socket
import json
from MessageReceive import MessageReceiver
# -*- coding: utf-8 -*-

class Client(object):

    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, host, server_port):
        self.connection.connect((host, server_port))

        serverThread = MessageReceiver(client, self.connection)
        serverThread.daemon = True
        serverThread.start()

    def receive_message(self, message, connection):
        response = json.loads(message)

        if response.get('response') == 'error':
            print response.get('content')

        elif response.get('response') == 'history':
            print "Welcome, " + response.get('sender')
            for message in response.get('content'):
                print message

        elif response.get('response') == 'info':
            print response.get('content')

        elif response.get('response') == 'message':
            print response.get('content')

    def send(self, data):
        if data.startswith("/login"):
            try:
                username = data.split()[1]
            except IndexError:
                username = ""
            data = {'request': 'login', 'content': username}
        elif data == "/logout":
            data = {'request': 'logout', 'content': None}
        elif data == "/names":
            data = {'request': 'names', 'content': None}
        elif data == "/help":
            data = {'request': 'help', 'content': None}
        else:
            data = {'request': 'msg', 'content': data}
        
        self.connection.sendall(json.dumps(data))

    def disconnect(self):
        self.connection.close()


if __name__ == "__main__":
    client = Client()
    client.start('localhost', 9999)

    while True:
        message = raw_input('-- ')
        client.send(message)
        
        if message == '/exit':
            break

    client.disconnect()
