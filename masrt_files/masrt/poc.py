from hashlib import sha256
import os
import socket
import threading
import time

message="enter a string whose sha256 hash in hex satisfies, sha256(string[-6:]) = "


def hash_gen():
	HASH=sha256(os.urandom(16)).hexdigest()[-6:]

	return HASH


class POW(threading.Thread):
	def __init__(self,conn,addr):
		threading.Thread.__init__(self)
		self.csocket=conn

	def run(self):
		self.csocket.sendall(message.encode())
		
		HASH=hash_gen()
		self.csocket.sendall(HASH.encode()+b"\n")
		self.csocket.sendall(b"> ")

		string=self.csocket.recv(2048)[:-1]

		check=sha256(string).hexdigest()[-6:]
		
		if check!= HASH:
			self.csocket.sendall(b"fail")
		else:
			self.csocket.sendall(b"pass")

		self.csocket.close()



host=''
port = 1337
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host,port))

while True:
	server.listen(1)
	conn,addr=server.accept()
	with open("log.txt",'a+') as f:
		f.write(f"{time.asctime()} connect from {addr}\n")
	f.close()

	new_server=POW(conn, addr)
	new_server.start()