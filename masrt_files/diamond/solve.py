from scapy.all import *

data=rdpcap("dump-2.pcap")

png=bytearray()
for i in range(len(data)):
	try:
		a=data[i].load.decode()
		if 'iitism.ac.in' in a:
			print(a.split('.')[0])
			png.append(int(a.split('.')[0]))
	except:
		pass

open('abc.jpg','wb').write(png)
