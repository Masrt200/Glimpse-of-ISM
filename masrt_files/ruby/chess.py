import random
from functools import reduce
import operator as op
import socket
import threading
import time


def make_chessboard(init):
	
	board="-"*33+"\n"
	for i in range(8):
		board+="|"
		for j in range(8):
			if init[i*8+j]:
				board+=" H "
			else:
				board+=" T "
			board+="|"

		board+="\n"+"-"*33+"\n"
	return board


def me_n_warden(init):

	warden_key=random.randint(0, 63)

	current_state=reduce(lambda x,y: x^y, [i for i,bit in enumerate(init) if bit])
	
	my_flip=current_state^warden_key
	init[my_flip]^=1

	return warden_key,init


class WARDEN(threading.Thread):
	def __init__(self,conn,addr):
		threading.Thread.__init__(self)
		self.csocket=conn
		self.win=True

	def run(self):
		title=b"          _  _  _      __  _  _ ____ _ _ \n\\    //\\ |_)| \\|_|\\ |/(_  / \\|_|_ | / |_ \n \\/\\//--\\| \\|_/|_| \\| __) \\_/| | _|_\\_|_ \n                                         \n"
		
		self.csocket.sendall(title)

		messages=[b"Here's your chessboard, find the Key\n\n",b"\nApparently, the warden knows about the BF approach.\n Four more doors await you\n\n",b"\nTime is of the essence, 3 to go\n\n",b"\nPENULTIMATE DOOR\n\n",b"\nI see freedom!? Shinzou Sasaageo!!!\n\n"]	
		#self.csocket.sendall(b"Here's your chessboard, find the Key\n\n")

		for i in range(5):
			self.csocket.sendall(messages[i])
			premise=[random.randint(0,1) for i in range(64)]

			key_location,premise=me_n_warden(premise)

			self.csocket.sendall(make_chessboard(premise).encode())
			self.csocket.sendall(b"key's at: ")

			try:
				your_guess=self.csocket.recv(2048)[:-1].decode()
			except:
				self.win=False
				with open("log.txt",'a+') as f:
					f.write(f"{time.asctime()} unexpected close from {addr}\n")
				f.close()
				break

			try:
				your_guess=int(your_guess)
			except:
				self.win=False
				break


			if your_guess==key_location:
				self.csocket.sendall(b"Impressed")
			else:
				self.win=False
				self.csocket.sendall(b"I believe, you failed in electronics")
				break

		if self.win:
			self.csocket.sendall(b"\nThe Warden hopes you enjoy your freedom, Until next time")
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

	new_server=WARDEN(conn, addr)
	new_server.start()
