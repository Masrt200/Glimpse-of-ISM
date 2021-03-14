#!/usr/bin/env python3
import socket
import random
import threading
import time
from secret import FLAG
from Crypto.Util.number import bytes_to_long

m=int.from_bytes(FLAG.encode(),'big')

primes=open("primes.txt").read().strip().split('\n')
primes=[int(i) for i in primes]

def keygen():
	p=random.choice(primes)
	q=p
	while q==p:
		q=random.choice(primes)

	n=p*q
	e=65537
	c=pow(m,e,n)

	return n,e,c

class RSA(threading.Thread):
	def __init__(self,conn,addr):
		threading.Thread.__init__(self)
		self.csocket=conn

	def run(self):
		self.csocket.sendall(b"flag server 3.14\n")
		self.csocket.sendall(b"all messages sent here are encrypted\n\n")

		n,e,c=keygen()
		self.csocket.sendall(f"n: {n}\n".encode('utf-8'))
		self.csocket.sendall(f"e: {e}\n".encode('utf-8'))
		self.csocket.sendall(f"c: {c}\n".encode('utf-8'))

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

	new_server=RSA(conn, addr)
	new_server.start()