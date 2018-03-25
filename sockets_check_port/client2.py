import socket
import pickle	
import sys
from contextlib import closing

def check_socket(host, port):
	with closing(socket.socket()) as s:
		try:
			s.connect((host, port))
			print('Port is open')
			resp = pickle.loads(s.recv(1024))
			print(resp['msg'])
		except ConnectionRefusedError:
			print('Port is not open')
		except:
			e = sys.exc_info()[0]
			print(e)
		
host = socket.gethostbyname(socket.gethostname())
port = 8080
check_socket(host, port)
