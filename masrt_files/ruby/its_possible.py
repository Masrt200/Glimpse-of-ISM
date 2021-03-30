from pwn import *
import time
r=remote("ctf.glimpse-of-ism.ml",9001)

print(r.recv(1024))
r.sendline(b'petro_wale_soo_lucky')
print(r.recvline())
r.recvline()

time.sleep(1)
for i in range(5):
	

	data=r.recv(4096).decode()

	
	print(data)
	data=data.split("\n\n\n")[1].replace("-",'')
	data=data.replace(' ','')[:-10].replace('|','').replace('\n','')
	print(data)
	val=0
	for i in range(64):
		if data[i]=='H':
			val^=i

	print(val)

	r.sendline(str(val))
	time.sleep(1)

print(r.recv(2048))