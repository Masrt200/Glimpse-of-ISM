from pwn import *
import time
r=remote("127.0.0.1",1337)

time.sleep(1)
for i in range(5):
	data=r.recv(4096).decode()
	print(data)
	data=data.split("\n\n")[1].replace("-",'')
	data=data.replace(' ','')[:-10].replace('|','').replace('\n','')

	val=0
	for i in range(64):
		if data[i]=='H':
			val^=i

	print(val)

	r.sendline(str(val))
	time.sleep(1)

print(r.recv(2048))