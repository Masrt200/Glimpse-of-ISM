from pwn import *
from math import gcd

N=[]

found=0
while True:
	r=remote('ctf.glimpse-of-ism.ml',7001)

	print(r.recv(1024))
	r.sendline(b'the_best_hostel_period')
	print(r.recvline())
	r.recvline()
	r.recvline()
	r.recvline()
	r.recvline()

	data=r.recv(4096).decode().split('\n')[:-1]
	data=[int(i.split(': ')[1]) for i in data]
	
	if data[0] not in N:
		N.append(data[0])

	for i in N:
		p=gcd(i, data[0])
		if i!=data[0] and p!=1:
			q=data[0]//p
			print(p,q,data[0])
			found=1
		break

	if found:
		break

tot=(p-1)*(q-1)
d=pow(65537,-1, tot)
m=pow(data[2],d,data[0])
print(bytes.fromhex(hex(m)[2:]))

	