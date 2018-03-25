import socket
import pickle
from contextlib import closing

def check_socket(host, port):
	with closing(socket.socket()) as s:
		if s.connect_ex((host, port)) == 0:
			print('Port is open')
			resp = pickle.loads(s.recv(1024))
			print(resp['msg'])
		else:
			print('Port is not open')
		
host = socket.gethostbyname(socket.gethostname())
port = 8080
check_socket(host, port)
