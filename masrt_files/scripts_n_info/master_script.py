'''
sapphire
'''


from pwn import *

def sapphire():
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


'''
ruby
'''

def ruby():
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

'''
sac
'''

def sac():
	r=remote("ctf.glimpse-of-ism.ml",8001)

	print(r.recv(1024))
	r.sendline(b"where_we_will_meet_the_most")
	print(r.recvline())
	print(r.recvline())
	print(r.recv(4096).decode())
	r.sendline(b"`<flag.txt`")
	print(r.recv(1024).decode())



'''
rosaline
'''

def rosaline():
	from string import printable
	s = remote("ctf.glimpse-of-ism.ml", 5001)

	print(s.recv(1024))
	s.sendline(b'this_server_is_notorious')
	print(s.recvline())
	s.recvline()


	flag = ""
	alphabet=a=",:!abcdefghijklmnopqrstuvwxyz_1234567890{}ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	pos=1
	while 1:
	    for c in alphabet:
	        s.recvuntil("> ")
	        _flag = c
	        s.send(f'cat flag.txt| cut -b {pos} | grep -E "{c}"\n')
	        rc = int(s.recvline().strip())
	        if rc == 0:
	            flag += c
	            pos+=1
	            print(flag)
	            break


sac()
ruby()
sapphire()
rosaline()