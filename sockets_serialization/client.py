import socket
import pickle

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 8080
s.connect((host, port))
resp = pickle.loads(s.recv(1024))
print(resp['msg'])
s.close()
