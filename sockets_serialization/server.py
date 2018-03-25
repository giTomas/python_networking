# http://www.tutorialspoint.com/python/python_networking.htm

import socket               	# Import socket module
import pickle

msg = {'msg': 'Hello, my client! '}


s = socket.socket()             # Create a socket object
host = socket.gethostbyname(socket.gethostname())     # Get local machine name
port = 8080                     # Reserve a port for your service.
s.bind((host, port))            # Bind to the port

s.listen(5)                     # Now wait for client connection.
while True:
   c, addr = s.accept()         # Establish connection with client.
   print('Got connection from {}'.format(addr))
   c.send(pickle.dumps(msg))
   c.close()                    # Close the connection


